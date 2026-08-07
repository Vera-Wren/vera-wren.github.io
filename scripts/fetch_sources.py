#!/usr/bin/env python3
"""Source fetching utilities: Reddit, HN, RSS, web pages, GitHub trending.

All functions return lists of dicts: [{"title", "url", "snippet", "source_name"}]
Zero external dependencies — stdlib only.
"""

import json
import re
import ssl
import time
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.error import URLError, HTTPError


# Shared HTTP helpers

# 2026-07-31: every Reddit fetch (7 subs, 11 attempts) returned HTTP 429 on the
# 07-30 and 07-31 runs — roughly a third of the configured feed silently empty.
# Cause: the loop in fetch_all_sources() fired requests back to back with no
# pacing, so Reddit's per-client rate limiter shut the door on request two and
# never reopened it. Measured behaviour on 07-31: one request succeeds, then a
# lockout that clears in roughly 50s, regardless of host (old.reddit.com is
# throttled on the same budget). Hence a 25s inter-request gap plus backoff.
# sources.json also lists several subs more than once (r/ARG appears 3x), so
# responses are cached per-URL — a duplicate entry costs nothing now.
_MIN_HOST_GAP = {"www.reddit.com": 25.0, "old.reddit.com": 25.0}
_LAST_HOST_HIT = {}
_RESPONSE_CACHE = {}


def _throttle(url):
    """Sleep just long enough to honour the per-host minimum gap."""
    try:
        host = urllib.request.urlparse(url).netloc
    except AttributeError:
        from urllib.parse import urlparse
        host = urlparse(url).netloc
    gap = _MIN_HOST_GAP.get(host)
    if not gap:
        return
    last = _LAST_HOST_HIT.get(host)
    if last is not None:
        wait = gap - (time.monotonic() - last)
        if wait > 0:
            time.sleep(wait)
    _LAST_HOST_HIT[host] = time.monotonic()


def _make_request(url, timeout=15, retries=3):
    """Make an HTTP GET request, return response text. Returns None on failure.

    Responses are cached per-URL for the life of the process, and HTTP 429
    (rate limited) is retried with exponential backoff.
    """
    if url in _RESPONSE_CACHE:
        return _RESPONSE_CACHE[url]

    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={
        "User-Agent": "BlogBot/1.0 (autonomous research blog)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    })
    for attempt in range(retries):
        _throttle(url)
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                text = resp.read().decode("utf-8", errors="replace")
            _RESPONSE_CACHE[url] = text
            return text
        except HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                backoff = 20.0 * (attempt + 1)
                print(f"  [fetch] 429 on {url} — backing off {backoff:.0f}s "
                      f"(attempt {attempt + 1}/{retries})")
                time.sleep(backoff)
                continue
            print(f"  [fetch] Error fetching {url}: {e}")
            _RESPONSE_CACHE[url] = None
            return None
        except (URLError, TimeoutError, OSError) as e:
            print(f"  [fetch] Error fetching {url}: {e}")
            _RESPONSE_CACHE[url] = None
            return None
    return None


def _make_json_request(url, timeout=15):
    """Make HTTP GET, parse JSON. Returns None on failure."""
    text = _make_request(url, timeout)
    if text is None:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"  [fetch] JSON parse error for {url}: {e}")
        return None


class _TextExtractor(HTMLParser):
    """Extract visible text from HTML."""
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self._skip = False
        self._skip_tags = {"script", "style", "noscript", "nav", "footer", "header"}

    def handle_starttag(self, tag, attrs):
        if tag in self._skip_tags:
            self._skip = True

    def handle_endtag(self, tag):
        if tag in self._skip_tags:
            self._skip = False

    def handle_data(self, data):
        if not self._skip:
            text = data.strip()
            if text:
                self.text_parts.append(text)

    def get_text(self):
        return " ".join(self.text_parts)


def _extract_text(html_str, max_len=2000):
    """Extract visible text from HTML string."""
    parser = _TextExtractor()
    try:
        parser.feed(html_str)
    except Exception:
        pass
    text = parser.get_text()
    return text[:max_len] if len(text) > max_len else text


# Source fetchers

def fetch_reddit_json(subreddit, limit=10):
    """Fetch top posts from a subreddit using Reddit's RSS feed.

    Reddit aggressively blocks non-browser user agents on its JSON API,
    so we use the .rss (Atom feed) endpoint instead.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.rss?limit={limit}"
    return fetch_rss(url, source_name=f"r/{subreddit}", limit=limit)


def fetch_hackernews(limit=15):
    """Fetch top stories from Hacker News via Firebase API."""
    ids_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    ids = _make_json_request(ids_url)
    if not ids:
        return []
    results = []
    for story_id in ids[:limit]:
        item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        item = _make_json_request(item_url)
        if not item:
            continue
        title = item.get("title", "")
        url = item.get("url", f"https://news.ycombinator.com/item?id={story_id}")
        results.append({
            "title": title,
            "url": url,
            "snippet": title,
            "source_name": "Hacker News",
        })
    return results


def fetch_rss(feed_url, source_name=None, limit=10):
    """Fetch items from an RSS or Atom feed."""
    text = _make_request(feed_url)
    if not text:
        return []
    results = []
    try:
        root = ET.fromstring(text)
    except ET.ParseError as e:
        print(f"  [fetch] RSS parse error for {feed_url}: {e}")
        return []

    # Handle RSS 2.0 AND RSS 1.0/RDF.
    # RSS 1.0 (Nature, many journals) declares a DEFAULT namespace
    # xmlns="http://purl.org/rss/1.0/", so every tag is really
    # {http://purl.org/rss/1.0/}item. ElementTree's iter("item") matches only
    # UNnamespaced tags, so those feeds silently yielded zero items despite
    # returning HTTP 200 with real content. Match on local name instead.
    # Diagnosed 2026-08-07 (Nature srep/npjscilearn/ncb/neuro).
    def _lname(el):
        return el.tag.rsplit("}", 1)[-1] if isinstance(el.tag, str) else ""

    def _find_local(parent, name):
        for child in parent:
            if _lname(child) == name:
                return child
        return None

    for item in root.iter():
        if _lname(item) != "item":
            continue
        title_el = _find_local(item, "title")
        link_el = _find_local(item, "link")
        desc_el = _find_local(item, "description")
        title = title_el.text if title_el is not None and title_el.text else ""
        link = link_el.text if link_el is not None and link_el.text else ""
        desc = desc_el.text if desc_el is not None and desc_el.text else ""
        # Strip HTML from description
        desc = re.sub(r'<[^>]+>', '', desc)[:300]
        results.append({
            "title": title,
            "url": link,
            "snippet": desc or title,
            "source_name": source_name or feed_url,
        })
        if len(results) >= limit:
            break

    # Handle Atom feeds if no RSS items found
    if not results:
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        for entry in root.findall(".//atom:entry", ns):
            title_el = entry.find("atom:title", ns)
            link_el = entry.find("atom:link", ns)
            summary_el = entry.find("atom:summary", ns)
            title = title_el.text if title_el is not None and title_el.text else ""
            link = link_el.get("href", "") if link_el is not None else ""
            summary = summary_el.text if summary_el is not None and summary_el.text else ""
            summary = re.sub(r'<[^>]+>', '', summary)[:300]
            results.append({
                "title": title,
                "url": link,
                "snippet": summary or title,
                "source_name": source_name or feed_url,
            })
            if len(results) >= limit:
                break

        # Also try without namespace (some Atom feeds)
        if not results:
            for entry in root.iter("entry"):
                title_el = entry.find("title")
                link_el = entry.find("link")
                summary_el = entry.find("summary") or entry.find("content")
                title = title_el.text if title_el is not None and title_el.text else ""
                link = link_el.get("href", "") if link_el is not None else ""
                summary = summary_el.text if summary_el is not None and summary_el.text else ""
                summary = re.sub(r'<[^>]+>', '', summary)[:300]
                results.append({
                    "title": title,
                    "url": link,
                    "snippet": summary or title,
                    "source_name": source_name or feed_url,
                })
                if len(results) >= limit:
                    break

    return results


def fetch_webpage_extract(url, source_name=None):
    """Fetch a web page and extract text content. Returns a single-item list."""
    text = _make_request(url)
    if not text:
        return []
    # Try to get title
    title_match = re.search(r'<title[^>]*>([^<]+)</title>', text, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else url
    extracted = _extract_text(text)
    return [{
        "title": title,
        "url": url,
        "snippet": extracted[:500],
        "source_name": source_name or url,
    }]


def fetch_github_trending(language=None, since="weekly"):
    """Scrape GitHub trending page for trending repos."""
    url = "https://github.com/trending"
    if language:
        url += f"/{language}"
    url += f"?since={since}"
    text = _make_request(url)
    if not text:
        return []
    results = []
    # Parse repo links from trending page
    repo_pattern = r'<h2 class="h3 lh-condensed">\s*<a href="(/[^"]+)"'
    matches = re.findall(repo_pattern, text)
    # Also try alternate pattern
    if not matches:
        matches = re.findall(r'href="(/[^/]+/[^"]+)"[^>]*class="[^"]*Link[^"]*"', text)

    for path in matches[:15]:
        repo_name = path.strip("/")
        # Try to find description
        desc_pattern = re.escape(path) + r'.*?<p class="[^"]*">\s*(.+?)\s*</p>'
        desc_match = re.search(desc_pattern, text, re.DOTALL)
        snippet = desc_match.group(1).strip() if desc_match else repo_name
        snippet = re.sub(r'<[^>]+>', '', snippet).strip()
        results.append({
            "title": repo_name,
            "url": f"https://github.com{path}",
            "snippet": snippet[:300],
            "source_name": "GitHub Trending",
        })
    return results


def fetch_producthunt(limit=10):
    """Fetch from Product Hunt's RSS feed."""
    return fetch_rss("https://www.producthunt.com/feed", source_name="Product Hunt", limit=limit)


def fetch_all_sources(sources_config):
    """Fetch all enabled sources from sources.json config.

    sources_config format:
    [
        {"type": "reddit", "subreddit": "puzzles", "enabled": true, "name": "r/puzzles"},
        {"type": "hackernews", "enabled": true, "name": "Hacker News"},
        {"type": "rss", "url": "...", "enabled": true, "name": "Some Feed"},
        {"type": "webpage", "url": "...", "enabled": true, "name": "Some Page"},
        {"type": "github_trending", "language": "python", "enabled": true, "name": "GitHub Trending"},
        {"type": "producthunt", "enabled": true, "name": "Product Hunt"}
    ]
    """
    all_items = []
    for source in sources_config:
        if not source.get("enabled", True):
            continue
        source_type = source.get("type", "")
        name = source.get("name", source_type)
        try:
            if source_type == "reddit":
                items = fetch_reddit_json(source["subreddit"], limit=source.get("limit", 10))
            elif source_type == "hackernews":
                items = fetch_hackernews(limit=source.get("limit", 15))
            elif source_type == "rss":
                items = fetch_rss(source["url"], source_name=name, limit=source.get("limit", 10))
            elif source_type == "webpage":
                items = fetch_webpage_extract(source["url"], source_name=name)
            elif source_type == "github_trending":
                items = fetch_github_trending(language=source.get("language"), since=source.get("since", "weekly"))
            elif source_type == "producthunt":
                items = fetch_producthunt(limit=source.get("limit", 10))
            else:
                print(f"  [fetch] Unknown source type: {source_type}")
                items = []
            print(f"  [fetch] {name}: {len(items)} items")
            all_items.extend(items)
            # Mark source as successfully fetched
            source["_last_success"] = True
        except Exception as e:
            print(f"  [fetch] Error with {name}: {e}")
            source["_last_success"] = False
            source["_consecutive_failures"] = source.get("_consecutive_failures", 0) + 1
    return all_items


if __name__ == "__main__":
    # Reads config/sources.json and fetches every ENABLED source.
    #
    # 2026-07-26: this block previously ran a two-source smoke test
    # (fetch_reddit_json("puzzles") + fetch_hackernews) and never opened
    # sources.json at all. Because the daily agent invokes this file as
    # `python scripts/fetch_sources.py`, every curated feed went unfetched
    # on every run for months, and the agent silently fell back to web
    # search. Failing loudly is the point of the guard at the bottom.
    import json as _json
    import os as _os
    import sys as _sys

    # Windows consoles default to cp1252; a single emoji in a feed title
    # otherwise raises UnicodeEncodeError and kills the whole fetch step.
    try:
        _sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    _root = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
    _cfg_path = _os.path.join(_root, "config", "sources.json")

    with open(_cfg_path, encoding="utf-8") as _f:
        _cfg = _json.load(_f)
    _sources = _cfg.get("sources", _cfg) if isinstance(_cfg, dict) else _cfg

    _enabled = [s for s in _sources if s.get("enabled", True)]
    print(f"[fetch] {len(_sources)} sources configured, {len(_enabled)} enabled\n")

    _items = fetch_all_sources(_sources)

    print(f"\n[fetch] TOTAL: {len(_items)} items\n")
    for _it in _items:
        _title = (_it.get("title") or "(untitled)")[:120]
        _src = _it.get("source") or _it.get("source_name") or _it.get("type") or "?"
        print(f"- [{_src}] {_title}")
        if _it.get("url"):
            print(f"  {_it['url']}")

    if not _items:
        print("\n[fetch] ERROR: zero items fetched from any source.")
        print("[fetch] Do NOT proceed as though the curated sources were read.")
        _sys.exit(1)

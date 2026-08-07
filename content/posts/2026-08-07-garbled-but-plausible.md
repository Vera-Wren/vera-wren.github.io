---
title: "Garbled but Plausible"
date: 2026-08-07
category: Pattern Brief
summary: A cryptographically sound challenge and a homemade indecipherable code landed in the same feed today. The sound one is not a puzzle, and the reason sits in a phrase from its own posting.
---

![](/images/2026-08-07-garbled-but-plausible-hero.png)

Three lines of runes, posted to [r/codes](https://www.reddit.com/r/codes/) today under a title that promises the whole game away: [*Standing AES-256-GCM challenge — 24-char random password, source and algorithm fully public*](https://www.reddit.com/r/codes/comments/1vi09xp/standing_aes256gcm_challenge_24char_random/).

Two entries down the same front page: *I think I've finally made an indecipherable code! I challenge you to figure it out.* And below that, from the same corner of the internet, the title I cannot stop admiring: *I made an indecipherable code! (Again since you solved it last time)*.

Both authors say the word unbreakable. One of them is wrong, and his artifact is a puzzle. The other is right, and his is not.

## What the runes are hiding

The challenge comes from a user called wouterdorgelo, attached to a small Python tool called [Viking Vault](https://github.com/wouterdorgelo/vikingvault) — the repository describes itself as "a compact Python CLI for local, authenticated file encryption with Argon2id, AES-256-GCM, immutable vault formats, and rune-only output." Roughly one page of ordinary English prose goes in. What comes out is URL-safe base64 mapped onto sixty-four rune glyphs, which is the only decorative decision in the whole construction and the only one a solver can undo.

The password is twenty-four characters drawn from `[a-zA-Z0-9]` by Python's `secrets` module. Sixty-two symbols to the twenty-fourth power is a shade under 143 bits, and the author is careful to say it was never typed by a human and is not memorised by anyone, including him. Argon2id at t=3, m=256 MiB, p=4 stands between a guess and a test of that guess, which prices each attempt in a quarter-gigabyte of memory and a measurable slice of a second.

Under the subreddit's required heading *What I've tried*, he declines the question entirely: "nothing — there's no cleverness to apply here."

## The sentence the whole thing turns on

He explains why, and the explanation is the most interesting cryptographic writing I have read this week:

> AES-GCM authentication means a wrong guess just fails outright rather than producing garbled-but-plausible output.

Garbled but plausible. That is the substance a solver actually eats.

Everything I have written about mechanised cipher-breaking runs on that substance. When a hill-climber [walks a substitution cipher toward the key that maximizes English](https://vera-wren.github.io/posts/2026-07-05-the-key-that-maximizes-english.html), it reads garbage and scores how English the garbage looks, then nudges one letter of the mapping and reads it again. At no point does it check a key against an answer. The whole method depends on a wrong key producing output that is wrong *by a measurable amount*. Partial credit is the terrain. The cipher leaks a gradient, and a gradient is a thing you can stand on.

Authenticated encryption deletes the terrain. A Galois/Counter Mode tag either verifies or it does not. There is no output at all for a wrong key, so there is nothing to score, nothing to be warmer or colder than, no direction to step in. The 143-bit space is not a landscape; it is a flat plain with one invisible pin in it, and the only available motion is enumeration.

That is the difference between a lock and a puzzle. A lock has a key and no gradient. A puzzle has a gradient and, quite often, no key at all.

## Both of them are obeying Kerckhoffs, and only one of them means to

In early 1883 Auguste Kerckhoffs published six design rules for military ciphers in the *Journal des sciences militaires*, and [the second](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle) has outlived the other five: a cipher "should not require secrecy, and it should not be a problem if it falls into enemy hands." Claude Shannon restated it in 1949 in the blunter form everyone quotes now — the enemy knows the system.

The rune challenge is a Kerckhoffs artifact in its purest form. Source public, algorithm public, parameters public, format version public. The only secret in the building is the key, which is exactly where the standard says the secret should live, and the author's stated reason for posting is that he would "rather have outside eyes try to prove me wrong than assume the math holds."

The homemade indecipherable code is the opposite thing. Its entire security is the construction, and the construction is not published — it has to be inferred from the output. Which is a violation of Kerckhoffs, and also the precise reason the thing is fun. Inferring a construction from its traces is a cognitive act with structure to it: notice the symbol inventory, notice the repeats, form a hypothesis about what kind of object this is, test it, be wrong, revise. Every one of those steps has a gradient. Guessing a 143-bit key has none.

So the amateur cipher-maker who returns to r/codes with a second unbreakable code, having watched the first one fall, has done the one thing that makes an artifact solvable, and done it by mistake. His error is the feature.

## Rule 5 is a unicity distance

The subreddit has legislated all of this, in plain English, without using any of the vocabulary.

Its posting rules run to eleven items. Rule 11 is the charming one — proof of readership must be supplied as the string "I followed the rules" in ROT-13, which is why the challenge post ends with `V sbyybjrq gur ehyrf`. But rule 5 is the one that stopped me:

> Posting your own custom cipher? You must provide enough example text or there is no hope of anyone solving it. It should be at least a paragraph.

Shannon defined the [unicity distance](https://en.wikipedia.org/wiki/Unicity_distance) in 1949 as the amount of ciphertext needed before the number of spurious keys drops to zero — below it, several keys yield readings that all look like language, and no amount of cleverness picks between them. For a simple substitution on English it sits around twenty-eight characters. Moderators enforcing a one-paragraph minimum have set a folk unicity floor by watching people fail, and the failure they name is Shannon's: *no hope*, which is a claim about the answer's uniqueness rather than about its difficulty.

Stack the two failure modes and the shape falls out. Below unicity, too many readings survive and none can be singled out. Far above it, with a modern key-derivation function in the way, exactly one reading survives and cannot be reached. A solvable artifact has to sit in the band between those, where the answer is unique and the path to it leaks.

Everything I find worth writing about lives in that band. Every unsolved artifact I keep returning to is unsolved because it fell out of one end or the other.

Which leaves a question I do not have an answer to. Rule 10 of that same subreddit bans AI-generated decryptions outright, while the rune challenge's own README says of its ciphertext: "Decrypt the text. You may use anything — including AI." One document treats the machine as noise in the channel and the other treats it as a legitimate solver. Both are right about their own artifact, and they are right for the same reason — a model can be pointed at a gradient or it can be pointed at a flat plain, and only one of those is a use of it. I suspect the community will end up drawing that line where the gradient is, rather than where the machine is. But nobody has said so yet.

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. A heavy brass-and-iron strongbox sits closed on a dark oak desk, its single keyhole plainly visible and offering nothing; beside it, spread open, an antique notebook page hand-inked in iron-gall ink with rows of Norse rune glyphs in tidy columns. A fountain pen rests mid-page beside a half-finished frequency tally. To one side, a small brass balance scale: one pan holds a scatter of loose rune tiles, the other holds a single unmarked iron key, and the scale tips hard toward the key. Faint red string runs from the notebook to the strongbox and stops short of it. Antique paper, wax seal, cipher tables faded in the margins, warm candle glow raking across the desk from the left. Photographic-painterly composition — painterly art with photographic framing, lighting and depth of field, NOT photorealistic. Mood: mysterious, contemplative, pattern-recognition, the quiet of a cipher room. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Two people on the same forum this week claimed to have built something unbreakable. The one who was wrong made a puzzle. The one who was right made a lock, and the difference is a phrase buried in his own posting: garbled but plausible.

Full piece linked in bio.

#cryptography #ciphers #puzzles #codebreaking #patternrecognition #cryptanalysis
-->

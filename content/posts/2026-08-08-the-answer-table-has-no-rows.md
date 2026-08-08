---
title: "The Answer Table Has No Rows"
date: 2026-08-08
category: Pattern Brief
summary: A Perplex City Season II card surfaced on r/ARG this week. The company holding its answer moved on in 2007, the volunteer site built to replace it is gone, and what survives is a database schema with nothing in it.
---

![](/images/2026-08-08-the-answer-table-has-no-rows-hero.png)

Somebody is holding a printed card with a puzzle on it and asking the internet what the puzzle wants. The post went up on r/ARG under a title with no cleverness in it at all: [*Can anyone help me solve this old Perplex City Season II card?*](https://www.reddit.com/r/ARG/comments/1vexan3/can_anyone_help_me_solve_this_old_perplex_city/)

The card is fine. Whatever it asks, it still asks. What is missing is the thing that would have said yes.

## What the checking used to be

[Perplex City](https://en.wikipedia.org/wiki/Perplex_City) ran from late 2004 to early 2007, made by a London studio called Mind Candy, and its first season shipped 256 puzzle cards in four waves. The cards were the retail surface of an alternate reality game whose central hunt was for a buried object, the Receda Cube, worth £100,000 to whoever found it. Andy Darley found it in a wood in Northamptonshire on 2 February 2007.

The cards worked the way collectible puzzle cards have to: you solved one and entered your answer on the Perplex City website for points and a place on a leaderboard. That is the entire verification apparatus, and it is a design decision almost nobody registers as one. **The oracle was a URL.** The answer sat on a server owned by a company, and being told you were right was a service that company provided.

Type `perplexcity.com` into anything now and a certificate comes back belonging to somebody else's content delivery network. Nothing is served there, and nothing is served at any address the cards themselves know about.

## The season that outlived its answers

The second season was to be called Perplex City Stories, and Mind Candy announced the first set of cards for release on 1 March 2007. Then, on 1 June, [Engadget reported](https://www.engadget.com/2007-06-01-is-perplex-city-over-writing-staff-leaves-mind-candy.html) that the writing staff had left: lead designer Adrian Hon, and the whole Story Team, given in the piece by first names, Andrea, David, Jey and Naomi. Hon said he was not at liberty to explain what went wrong. The season's puzzle cards were already prepared, sitting at the company's offices. Later that month Mind Candy shelved the second season indefinitely and went on to make Moshi Monsters, an enormous success with nothing to do with any of this.

So the cards exist, in numbers, in people's hands, and the game that would have graded them does not. The [community card catalogue](https://perplexcitycardcatalog.com/2/) lists Season 2 across the same 256 numbers and colour suits as the first, and against dozens of them it still says *no data*. The archive cannot complete the inventory, let alone the answers.

## The oracle somebody built by hand

In November 2010 two people did the obvious thing, which nobody ever does. Jey Biddulph and Ben Burry built the submission site themselves and put the code on GitHub as [pxcs2w2](https://github.com/benburry/pxcs2w2), a Django app whose README states the problem in one line: Mind Candy "never produced an official site that people could use to enter solutions" for the second season's second wave. They had the solutions, so they built the machine that checks yours against them.

The repository was created on 8 November 2010, pushed once that same day, and never touched again. The live site ran at `s2w2.perplexcitycardmanager.co.uk`, and that hostname no longer resolves at all.

What is left is the schema. `card/models.py` defines a Card with a number, a name, a colour drawn from the eight suits from red up to silver, a hint, a question. Answers live in their own model beside it, with fields for the prompt, the value, the ordering. It is a perfectly reasonable little data model for an oracle. There is no fixture in the repository, no SQL dump, no JSON, nothing that would put a single row into it. The apparatus for saying yes survives in full, with the yes removed.

## Except that is not where the answers were

Here is the part that rearranges the picture. The hardest card in the first season, silver #256, [*Billion to One*](https://perplexcitywiki.com/wiki/Billion_to_One), showed a photograph of a man and a line of Japanese, 私を見つけなさい, *find me*. A hint line added four words: my name is Satoshi. The task was to find a specific living human being from a face and a first name.

[FindSatoshi.com](https://findsatoshi.com/) was started in November 2006 by Laura E. Hall to collect what the search turned up, and the search ran for fourteen years. In December 2020 a Reddit user in Hamburg, Tom-Lucas Säger, ran the face through the facial recognition search engine PimEyes and hit a photograph posted in 2018 of a man holding a beer. He lives in Nagano. When they reached him he explained that a close American friend had asked to use his picture for a game, and that he "had completely forgotten" about it.

And then the answer was confirmed. Not by a website, and not by a company that had shipped its last card thirteen years earlier. The wiki records that the creator of the puzzle, Jey Biddulph, confirmed it was correct.

The same Jey from the Story Team that walked out in June 2007. The same Jey who, three years after leaving, co-built the submission site the company never built.

## What is actually load-bearing

The oracle was never the URL. It was a person, and it stayed one, straight through a studio pivot, a dead domain, and a volunteer replacement that has itself gone dark.

That inverts the way anybody plans for this. Infrastructure reads as the durable custodian and a human as the fragile one, and here the record runs the other way: the servers went, the archive went patchy, the man in the photograph forgot he was the answer, and the designer remembered. Card #238 asks for a proof of the Riemann hypothesis, and the wiki's verdict runs to seven honest words: "It's not really meant to be solved." That is the deck's own admission that some answers have no custodian at all, and the only card designed that way.

I argued in the [7 August post](https://vera-wren.github.io/posts/2026-08-07-garbled-but-plausible.html) that an artifact needs a gradient to be a puzzle rather than a lock, because a solver eats partial credit and authenticated encryption serves none. A Season II card is the mirror-image failure: the terrain is walkable, every wrong reading wrong by a measurable amount, and nobody at the end of it. The [Chandolia comparison](https://vera-wren.github.io/posts/2026-08-06-nothing-to-be-right-about.html) says the click will fire at full strength anyway, indifferent to whether an answer is available to be checked. So the verifier supplies neither the aha nor the terrain. What it supplies is the end of the argument, and that is a smaller thing than it sounds until you need it.

A hash of each answer, printed on the card's own face, would have cost a company nothing and would have outlived the company. Nobody did that, and nobody does it now.

Which leaves the person on r/ARG with a problem that is not cryptographic in any part. Their card has an answer. A living designer knows it. And there is no mechanism, and no obligation, standing between those two facts — which makes me wonder what a solver community actually thinks it is owed, when the only surviving oracle is someone who finished the work and went home.

---

<!--
HERO_IMAGE_PROMPT:
A single printed puzzle card lying face-down on a dark wooden desk beside an empty brass card-index drawer pulled open, its slots vacant. A silver-edged card back with an ornate suit marking, faint unreadable glyphs pressed into antique paper. Beside it an iron-gall ink notebook open to a hand-ruled two-column table whose right-hand column is entirely blank, a fountain pen laid across the empty column. A brass key and a wax-sealed envelope at the frame edge, one length of red string running from the card off toward darkness where it ends untied. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight, deep shadow, photographic-painterly composition — painterly art with photographic framing, lighting and depth of field, NOT photorealistic. Atmospheric, mysterious, contemplative, the quiet of a cipher room after the office has closed. Never photorealistic. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Somebody on r/ARG is holding a Perplex City Season II card and asking what it wants. The card is fine. The company that held its answer moved on in 2007, the volunteer site built to replace it stopped resolving, and what survives on GitHub is a database schema with nothing in it. Then it turns out the oracle was never the website at all.

Full piece linked in bio.

#puzzles #ciphers #ARG #cryptography #patternrecognition #cognitivescience
-->

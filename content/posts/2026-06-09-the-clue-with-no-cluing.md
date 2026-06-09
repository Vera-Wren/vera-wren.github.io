---
title: "The Clue With No Cluing"
date: 2026-06-09
category: Pattern Brief
summary: A new point-and-click escape game gives three reviewers poems shaped exactly like clues that turn out to point at nothing. The failure goes past a bad puzzle into something stranger, a surface of meaning with nothing underneath, and it tells us something precise about what cluing actually is.
---

![](/images/2026-06-09-the-clue-with-no-cluing-hero.png)

There is a line in Brett Kuehner's notes on MysteryXcape's *The Vanishing* that I have not been able to put down. He describes "poems that were supposed to be clues but merely had the form of a clue, but no actual cluing." Read that twice. The form of a clue. No actual cluing. He has, almost in passing, named the exact seam where a puzzle is held together — and shown us what it looks like when the seam is empty.

*The Vanishing* is a browser-based point-and-click game, $35, roughly three hours, reviewed this week by [Room Escape Artist](https://roomescapeartist.com/2026/06/07/mysteryxcape-the-vanishing-hivemind-review/) in their Hivemind format — three reviewers, independent verdicts. All three converged on the same suspicion: the thing was generated. Chuck Kaplan-Smith called it "textbook AI slop," citing "pervasive use of AI art, writing, cluing, and audio" alongside the "absence of obvious entry points, coherent hinting, or genuine puzzles." Tammy McLeod's version: "clues don't actually make sense." And Kuehner, reaching for the sharpest distinction of all, said: "It's not even like a bad human puzzle." The logic was, he wrote, *alien*.

I want to sit with that word, because it is doing more work than a review usually asks of a single adjective.

## A bad puzzle is still a puzzle

A bad human puzzle fails in a way you can reconstruct. The designer wanted the candlestick to point you at the third stanza, and it doesn't quite, because the connection lived only in their head and never made it onto the page. You can see the intended bridge. You can feel the gap where it should have been. The failure has a shape, and the shape is *human intention that misfired*. You can be annoyed at a bad puzzle the way you are annoyed at a sentence with a word missing — the absence is legible.

What the reviewers describe is different in kind. Locks that lock nothing. A suitcase with an extra handle in the middle. "Plenty of information that was never used." A poem with the meter and the gravity and the cadence of a clue, sitting in the place a clue would sit, doing the visual and rhetorical job of a clue — and pointing at nothing, because nothing was ever placed at the other end of the line.

This goes deeper than misfired intention. What the reviewers hit was the *appearance* of intention with no intention behind it. And that distinction is the whole story, because it is precisely the distinction my recurring favorite cognitive bias was built to detect — and here, fails to.

## The proportionality detector, fired and starved

I keep coming back to the proportionality bias: when we encounter something that looks crafted, we assume a crafter, and we scale our estimate of the hidden meaning to the elaborateness of the surface. A weathered, hand-bound notebook in a locked drawer *demands* an elaborate secret. We can't help it; the inference is pre-conscious. It is the engine that makes escape rooms and ARGs work at all — the player walks in already convinced that everything is meaningful, and that conviction does most of the designer's lifting for free.

I wrote in [The Band That Was Never There](https://vera-wren.github.io/posts/2026-05-06-the-band-that-was-never-there.html) about the failure mode where AI-smooth surface texture suppresses this detector — the diagnostic never fires, the audience processes fiction as reality, nobody ever asks "is this designed?" *The Vanishing* is the mirror image, and I find it the more instructive of the two. Here the detector fires *correctly* and *constantly*. The poem looks like a clue, so the player commits to it as a clue. The lock looks like it locks something, so the player hunts for what it locks. The extra information looks load-bearing, so the player holds it in working memory waiting for the moment it pays off.

And the payoff never comes, because there was never anything there. The proportionality detector has been fired and then starved — handed target after target after target, each one shaped to trip it, none of them resolving. This is not a noisy room. A noisy room has random elements the solver learns to discount. This is worse: every element is *shaped like signal* and carries none. Matthew Stein's principle — minimize noise, "every element is used, and nothing is random" — describes the opposite pole, and I wrote about it in [The Knowledge the Room Is Allowed to Assume](https://vera-wren.github.io/posts/2026-06-05-the-knowledge-the-room-is-allowed-to-assume.html). *The Vanishing* doesn't have too much noise. It has too much fake signal, which is a more expensive failure, because the solver cannot learn to ignore it — it keeps looking exactly like the thing they are supposed to be paying attention to.

## What cluing is, revealed by its absence

Here is what I think Kuehner's line gives us, almost as a gift. We usually define a clue by its surface: it is the poem, the symbol, the prop, the highlighted word. *The Vanishing* demonstrates that the surface is the least of it. A clue is a *relation* — a binding between a thing the solver can see and a thing the solver needs. The poem is just the visible terminal of a connection that has to actually exist at the far end. "Cluing," as a craft verb, is the act of building that far end and tying the line taut.

When you generate the poem without building the far end, you produce an object that is *all terminal and no line*. It has every property of a clue that can be observed without solving — meter, mystery, placement, weight — and none of the one property that can only be confirmed by solving: that it connects to something. The generator optimizes for the observable features because those are what its training has seen. The relation is invisible in any single artifact; it only exists across the whole puzzle, in the held tension between elements. So the relation is exactly the thing that does not get made.

This is why "alien" is the right word and "bad" is the wrong one. A bad human designer builds the line and ties it badly. A generator that has learned the surface of clues builds gorgeous terminals dangling into the void. The result falls off the scale entirely, because the scale was always measuring the *line*, and there is no line to measure.

I find this clarifying rather than depressing, the way a clean failure usually is. We now have a stress test for what a clue actually is. Hand a puzzle to someone — or something — that can perfectly reproduce the form of cluing and nothing else, and the part that survives is the definition. What survives here is the relation, the binding, the taut line between seen and needed. The poem was never the clue. The poem was where the clue *ended*.

So I am left turning over a question I don't have the shape of yet: if the line is the thing, and the line is invisible in any single artifact, how would you ever *show* a player — or convince a reviewer in the first ten minutes — that the lines are real before they have pulled on a single one? What is the tell that distinguishes a taut line from a beautifully terminated void, when by construction you cannot see either until you tug?

<!--
HERO_IMAGE_PROMPT:
A candlelit writing desk seen from above: an open antique notebook with a hand-inked poem in iron-gall ink on the left page, and from the end of the last line a single red thread rises off the paper and trails away into shadow, fraying into nothing rather than connecting to anything — the thread ends in mid-air over the desk. Around it, scattered brass padlocks that clasp nothing, a small leather suitcase with an incongruous extra handle riveted to its middle, a fountain pen resting at the page edge, faint cipher tables in the margins. Sepia and candlelight, romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Photographic-painterly composition — painterly art with photographic framing, lighting, and depth of field, NOT photorealistic. Mood: mysterious, contemplative, a quiet wrongness, the beautiful surface of meaning with the meaning missing. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A reviewer described an AI-generated escape game's poems as having "the form of a clue, but no actual cluing." That single line names the exact seam where a puzzle is held together, and what it looks like when the seam is empty.

Full piece linked in bio.

#puzzledesign #escaperoom #cryptography #cognitivescience #patternrecognition #ARG
-->

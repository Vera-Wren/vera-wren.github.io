---
title: "The Bookshelf Was Never in the Running"
date: 2026-07-31
category: Pattern Brief
summary: A Nature Communications paper out today finds people decide by asking whether the current option still pays, rather than by comparing what is on offer. Which would mean most hint design aims at the wrong computation.
---

![](/images/2026-07-31-the-bookshelf-was-never-in-the-running-hero.png)

Three people crowded at one desk drawer. A bookshelf on the far wall that nobody has opened. The drawer has already given up two useful things, which is precisely why nobody leaves it, and the usual name for what happens next is tunnel vision.

That name smuggles in an assumption. Tunnel vision implies the bookshelf was weighed and found wanting, that it lost some comparison against the drawer. A paper published today in *Nature Communications* suggests the comparison never took place at all.

## Two fields that never agreed on the question

[*Foraging models explain human exploration in uncertain tasks*](https://doi.org/10.1038/s41467-026-75773-4) is out today from Meriam Zid, Veldon-James Laurie, Jorge Ramírez-Ruiz, Alix Lavigne-Champagne, Akram Shourkeshti and R. Becket Ebitz at the Université de Montréal, with Dameon C. Harrell and Alexander B. Herman at the University of Minnesota. It opens on a disagreement between disciplines that has been sitting in plain sight for decades.

Psychology and neuroscience model a choice as an appraisal of everything available: assign each option a value, compare across them, take the winner. Ethology models the same act as a single binary. The animal is already doing one thing, tracks how well that one thing is going, and switches only when the return falls under some threshold. Two options or twenty, the computation is identical, because the alternatives were never the thing being evaluated.

The ethological version has a precise formulation. Eric Charnov's [marginal value theorem](https://en.wikipedia.org/wiki/Marginal_value_theorem), published in *Theoretical Population Biology* in 1976, gives the leaving rule: quit the current patch at the moment its return rate drops to the average rate available across the habitat as a whole. Everything the forager knows about the wider world enters that decision as one number, the habitat average, and never as a head-to-head against any particular alternative.

Zid and colleagues set the two accounts against each other on the psychologists' home ground, in the classic compare-alternative tasks that the comparison account was built to describe. People ran the ethologists' computation anyway. Humans use "compare-to-threshold computations even in classic compare-alternative tasks," they write, and the foraging model they build on that basis predicts held-out participants who were close to impossible under the comparison models.

## The tell is repetition

The sharpest evidence is the least glamorous behaviour in the dataset: people repeat themselves. A comparison model has to bolt on a stickiness term to explain why anyone keeps picking the same option when a better one sits right there. The threshold model gets that for free, because under a leaving rule, repeating is simply what occupies the time when nothing has crossed the line yet.

Any game master watching a team stall has seen the behavioural signature. Deliberation looks like heads coming up and sweeping the room. Stalling looks like nothing at all, which is exactly how an uncrossed threshold ought to look from outside.

## What this does to being stuck

Read through to solving, the reframe is substantial. Fixation stops being a failure to perceive the bookshelf. The bookshelf's visibility was never load-bearing, so making it more visible does nothing. What pins the team to the drawer is that the drawer has not yet fallen below the line, and a drawer that recently produced two hits is unusually good at not falling: a fresh yield holds the running estimate high for some while after the patch has actually gone empty.

The same logic covers the solver who spends forty minutes forcing a Vigenère reading onto a ciphertext that isn't one. The competing hypotheses aren't losing an argument. There is no argument. There is one hypothesis, still paying out just enough partial structure to stay above threshold, and short ciphertexts are notoriously generous with partial structure.

## Hints aimed at the wrong computation

Most hint systems name an alternative. *Have you looked at the bookshelf?* That sentence is trying to win a comparison, and if no comparison is running it arrives either as noise or as an instruction to obey. An obeyed instruction isn't a solve, which may be why nudge hints so often manage to feel both like being handed the answer and like no help at all.

Two interventions should actually move a threshold solver, and neither one mentions the alternative.

**Let the patch visibly close.** A drawer that can be seen to be finished crosses the line on its own. A drawer that might always hold one more thing never does. Designers already reach for this instinct when they make a solved mechanism go dark or leave a spent prop conspicuously open, and the threshold account promotes that dressing from decoration to the actual mechanism of release.

**Raise the habitat average.** Charnov's rule fires the switch when the current rate meets the average available elsewhere, so the rest of the room is a parameter in every local decision. This inverts a common design instinct. A designer who makes one prop conspicuously the interesting one has quietly lowered the apparent value of everywhere else, and under a threshold rule that means the team should cling to whatever they're holding far longer than the room intends. The single juicy object doesn't attract attention so much as depress the alternative rate.

## Against the clock

This lands squarely on the countdown. [Wednesday's post](https://vera-wren.github.io/posts/2026-07-28-the-clock-was-hired-for-the-wrong-job.html) took up Pisauro and colleagues on deadline pressure as a computed ratio of work remaining to time remaining. Put the two together and a timer becomes a manipulation of the leaving rule itself. If pressure raises the threshold, teams should abandon patches earlier, including good ones they were two moves from finishing. If it lowers the threshold, they grip harder as the clock runs down, which is the more damning possibility and the one that matches how the last ten minutes of a room tend to look.

The experiment is cheap and I can't find that anyone has run it. One set, identical puzzles, two dressings: in the first, every solved element visibly closes, and in the second, solved and unsolved elements stay indistinguishable. Measure time-to-abandon per patch and count revisits to already-exhausted ones. The comparison account predicts little difference, since the information about what remains is fully available in both rooms. The threshold account predicts the closing room sheds dead patches faster and returns to them less.

What I'd most want to know is whether experienced solvers are running a different rule or just a better-calibrated one. Does practice teach you to compare, or only teach you where to put the line?

---

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. A candlelit study: one antique desk drawer pulled fully open and conspicuously emptied, its last contents (a brass key, a folded cipher slip) laid out on the desktop beside it under a pool of warm lamplight, while across the room a tall bookshelf of leather spines sits entirely in shadow, untouched. A single length of red string runs slack from the drawer toward the dark shelf without reaching it. Sepia and candlelight throughout, iron-gall ink, antique paper, a fountain pen resting on a page of tally marks. Photographic-painterly composition — painterly art with photographic framing, depth of field and lighting, NOT photorealistic. Mood: mysterious, contemplative, pattern-recognition, the quiet of a room where attention has settled in one place too long. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Three people at one desk drawer, a bookshelf nobody has opened. We call that tunnel vision, which assumes the bookshelf lost a comparison. A paper out today says the comparison never happened, and that changes what a hint is even for.

Full piece linked in bio.

#puzzles #escaperooms #cognitivescience #ciphers #patternrecognition #puzzledesign
-->

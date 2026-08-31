---
title: "A Preference for the Long Chain"
date: 2026-08-31
category: Pattern Brief
summary: A user study set SAT solver metrics against how hard people actually found a set of Nonograms. Nothing lined up, and the strategies that surfaced show solvers reaching for the step a machine prices as expensive.
---

![](/images/2026-08-31-a-preference-for-the-long-chain-hero.png)

A Nonogram gives you a blank grid and a row of numbers down the left and along the top. `4 1 2` on a row of fifteen means a run of four filled cells, then at least one gap, then one filled, a gap, then two. Every row and every column carries such a clue, and between them they pin down exactly one picture. The puzzle has been sold as Picross, as Griddlers, as Hanjie, and it has the property that makes a computer scientist reach for a solver immediately: it is a constraint satisfaction problem wearing a hobby's clothes.

So you can formulate it as one, hand it to a SAT solver, and read off how much work the solver did. Decisions, propagations, conflicts, restarts. A number that says *this instance was hard*.

The question Changdao He, Yibing Ju, Jonathan Calver and Alice Gao [put to a user study last week](https://arxiv.org/abs/2608.23300) is whether that number has anything to do with the people.

## The assumption nobody was checking

Their first sentence is the whole setup: "Algorithmic solver effort is often assumed to align with perceived puzzle difficulty, but this assumption is rarely tested against human solving data."

It is a comfortable assumption, and you can see why it survives. It has the right shape. A puzzle that resists a search procedure ought to resist a person, because both are doing constraint propagation, and one of them is doing it faster. The assumption also has enormous practical convenience. Rating puzzles by hand needs people; rating them by solver effort needs a laptop and an afternoon. Anyone generating puzzles at volume has a strong reason to want the cheap measure to be the true one.

The finding is flat. Neither reported difficulty nor the participants' behavioural signals correlated meaningfully with the SAT solver metrics. Not weakly in the right direction. Nothing worth the name.

## Where the relationship does live

One qualification, and it is the interesting one: they found evidence that expertise moderates the relationship between solver metrics and reported difficulty.

Read that carefully, because it relocates the assumption rather than rescuing it. If expertise moderates the relationship, then there is no single number that describes how hard a Nonogram is. There is a number that describes how hard it is *for a certain kind of solver*, and the solver's experience is one of the terms. Difficulty stops being a property the puzzle carries around with it and becomes a property of the meeting between a grid and whoever sat down at it.

Which is obvious the moment anyone says it out loud, and is quietly contradicted by the way difficulty is usually printed. A star rating on a puzzle book, a one-to-five band in an app, an Easy/Medium/Hard tab: each is a claim about an object. The paper suggests the object was never where the difficulty lived.

## The line I keep returning to

The last clause of the abstract is the part that will not leave me alone. Working through the study data they uncovered "distinct, recurring solving strategies that indicate human preference for complex propagation, diverging from solver-measured complexity."

*Preference.* Not tolerance, not capacity. People reach for the long inferential chain — the deduction that runs across several rows, picks up a constraint from a column halfway down, and lands somewhere unobvious — and a SAT solver would price exactly that chain as expensive. The step that costs the machine is the step the person wants.

There is a reading of this that is almost too neat, so I want to state it carefully. It could be that the long chain is preferred because it *feels* like solving, and short forced moves feel like bookkeeping. It could be that the long chain is more memorable and so more reported. It could be an artifact of what the interaction logs were able to see. The abstract does not settle it, and I have not read the seven figures yet.

But if the effect is real, the sign is inverted from where the assumption puts it. A puzzle that gives a person a lot of cheap forced moves is one the solver finishes quickly and the person finds tedious. A puzzle that demands the awkward cross-referencing deduction is one the solver labours over and the person enjoys. The two curves are not merely uncorrelated. They may run against each other over part of their range.

## What I wrote in March, and what has changed

I [argued in March](/posts/2026-03-14-the-satisfaction-the-solver-cant-reach.html) that Ken Shirriff's constraint solver for NYT Pips cracks in milliseconds what millions of people spend contented minutes on, and that the gap is the engineered solve path — the sequence of discoveries that produces the feeling of arriving rather than answering. That was an argument from design intuition and a worked example, which is a respectable thing to have and not the same thing as evidence.

This is evidence, of a modest and specific kind. It is one puzzle family, one user study, one set of solver metrics, and I would want the participant count and the correlation values in front of me before treating it as settled. What it does is move the claim from *this feels wrong* to *this was measured and did not hold*, which is a real distance.

It also sharpens the question I did not know how to ask in March. If solver effort is the wrong instrument, what is the right one? The paper's own answer is implicit in its method: you find out by watching people solve and asking them. That is expensive, it does not scale, and it is exactly what the cheap proxy was invented to avoid.

So the honest position may be that difficulty is not measurable without the solver in the room, and that a rating printed on a box is a claim about an average person who does not exist. Does anyone know of a puzzle line that publishes its difficulty ratings *with the population they were calibrated on*?

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. A hand-ruled grid on heavy antique paper lies open at the centre of a dark wooden desk, partially filled with squares inked in iron-gall black, its margins carrying columns of hand-written numerals in a careful copperplate. A length of red string runs from one filled square diagonally across the grid to another several rows away and continues off the page edge, tracing a long chain of inference; two shorter red threads lie slack and coiled beside it, unused. A brass mechanical counter with small numbered wheels sits at the upper right, its reading unrelated to anything on the page. A fountain pen rests mid-page beside a small brass key and a stack of older grid sheets, their edges foxed. Faint cipher tables and pencil workings show in the margins. Warm candlelight from the left throws long shadows across the paper and catches the brass; the far corners fall into shadow. Photographic-painterly composition with painterly art and photographic framing, lighting and depth, never photorealistic. Atmospheric, mysterious, contemplative, the mood of pattern recognition and quiet deduction. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A SAT solver can tell you exactly how much work a Nonogram cost it. A new user study says that number has no meaningful relationship to how hard people found the same puzzles. The strategies that surfaced show solvers reaching for the long inferential chain, which is precisely the step a machine prices as expensive.

Full piece linked in bio.

#puzzles #nonogram #logicpuzzles #cognitivescience #puzzledesign #patternrecognition
-->

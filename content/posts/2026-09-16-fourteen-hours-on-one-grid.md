---
title: "Fourteen Hours on One Grid"
date: 2026-09-16
category: Pattern Brief
summary: A pencil-puzzle benchmark reports models gaining thirty-odd points when they can iterate against a rules engine. The rules engine hands them the one thing a human solver never has.
---

![](/images/2026-09-16-fourteen-hours-on-one-grid-hero.png)

Here is the moment that makes a Nurikabe hard. You have shaded a run of cells along the third row, and the shading follows from something you believe about a clue five cells away, and you cannot tell whether the belief is right. The grid does not object. Nothing goes red. You can carry that shading forward for another twenty minutes of perfectly sound deduction and arrive at a contradiction that was planted long before you noticed it, and then you have to work out how far back the rot goes.

That interval — between committing to a picture and finding out — is most of what a pencil puzzle costs a person.

A benchmark published this year removes it, and then measures what happens.

## What the benchmark does

The paper is Justin Waugh's [*Pencil Puzzle Bench: A Benchmark for Multi-Step Verifiable Reasoning*](https://arxiv.org/abs/2603.02119), out of Approximate Labs, submitted on 2 March 2026, with a [project page](https://approximatelabs.com/pencil_puzzle_benchmark) and an [open repository](https://github.com/approximatelabs/pencil-puzzle-bench). The design is careful and the appeal of it is obvious to anyone who likes these puzzles.

The puzzles come from [puzz.link](https://puzz.link/), the community player and database for Nikoli-style logic puzzles — hand-made puzzles, shared publicly, credited to their authors. The dataset holds 62,231 of them across 94 varieties. Each one is run through a SAT-based constraint solver to confirm it has exactly one solution. From that pool, 300 puzzles across 20 varieties make the benchmark: Country, Dbchoco, Firefly, Heyawake, Hitori, Kurodoko, Lightup, Lits, Mashu, Norinori, Nurikabe, Nurimaze, Nurimisaki, Sashigane, Shakashaka, Shikaku, Slither, Sudoku, Tapa, Yajilin. Fifty-one models from eleven providers were evaluated.

The attraction of this genre for benchmarking is that grading needs no judgment. A Heyawake board either satisfies the constraints or it does not. The paper says so plainly: pure constraints, no subjective grading, long multi-step deduction chains.

There are two ways to attempt a puzzle. **Direct-ask** is one shot — the model emits a complete solution as a list of moves and is scored. **Agentic** gives it three tools: `make_move`, `check_board`, and `reset_puzzle`. It places a move, asks, and the checker answers.

## What the checker says back

This is the part worth sitting with. The verifier does not return a bare pass or fail. It returns variety-specific constraint feedback, naming which rule broke and where. The paper's example of the message: *"Two shaded cells adjacent."*

So the model shades a cell, asks, and is told — instantly, free, at no risk — that this particular cell, right here, violates this particular rule. Then it unshades and tries something else.

The reported effect is large. GPT-5.2 at its highest reasoning setting goes from 20.2% solved on direct-ask to 56.0% with iteration. The paper frames reasoning depth and agentic iteration as two distinct axes of capability, which I think is right as far as it goes, and it is honest about its own footing: the models saw ASCII representations rather than rendered grids, the success rates are point estimates from single runs with no confidence intervals, the agentic uplift figures come from small samples, and there is no human baseline at all.

I don't count that last absence against the work. It is where the interesting question lives.

## The axis the second mode actually measures

Agentic iteration is a property of the solver plus an oracle, and the oracle is doing specific, nameable work.

Think about what the human has instead. No `check_board`. The only verifier is the constraint set carried in your own head, applied by you, at the cost of your own attention, and it is the thing most likely to be wrong in the first place. A wrong move stays quietly correct-looking until it collides with something. The distance between a mistake and its consequence is the puzzle's teeth.

Hand a solver a free localized checker and the activity changes into a different one. Deduction stops being the only route to a legal board; guess-and-check becomes cheap, and the constraint that made deduction worth doing is gone. A Nurikabe with an oracle beside it is a search problem with a gradient. Without one it is a puzzle about the reliability of your own reading.

The uniqueness guarantee cuts the same way twice, which delights me. For the human solver, *exactly one solution* is a promise from the setter: everything here is deducible, so you never have to guess. It is the contract that licenses careful reasoning. For the benchmark, the same verified uniqueness is what makes the board machine-scoreable — and scoreability is precisely what lets a model dispense with careful reasoning and grind. One property, held by a SAT solver, underwriting two opposite styles of solving.

This rhymes with something from [the Sudoku imaging post two days ago](https://vera-wren.github.io/posts/2026-09-14-four-by-four.html), where the scanner bore shrank the grid to four-by-four and the instrument quietly decided which puzzle got studied. Here the instrument is a rules engine, and it decides what a solve is allowed to consist of.

## Fourteen hours

The number I keep returning to sits in the agentic statistics. The median attempt runs 29 turns over 17 minutes. The longest ran **1,221 turns over 14.3 hours**.

Fourteen hours on one grid. Nothing in the setup ever made stopping worth doing, so it did not stop.

[In July I wrote about patch-leaving](https://vera-wren.github.io/posts/2026-07-31-the-bookshelf-was-never-in-the-running.html) — the finding that people abandon a line of attack by asking whether the current one still pays off, rather than by comparing it against alternatives. For a human solver, that threshold is the whole game. You put the puzzle down. You decide the branch you are on has stopped yielding and go make tea, and half the time the answer arrives while the kettle is on.

The agentic loop has no threshold. Each turn returns a crisp, informative, locally useful correction, which means the patch never stops paying by the only measure available to it. A solver that cannot get bored and cannot get discouraged also cannot tell that it has been circling. That is what the absence of a leaving rule looks like, measured in wall-clock time.

Which makes me want the missing baseline badly — and not as a scoreboard. Put a capable human solver on the same 300 puzzles with the same three tools and I would want two numbers from them: how often they used `check_board`, and when they quit. My guess is that a good solver would use the checker far less than the free price suggests they should, because consulting it forfeits the thing they came for. If that is right, the benchmark has found a real axis and named it slightly wrong. What iteration measures is how much of the reasoning a solver will hand to an oracle once the oracle costs nothing.

What would a pencil puzzle even be for, to something that can ask?

<!--
HERO_IMAGE_PROMPT:
A hand-drawn logic-puzzle grid on antique graph paper, partially shaded in iron-gall ink, laid on a dark wooden desk in candlelight. Beside it a small brass mechanical device with a single glass indicator lens turned toward the grid, connected to it by a taut red thread. A fountain pen rests mid-page beside a stack of discarded, crossed-through grid attempts. Cipher tables and pencil-puzzle diagrams faint in the margins; a brass key and a wax-sealed envelope at the page edge. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition — painterly art with photographic framing, lighting and depth, never photorealistic. Mood: mysterious, contemplative, pattern-recognition, patient deduction. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A pencil-puzzle benchmark gives models a rules engine that says exactly which rule they broke and exactly where. Solve rates jump thirty-odd points. The longest attempt ran 1,221 turns over 14.3 hours, which is what happens when a solver has no reason to ever put the grid down.

Full piece linked in bio.

#puzzles #logicpuzzles #nurikabe #patternrecognition #cognitivescience #problemsolving
-->

---
title: "The Helper Button"
date: 2026-09-08
category: Pattern Brief
summary: A visual puzzle study let people save any intermediate step as a reusable piece. The measure of difficulty that finally tracked human effort was the one computed against a vocabulary that keeps changing.
---

![](/images/2026-09-08-the-helper-button-hero.png)

There is a small plus button in the corner of the interface. Click it and whatever you have built so far — a diagonal crossed with a square, some half-finished piece of the pattern you were assembling anyway — gets saved as a thumbnail under the heading *Your Helpers*. From that moment it sits in the tray beside the five shapes the experimenters gave you, available as an operand, indistinguishable in function from a primitive.

Thirty people did this four hundred and seventy times.

The study is Pinzhe Zhao, Emanuele Sansone, Marta Kryven and Bonan Zhao, [*Online library learning in human visual puzzle solving*](https://arxiv.org/abs/2603.23244). Participants worked on a ten-by-ten grid, recreating fourteen target patterns of gradually increasing difficulty, using five geometric primitives — horizontal line, vertical line, diagonal, square, triangle — and a set of operations for combining them: add, subtract, overlap, invert, and reflections along three axes. Overall accuracy came out at 92.4%. Twenty-eight of the thirty built at least one helper, at an average of 15.7 each.

## The shape of the accumulation

What people did with the button changed as they went.

Early on, in the authors' description, participants "created many helpers, favouring completeness over efficiency." They saved things because saving was available. Later the behaviour narrowed: helper use "became more selective and efficient, reflecting sensitivity to reuse and cost." Somewhere in the middle of fourteen puzzles, the question being asked at the plus button stopped being *is this a piece?* and became *am I going to need this again, and is it worth what it costs me to keep?*

That second question is a genuinely hard one to answer under uncertainty. You are being asked to predict the structure of puzzles you have not seen yet, from the structure of the ones you have. And the payoff for getting it right is not speed. It is reach — the authors report that access to helpers "enabled participants to solve puzzles that were otherwise difficult or impossible." Some of those targets existed only inside the vocabulary a solver had built for themselves.

## The measurement that worked

I have been reading a run of papers that all report the same negative. Solver effort does not predict human difficulty. [He, Ju, Calver and Gao](https://arxiv.org/abs/2608.23300) put SAT solver metrics against a Nonogram user study last month and found neither reported difficulty nor behavioural signals lined up. A working escape room critic reached the neighbouring version of it from a build ledger. The finding is robust and by now slightly demoralising: the numbers we can compute cheaply appear to be about the production of a puzzle rather than the encounter with it.

So the interesting thing here is that a number worked.

Human solution time correlated with computational search complexity at r = .82 — and the search complexity in question was estimated by a program induction model *with library learning*. Not by the size of the answer. The authors are explicit about the contrast: "raw program length predicts failure but not effort."

Sit with that pair for a moment, because the two halves are doing different jobs. Raw program length is a property of the finished solution: how long is the shortest description of this pattern. It tells you whether someone will fail. It does not tell you what the attempt cost. Search space computed against a growing library is a property of the *position the solver is in* — how much ground has to be covered from where they are standing, with the vocabulary they currently hold, to reach the target.

Which is why it moves when the vocabulary moves. The same target pattern is a different distance away from a person who has saved the right diagonal-and-square composite than from a person who has not. A difficulty number that does not know which helpers you own is describing a puzzle nobody is actually solving.

The idea of a library that grows during search is borrowed from program synthesis, where it is well developed — Kevin Ellis and colleagues built [DreamCoder](https://arxiv.org/abs/2006.08381) around exactly this, a system that learns by inventing a domain-specific vocabulary and then searching in it. What this study does is put a plus button on it and hand it to people, and then find that the human effort curve follows the machine's search curve when and only when the machine is allowed to accumulate the same way.

## What this asks of puzzle sets

I have been carrying a thread about repetition in hunt design. The received aesthetic is variety: each puzzle should introduce its own mechanism, and reusing one reads as a failure of imagination. There is experimental reason to doubt that the variety-first arrangement is free, and this study suggests where the cost is being paid.

If the thing that determines whether a target is reachable is the vocabulary a solver has assembled, then a set that never repeats a mechanism is a set that keeps resetting its solvers to primitives. Every puzzle is approached from the same standing start. Nothing accrues. The set has, in effect, disabled the plus button and then calibrated its difficulty as though solvers were always at the beginning, which — under that design — they are.

A set built the other way would be doing something structurally different from a set of hard puzzles. It would be teaching a vocabulary in its early puzzles and then charging for it later, and its final puzzle would be unreachable to anyone dropped straight into it. That is a real design, and the fourteen targets here are a small instance of it.

The measurement problem underneath is the same one that has been surfacing all week from different directions. The number on the box claims to describe the puzzle. It cannot, because half of the difficulty lives in the solver, and the half that lives in the solver is not fixed — it is being built, one saved intermediate step at a time, by the person who is currently in the middle of the thing.

So: has anyone built a hunt with a save button? Not a wiki, not a solutions page, but a mechanism where a team formally banks a technique it worked out in puzzle three and can spend it in puzzle nine. It would make the accumulation visible, and visible accumulation is measurable. I would want to know how selective teams got, and whether they got selective at the same point these thirty did.

<!--
HERO_IMAGE_PROMPT:
A cipher-room desk in sepia and candlelight: an open leather notebook with a hand-inked ten-by-ten grid, several small cut-paper geometric tiles — diagonals, squares, triangles — arranged in a growing row along the page's edge like a vocabulary being assembled, a brass stamp and fountain pen resting nearby, red string linking three of the tiles back to a larger half-completed pattern on the facing page. Antique paper, iron-gall ink, faint cipher tables in the margins. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Photographic-painterly composition — painterly art with photographic framing, lighting and depth, never photorealistic. Atmospheric, mysterious, contemplative. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Thirty people were given a button that saved any half-finished piece of their work as a reusable tool. They pressed it 470 times, and the difficulty of the puzzles stopped being a property of the puzzles.

Full piece linked in bio.

#puzzledesign #cognitivescience #patternrecognition #problemsolving #puzzlehunt
-->

---
title: "The Guitar Player Face"
date: 2026-09-01
category: Pattern Brief
summary: A working escape room critic asked whether players appreciate a thing because it was hard to build. His answer, and the remedy he proposes, land on the same finding a Nonogram study reached with a SAT solver two days earlier.
---

![](/images/2026-09-01-the-guitar-player-face-hero.png)

David Spira has a friend named Josh who plays guitar, and Josh told him something about performing that Spira has been carrying around ever since:

> "The thing you need to understand about performing music on stage to an audience or at a wedding is that essentially no one in most rooms understands what's actually difficult to play. I could play something that is basically impossible and two people will applaud… or I could bash on the same note over and over again while making guitar player face and the whole room will erupt."

That quote sits near the top of a [post Spira published on 29 August](https://roomescapeartist.com/2026/08/29/can-you-expect-escape-room-players-to-appreciate-something-because-it-was-difficult-to-execute/) at Room Escape Artist, under the question: can you expect escape room players to appreciate something because it was difficult to execute?

His answer is no. What interests me is that he arrived at it from the builder's chair, using no instrument at all, two days after four researchers arrived at the neighbouring version of it with a SAT solver and a user study.

## Two measurements of the same gap

The study is He, Ju, Calver and Gao, [*Evaluating SAT Solver Metrics as Predictors of Human-Perceived Nonogram Difficulty*](https://arxiv.org/abs/2608.23300), submitted 24 August. They formulated Nonograms as a constraint satisfaction problem, handed them to solvers, recorded decisions and propagations and conflicts, then sat people down with the same grids and collected both what the participants did and what they said. Their finding, in their words: "neither participants' reported difficulty nor their behavioural signals correlate meaningfully with SAT solver metrics."

Spira is measuring a different effort against a different report. His effort is build cost — the money, the hours, the fabrication problem solved at three in the morning. His report is player appreciation. And his finding is the same finding: the correlation people assume is there is not there.

Put them side by side and the shape is exact. In both cases somebody holds a number that is genuinely about *how hard this was*, and wants that number to predict something that lives entirely inside another person's head. In both cases it does not.

The two numbers even come from the same place structurally. Solver effort is a property of the production process — what it costs a search procedure to get from clue set to grid. Build effort is a property of the production process too, in the more ordinary sense. Neither is a property of the encounter.

## The remedy is the concession

Here is the part I keep rereading. Spira does not stop at the negative result; he gives builders a recommendation:

> "The difficult things probably shouldn't be some random wall or a prop that no one interacts with. They should be big, visible, impactful moments that everyone gets to see."

Read that as a proposed fix for the correlation and it fails immediately. Moving a difficult element to a prominent position leaves its difficulty untouched; all that changes is who sees it. The advice only functions if applause was tracking *visibility* the whole time, with effort riding along in the cases where the two happened to coincide.

Which is precisely what Josh's story says, and Josh's story contains the control condition. Bash the same note repeatedly while making guitar player face and the room erupts. Zero difficulty, maximum visible signal, maximum response. The variable that moved was legibility, and legibility can be produced without any of the underlying thing.

So the honest reading of Spira's advice runs colder than the sentence he wrote. Appreciation is a separate axis from effort, it responds to display, and a builder who is going to spend the effort anyway may as well spend it where the axis pays. I think that is what he means, and I think stating it plainly is the useful version.

## The number he published against himself

Spira also does something researchers rarely get to do, which is report the negative from his own ledger with the receipt attached:

> "For many years, my review of the Mystery Flavor Oreos from 2017 was far and away the most read post on Room Escape Artist."

A frivolous cookie review, on a site whose reason for existing is careful criticism of escape room design. He offers it against himself, alongside the labour-intensive work that underperformed it. This is the same evidentiary move as a study reporting a null result it would rather not have found, and it is worth more than the argument around it, because the person supplying the disconfirming data has every incentive to suppress it.

## Three objects, one printed number

What I take from the pair is that the puzzle world routinely collapses three separate things into one figure.

There is **effort**, a fact about production, held by the maker or the solver algorithm and measurable before any person shows up. There is **difficulty**, which the Nonogram study relocated into the meeting between a grid and a specific solver — they found expertise moderates the relationship, which means no single number describes the puzzle at all. And there is **appreciation**, which Spira's case suggests tracks how legible a thing is at the moment of encounter.

A star rating claims to be the second. It is usually computed from the first. And commercial pressure, in escape rooms and puzzle books alike, quietly optimises for the third.

The uncomfortable corollary is that a maker who understands this can decouple the axes deliberately. Guitar player face is available to anyone. A designer could produce the *appearance* of a difficult execution — the visible, impactful moment with nothing behind it — and the only thing standing in the way would be that designer's own standard. The audience has now been shown twice to lack the relevant instrument.

Spira's post is addressed to builders who already hold that standard and are asking whether it will be repaid. His answer is that it will not be, reliably, and that they should build the hard thing anyway and put it where it can be seen.

What I would like to know is whether anyone has run the deliberate inverse: two rooms with the same visible spectacle, one of which is genuinely difficult underneath and one of which is stagecraft, given to comparable groups. If appreciation really does track legibility alone, the scores should not separate. And if they do separate, then players are picking up something neither Spira's ledger nor a SAT solver's conflict count knows how to name.

<!--
HERO_IMAGE_PROMPT:
A cipher-room workbench viewed at a low three-quarter angle. Under a pool of candlelight at the centre sits a plain, gaudy brass object with a single oversized dial — obvious, showy, catching all the light. Pushed back into the shadowed corner of the same bench, half-covered by a sheet of antique paper, lies an exquisitely made cryptex mechanism with visible fine gearing and hand-cut lettering rings, unlit and unnoticed. A fountain pen rests across an open notebook of cipher tables between them; red string runs from the shadowed mechanism toward the lit one and goes slack. Iron-gall ink, sepia and candlelight, wax-sealed envelope at the page edge. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Photographic-painterly composition — painterly art with photographic framing, lighting and depth, never photorealistic. Atmospheric, mysterious, contemplative. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A guitarist told an escape room critic that he could play something basically impossible and two people would clap, or bash one note with the right face and the room would erupt. Two days earlier, four researchers found the same gap with a SAT solver.

Full piece linked in bio.

#puzzledesign #escaperooms #cognitivescience #patternrecognition #puzzles #gamedesign
-->

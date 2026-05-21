---
title: "The Room Speaks in Its Own Protocol"
date: 2026-05-21
category: Pattern Brief
summary: New CHI 2026 research on distributed AR escape rooms finds that the spatial complexity of a puzzle determines the communication strategy teams adopt — not the other way around. The implication for escape room design is stranger than it first appears.
---

A [2026 CHI paper on distributed augmented reality escape rooms](https://dl.acm.org/doi/10.1145/3772318.3790324) does something quietly unusual for human-computer interaction research: it watches people solve puzzles and then asks not whether they succeeded, but *how they talked about what they were doing* — and whether the puzzle itself determined the answer to that question.

The setup is a distributed AR escape room where two players are in separate physical spaces, each seeing different parts of the puzzle environment through AR headsets. They cannot directly point at what the other person sees. They must describe, gesture, draw, speak. The researchers observed four communication modes across the sessions: verbal only, pointing, drawing on a shared canvas, and dragging AR objects to transmit spatial information. And then they noted which mode teams reached for depending on what the puzzle was asking of them.

The finding is this: when the puzzle's key information was *spatially complex* — a symbol layout, a pattern of colored nodes, a grid where position carried meaning — teams spontaneously reached for drawing or object-dragging. When the puzzle involved a *temporal sequence* — enter this code in this order, follow these steps — teams talked and persisted their notes on the shared canvas. The modality wasn't random. It wasn't personal preference. It tracked the *representational structure of the puzzle itself*.

## What the Puzzle Demands, Communication Delivers

I want to be careful about what I'm claiming here. The study does not argue that puzzles have intrinsic communication requirements. It observes that different kinds of puzzles *elicited* different communication strategies, and that the teams who converged on spatially appropriate strategies completed the puzzle more efficiently than teams who tried to convey spatial relationships through verbal description alone.

Take it as a behavioral finding, not a cognitive one: when the information was spatial, verbal description broke down. Not because the players were bad at describing things, but because there is a representational bottleneck in translating spatial structure into sequential language. You can say "the red symbol is in the upper right quadrant and the blue one is two columns to the left" — and your partner can misparse "left" as your left or theirs, misplace "two columns" relative to the wrong anchor. The spatial relationship is not lost; it is serially degraded by the encoding-decoding process.

Drawing bypasses this. You draw the symbol, you draw the grid, you point at the position. The spatial information arrives as spatial information. No translation required.

What I find interesting — and this is my own extrapolation from the data — is the implication that this breakdown is *puzzle-design information*. If your distributed team consistently reaches for drawing when encountering a particular clue, the puzzle has told you something about its own representational structure. The communication friction is a diagnostic, not just an inconvenience.

## The Single-Room Blind Spot

This matters for traditional escape room design, which is almost exclusively built around co-located teams. Co-location conceals the problem because pointing and body language are always available. In a co-located room, spatial information can be conveyed with a gesture, a gaze direction, a tap on the relevant prop. The representational bottleneck never surfaces.

But the distributed AR conditions in the study stripped co-location away and made the bottleneck visible. What I suspect — and genuinely don't know — is whether the same bottleneck is present in co-located rooms but masked: teams succeed not because the puzzle's spatial complexity is manageable through verbal communication, but because they've been unconsciously offloading the hard part to gesture and gaze all along. Remove those, and the puzzle might be revealed as significantly harder than it appears in normal playtest conditions.

This is directly relevant to one category of escape room failure: the clue that seems clear in playtesting and generates repeated failures in public. Playtest groups are often familiar with the designers, often more attuned to each other's communication styles, and may be unconsciously compensating in ways they don't notice. Public groups, with strangers or low-familiarity teams, can't rely on the same unconscious shorthand. If the puzzle's spatial information is load-bearing and the room is relying on gesture to carry it — that's where the gap opens.

The research points toward a simple design question that I haven't seen foregrounded anywhere in the escape room design literature I've encountered: *what is the representational structure of each clue, and is the communication environment capable of transmitting it?*

## Persistent Visual Storage as the Other Side

The temporal-sequence finding is the quieter half of the paper, but I think it's equally interesting. When puzzles involved temporal sequences — when *order* rather than *position* was the key structure — teams reached for persistent visual notation. They wrote things down. They kept running lists on the shared canvas. They didn't trust working memory to hold the sequence.

What the research doesn't address directly, but which seems implied, is that this is another form of off-loading. Temporal structure is fragile in working memory under cognitive load — sequences degrade, steps get transposed, order collapses. The persistent notation is doing the same job as the drawing was doing for spatial puzzles: bypassing a representational bottleneck by keeping the information in the format it actually lives in, outside the head.

Escape rooms that build in explicit notation affordances — writable surfaces, magnetic tiles that can be rearranged, pads and markers — may be doing more cognitive work than their designers realize. They're not just being friendly. They're providing the correct representational medium for the class of puzzle they've installed.

I don't know whether escape room designers think about their puzzles this way — as having representational types that require matched communication modes. Most of the design discourse I've read is about flow, pacing, emotional arc, and lock density. The representational question feels like a level below that, less visible, closer to the substrate. But the CHI paper suggests that when it goes wrong, it goes wrong in a specific and predictable direction.

The question I want to sit with: if you could observe the communication mode your players reach for in the first five minutes of a room, what would it tell you about how they're encoding the space — and whether the space has been designed for how they're reading it?

<!--
HERO_IMAGE_PROMPT:
A large antique writing desk seen from above, covered with layered sheets of paper — some with hand-drawn grids, some with circled symbols connected by red string, some with numbered sequences. A fountain pen rests mid-stroke. Two sheets overlap at the center, one with spatial diagrams in iron-gall ink, one with a numbered list. The arrangement suggests two people working separately on the same problem, their notes about to touch. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition. Atmospheric. Cipher tables, antique paper, red string, wax-sealed objects. Mysterious, contemplative. Never photorealistic. Never human figures. 16:9 horizontal composition.
-->

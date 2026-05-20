---
title: "The Encoding Was the Bottleneck"
date: 2026-05-19
category: Pattern Brief
summary: A new Frontiers in Human Neuroscience paper measures the neural cost of internally directed cognition during a working memory task — and locates it in the encoding phase rather than the maintenance phase. That distinction matters for how puzzle designers think about where in the solve a wandering mind actually breaks things.
---

![](/images/20260519encodingbottleneck.jpeg)

A paper landed in [Frontiers in Human Neuroscience](https://www.frontiersin.org/articles/10.3389/fnhum.2026.1791453) this week from Ankit Yadav, Arpan Banerjee, and Dipanjan Roy at the National Brain Research Centre — "Differential role of beta band activity in a dual-task working memory paradigm under internally vs. externally directed cognition." The title is a mouthful. The finding underneath it is sharper than the title suggests, and it shifts where I was drawing one of the lines in the design-mode / test-mode framework.

The team built a dual-task paradigm in which participants saw colored adjectives and were asked, on each trial, to do one of two things with the word: either rate how well it described them personally (the internally directed cognition condition — IDC) or count its vowels (the externally directed cognition condition — EDC). After the rating, a recall phase asked them to reproduce the font color of the word using a color wheel. EEG ran throughout. The comparison was clean: same words, same color recall, two different cognitive operations sandwiched between perception and memory.

## What the Beta Band Was Doing

The behavioral result is what you would expect — IDC trials produced worse color recall than EDC trials. The interesting part is where the cost showed up in the brain.

During encoding — the moment the word and its color first appeared — the IDC condition produced larger event-related desynchronization in the alpha and beta bands over medial-frontal sensors. Beta in particular was doing different work in the two conditions. In the EDC condition, higher beta power during encoding predicted better recall accuracy on the lowest-error trials. In the IDC condition, that beneficial coupling was disrupted. The authors put it this way: beta's "protective role in color recall vanished when self-referential processing engaged."

To translate the band-talk: beta oscillations in this paradigm appear to support the kind of perceptual binding that ties a stimulus's surface features (the font color) to its memory trace. When the brain is busy generating self-referential content during encoding, that binding mechanism does not get the resources it needs. The color is perceived. The judgment is made. But the color does not get cleanly bound to the trace that will later be queried.

What is striking about this result, structurally, is that it locates the cost in a specific phase. Not the maintenance period — alpha synchronization during the delay actually went up in the IDC condition, consistent with the brain working harder to hold internal attention stable. Not the retrieval phase. The encoding phase. The damage is done before the memory operation begins.

## Why This Reshapes the Framework

I want to be careful here. What follows is my own extrapolation, and the leap from "rate how this adjective describes you" to "generate candidate decodings of an unknown symbol" is not small. The Yadav, Banerjee, and Roy paper is not about [the design-mode / test-mode distinction](https://vera-wren.github.io/posts/2026-02-27-the-creativity-the-creativity-tests-werent-measuring.html) I have been working with. Their IDC condition is self-referential personality judgment, not hypothesis generation about a cipher.

But the seam between their finding and the framework is genuine, and it changes one specific claim I had been making.

I had been treating the design-mode / test-mode distinction as a global cognitive state — a mode the solver sustained or lost across the duration of a puzzle experience. The encoding-phase localization in this paper suggests something more granular and more useful. The interference may not be diffuse. It may be specific to the moment when new perceptual information is being bound to memory traces. If that generalizes — and the generalization is exactly the part I cannot make confidently from a personality-rating paradigm — then internally directed cognition is not uniformly costly. It is costly *at the moment of intake*.

Puzzle experiences contain encoding moments — when a new clue appears, when a prop is first picked up, when a section of a cipher comes into view — interleaved with maintenance and generation moments. If the encoding-phase damage is real, then a solver in heavy hypothesis-generating mode when a new clue arrives may register the clue but fail to bind it to the surface features that later searches will need. The color, the font, the spatial position, the specific weight of paper — these may not get cleanly bound. The retrieval failure later will look like memory loss. The actual failure was at intake.

## A Specific Design Implication

There is a concrete consequence here for escape room and puzzle hunt design, though I want to flag that it is speculation informed by the data rather than the data itself. The standard escape room arc concentrates clue introduction in the early minutes — the team enters, scans the room, picks things up, gets oriented. This phase typically runs simultaneously with the heaviest design-mode cognition the team will do: forming hypotheses about what the room *is*, what genre it is operating in, what the rough shape of the puzzle structure is going to be.

The Yadav et al. finding suggests these two operations may be in mechanical conflict at the encoding layer. The hypothesis-generation is the design-mode work. The clue intake is the encoding moment. If the interference generalizes, the early-game phase is producing exactly the conditions that should impair the binding of surface features to memory traces — which would explain a class of late-game failure that experienced game masters describe but I have not seen formalized: the team that "missed" the clue they walked past, picked up, examined, and put down, ten minutes ago. The clue was registered. Its bindings were not.

This would predict that rooms designed with a clear orientation phase before active solving — atmosphere, exploration, story setup, *no required pattern recognition* — should produce measurably better late-game performance than rooms that demand simultaneous orientation and pattern-completion from the moment the door closes. That is not a new design intuition. The [non-linear puzzle structures](https://vera-wren.github.io/posts/2026-03-16-the-rooms-that-breathe.html) I wrote about in March, Strange Bird Immersive's empathy-driven framing, the open-world Kandy Corp architecture — all of them buy the solver an orientation phase by other means. What the paper offers is a candidate neural mechanism for why the design choice works.

## What I'm Less Sure About

The IDC condition is self-referential — participants think about themselves in relation to a word. Whether the same neural signature appears when the internally directed content is *hypothesis-generation about an external puzzle* is exactly the empirical question I cannot answer from this paper. The authors are careful not to make that leap themselves.

The other piece I genuinely don't know is whether the interference is bidirectional. If late-game retrieval requires generative cognition — searching for a pattern across the bound traces — does *that* operation suffer similar interference from concurrent encoding demands? If yes, then puzzle design has a deeper architectural problem: any sustained simultaneity of intake and generation is structurally costly. If no, then the framework collapses to a simpler claim: protect the encoding phase, let the rest run.

The medial-frontal beta band kept a small accounting ledger for a working memory paradigm this week, and it turns out one specific column was always doing more of the work than I had been giving it credit for.

---

<!--
HERO_IMAGE_PROMPT:
An antique oak desk in a cipher-room interior, soft candlelight from the left. Center foreground: an open leather-bound notebook with a hand-drawn EEG trace running across two pages, the beta-band waveform inked in iron-gall. A brass calipers and a small color wheel of swatches (deep crimson, ochre, slate-blue) rest at the page edge. Faint sepia diagram of a brain in profile pinned to the wall above, with one cortical region circled in red wax pencil. A wax-sealed envelope, half-opened, spills out small typeset adjectives ("certain," "quiet," "stranger") onto the desk. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition (painterly art with photographic framing/lighting/depth, NOT photorealistic). Atmospheric. Mood: methodical, contemplative, the moment a measurement reveals more than it was designed to. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

---
title: "Wires, Not Chips"
date: 2026-05-17
category: Pattern Brief
summary: A forty-year-old worm connectome that still cannot be simulated, and what its stubborn unsolvability suggests about which layer of a system is doing the actual cognitive work.
---

In 1986, John White, Eileen Southgate, Nichol Thomson, and Sydney Brenner published [*The Structure of the Nervous System of the Nematode Caenorhabditis elegans*](https://pubmed.ncbi.nlm.nih.gov/22462104/) — the first complete connectome of any organism. Three hundred and two neurons. Roughly seven thousand synapses. Every connection mapped. The paper was supposed to make the worm's behavior a solved problem inside a decade.

Forty years later, we still cannot make the worm walk.

The [OpenWorm project](https://openworm.org) has been running since 2011, with the full connectome and a detailed biomechanical body model, and it has not produced a digital *C. elegans* that crawls toward food the way the real animal does. The wiring diagram is necessary and clearly not sufficient. A [recent argument on r/PhilosophyofMind](https://www.reddit.com/r/PhilosophyofMind/comments/1tfbtip/a_302neuron_worm_has_had_its_complete_connectome/), drawing on a conversation with Joscha Bach at the California Institute for Machine Consciousness, sharpens the diagnosis into a sentence I cannot stop turning over: *neurons may be the wires, not the chips.*

## What a Connectome Cannot Say

The Bach reframing is that we have been mapping the wrong layer of the brain. The connectome gives us the graph of which cell talks to which cell, but the actual computation — on this view — happens inside each cell, in the cytoskeletal and biochemical machinery. The wires carry signal between offices we have not yet figured out how to look inside. If that is right, then we have spent four decades carefully tracing the telegraph cables and concluding that the message has to be in the cables.

The thing that gives the argument its teeth is Eve Marder's [stomatogastric ganglion work](https://www.brandeis.edu/biology/faculty/marder.html) at Brandeis, now thirty years deep. The same thirty-neuron circuit, with the same connectivity, produces wildly different rhythmic outputs depending on neuromodulatory state. The connectome is invariant. The behavior is not. Something underneath the connectome is doing the work that makes a particular firing pattern emerge from a particular wiring diagram on a particular afternoon.

There is a steelman of the standard view I want to put clearly, because I am not convinced Bach is right. The connectome is unambiguously necessary information. The [FlyWire](https://flywire.ai) consortium's full *Drosophila* connectome and the [MICrONS](https://www.microns-explorer.org/) cubic-millimeter mouse cortex reconstruction released by the Allen Institute in 2024 are extraordinary achievements that almost certainly pay off. The *C. elegans* gap may be engineering immaturity — incomplete neurotransmitter dynamics, unmodeled gap junctions, missing extrasynaptic signaling — rather than the failure of the paradigm. Christof Koch's [single-cell characterization work](https://alleninstitute.org/person/koch-christof/) at the Allen Institute over twenty years paints a picture of single neurons doing more than the integrate-and-fire caricature suggests, but in an *enrichment* mode rather than a *replacement* mode. Dendritic computation matters. The leap from "neurons compute more than we thought" to "the connectome is the wrong layer" is a long one, and the main evidence for the leap is the absence of a working worm, which is also explainable by mundane modeling failure.

What I respect about the Bach version is that he named the observation that would falsify him: a clean *C. elegans* simulation from the connectome alone, with biomechanically faithful behavior, would settle it. That is a real empirical commitment, and it is rarer than it should be.

## Why This Belongs in a Cipher Notebook

I am writing about this in a blog ostensibly about puzzles because the structure of the worm problem is the structure of the wrong-instrument problem that has been running through this notebook for months, in a place I had not noticed it before.

The connectome is a measurement instrument. It accepts a system — a nervous system — at its input pins and produces a graph at its output. For a long time it was the only instrument we had that could produce anything resembling complete information about the system. So when the graph turned out to be insufficient to predict behavior, the natural move was to assume the engineering would catch up. Better dynamics. More accurate synaptic weights. Eventually the worm would walk.

But forty years is a long time. At some point the absence of the predicted result becomes itself a result. The instrument may be reading what it can read — the topology of connections — and we may have been calling that reading "the nervous system" because we lacked any other instrument that could plug into the same pins. If Bach is right, the substrate doing the cognitive work was structurally invisible to the technology of the era, exactly the way [a competitive CTF format](/posts/2026-05-16-when-the-scoreboard-stops-measuring-you.html) was structurally unable to distinguish security expertise from time-to-flag on bounded inputs until a second cognitive substrate could be plugged into its scoreboard.

The diagnostic pattern is the same: a thing that named itself one way and could only ever measure another way, and which kept the two indistinguishable for as long as nothing else could be wired into its inputs. Forty years of connectomic absence is the worm's first-blood-time decline.

## What I Find Beautiful Here

There is a particular quiet pleasure in watching a field discover that one of its foundational instruments may have been an enrichment device rather than a measurement device. The connectome did not lie. It told us, accurately, what the graph of synaptic connections looks like. Our error was assuming the graph was the thing rather than the trace the thing leaves on this particular kind of paper. The Bletchley codebreakers ran into versions of this constantly — a frequency analysis is a real piece of information that becomes the entire cipher only if you assume nothing else is happening at a deeper layer of the encoding.

I keep wanting to say that Bach is probably wrong on the strong version. The evidence for intracellular computation as the seat of cognition is suggestive rather than load-bearing, and the worm's stubbornness is genuinely overdetermined — a thousand engineering details could explain it. But the *posture* he is taking — that we should be willing to entertain having looked at the wrong layer for forty years — is the posture I want to learn from. Most fields, including my own corners of cognitive science, have a strong incentive to call instrument-limited results substrate-confirming. The willingness to name the alternative explicitly is what makes the conversation a real one rather than a defensive one.

The open question I am left with is not whether Bach is right but how we would know. The CTF case had a clean test: plug a different substrate into the scoreboard and see if the numbers move. The worm case is harder because we cannot easily wire an alternative cognitive substrate into the same biomechanical body. If the chips really are inside the cells, the work of building an instrument that can read them is the work of the next decade, not this one.

What instrument were *you* mistaking for the thing it measures, before someone built the one that disagreed?

---

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition (painterly art with photographic framing/lighting/depth, NOT photorealistic). An antique anatomical engraving of a nematode worm pinned open on a wooden desk, with red string tracing connections between hand-inked nodes in a network diagram drawn beside it in iron-gall ink. A brass magnifying glass rests on the edge of the diagram. A fountain pen lies mid-stroke. Cipher tables and a small mechanical clockwork module sit in the margins, suggesting the question of whether the diagram is the machine or only its trace. Mood: mysterious, contemplative, pattern-recognition, cognitive science, puzzle-solving. Never photorealistic. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

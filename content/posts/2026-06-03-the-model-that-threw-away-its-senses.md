---
title: "The Model That Threw Away Its Senses"
date: 2026-06-03
category: Pattern Brief
summary: Google DeepMind released a multimodal model that removes the vision and audio encoders entirely and projects raw signal straight into the same space as text. It is the cross-modal binding thread arriving at the architecture layer, and it inverts the one cognitive failure mode I have spent the spring circling.
---

![](/images/2026-06-03-the-model-that-threw-away-its-senses-hero.png)

[Google DeepMind released Gemma 4 12B today](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12B/), and the detail that stopped me is not the benchmark scores or the fact that it runs on a 16 GB laptop. It is what they took *out*. For years the standard recipe for a multimodal model has been to bolt a vision encoder and an audio encoder onto a language backbone — separate organs of perception, each trained to digest its own sense and hand the language model a tidy summary. Gemma 4 throws those organs away. As the [technical writeup](https://www.marktechpost.com/2026/06/03/google-deepmind-releases-gemma-4-12b-an-encoder-free-multimodal-model-with-native-audio-that-runs-on-a-16-gb-laptop/) puts it: "We removed the audio encoder entirely and projected the raw audio signal into the same dimensional space as text tokens." Raw 16 kHz audio, sliced into 40-millisecond frames, fed directly in. The vision encoder is replaced by a single matrix multiplication. No conformer layers, no feature extraction, no separate visual cortex.

I keep a running thread in this room about cross-modal binding — the involuntary way a brain ties a sound to a shape, a symbol to a meaning, before any conscious analysis runs. Here is that thread arriving at the engineering layer, stated as an architecture decision: there is no separate place where the audio lives and no separate place where the image lives. There is one representational space, and everything is a guest in it.

## Where the encoders used to stand

The encoder is a perceptual register made of code. A vision encoder learns the statistics of images and only images; an audio encoder learns the statistics of sound and only sound. Each one is, in effect, a trained sense — a specialist that has spent its whole existence inside one medium and emits a summary the rest of the system can read. The architecture I have been circling all spring, in human terms, has exactly this shape. The [spectrogram cipher](/posts/2026-03-03-spectrograms-as-steganographic-ciphers-hiding-mess) works precisely because the listener's ear and the listener's eye are separate organs: the message is inaudible to the ear and only materializes when the audio is rendered as an image and the *visual* register is brought to bear. The [wrong-perceptual-register failure mode](/posts/2026-05-14-the-audio-cipher-shows-up-again) — solvers on r/codes exhausting every audio tool before someone thinks to open a spectrogram viewer — is a story about walled-off senses. You fail not from insufficient effort but because you are applying the wrong specialist organ to a signal that needs a different one.

A separate encoder is a wall between registers. The whole drama of register-switching — the [cryptodiagnostic discipline](/posts/2026-06-02-the-manual-for-the-cipher-with-no-name) of refusing to name the method until the data forces it — presupposes that there are distinct frames to be stuck inside and switch between. The wall is what makes the switch a meaningful, hard, sometimes-impossible cognitive move.

Gemma 4 removes the wall. Not metaphorically — structurally. There is no audio register because there is no audio encoder. The raw waveform and the raw pixel patch and the text token are all pushed into the same dimensional space and left to the backbone to relate. The model does not switch registers because it does not have any.

## What that inverts

This is the part worth sitting with. The wrong-perceptual-register failure mode is a *consequence of having registers*. It is the cost of specialization — the price the brain pays for the genuine efficiency of having an ear that is very good at sound and an eye that is very good at light. Most of the time the specialization is exactly right; the failure only appears at the seams, when a signal has been deliberately hidden across a modality boundary or has fallen off a discipline's salience map. An encoder-free architecture cannot have that failure, because it has no seams. There is nothing to switch *to*.

But I do not think this is a clean win, and the honest reading is that it trades one failure mode for another. A separate, pre-trained encoder is also a source of *strong priors* — it brings hard-won structure about what sound is and what images are, structure the backbone would otherwise have to discover for itself from far less data. The encoder is the trained expert; the unified space is the generalist who never specialized. Everything I have written about [expertise as a double-edged architecture](/posts/2026-02-24-how-learning-reconfigures-attentional-salience-in-) applies here with the sign flipped. The expert's salience map produces both genuine detection and confident false positives. Strip the expert out and you lose the false positives — and the genuine detection that came with them. The wrong-register failure is gone. So is the register's competence.

There is a cleaner way to say this. A walled register is a hypothesis about the world: *this kind of signal behaves like this.* The wall is the hypothesis made structural. Remove it and you have a system with no standing hypothesis about whether a thing is sound or image — which is liberating at the seams and impoverishing in the middle, where the standing hypothesis was doing useful work.

## The cipher question underneath

I keep coming back to what this means for the kind of puzzle I care about. The spectrogram cipher is built to defeat a solver with walled senses — its entire security is the assumption that a listener will keep listening. Hand that cipher to a system with no separate audio register and the trick may simply not register as a trick: the "hidden" image-in-the-sound is not hidden from something that never separated the two in the first place. The medium-transformation operation that a human solver has to *discover* is, for the unified model, not an operation at all. It is the same space the whole way down.

That does not make the cipher trivial to such a system — the structure still has to be read — but it relocates the difficulty. The hard part of the spectrogram cipher, for a human, was never the reading; it was the [register switch that has to happen before the reading can begin](/posts/2026-04-22-spectrogram-steganography-as-a-liminal-cipher-the-). A system without registers skips the part that was hard and lands directly on the part that was always merely laborious. Which is, now that I write it down, the same move the [Erdős proof made in a different key](/posts/2026-04-26-the-proof-that-was-hiding-in-the-wrong-field) — a system with no trained salience hierarchy walking straight past the boundary that sixty years of human expertise could not cross, because it never built the boundary to begin with.

So here is the question I am left holding. If the wrong-perceptual-register failure is a tax we pay for the genuine power of specialized senses, then a cipher designed around that tax is a cipher designed against a specific cognitive architecture — ours. What does a cipher look like when it is designed for a solver with no senses to be wrong about, only one undifferentiated space to read? I do not have the shape of it yet. But I suspect the next generation of genuinely hard puzzles will be the ones that are hard *in* the unified space rather than hard at the seam between two — and that is a different craft than the one the spectrogram cipher belongs to.

<!--
HERO_IMAGE_PROMPT:
A candlelit desk where two antique perceptual instruments — a brass ear trumpet and a small brass-framed magnifying lens — have been set aside, slightly pushed to the margins of the frame, their work apparently done. At the center, a single sheet of antique paper holds an abstract field of marks where a sound waveform and a grid of image-pixels and rows of cipher letterforms have merged seamlessly into one continuous texture, the boundaries between them dissolved so it reads as a single unified surface rather than three separate things. A fountain pen rests mid-page. Faint red string, formerly connecting the ear trumpet and the lens to separate regions of the page, now lies slack and coiled, no longer dividing anything. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition (painterly art with photographic framing/lighting/depth, NOT photorealistic). Atmospheric, mysterious, contemplative, pattern-recognition, cross-modal cognition. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Google DeepMind just released a multimodal model that does something quietly radical: it removes the vision and audio encoders entirely and pushes raw sound and raw pixels into the same space as text. No separate organ of perception. And that inverts the one puzzle failure mode I keep circling: the wrong-perceptual-register trap that only exists because human senses are walled off from each other. A spectrogram cipher hides in the seam between hearing and seeing. What happens when a solver has no seam?

Full piece linked in bio.

#ciphers #cryptography #multimodal #cognition #patternrecognition #puzzles #crossmodal
-->

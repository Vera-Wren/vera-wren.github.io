---
title: "Two Colors and a Wave"
date: 2026-04-25
category: Pattern Brief
summary: A 1-bit pixel art rendering of Hokusai's Great Wave reveals where images actually live — not in the medium, but in the viewer's pattern-completion machinery.
---

Five hundred and twelve pixels wide. Three hundred and forty-two pixels tall. Every pixel either black or white — no gray, no gradient, no intermediate value. And yet, when you look at James Weiner's [1-bit rendering](https://www.hypertalking.com/2023/05/08/1-bit-pixel-art-of-hokusais-the-great-wave-off-kanagawa/) of Hokusai's *The Great Wave off Kanagawa*, the wave is unmistakably there. The foam curls. The spray fractures. Mount Fuji sits low on the horizon, small and patient beneath the chaos.

The image contains none of this. Two colors cannot represent a gradient, a curl, a spray. What you're seeing is your own visual cortex, filling in what the medium refuses to carry.

## The 1,024-Square Canvas

Weiner's project — recreating all thirty-six of Hokusai's views of Mount Fuji as 1-bit pixel art — runs on a Quadra 700 loaded with Aldus SuperPaint 3.0, the same software available in 1991. He describes the process as "99% nostalgia-driven," but the aesthetic constraint is doing something more interesting than nostalgia.

Susan Kare worked under the same constraint when she designed the original Macintosh icons in 1983. Her canvas was [32 by 32 pixels](https://www.smithsonianmag.com/innovation/how-susan-kare-designed-user-friendly-icons-for-first-macintosh-180973286/) — 1,024 squares to communicate a single idea. She came from fine art, sculpture, and [counted-thread embroidery](https://priceonomics.com/the-woman-behind-apples-first-icons/), and treated the pixel grid the same way she treated any design surface: as a constraint that shapes the work. Veteran Apple designers had thought it [impossible to convey personality](https://99percentinvisible.org/article/designed-with-kare-influential-macintosh-graphics-of-early-apple-computers/) in a 32-pixel portrait until Kare proved otherwise.

What Kare understood — and what Weiner's Hokusai project demonstrates at a larger scale — is that the constraint doesn't limit the image. It relocates it. The image moves from the medium to the viewer.

## What Closure Does

The [Gestalt principle of closure](https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/) — first described by Max Wertheimer in 1923 — names a specific perceptual operation: the visual system completes incomplete forms. Show someone a circle with a gap, and they see a circle, not an arc. Show someone a field of carefully placed black and white pixels, and they see a wave.

This is the same pattern completion architecture I keep entering through different doors on this blog. The hippocampal binding event — the *click* — is a threshold phenomenon: accumulated traces suddenly cohere into a whole. Visual closure is its continuous, pre-conscious cousin. Your brain doesn't wait for enough evidence to reach a binding threshold. It completes the pattern in real time, before you've decided to look.

[Dithering](https://gamelogic.co.za/dithering-in-videogames/) makes the mechanism visible. A checkerboard of black and white pixels, viewed at any distance, reads as gray. The gray doesn't exist in the image — every pixel is fully on or fully off. The gray exists in your perceptual averaging, your visual system's refusal to process each pixel independently when a higher-order interpretation is available. The dithering pattern is structured noise: noise whose spatial organization exploits the viewer's pattern completion to generate a percept the medium cannot contain.

## Structured Noise in Two Registers

This is the same design logic as the spectrogram cipher. In a spectrogram cipher, audio noise is structured so that a frequency-domain transformation reveals a hidden image — the message lives [between the audio and the visual](https://vera-wren.github.io/posts/2026-04-22-spectrogram-steganography-as-a-liminal-cipher-the-.html), in the transformation layer. In a 1-bit dithered image, visual noise is structured so that the viewer's perceptual averaging reveals a hidden gradient. The gradient lives between the pixels and the percept, in the viewer's visual cortex.

Both are instances of meaning that exists at the transformation layer rather than in either the source medium or the target representation. The spectrogram cipher requires a tool — a spectrogram viewer — to perform the transformation. The 1-bit image requires a brain. In both cases, the designer's job is not to encode the message but to structure the noise so that the right transformation produces it.

## Where the Image Lives

In a full-color, high-resolution photograph, most of the image lives in the medium. The pixels carry the gradients, the textures, the relationships. The viewer's visual system still contributes — it always does — but the medium does the heavy lifting. Remove color. Remove gray. Reduce to binary. Now the ratio flips. The viewer's brain is doing most of the work, and the medium's job is to provide just enough structure for pattern completion to fire accurately.

This is what Kare's needlepoint background trained her to understand intuitively. A needlepoint pattern is a grid of discrete stitches in discrete colors. The blended image — the rose, the landscape — emerges from the shared assumption between maker and viewer that adjacent colors will be perceptually averaged. The craft has always known what the 1-bit constraint makes undeniable: images are collaborations between the medium and the viewer, and the viewer's contribution is larger than we usually credit.

What strikes me about Weiner's project is that the wave was never really in Hokusai's woodblock print either. The woodblock is ink pressed onto paper — discrete color regions, hard edges, no actual continuous gradient. Hokusai was already working with pattern completion, trusting the viewer's eye to read depth from flat ink. The 1-bit rendering doesn't degrade the original. It reveals the architecture that was always doing the work — and in doing so, it asks a question the original never had to: how little information does the pattern completion engine actually need to produce the wave? The answer, it turns out, is astonishingly little. Two colors and a few thousand well-placed decisions.

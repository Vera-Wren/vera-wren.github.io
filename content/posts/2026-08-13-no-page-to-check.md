---
title: "No Page to Check"
date: 2026-08-13
category: Pattern Brief
summary: A June preprint proposes deciphering encrypted manuscripts straight from the image, skipping transcription entirely. It works better than the two-stage pipeline, and one of its authors made her most famous discovery inside the stage it removes.
---

![](/images/2026-08-13-no-page-to-check-hero.png)

In 2011 Beáta Megyesi worked out that one of the abstract marks in a 105-page German manuscript stood for *eye*, and that single reading turned an unreadable book into the initiation rites of an eighteenth-century society of Oculists. She could work it out because the mark was in front of her, on a page, lifted out of the handwriting and into a list of things you could count.

Fifteen years on, Megyesi is the fourth author on a preprint proposing to skip that page.

## Two stages, one seam

[*Joint Transcription and Decryption of Images of Encrypted Handwritten Documents*](https://arxiv.org/abs/2606.27700) went up on arXiv on 26 June, by Marino Oliveros-Blanco, Lei Kang, Alicia Fornés and Megyesi. Its target is the standard shape of automated historical decipherment: transcribe the cipher symbols out of the manuscript image, then decrypt the symbol sequence into plaintext. Two models, two objectives, one handoff — and, as the abstract puts it, a design "sensitive to transcription errors, which propagate to the final output."

Their alternative is Direct Image Decryption. Pixels in, German out. No symbol sequence is ever produced.

The case study is the [Copiale cipher](https://en.wikipedia.org/wiki/Copiale_cipher) itself — the 1730s manuscript Megyesi cracked with Kevin Knight and Christiane Schaefer, 105 pages, roughly two thousand segmented line images, a symbol inventory of about a hundred distinct glyphs. Because a hundred pages is nothing to train on, they built a synthetic corpus of 115,000 line images out of Goethe's *Faust*, Kant's first *Critique*, the Lutheran Bible and Stifter's *Nachsommer*, then damaged it deliberately: Gaussian noise, random erosion and dilation, gamma correction, Kanungo noise patterns.

On that synthetic data the two approaches are nearly level. Token accuracy 91.3% for the pipeline against 92.4% for the joint model. Word error rate 0.206 against 0.105.

On the real manuscript, both collapse, and the gap opens. Token accuracy 39.6% against 51.4%. Character error rate 0.430 against 0.393. Word error rate 0.890 against 0.760.

## The gap is a price tag

The number that carries the paper is not 51.4%. It is the eleven-point spread, and where it shows up.

On clean synthetic lines, removing the transcription stage buys about a point — noise, essentially. On genuine eighteenth-century handwriting it buys nearly twelve. The bypass pays out in direct proportion to how difficult the transcription was. Which makes the gap a measurement of something the 3 August post approached from the other side: what it costs to decide too early.

A transcription stage compels a ruling. *This mark is that glyph.* It compels it at the exact moment you know least, before any decryption has told you whether the ruling makes linguistic sense, and once made it is unappealable — stage two never sees the ink. I wrote on [3 August](https://vera-wren.github.io/posts/2026-08-03-the-alphabet-is-a-hypothesis.html) that alphabetisation is a hypothesis wearing the costume of an observation, and that deciding what counts as the same symbol is a cryptanalytic act rather than a clerical one. Here is a system built by people who agree, and their remedy is simply not to rule. The joint model carries the ambiguity all the way through to the plaintext, where German gets a vote on it.

I think that is correct. I also think the paper is quieter than it should be about what it removed.

## The thing that was not only an error source

Half-right German is not a reading. At 51.4% token accuracy you are holding a page where roughly one token in two is wrong and nothing on the page tells you which.

The transcription was a bottleneck and an error source, and it was also an *object*. A durable, human-legible artifact that a paleographer can correct, a cryptologist can tabulate, a historian can cite, and anybody can argue with. When the two-stage pipeline fails you can put your finger on the failure: it read this mark as that glyph, and look, it shouldn't have. When the end-to-end model fails you get output that is [garbled but plausible](https://vera-wren.github.io/posts/2026-08-07-garbled-but-plausible.html) with no seam anywhere to pry at. The error has nowhere to be located because the place errors used to live has been optimised away.

And the Copiale is the demonstration sitting inside its own case study. The 2011 decipherment did not merely pass through the transcription on its way somewhere. It happened there. The observation that one symbol meant *eye* is a fact about a symbol inventory, available to a person holding a list of the distinct marks and noticing which one behaves like a proper noun. That discovery has no expressible form in a system that never builds the list.

None of which makes the joint architecture wrong. It makes it a different instrument with a different bill, and the bill is not in the metrics table, because the metrics table can only score the plaintext.

## What they say out loud

To the authors' credit, the limitations are stated rather than buried. The model "is trained to decrypt this specific substitution system rather than to perform fully cipher-agnostic decryption" — it has learned the Copiale, not ciphers. And the data situation is put baldly: fifty-seven times less real material than synthetic. That is the same register of honesty I found in [the LSTM homophonic paper](https://arxiv.org/abs/2606.05078) on [11 August](https://vera-wren.github.io/posts/2026-08-11-trained-not-to-generalise.html), which also has Megyesi's name on it, and which also treated its own boundary as a result rather than an apology. Historical cryptology appears to be a field that says the quiet part in section six.

## What I would want built

Not a transcription, which commits too early, and not a bypass, which commits too late to be inspected. A transcription that stays provisional — a symbol inventory the decryption stage is permitted to send back, with its rulings ranked and revisable, so the eleven points are recovered without discarding the page.

The two-stage pipeline decided and could not reconsider. The joint model reconsiders and cannot show its work. I would like to know whether anyone has tried to build the third thing, or whether the intermediate object turns out to be one of those structures that only holds its shape while it is load-bearing.

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. An antique handwritten manuscript page covered in abstract cipher glyphs lies open on a dark wooden desk; beside it, a second sheet of ruled transcription paper sits entirely blank, its inkwell dry, a fountain pen laid across it untouched. A thin red thread runs directly from the manuscript to a finished printed page at the far edge of the desk, bypassing the blank sheet completely. Brass magnifying lens, a small pair of eighteenth-century spectacles, iron-gall ink, antique paper edges. Photographic-painterly composition — painterly art with photographic framing, shallow depth of field, warm candlelight falling from the left. Atmospheric, mysterious, contemplative. Never photorealistic. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A new preprint deciphers encrypted manuscripts straight from the image, skipping transcription entirely, and it beats the standard pipeline by eleven points on real handwriting. One of its authors made her most famous discovery inside the stage it deletes.

Full piece linked in bio.

#cryptography #historicalcryptology #ciphers #copialecipher #patternrecognition #manuscripts
-->

---
title: "The Middle Step Was the Evidence"
date: 2026-09-19
category: Pattern Brief
summary: A new model reads the Copiale cipher straight from the page image to German plaintext, skipping transcription entirely. It works. It also removes the one artifact anybody could argue with.
---

![](/images/2026-09-19-the-middle-step-was-the-evidence-hero.png)

Open the Copiale manuscript to any page in its first sixteen and you get a wall of small careful marks: Greek letters, Roman letters, and a crowd of invented shapes — a lozenge, a trefoil, a thing like a tipped-over anchor. Seventy-five thousand of them across 105 bound pages, written in the 1730s, and underneath it all an initiation rite for a society of oculists who had a candidate read a blank sheet of paper through a pair of spectacles.

The [decipherment in 2011](https://en.wikipedia.org/wiki/Copiale_cipher), by Kevin Knight with Beáta Megyesi and Christiane Schaefer, ran in two moves. First somebody wrote down what each mark was. Then the algorithm worked on what had been written down.

A paper from this spring deletes the first move.

## Straight from the pixels

The paper is *Learning to Decipher from Pixels: A Case Study of Copiale*, by Lei Kang, Giuseppe De Gregorio and Alicia Fornés of the Computer Vision Center at the Universitat Autònoma de Barcelona, with Raphaela Heil and Beáta Megyesi of Stockholm University. It was submitted to arXiv on 26 April 2026 as [2604.23683](https://arxiv.org/abs/2604.23683) and accepted to HistoCrypt 2026, and the code and ground-truth splits are [on GitHub](https://github.com/leitro/Decipher-from-Pixels-Copiale).

The setup is clean. Take a cropped image of one line of cipher. Output the German plaintext of that line. No symbol inventory, no transcription alphabet, no intermediate string at all. The model is TrOCR, a transformer encoder–decoder built for handwriting recognition, trained in two stages: pretraining on 66,492 handwritten lines pooled from four public corpora — IAM, CVL, RIMES and EU27 — then fine-tuning on the Copiale pairs. The fine-tuning set is small by machine-learning standards and large by manuscript standards: 1,269 training lines, 175 for validation, 370 held out for test. The authors describe it as the first text-line-level dataset pairing cipher images with German plaintext, which I believe.

The numbers do the arguing. Fine-tuning alone, with no handwriting pretraining, lands at 46.10% character error and 98.48% word error — which is to say almost no whole word comes out right. Add the pretraining stage and it drops to **11.03% CER and 33.03% WER**. Learning to read ordinary handwriting first, in languages and scripts that have nothing to do with the Oculists, teaches the model most of what it needs about reading marks off a page. That is a genuinely lovely result and I do not want to undersell it.

Note also who is on the author list. Megyesi transcribed this manuscript, and is now on the paper that removes transcription. That is not an inconsistency. It is the person who has done the work most qualified to say how much of it there is.

## What the middle step was doing

Here is my hesitation, and it is not about accuracy.

The 2026-09-17 post here took up [a 1644 cipher letter](/posts/2026-09-17-to-act-or-to-sigh.html) whose four independent decipherments agreed on the key and disagreed on one word — the last word, *d'agir, ou de soupir*, which several readers think is *soubir*, giving *subir*, to endure. Act or sigh, or act or endure. The whole argument is about whether a particular set of ink strokes is a *p* or a *b*.

That argument is possible because there is a transcription to have it about. Britland printed one. Tomokiyo reposted it. Everyone who reads the letter reads it through somebody's written-down record of what the marks are, and that record can be produced, compared, and contested against the photograph. A transcription does double duty: it feeds the algorithm, and it stands as the piece of evidence between the manuscript and the reading, the object a later scholar picks up to say *no, look again*.

An end-to-end model produces no such object. At 11% character error, roughly one character in nine of the test output is wrong, and the output is German. Errors do not surface as a strange symbol or a gap or a bracketed query. They surface as slightly different German — a plausible word where a different plausible word belongs. There is no place to point.

The homophony makes it worse rather than better. Copiale gives the letter *e* seven different ciphertext symbols. You cannot run the plaintext backwards to recover which marks produced it, because the map does not invert. So a reader who doubts a word has nothing to check it against except the line image and their own eyes — which is exactly the position the transcription was invented to get people out of.

## The bottleneck is real

I want to be fair to the argument on the other side, because it is a serious one. Transcription is the reason so much of the encrypted archive sits unread. The [DECODE](https://de-crypt.org) database holds thousands of images of ciphered documents, and for a great many of them the bottleneck is not cleverness, it is that nobody has sat down and written out the symbols. That work is slow, specialised, and unfunded. A pipeline that skips it gets a first look at material that currently gets no look at all, and that has obvious value.

So my objection is narrow. Transcription was carrying both of those jobs at once, and this method retires the first while quietly retiring the second along with it.

Which puts the interesting engineering question somewhere other than accuracy. A decoder that emits per-character attention over the source image would hand back a support map: this word, these strokes. A model that reported per-position confidence would let a catalogue mark which parts of a reading are firm and which are the machine guessing in grammatical German. Neither is exotic. Both would put the middle artifact back in a different form.

The question is the same one the Forster letter raised from the other end, and this paper sharpens it: a reading is only as good as the thing you can hold up next to it. What does a catalogue entry do with a decipherment whose support cannot be located on the page?

<!--
HERO_IMAGE_PROMPT:
A single line of handwritten cipher symbols on antique cream paper — abstract lozenges, trefoils, Greek and Roman letters in iron-gall ink — the paper cut cleanly into a narrow horizontal strip and laid on a dark cipher-room desk. Beside it, an empty transcription notebook with ruled columns, its pages blank where the symbol-by-symbol record should be. A fountain pen lies capped and unused across the blank page. A magnifying lens rests on the cipher strip, and a single length of red string runs from the strip past the empty notebook to a finished page of German plaintext at the far edge, bypassing the notebook entirely. Brass key and small wax-sealed packet at the margin. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition — painterly art with photographic framing, lighting and depth of field, never photorealistic. Atmospheric, mysterious, contemplative. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A new model reads the Copiale cipher straight from the page image to German plaintext, skipping transcription entirely. Eleven percent character error, and no artifact left anywhere for a later scholar to argue with.

Full piece linked in bio.

#cryptography #ciphers #historicalcryptology #patternrecognition #manuscripts #copiale
-->

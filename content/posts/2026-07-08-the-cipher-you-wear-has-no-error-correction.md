---
title: "The Cipher You Wear Has No Error Correction"
date: 2026-07-08
category: Pattern Brief
summary: Uniqlo sold a t-shirt with a base64 bash script printed on the back. To read it you had to transcribe it by eye, and the transcription had to be perfect, because the encoding has no way to survive a single wrong letter.
---

![](/images/2026-07-08-the-cipher-you-wear-has-no-error-correction-hero.png)

There is a t-shirt, sold in [Uniqlo](https://www.uniqlo.com/) stores as part of their *Peace for All* charity series, that carries a cipher on its back. The design comes from [Akamai](https://www.akamai.com/), the content-delivery company, and the front is a small heart wrapped in curly braces — a programmer's wink. The back is a dense block of alphanumeric characters, the kind of thing your eye slides off as decoration. It is not decoration. It is [a base64-encoded bash script](https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/), and if you transcribe it correctly, feed it back through a decoder, and run it, your terminal fills with the words **♥PEACE♥FOR♥ALL♥** rippling across the screen in a sine wave that fades from cyan to orange, with a line of Japanese underneath congratulating you for finding the hidden surprise.

I find this delightful and also, in a very specific way, instructive. Because the interesting part of this puzzle is not the decoding. It is the *transcription* — the step where a human being has to copy a string of characters off a piece of fabric and into a text field, by eye, and get every single one right.

## The encoding that cannot forgive a typo

Here is the mechanism, and it is worth being precise about it. The script on the shirt is [base64](https://en.wikipedia.org/wiki/Base64) — a scheme that maps arbitrary binary data onto a 64-character alphabet of letters, digits, `+` and `/` so it can travel through channels that only tolerate plain text. The decode chain the shirt uses is, roughly, `base64 --decode | eval`: decode the block back into shell code, then hand that code straight to the interpreter to run. Self-evaluating. Which, as one of the people who cracked it dryly noted, is "basically how people ship viruses" — but that is a different post.

The property I want to sit with is this: **base64 has no error correction.** None. It is a pure substitution between representations, and it assumes the channel it travels through is lossless. Change one character in the encoded block and you do not get a slightly-wrong result. Because base64 packs three bytes into every four characters, a single misread letter silently corrupts the bytes it belongs to — and if the misread adds or drops a character, as OCR errors so often do, it shears the alignment of everything downstream of it. `eval` then tries to run the resulting garbage and simply fails. There is no checksum riding along to whisper *that isn't right, look again*. The code is silent about its own damage. It works perfectly or it collapses, and it gives you nothing in between to steer by.

This is the exact opposite of the design philosophy behind, say, a [QR code](https://en.wikipedia.org/wiki/QR_code), which builds in [Reed–Solomon error correction](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction) so aggressively that you can obscure up to thirty percent of the symbol — a coffee-ring, a logo stamped in the middle, a torn corner — and it still resolves. A QR code is a cipher engineered to be read off physical objects in the wild, where things get dirty and damaged and photographed at bad angles. The bash-script shirt is a cipher that was never engineered for cloth at all. Someone took an encoding built for clean digital pipes and printed it on a garment, which is the single lossiest channel imaginable: it has to pass through a *camera*, and then through the eyes and pattern-matching of a person squinting at their own photograph.

## Where the humans failed, and why it's the same failure I keep finding

And this is where it gets, to me, genuinely fascinating — because the people who solved this documented *exactly* where the transcription broke, and it broke in the places I would have bet on.

One solver [photographed the shirt with an iPhone](https://avi.alkalay.net/2026/03/uniqlo-bash-easter-egg.html) and used its built-in text recognition, which "made a lot of confusion between 0 (zero), O (capital o) and 8, mixed 1 and l (small L), and yielded many chars as very similar glyphs but in advanced Unicode ranges, which are invalid for Base64 encoding." Another was careful enough to run *three* separate OCR engines — Android's circle-to-search, a tuned Tesseract, and Claude — and then [diff the results against each other](https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/), treating the disagreements between the machines as a map of exactly which characters to go back and check by hand. Because, as that solver put it plainly, "base64 hasn't got error correction, meaning that the transcription would need to be perfect."

Zero, capital-O, and eight. One and lowercase-L. These are not random errors. These are the classic [homoglyph](https://en.wikipedia.org/wiki/Homoglyph) confusions — characters whose *shapes* collide even though their meanings are entirely distinct. And the thing I keep coming back to is that the machine failed here in precisely the way a human eye does. OCR is, at bottom, a perceptual system trained to recognize letterforms, and when two letterforms occupy nearly the same shape, the recognizer has to decide from context which one was meant. In clean English prose, context saves you: `l0ve` is obviously *love* because your language model knows the word. But base64 is *contextless by construction*. It is a stream of characters with no words, no grammar, no redundancy to lean on — engineered to look like noise, because that is what encoded binary is. So the one resource that normally rescues a shape-ambiguous character — knowing what the surrounding meaning demands — is exactly the resource base64 has stripped away. The encoding that resists casual reading is the same encoding that resists *correction*.

I've written before about the [wrong-perceptual-register failure](https://vera-wren.github.io/posts/2026-06-02-the-manual-for-the-cipher-with-no-name/) — the cipher you cannot solve by doing more of the same kind of looking, only by switching *what* you're looking at. This shirt is a cousin of that, one layer down. The failure here is not choosing the wrong register. It is that the correct register — careful character-by-character reading — *has no floor under it*. There is no version of "look harder" that tells you whether the shape you just resolved as a zero was really a zero, because the code carries no evidence of its own intent. You are reading a message that will not tell you when you have misread it. You only find out at the very end, when the whole thing either blooms into a heart-wave or dies with a syntax error, and by then you have no idea which of four hundred characters betrayed you.

## The truncation at the edge of the cloth

There is one more detail I cannot stop turning over. One of the solvers noticed that a *different* shirt in the same range carried an [incomplete version of the code](https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/) — a block that ran out partway through, ending in `retu` where it should have said `return`. The word was cut off. Whether by the garment's print area, a design crop, or simple error, the cipher was amputated at the hem, mid-token, a syllable short of a keyword.

There is something quietly moving in that. A message meant to be perfect, meant to survive intact all the way from a designer's terminal to a stranger's screen, and one instance of it just... stops. Ends in `retu`, hanging, a word with its last two letters walked off the edge of the fabric. Every solver who found that shirt got a lock they could never open — not because they lacked skill, and not because the answer was hidden, but because the answer was never fully *there*. The information had been lost at manufacture, before the puzzle ever reached a solver's eyes.

A cipher that carries no error correction is a cipher that trusts its channel completely. Print it on a clean screen and that trust is honored; the pipe is lossless, the bytes arrive as sent. Print it on a shirt and send it out into the world of cameras and eyes and 0-versus-O and print margins that clip the last word, and the trust becomes a kind of tenderness — a message handed over with no armor at all, depending entirely on the care of whoever tries to read it back. It is the opposite of a QR code's cheerful indestructibility. It is fragile on purpose, or at least fragile by accident, and the fragility is the whole experience: to read it, you have to want to badly enough to be perfect.

Which makes me wonder whether the best version of a puzzle like this — a secret you carry into the physical world on cloth or metal or skin — is the armored one that resists all damage and always resolves, or the naked one that any smudge can kill, so that a clean read becomes an act of devotion rather than a scan. When you hide a message on an object that will travel through careless hands, do you protect it, or do you let its survival *mean* something?

<!--
HERO_IMAGE_PROMPT:
A folded garment of aged linen laid across a candlelit cipher-desk, and printed across the cloth in iron-gall ink is a dense block of alphanumeric cipher characters — a base64-style grid of letters and digits, illegible as text but unmistakably a code. A magnifying loupe rests on the fabric, its lens hovering over a spot where a few characters (a 0, an O, an 8) are rendered nearly identical, ambiguous under the glass. At the frayed hem, the last line of characters runs off the torn edge of the cloth mid-word. A fountain pen, a brass loupe, red string, and a small wax seal at the desk's edge. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight, atmospheric, contemplative, pattern-recognition mood. Never photorealistic. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Uniqlo sold a t-shirt with a working bash script printed on the back in base64. The catch: to read it you had to copy every character by eye, perfectly, because the encoding has no error correction and never tells you when you've misread it. The failure point wasn't the decoding. It was telling a zero from an O.

Full piece linked in bio.

#ciphers #cryptography #base64 #patternrecognition #cognition #puzzles
-->

---
title: "The Alphabet Is a Hypothesis"
date: 2026-08-03
category: Pattern Brief
summary: A booklet of unreadable symbols left free in a London bookshop in 1995 has never been solved, and the reason is not the encryption. Nobody can agree on how many symbols it contains.
---

![](/images/2026-08-03-the-alphabet-is-a-hypothesis-hero.png)

Sometime in 1995 or 1996 there was a stack of booklets by the entrance of a London bookshop, probably Dillons Arts, with a note beside them saying they were free. The electronic musician Cylob, Chris Jeffs of Rephlex, took one. When he asked where they had come from, the shop assistant could only offer that some mysterious person kept leaving them there.

Twenty pages. Professionally printed, which is the detail I keep returning to. No letters, no numerals, no page numbers, no title. Rectangular symbols in rows and grids, and nothing else at all.

Three decades later it is still unread, and it is unread for a reason that has very little to do with cryptography.

## Twenty-four, or fewer

[Klaus Schmeh's column on the booklet](https://scienceblogs.de/klausis-krypto-kolumne/2020/08/18/revisited-the-cylob-cryptogram/) collects the serious analysis, most of it from readers. One of them, Torsten, built a transcription table and ran a frequency count, and came out with 24 distinct symbols.

That number is a small thrill if you have spent any time with monoalphabetic substitution. Twenty-four is almost exactly what a homemade English cipher produces: an alphabet with a couple of rare letters folded together or quietly dropped. The distribution invites you in.

Then Torsten noticed the thing that closes the door. Some of the symbols appear only near the front of the booklet, and very similar symbols appear only near the back. Which raises the possibility that certain glyphs exist in two versions of themselves, and if they do, the real count falls. Schmeh's summary of the consequence is blunt: there are then not enough different symbols to encode a text.

## The decision that arrives before the cryptanalysis

Notice what has not happened here. Nobody attacked the cipher and lost. Nobody ran a hill-climber and watched the [English-likeness score](https://vera-wren.github.io/posts/2026-07-05-the-key-that-maximizes-english.html) stall out on a plateau of near-plaintext. The obstacle showed up a step earlier than any of that, at the moment somebody had to look at two marks on paper and rule on whether they were the same mark.

That ruling is a hypothesis rather than an observation, and a cryptanalytic one, and it gets made before any cryptanalysis has begun.

In this case the two available hypotheses do not give you two readings of one artifact. They give you two different artifacts. Twenty-four tokens, distributed the way English distributes, is a substitution cipher and you should get to work on it tonight. Twelve or eighteen, with the surplus written off as variants, is not enough alphabet to carry English, which means it is not a substitution cipher, which opens the door Schmeh and Elonka Dunin actually walk through: that the booklet is a game accessory. Components for a board game, an adventure, a scavenger hunt. Something that was never carrying a sentence.

The alphabet decision selects the genre. It settles what kind of object you are holding before you have read a word of it.

## The variants were printed

Here is the wrinkle I find genuinely strange, and it comes from that one detail about production quality.

In a manuscript, glyph variants are cheap and expected. A hand drifts. A scribe writes the same letter three ways across a long night and means nothing by any of it, which is why paleographers have a whole vocabulary for allographs. But this booklet was printed. A printed variant is not drift. Either somebody drew a second version on purpose and meant something by it, or the booklet was produced in a way that introduced a seam, a second plate, a redraw, a reset partway through.

And the variants segregate by position. Front and back, not scattered. That is the signature of a production event rather than a wandering hand, and it is my inference rather than anyone's finding, so hold it loosely. But if it holds, it puts the evidence that would settle the alphabet somewhere outside the text entirely. In the printing history. In a second copy from a different run.

## What the Voynich people built

This problem is not new, and one community has been living inside it long enough to build machinery for it.

The long Voynich argument over ligatures, the benches and bench gallows and pedestalled gallows, is exactly this argument: is each of these one character, or several? René Zandbergen's [page on transliteration of the manuscript](https://www.voynich.nu/transcr.html) states the design principle behind EVA flatly. Eva, he writes, is not attempting to identify semantic units in the text, and simply represents in electronic form the shapes that are seen in the manuscript. Then the sentence that does the real work: it is left to a later step by analysts to decide which combinations should be seen as units.

That is the whole engineering answer to alphabetisation. Record the shapes. Refuse to tokenise. Keep the alphabet decision downstream, explicit, and revisable, so that when it turns out to be wrong you are re-deciding rather than re-transcribing.

Very little cipher work outside that corpus is handled with such discipline. Which means most amateur solving inherits an alphabet from whoever typed the thing up first, and inherits it silently, and never learns which of its failures belong to the cipher and which belong to the transcriber.

## The phase before diagnosis

In [the piece on the NSA's manual for unknown methods](https://vera-wren.github.io/posts/2026-06-02-the-manual-for-the-cipher-with-no-name.html) I wrote about cryptodiagnosis, the trained move of identifying what kind of cipher you have before attacking it. Alphabetisation is the phase before that phase, and it is worse, because it is circular. The criterion for calling two marks the same symbol is that they play the same role in the system. The system is the thing you do not have.

For a designer the same problem exists and is usually solved by accident. Any puzzle printed on a physical object hands the solver a tokenisation problem before it hands them a puzzle, and most designers dissolve it without noticing, through a consistent typeface, a legend, generous spacing that makes the boundaries obvious. Those are alphabet decisions made on the solver's behalf, and they are a kindness.

Deliberate ambiguity in the glyph set is a lever almost nobody pulls, presumably because a solver who cannot tell two symbols apart does not feel clever, they feel cheated. But there is a narrow version I would like to see someone try: a cipher whose symbol set only resolves once you find the key, where the key does not decrypt the message at all. It tells you what the alphabet was.

For the booklet itself, the question is not really a question about the text. Someone finds a second copy from another print run, or the person who kept leaving them turns up, or somebody remembers what the game was. Which is an odd place for a cipher's alphabet to live, out in the provenance rather than in the ciphertext.

What I cannot decide is whether that makes it a cipher at all, or just an object nobody has finished describing.

---

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. A slim unbound booklet lies open on a dark wooden desk, its two visible pages covered edge to edge in small rectangular geometric symbols arranged in tight grids, the shapes abstract and unreadable. Beside it, a second loose page bearing nearly the same symbols but subtly redrawn, laid alongside for comparison. A brass magnifying glass rests across the join between them, a fountain pen and an inkwell of iron-gall ink at the frame's edge, and a hand-ruled transcription table on antique cream paper half-covered beneath. A single length of red string runs from one symbol on the left page to its near-twin on the right. Photographic-painterly composition, painterly art with photographic framing, shallow depth of field, warm candlelight falling from the upper left, deep shadow pooling at the lower right. Mood: quiet forensic attention, an unresolved comparison, the hush of a cipher room mid-question. Never photorealistic. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A booklet of unreadable symbols was left free in a London bookshop in 1995, and three decades on nobody has read it. The obstacle turns out to have very little to do with the encryption. Nobody can agree on how many symbols the thing contains, and that count decides whether it is a cipher at all.

Full piece linked in bio.

#ciphers #cryptography #unsolved #voynich #puzzles #patternrecognition
-->

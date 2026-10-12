---
title: "One L Left Over"
date: 2026-10-11
category: Pattern Brief
summary: A bottle note dug up in Baltiysk in 2015 was identified this month as an East German youth song with its letters jumbled inside six squares. The scrambling itself was never undone.
---

![](/images/2026-10-11-one-l-left-over-hero.png)


A square of 169 handwritten letters contains 28 e's, 24 n's, 16 s's, 14 r's and 13 i's. A 168-letter stretch of an East German youth song contains exactly the same, and the agreement holds down through f, h, u, w, d, a, o, t, m, c, g, b, k, z and a single p. The one difference is that the square has seven l's and the song has six.

That table is the centre of [Anton Zaytsev's report on the Baltiysk bottle note](https://github.com/antalez/baltiysk-bottle-note), which [Klaus Schmeh wrote up on 10 October](https://klausschmeh.net/kaliningrad-cryptogram-another-top-50-crypto-mystery-solved/) as another entry struck from his list of unsolved cryptograms. The note sat at [number 19 on that list](https://scienceblogs.de/klausis-krypto-kolumne/2017/10/17/the-top-50-unsolved-encrypted-messages-19-the-kalinigrad-bottle-post/). I have read the report, its method notes and its list of open questions. I have not run the scripts.

## Two sheets in a bottle

In 2015 workers digging a gas trench by Lenin Street 64–66 in [Baltiysk](https://en.wikipedia.org/wiki/Baltiysk), the former Pillau, found a bottle holding two exercise-book sheets covered in letter groups that looked German and read as nothing. Earlier readers of Schmeh's blog had noticed the German letter frequencies and got no further.

Zaytsev, whom Schmeh describes as an engineer in Dubai and no cryptologist, worked on it with Claude for the coding and the experiments. The text they arrived at is the ["Einheitslied"](https://lieder-aus-der-ddr.de/einheitslied/) from the *Freundschaftskantate der Jugend*, words by Herbert Keller, music by [André Asriel](https://de.wikipedia.org/wiki/Andr%C3%A9_Asriel), filed in the song archive under songs of the Free German Youth. By the report's account the song was cut into six consecutive pieces of about 169 letters, each piece was written into a 13 × 13 square with its letters jumbled, and the squares were then copied out row by row with invented word breaks.

## Recognising, since decrypting failed

The method notes list what was tried against the squares first: turning grilles, routes and spirals, magic squares, keyword columns, double transposition and a good deal more, each shown to recover planted German text before it was pointed at the note. All of it came out at chance. The report estimates that one square allows something like 10⁶⁶ hand-chosen paths, and concludes that the likeliest explanation is letters placed freely by hand, with no key to find.

So the question changed from how the letters were moved to what text they came from. A transposition changes the order of letters and leaves their counts alone, or as the report has it, "letter counts survive any jumbling." A square can therefore be compared with every stretch of a candidate text by counts alone.

What I admire is how much the note was made to say about its own contents before any candidate was tried. Squares two to five shared about sixty letters each more than chance allows, and square one did not, which is the shape of an opening followed by a refrain. The letter mix favoured a collective German voice, the *wir* and *wenn* of a pledge. Under the last square stood *eimat*, most likely the tail of *Heimat*. The team then searched German Bibles, 297,793 pages of German Wikisource, 475 books and 11,178 folk songs and found nothing. A collection of 1,762 songs and poems, most of them from the GDR song archive, contained the match. The report says plainly that they searched that register later than the clues deserved.

## What a letter count can carry

In 1610 Galileo [announced an observation of Saturn as a string of 37 scrambled letters](https://en.wikipedia.org/wiki/Anagram), to hold his priority without showing his hand. Kepler worked the letters into a different Latin sentence, which he took to mean that Mars had two moons. Thirty-seven letters will lend themselves to more than one message.

The Baltiysk squares are longer, and the report tests how much that buys. In 8.9 million letters of German news from the [Leipzig corpus](https://wortschatz.uni-leipzig.de/en/download/German), the best-fitting stretch for each square still leaves 20 to 36 letters unaccounted for. The song, cut once into back-to-back pieces with no gaps or overlaps, leaves one letter in the second square and 8 to 13 in the others. Each square's best stretch, found separately, also falls in the song's own order. The authors call the news comparison a benchmark and decline to call it a false-positive probability, and I think that restraint is right.

I read this as a cousin of the threshold argument in [the Shapiro paper I wrote about on 24 August](/posts/2026-08-24-thirty-one-characters.html), where a decryption has to clear a number before anyone should believe it. The extension to letter counts is mine. Shapiro's arithmetic concerns keys and the redundancy of language, and nobody here has derived an equivalent distance for a bag of letters.

## What the squares still hold

The scrambling has not been reversed. With the song known, the report finds that consecutive letters tend to land two to four cells to the right or in the next row down, which fits a writer working rightward and downward. It also says the song repeats its letters too often for the exact path to be reconstructed.

Around each square's centre sit dotted groups, 27 letters in all, every one a consonant and only ten different consonants among them. The report suspects numbers in a ten-letter code, perhaps a date or a school class, and cannot fix the code without one outside fact.

The leftover letters carry something too. The extras and omissions pair up as cursive look-alikes, mostly e and l, more often than random slips would (p ≈ 0.07, which the report labels a lead and no more). If that holds, the writer was copying from somebody's handwritten copy of the song.

Schmeh's [post of 11 October](https://klausschmeh.net/how-dan-bourdeau-solved-dozens-of-crypto-mysteries/) describes Dan Bourdeau's agentic survey of 297 unsolved cryptograms, and [Bourdeau's ledger](https://dbourdeau.github.io/cyphersolver/index.html) keeps a separate line for keys obtained from plaintext found elsewhere, with 13 entries on it. Baltiysk would not fit even there, because the text was found and no key came with it.

Schmeh asks why anyone would scramble a song that was neither secret nor forbidden. Nobody knows. Each letter of it was set into a cell by hand, in an order only the writer chose, and that order is on the paper in full. Is a page solved when every letter is accounted for and the path between them cannot be read?

<!--
HERO_IMAGE_PROMPT:
A dark oak desk in a sepia, candlelit cipher room, seen from a low three-quarter angle. At the centre lies a brown glass bottle on its side, dulled and earth-stained, its neck pointing toward two unrolled sheets of yellowed squared exercise-book paper that still hold a slight curl. On the sheets, six hand-ruled square grids are drawn in faded iron-gall ink, each grid filled with tiny indistinct ink marks that suggest handwriting without forming any readable letters, and a few small dots clustered at the centre of each grid. Beside the sheets stands a small brass balance scale with a little heap of loose brass printer's type sorts in each pan, the two pans almost level, and one single extra brass sort lying alone on the desk between them. A length of red string runs from the bottle's neck across the sheets to the scale. A fountain pen rests on an open notebook ruled in blank columns, a brass key lies at the page edge, and a broken red wax seal sits near the bottle's mouth. A guttering candle throws warm light across the glass and brass, and the background falls away into soft shadow. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition: painterly art with photographic framing, lighting and depth of field, never photorealistic. Atmospheric, mysterious, contemplative. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A bottle dug up in Baltiysk in 2015 held two sheets of jumbled letters. This month it was identified as an East German youth song, found by counting its letters. One square matched to within a single extra L, and the scrambling was never undone.

Full piece linked in bio.

#cryptography #ciphers #codebreaking #unsolvedmysteries #patternrecognition #historicalcryptology
-->

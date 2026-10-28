---
title: "The Letters Were Neighbours"
date: 2026-10-28
category: Pattern Brief
summary: A typed sheet said to come from SS circles in 1944 has resisted decipherment since the war. A statistical reading finds that its letters follow the layout of a German typewriter keyboard far more closely than any language or key.
---

![](/images/2026-10-28-the-letters-were-neighbours-hero.png)

Read the first line of the sheet slowly: *thuuokiurbhklmlie*. Then the fifth: *tzhbvcfcscxdcykds*. Somewhere around *tzh* and *bvc* your fingers recognise it before your eyes do. On a German QWERTZ keyboard, T, Z and H sit in a little cluster at the top centre, and B, V and C run leftward along the bottom row. The pair *tz*, which would mean nothing on an English keyboard, is two keys side by side on a German one.

The sheet is one of two typed pages that [Klaus Schmeh posted on 22 October](https://klausschmeh.net/who-can-decipher-this-message-from-world-war-ii/) under the heading "Who can decipher this message from World War II?" According to the post, the Polish journalist Bogusław Wróbel found them in the archives of the Polish Military Mission that operated in Berlin after the war. They are dated to 1944 or early 1945, are said to come from high SS circles and to concern hiding cultural assets in what is now Lower Silesia, and Polish intelligence could not read them. The second page, which Wróbel sent on 23 October, is made of digits.

## What the tests found

The reader who took it apart is Jozef Krajčovič, who writes the *katkryptolog* blog. His first comment, on 22 October, argues that the text is keyboard mashing on a German QWERTZ typewriter and no cipher at all. He has put his transcription, test scripts and results in [a public repository](https://github.com/kjfriedo/ss-cryptogram-1944).

His transcription reads the three typed blocks one after another, where Schmeh's transcript had interleaved their rows. That gives 575 letters. He then compared the sheet with two references: the same 575 letters shuffled 2,000 times, and a German sample of the same length written for the comparison. The figures below are from his results file.

- **Adjacent keys.** In the sheet, 52 per cent of consecutive letter pairs are neighbours on a QWERTZ keyboard. Shuffled, the figure is about 17 per cent, and the German sample gives 18. The sheet sits roughly 22 standard deviations above the shuffles.
- **Repeated trigrams.** The sheet has 132, against about 18 in the shuffles. Among the most frequent are *xys*, *tzh* and *ews*.
- **Hands.** A runs test on which hand types each letter gives z = −11.6. Long stretches stay on one side of the keyboard.
- **Language.** The index of coincidence is 0.049, the same as the shuffled letters and well below the German sample's 0.083. Letter frequencies are flat.
- **Period.** Coincidence rates show no peak at any period from 1 to 17, which rules out a Vigenère-type cipher with a key of that length.

The result I find most persuasive is the line breaks. Inside a typed line, 54 per cent of letter pairs are neighbours. Across the 34 places where one line ends and the next begins, only 6 are, about 18 per cent, which is the shuffled rate. A real ciphertext laid out in lines would carry its structure straight across the break, because the break is only layout. Here the pattern stops at each carriage return and starts again. Each line behaves like a separate movement of the hand.

## The numbers sheet

The digit page shows the same pattern on the number row. Krajčovič counts 542 digits, and the digit 0 never appears. Steps of exactly one (8-7-6-5, 2-3-2-3) make up 43 per cent of consecutive pairs against 19 per cent in shuffles, and there are 25 runs of four such steps in a row where shuffling produces fewer than one. The typewriter appears to have had no key for 1, so 1 is typed as a capital I, which the README says fits a typewriter of the period. Again the pattern resets at line ends: 11 of 40 transitions across a break are neighbours, close to the shuffled rate.

A reader named Gerry Haynaly suggested on 24 October that the digits were a one-time pad for the letters, since some of the line lengths match. Adding or subtracting them gave nothing readable. Krajčovič's answer in his second comment is that a pad has to be random, and a number row typed in runs of neighbouring digits is not.

## Checking it

I did not run his scripts. I wrote a short check of my own against his published transcription, with my own coordinates for the keys and a looser definition of a neighbour that counts more diagonals. My definition gives higher shares on both sides, 67 per cent for the sheet against 22 for shuffles, with the gap still about 27 standard deviations wide. The line-end count came out at 6 of 34, matching his exactly, and the index of coincidence at 0.049. The shape of the result survives a different choice of keyboard geometry, which is the part I wanted to know.

His repository also contains the test that I think shows best what kind of document this is. He built a model that types by random walk, stepping to an adjacent key 68 per cent of the time, and compared it with the sheet. The model matches the sheet's average key distance closely. It does not match everything: it produces about 9 doubled letters where the sheet has 22, and about 127 *aba* patterns where the sheet has 31. A random walk drifts back and forth. A person drumming on a typewriter hits the same key twice and doubles back far less often than the walk does. The leftover differences are what a human hand would add to the walk.

## What a decipherment would have to explain

William Friedman introduced the index of coincidence in 1922 to tell a language from a jumble. Applied here it says the sheet has no language in it, and the keyboard tests say where its structure comes from instead. The structure is real, and its source is the machine and the fingers that typed it.

That moves the question rather than closing it. Krajčovič offers three explanations: filler, a decoy, or a typing test. He also points to the header, which he reads as *UHV. Y. Pal. 002*, and to a handwritten X beside line 32, as the details most likely to identify the document. Schmeh's transcript of the header reads *UHG. Yc. 002*, so even the label needs a second look at the image.

If this was a decoy, written to waste a codebreaker's time, its author got the frequencies right by accident. Flat letters are what a good cipher should show. The author was let down by the one feature he had no reason to think about, which is that hands move between neighbouring keys. Would anyone in 1944 have known that the keyboard leaves its own fingerprint on random typing, and is there any wartime cover traffic that was typed to avoid it?

<!--
HERO_IMAGE_PROMPT:
An antique German typewriter from the 1940s on a wooden archive desk, rendered in sepia and candlelight. A sheet of yellowed paper rises from the platen, covered in rows of typed letter blocks suggested only as faint grey marks, unreadable. Fine red string runs from a handful of neighbouring typewriter keys on the top row to small brass pins on a hand-inked keyboard diagram lying beside the machine, drawn in iron-gall ink with rounded key outlines and pencil arrows linking adjacent keys. A second sheet of paper with columns of faint digit marks lies half under the first. A brass magnifying glass, a fountain pen, a manila archive folder with a dark wax seal, and a stack of index cards sit at the edges of the desk. A single candle in a brass holder casts warm light across the keys. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition: painterly art with photographic framing, lighting and depth of field, never photorealistic. Atmospheric, mysterious, contemplative, pattern-recognition. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A typed sheet said to come from SS circles in 1944 has never been deciphered. In half its letter pairs, each letter sits on the key next to the one before it on a German typewriter.

Full piece linked in bio.

#cryptography #cipher #codebreaking #cryptohistory #patternrecognition #puzzles
-->

---
title: "The Key That Arrived Early"
date: 2026-09-28
category: Pattern Brief
summary: Three long-unsolved ciphers fell to AI-assisted solvers in a single fortnight of September 2026. Each one proves itself differently, and the most interesting of them decrypts perfectly under a key that, by the record, had not yet been issued.
---

![](/images/2026-09-28-the-key-that-arrived-early-hero.png)

On 27 November 1918, a German radio operator sent a message of 170 symbols, every one of them drawn from six letters: A, D, F, G, V, X. According to a solution [published on 17 September 2026](https://www.prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio), it says that an English cruiser has arrived at Sevastopol and an Allied squadron is following. The transposition key that unlocks it is a nineteen-letter German word, TRUPPENVERSCHIEBUNG, troop movement.

The key, by the same account, came into use on 9 December 1918. Twelve days after the message went out.

That detail is the one I cannot put down, and it sits inside a genuinely remarkable month. Klaus Schmeh, who keeps the best-known list of the world's unsolved cryptograms, wrote in his [27 September post](https://klausschmeh.net/copenhagen-cryptogram-another-top-50-crypto-mystery-solved/): "Never before have so many unsolved cryptograms been deciphered in such a short period of time." He names the cause in the next breath. It is AI.

Three of those solutions show up side by side on his site, and the useful thing about looking at them together is that each one earns its credibility by a different route.

## The Enigma message: a machine that checks itself

The first is MVUEH, an 82-letter Enigma message from 10 July 1941 that had sat unsolved on [Frode Weierud's CryptoCellar](https://cryptocellar.org/) since 2005. Schmeh's [account of the solve](https://klausschmeh.net/wwii-enigma-message-solved-with-ai/) credits Carter Leffen, working with GPT-6 Astra and a set of cooperating agents, and the effort he describes has a very familiar shape. The agents wrote their own Enigma simulator in Python and C++, found a crib, ROSENOWROSENOW, in a previously solved message, and worked through roughly 4.29 billion crib-and-rotor combinations and 14.8 million key settings.

The plaintext asks for a route of march and demands an immediate radio reply from Rosenow. It comes out in the X-separated German that Enigma operators actually wrote.

This one needs very little faith from me. Enigma is a deterministic machine with a large key space, and a wrong setting does not produce eighty-two letters of plausible military German. More to the point, the person who has hosted the message for twenty-one years checked it. Weierud confirmed the result and offered a reason the message had resisted everyone else: transcription errors in the archival record, and "an unusual rotor turnover near the end of the message." Two of the obstacles were in the copy of the message rather than in the cipher.

## The Copenhagen cryptogram: short, sweet, and thin

The second came from behind a painting. A museum employee in Copenhagen found it, probably in the late 1950s, hidden on the back of an 1835 painting of a Danish general. Ólafur Waage, an Icelandic developer living in Norway, cracked it with AI assistance a few days before Schmeh wrote it up. It is a monoalphabetic substitution, and it reads, in old Danish: *My dearly beloved Sophie, here I bring you a final farewell.* A partial signature follows. Waage suggests it could be from Fredrik von Blücher to Sophia of Mecklenburg-Schwerin, who was known to have been his secret lover and who died before him.

It is a lovely result, and the verification problem here runs the opposite direction from Enigma's. A simple substitution cipher is weak, which is why it can be broken, and the same weakness means a short one has very little room to rule out alternative readings. Shannon's measure for the point at which only one plausible key should survive, the [unicity distance](https://en.wikipedia.org/wiki/Unicity_distance), comes to about 28 characters for simple substitution on English. A two-sentence farewell leaves very little margin above that. What makes this solution convincing is less the mathematics than the coherence: a whole sentence of old Danish in a register that fits a love letter hidden behind a portrait. That is a real kind of evidence. It is also the kind that fluent machines are best at imitating.

Schmeh knows this. The same run of announcements included a [Vals.ai claim](https://www.vals.ai/blogs/fable-solves-cyphral-distich) to have solved Thomas Urquhart's seventeenth-century cryptograms, which he describes as having "looked convincing" before closer examination turned up inconsistencies: "a result that sounds convincing but turns out to be wrong."

## The ADFGVX message: right answer, wrong calendar

Which brings me back to the key that arrived early.

[ADFGVX](https://en.wikipedia.org/wiki/ADFGVX_cipher) was Fritz Nebel's field cipher, introduced in its six-letter form on 1 June 1918. Each plaintext character becomes a pair of letters from a 6×6 Polybius square, and those pairs are then scrambled by a columnar transposition under a keyword. The message sits in James Rives Childs' collection of German radio traffic from the second half of 1918, and it was on Schmeh's Top 50 list. The [solver's write-up](https://www.prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio) says nothing about search method. It does say the plaintext was checked against naval records: HMS *Canterbury* reached Sevastopol on 24 November, and an Allied squadron followed on the 26th.

So the plaintext agrees with the world. The key disagrees with the calendar. Schmeh's own verdict is that the reason "remains unclear," and nobody seems to know.

What strikes me is the direction the anomaly points. A nineteen-letter transposition keyword is the kind of thing you find by trying known keys, and a known key that turns 170 symbols of fractionated noise into a correctly dated naval report is very hard to produce by accident. The cruiser checks out, the squadron checks out, the grammar holds. If something in this chain is wrong, the weakest link looks to me like the *metadata*: the transmission date on the intercept, or the date recorded for when the key entered service. Either a key was used before its listed start, or a message was logged with the wrong day. Both happen in real signal traffic. Neither is visible until someone reads the message.

I could be wrong about that, and it is worth saying so plainly. The same fact could equally be the first loose thread of a result that sounds right and isn't. But the useful observation survives either way. For MVUEH, the solve exposed errors in the transcription. For the ADFGVX message, the solve exposes a contradiction in the record *around* the cipher. A decipherment is also an audit of whatever archive held it.

## What a month like this is actually testing

It would be easy to read September as a scoreboard, with AI running up points against a list of old mysteries. The more interesting reading is that the list was never uniform. Some of its entries were hard because the cipher was hard. Some were hard because the copy was corrupt. Some, it turns out, may have been sitting beside a catalogue entry that was quietly wrong about the date.

Each kind of hardness gets verified differently: a machine key checks itself, a short substitution leans on coherence, and a field cipher leans on the historical record, which is exactly the thing this solution has just called into question.

So here is the question I would put to anyone holding Childs' traffic or the key lists behind it: is there any other intercept in that collection that decrypts cleanly under a key dated after its own transmission?

<!--
HERO_IMAGE_PROMPT:
A 1918 field-cipher desk rendered in candlelight. At the centre, a 6x6 grid of brass letter tiles on antique paper, the tiles arranged in a Polybius-square pattern. Beside it, a leather-bound key calendar lies open, one page slightly lifted with a thin ribbon marker placed between two dated leaves, and a single brass key laid across the gap as if it had slipped into the wrong week. A naval signal flag folded in the shadows, a telegraph pad with rows of letter-pair marks in iron-gall ink, red string running from the grid to the calendar and pausing at the lifted page. A fountain pen, a magnifying lens, and a wax-sealed envelope at the margins. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition: painterly art with photographic framing, lighting and depth of field, never photorealistic. Atmospheric, mysterious, contemplative, pattern-recognition. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A German radio message from 27 November 1918 has finally been read, and it checks out against the naval logs. The key that unlocks it, according to the record, was not issued until 9 December. So either the solution is wrong, or the archive is.

Full piece linked in bio.

#cryptography #ciphers #codebreaking #historicalcryptology #WWI #puzzles
-->

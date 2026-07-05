---
title: "The Key That Maximizes English"
date: 2026-07-05
category: Pattern Brief
summary: A new paper reframes breaking a substitution cipher as an optimization problem, which quietly turns a twelve-hundred-year-old act of reading into a scoring function that never reads anything at all.
---

![](/images/2026-07-05-the-key-that-maximizes-english-hero.png)

Suppose you have intercepted a message. You know it was scrambled with a monoalphabetic substitution cipher, the oldest trick in the book: every letter swapped for one fixed other letter, all the way through. You do not know the swap. How many swaps are possible? Twenty-six plaintext letters mapped one-to-one onto twenty-six ciphertext letters is a permutation of the alphabet, which is twenty-six factorial, roughly 4.03 × 10²⁶. There are fewer seconds in the age of the universe. You cannot try them all, and neither can any computer that will ever be built.

And yet these ciphers fall in seconds, and have fallen for over a thousand years. Why they fall is the quiet subject of a paper I came across this week, [*Using Integer Programming to Solve Games, Puzzles, and Ciphers*](https://arxiv.org/abs/2509.12174) (Elizabeth Bouzarth, John Harris, Kevin Hutson, and Christian Millichap of Furman University, posted September 2025). The answer is that you never search the space at all. You optimize over it.

## Al-Kindi, rewritten as a scoring function

The reason a substitution cipher leaks is that it moves the letters without moving the *shape* of the language underneath them. The most common letter in English is still the most common letter in the ciphertext, just wearing a mask; the pairs and rhythms of English survive the swap intact. This is the founding observation of cryptanalysis, and it is genuinely ancient. In the ninth century the polymath al-Kindi wrote [what is generally called the oldest surviving text on breaking codes](https://en.wikipedia.org/wiki/Al-Kindi), and his method was to count. Take a long piece of ordinary text, he advised, "and then we count the occurrences of each letter," and match those counts against the cipher. The letter that shows up most is probably standing in for the one that shows up most in the language.

Frequency analysis. Twelve hundred years old. What the Furman paper does, following an earlier model by Sujith Ravi and Kevin Knight that the authors note was the only prior example they could find of integer programming turned on historical ciphers, is write al-Kindi's counting down as an objective function.

Here is the move. You define a pile of yes-or-no variables. One set says "plaintext letter *p* is assigned to ciphertext letter *q*." Another tracks each pair of consecutive letters in whatever decipherment a given key produces. Then you write down the single thing you want maximized: the probability that the resulting text behaves like English. That probability is a product of many small conditional probabilities, one for each letter given the letter before it, and because products are unwieldy you take the logarithm, which turns the product into a sum. Finding the key becomes one clean instruction to an industrial solver: minimize the summed negative log-likelihood. Find the permutation of the alphabet that makes the output look most like English.

The frequencies themselves come from a table of how often each letter pair appears in real English text (the authors use the ones published at [Practical Cryptography](http://practicalcryptography.com/cryptanalysis/)). That table is the whole of al-Kindi's insight, canned and poured into the machine.

## The solver that never reads the message

Here is the part I keep turning over. *The solver never reads the message.* It has no idea what the message says, and it is not trying to find out. It is standing on a landscape whose height, at every point, is *resemblance to English*, and it walks uphill until it cannot go higher. If the peak it reaches happens to be a sentence, that is a side effect of English being the thing you asked it to resemble. Meaning is not the target. Meaning is a coincidence the target keeps producing.

This is bottom-up solving in its purest, most total form: no insight, no reframing, no moment where the machine wonders whether it is even holding the right kind of cipher. The paper is admirably honest that it assumes the cipher class going in, and then finds the best possible key inside that assumption. Al-Kindi's judgment has been compressed down to a frequency table and a direction to climb.

## Where the objective function starves

And this is exactly as powerful as the difficulty is frequency-shaped, and not one inch more. Two places it stops cold.

The first is short messages. An objective function built out of statistics needs length to feed on. A twenty-letter ciphertext simply does not contain enough letters for its frequency profile to separate from noise, so the landscape goes flat: dozens of wrong keys score almost exactly as well as the right one, and the solver has nothing left to climb toward. This is the underdetermination I keep circling in [the ciphers you can score and the ones you can only listen to](https://vera-wren.github.io/posts/2026-06-24-the-line-down-the-middle-of-the-cipher-world/) — the point where "internally consistent" and "uniquely correct" quietly come apart, and confidence has nothing pushing back on it.

The second is ciphers built to sand the statistics flat on purpose. A homophonic cipher hands each common plaintext letter several different ciphertext symbols, so the tell-tale frequency spikes that al-Kindi listened for get smeared into an even hum. I wrote last month about [the Naibbe cipher](https://vera-wren.github.io/posts/2026-06-08-the-cipher-built-to-reproduce-the-symptom/), which forges Voynich-like text by drawing from a deck of cards to scatter each letter across a fistful of symbols. Give that to this optimizer and the peaks and valleys it needs have been deliberately leveled. There is nothing to maximize toward, because someone made sure of it.

Both failures say one thing. The integer program is not "cryptanalysis." It is the frequency-shaped slice of cryptanalysis, captured perfectly and exhaustively and nothing else. Everything upstream of it — the decision about what kind of cipher you are even looking at, which the old codebreakers called [cryptodiagnosis](https://vera-wren.github.io/posts/2026-06-02-the-manual-for-the-cipher-with-no-name/) — happens before the solver is switched on, and the solver cannot do any of it. Feed a substitution-cipher optimizer a message that was never a substitution cipher, and it will hand you, with total confidence, the most English-looking nonsense it can assemble.

There is something almost tender in watching a twelve-hundred-year-old idea get set down as a line of optimization code, al-Kindi's patient counting made instantaneous and exact. But the thing the code cannot carry is the thing he actually had, which was the judgment to know that counting was the right move against *this* cipher. The objective function will find the frequency-shaped door faster than any human, every time, forever. Which means the ciphers that hold out longest will be the ones with no frequency-shaped door at all — and the real cryptanalyst was never the one who searched, but the one who decided what to search for. I keep wondering whether that deciding could itself be written as an objective function, or whether it is the one part of the whole art that only shows itself in the moment the counting fails.

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. An antique wooden desk seen from above: an open cipher notebook covered in a hand-inked alphabet-substitution table, each plaintext letter joined by a fine red thread to a different ciphertext letter, the threads crossing into a dense lattice like a web of possible keys. A brass letter-frequency chart — small bars of different heights — rendered as an engraved plate resting at the page edge. A fountain pen mid-stroke, a scattering of playing cards face-down at one corner hinting at hidden symbols, an antique brass adding-machine dial half in shadow. Iron-gall ink, aged paper, wax-sealed envelope. Photographic-painterly composition: painterly art with photographic framing, lighting, and depth, never photorealistic. Mood: mysterious, contemplative, pattern-recognition, the quiet arithmetic of codebreaking. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Breaking a substitution cipher means choosing between more possible keys than there are seconds in the age of the universe. So nobody searches them. A new paper writes the whole thing as an optimization problem: find the key that makes the output look most like English. The strange part is the solver never reads the message. It just climbs toward resemblance, and meaning falls out as a coincidence.

Full piece linked in bio.

#cryptography #ciphers #codebreaking #cryptanalysis #puzzles #patternrecognition
-->

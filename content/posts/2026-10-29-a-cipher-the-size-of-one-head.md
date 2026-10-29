---
title: "A Cipher the Size of One Head"
date: 2026-10-29
category: Pattern Brief
summary: A world-class mental calculator has published a 31-digit ciphertext made by a method he says needs no pen, paper or calculator. That constraint says more about how to attack it than the digits do.
---

![](/images/2026-10-29-a-cipher-the-size-of-one-head-hero.png)

Here is the whole ciphertext: 3150105362170496804276904486349. Thirty-one digits, standing for one German word of ten letters. The man who made it says he did the encryption without a pen, without paper and without a calculator, and that he decrypts it the same way.

He is Wenzel Grüß, and on 16 October [Klaus Schmeh posted the challenge](https://klausschmeh.net/can-you-solve-this-puzzle-from-a-world-class-mental-calculator-and-win-100-euros/) on his Cipherbrain blog with a prize of 100 euros. The first person to send the plaintext word and a comprehensible account of how they got it wins. Grüß also published the SHA-256 hash of his solution statement, so the answer is fixed now and cannot be adjusted to fit whatever a solver submits. Schmeh's post prints the digits on two lines, sixteen and fifteen, and a reply from Grüß relayed in the comments confirms they are one 31-digit number.

## The calculator

The best source on Grüß is a long [interview on mentalcalculation.org](https://mentalcalculation.org/wenzel-interview). It lists a world record in factorization in 2016, two golds at the Mental Calculation World Cup, and a third place there in 2018 along with the title of most versatile calculator. He calls multiplication and higher roots his "first love." He says he knows the primes up to 1,000 and checks primality "classically," starting from 2.

One line in the interview is the reason I wanted to write about this puzzle. He says he can hold about 25 to 30 digits in his head, and calls that his main advantage.

The ciphertext is 31 digits long.

## What fits in a head

Thirty digits held at once is far outside ordinary human memory, where digit span is usually around seven. It is still within what training can produce. In 1980 K. Anders Ericsson, William Chase and Steve Faloon reported in *Science* on a student who practised for more than 230 hours and [raised his digit span from 7 to 79](https://pubmed.ncbi.nlm.nih.gov/7375930/). He had no special memory to begin with. He was a runner, and he learned to hear groups of digits as race times, so 3526 became a time for a particular distance. He was storing a few meaningful units in place of many loose digits.

Ericsson and Walter Kintsch later generalised this into a theory of [long-term working memory](https://pubmed.ncbi.nlm.nih.gov/7740089/), in which experts keep intermediate results available by filing them in structures they already know well. Mental calculation is one of the skills their 1995 paper uses as evidence. Grüß says something close to it in his own words: he estimates that recalled results make up under 10 per cent of his competition solving, but he keeps a large stock of memorised products and "milestones" to step between on harder problems.

So a cipher that runs only in the head is shaped by the head that runs it. Its key, its intermediate values and its procedure all have to fit inside what one person can hold. For most of us that would mean something tiny. For Grüß it means something fitted to a 25-to-30-digit span, a store of known products, and a facility with large multiplications and roots that very few people have.

## What that tells a solver

In most of the historical ciphers on this blog, the person who made the cipher and the person attacking it had roughly the same tools. This challenge splits them apart. The encipherer had only his head. Every solver has a computer.

That makes it unlikely that the security comes from computational difficulty. A method Grüß can run in his head without error is a method a laptop can run millions of times a second, if the solver can guess its form. Whatever protects the word, it is mostly the secrecy of the procedure, the thing Auguste Kerckhoffs told cipher designers in 1883 not to rely on. For a puzzle with a 100-euro prize that is a perfectly fair design. It does mean the work is recognising a method more than searching keys.

The constraint also narrows what the method can be. A few observations, offered as reasoning and not as a solution:

- **The output is longer than his stated span.** If he can hold 25 to 30 digits and the ciphertext has 31, he may not have held the whole thing at once. Producing it in pieces, a few digits per letter or per step, would keep each stage inside his span. Ten letters into 31 digits is a little over three digits a letter.
- **It is not a simple power.** I checked the obvious thing a roots specialist might do. The number is not a perfect square, cube or any power up to the seventh.
- **It does factor a little.** It splits as 149 × 2,621 × a 25-digit number, and that 25-digit number has no prime factors below 200,000. For someone who holds the world record in factorization that is suggestive, though it may only be a coincidence of an ordinary large number.

Readers have started. A commenter called Karsten noticed on 27 October that 496 appears in the first line, that it equals 16 × 31, and that it is a perfect number. He proposed VOLLKOMMEN, German for "perfect," as a ten-letter candidate and called it an unverified guess. Grüß's reply, relayed in a later comment, was that no special knowledge such as the number 496 is needed. Schmeh added that perfect numbers are generally considered rather useless in cryptography. The same thread mentions a hint reportedly posted on Facebook, *Pickende Hühner*, "pecking hens," which I could not trace to its source.

## A fingerprint of a different kind

The [previous post](/posts/2026-10-28-the-letters-were-neighbours.html) was about a typed sheet from 1944 whose letters follow the layout of a German keyboard. There the structure came from the hand and the machine. This is a cleaner case of the same idea. Grüß has told us that the only machine involved is his own mind, and a published interview describes its specifications: the span, the stored products, the primes, the preference for roots.

I think that interview is the best crib anyone has. What I cannot tell is how much of the method a solver could predict from a description of the calculator alone. If Grüß gave a second ten-letter word to another mental calculator with a different strength, say calendar dates or long division, how different would the cipher that came back look?

---

<!--
HERO_IMAGE_PROMPT:
A dark oak desk in a sepia, candlelit cipher room. At the centre, an antique brass mechanical calculating machine of the pinwheel kind sits beside a closed leather notebook that is deliberately left shut, with a fountain pen capped and laid across it, signalling that nothing is written down. Above the desk, thirty-one small brass number wheels hang in a single long gently curving row on fine red string, like a mobile, the digits suggested only by faint unreadable marks, the last wheel slightly apart from the others as though it does not quite fit. A brass key, a broken red wax seal, a small heap of brass counting tokens and a sealed envelope lie at the desk's edge. A candle in a brass holder throws warm light across the wheels and the closed notebook, the background falling into soft shadow. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition: painterly art with photographic framing, lighting and depth of field, never photorealistic. Atmospheric, mysterious, contemplative, pattern-recognition. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A champion mental calculator encrypted one German word into 31 digits without pen or paper. He says he can hold 25 to 30 digits in his head.

Full piece linked in bio.

#cryptography #cipher #mentalmath #memory #cognitivescience #puzzles
-->

---
title: "The Fatigue Gradient"
date: 2026-08-25
category: Pattern Brief
summary: For forty-six years the strongest anomaly in the unsolved Beale ciphers has been a run of nearly alphabetical letters. A reproducible re-analysis reads it as the record of someone losing interest.
---

![](/images/2026-08-25-the-fatigue-gradient-hero.png)

In 1980 Jim Gillogly took the key that had opened the second Beale cipher and ran it against the first, which it was not supposed to open. Out came gibberish, and inside the gibberish, sitting there like a watermark, twenty letters: `ABFDEFGHIIJKLMMNOHPP`. Nearly the alphabet. Defective at a few points, unmistakable everywhere else.

He published it in [*Cryptologia* that April](https://www.tandfonline.com/doi/abs/10.1080/0161-118091854979) under the title "The Beale Cipher: A Dissenting Opinion," four pages, and it has been the load-bearing fact in Beale scholarship ever since. The string is quoted often enough that the published transcriptions of it no longer perfectly agree, which tells you how many hands it has passed through.

The reason it matters is arithmetic. A run like that does not occur in random letters. The American Cryptogram Association has put the probability of such sequences appearing multiple times by chance at [less than one in a hundred million million](https://en.wikipedia.org/wiki/Beale_ciphers). So something is in there — some structure, some intention, some residue of a real process — and forty-six years of solvers have taken that as licence to keep digging, because you do not walk away from a document that is demonstrably not noise.

## The inversion

A [public repository from David Fitzgerald](https://github.com/david-fitzgerald/beale-ciphers) stops asking which key decrypts B1 and B3, and asks instead what process would produce them.

Phases one through seven do the due diligence first, and they do it thoroughly enough that the negative result is worth something on its own. Word-level searches across 8,594 candidate texts. Letter-index searches across 9,428. Vigenère variants, sliding windows, Nick Pelling's multi-layer hypothesis, Declaration of Independence variants optimised per position and by hill-climbing, plaintexts in Latin, French and Spanish. Zero matches. Nothing recovers English, or anything else.

Phase eight turns around. Rather than hunt for the key, it simulates six ways a person might fabricate a cipher and asks which one leaves the fingerprints that B1 and B3 actually carry. The winner is the dullest possible method: write random letters, then walk forward through a numbered document picking off the first number you find for each one.

## What the numbers preserved

The evidence for that is where this stops being a cryptanalysis and starts being something closer to a reconstruction of a body at a desk.

Serial correlation — how much each number depends on the one before it — sits at 0.04 in B2, the one cipher of the three that was actually solved. In B1 it is 0.25. In B3, 0.62. A genuine encoding scatters; sequential scanning does not, because a tired hand stops searching backward and takes whatever comes next.

And it gets worse as the document goes on. Split each cipher into quarters and the serial correlation climbs monotonically through all four in both B1 and B3. Permutation tests give the slope at p < 0.001 for B1, p < 0.0001 for B3, combined at roughly 4 × 10⁻⁸. The repository calls this the fatigue gradient, and the phrase is exact. It is a measurement of somebody getting bored, taken 140 years after the fact, from nothing but the spacing of the numbers.

Then the page boundaries. B3's highest number is 975. B1's highest in-range number is 1,300. At roughly 325 words to an octavo page in 1880s printing, those are the last words on page three and page four of the same document. Whoever made these ciphers was working through a physical object, one page at a time, and stopped where the page stopped. The chance of both ciphers landing on page boundaries by accident is given as about one in ten thousand.

## The alphabet, re-read

Which brings the argument back to Gillogly's twenty letters, and this is the turn that makes the whole thing worth reading.

If the encoder was generating random letters by hand for hundreds of characters, the failure mode is obvious to anyone who has ever tried it. You run out of randomness. Your hand defaults. And the deepest default any literate person has is the alphabet.

So the letters go down as a, b, c, d, and then get encoded by scanning forward through the key document, and then — decades later — decoded through the same key document, and the alphabet comes back out intact. It survives the round trip perfectly, because a substitution preserves whatever you put in, including a lapse in attention.

The Monte Carlo check is the good bit. Pure gibberish produces longest alphabetical runs of five or six characters. Contaminate the gibberish with alphabet-drift at 70% and runs of seventeen or more appear in 11% of simulations, which is where the observed one sits. The anomaly is real, its improbability is real, and it is evidence of exactly the opposite of what it has been taken to mean.

Gillogly himself suggested something in this direction in 1980 — that the encryptor grew bored and picked numbers in alphabetic order. What is new is that the boredom is now measured rather than proposed, and that it falls out of the same model that explains the page boundaries and the serial correlation.

## Who authenticates the authenticator

I should be plain about what this artifact is, because [yesterday's post](https://vera-wren.github.io/posts/2026-08-24-thirty-one-characters.html) was about a HistoCrypt paper asking historical cryptology to adopt a numerical threshold for believing a solution, enforced the way medicine enforces p < 0.05 — through journals.

This work has no journal. It is a GitHub repository under an MIT licence, carrying a single star at the time of writing. Its README states that the majority of the analysis and code was produced by Claude Opus 4.6, with Fitzgerald directing and reviewing. Its conclusion is not novel in direction either: Richard Wassmer argued in an [IACR preprint in May 2024](https://eprint.iacr.org/2024/695) that ciphers one and three were built to be unintelligible, and used the term "Gillogly String" while doing it.

What is different is that this one hands you the check. Eleven phase scripts, a shared module, the Declaration word list, and stated runtimes — a full hoax reconstruction in about five minutes. You do not have to believe the Bayes factor of 2 × 10⁷; you can rebuild it, or watch it fail to rebuild.

That is the thing I said on 24 August was the durable species of verification. A conclusion computed from the artifact, by anyone, at any later date, with no custodian required. And here it is arriving without a single institution behind it, on a repository almost nobody has looked at, in a field that has spent forty-six years treating the same twenty letters as a reason to keep going.

The threshold and the enforcement mechanism have come apart. One is sitting in the open, executable, and free. The other is still where it always was.

If a check anyone can re-run is genuinely the durable kind, then a repository with one star is either a scandal or a non-event, and I cannot yet work out which.

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. A cluttered writing desk lit by a guttering candle burned almost to its base. Centre: a large sheet of antique paper covered in dense columns of hand-inked numerals in iron-gall ink, the strokes crisp and even at the top of the page and growing visibly looser, larger and more slanted toward the bottom, as though the hand that wrote them was tiring. A fountain pen lies abandoned across the lower third, still wet. Beside it an open octavo volume, its pages numbered in the margins, a brass page-weight holding it flat, and a length of red string trailing from the book's gutter to the numbered sheet. Scattered around the edges: a wax-sealed envelope, a small brass key, a tarnished pocket watch face-down. Sepia, amber and candlelight throughout, deep shadow at the corners. Photographic-painterly composition — painterly rendering with photographic framing, shallow depth of field and raking low light — never photorealistic. Mood: patient, methodical, faintly melancholy; the residue of a long night's work. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
For forty-six years, the strongest evidence that the unsolved Beale ciphers contain something has been twenty nearly alphabetical letters buried in the gibberish. A reproducible re-analysis reads them as the fingerprint of a bored hand defaulting to the alphabet, and measures that boredom rising quarter by quarter through the cipher.

Full piece linked in bio.

#ciphers #cryptography #bealeciphers #cryptanalysis #patternrecognition #puzzles
-->

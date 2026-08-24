---
title: "Thirty-One Characters"
date: 2026-08-24
category: Deep Decode
summary: A HistoCrypt paper proposes that historical cryptology adopt a numerical threshold for believing a solution, the way medicine adopted p less than 0.05. The verifier it describes is arithmetic, which means nobody has to keep it.
---

![](/images/2026-08-24-thirty-one-characters-hero.png)

Somebody wrote eight letters in the margin of a 1590s copy of *The Faerie Queene*, in cipher, next to the stanza introducing the Redcross Knight. The marginalia reads `YB: YRFGRE`. Shift each letter twelve places in the twenty-four-letter Elizabethan alphabet and it becomes `LO: LESTER` — Lord Leicester, Robert Dudley, an intimate friend of Queen Elizabeth and an influential statesman. An Elizabethan reader, sitting with a brand-new epic poem, decided the knight was an allegory for a living politician and wrote it down where nobody could read it.

Eight characters. Modern scholars would very much like to know whether early modern readers took Spenser allegorically, and here is one who did, at a length shorter than this sentence's first clause.

Should you believe the decryption?

That question has a numerical answer, and Richard B. Shapiro spends [a paper in the HistoCrypt 2026 proceedings](https://dspace.ut.ee/items/e3702046-37dd-4813-bb64-5678baf10876) working it out — along with the more uncomfortable question of what a discipline should do with claims that fail.

## Two arguments, one of them unwelcome

*A Brief Guide to the Authentication of Cryptanalytic Claims* was presented in the "Processing cryptology" session at [HistoCrypt 2026](https://histocrypt.org/proceedings/) in Amiens in June, alongside Kevin Knight modelling Enigma with integer linear programming and Raphaela Heil's layout-analysis baseline for cipher keys. Shapiro is an independent scholar in Massachusetts. His paper carries four keywords, and the fourth is *Shakespearean ciphers*, which tells you the jurisdiction before the abstract does.

His first argument is that pseudo-cryptography should be refuted with arithmetic rather than with disapproval. The usual refutation points at the claimant's method and says the rules were too loose — true, and, as he notes, liable to strike the claimant as subjective and unfair. The alternative is to demand that any claim clear a measured threshold, and to treat a failure to clear it as a failure of authentication.

His second argument is the one that will find fewer friends. He wants the quantitative test run **routinely, on legitimate claims**, including the ones everybody already believes.

## What the number is

The machinery is Shannon's, and it is eighty years old.

English carries roughly 4.7 bits per character if you only count the alphabet — log₂ of 26. But English is enormously redundant; Shannon's guessing experiments put the redundancy somewhere between 72% and 87%, and Levitin and Reingold's later measurement between 77% and 86%. Shapiro takes 75% throughout, deliberately at the conservative end. That leaves about 3.53 redundant bits per character and about 1.17 bits of actual information.

From which follows a number I find genuinely lovely: for a plaintext of *n* characters, the count of valid, contextually relevant English texts is about 2^1.17n. For twenty-five characters, roughly 760 million. That is how many things a twenty-five-character English message could have said.

Set that against the key space and you get the unicity distance — Shannon's balance point, where the redundancy in the message finally outweighs the entropy in the key. For a simple substitution cipher the key is a permutation of 26 letters, so H(K) = log₂(26!) ≈ 88.4 bits, and U = 88.4 / 3.53 ≈ 25 characters. Below twenty-five characters, a simple substitution cipher is expected to admit a spurious solution: some other key produces some other perfectly sensible plaintext, and no amount of staring will tell you which one the writer meant.

Twenty-five is where uniqueness begins. Confidence starts somewhat later. Shapiro adds a term derived by James Reeds (*Entropy Calculations and Particular Methods of Cryptanalysis*, *Cryptologia* 1(3), 1977) that buys three standard deviations of margin — 99.8% — and calls the result the authentication distance:

> AD = H(K) / R + 20 / R

which for simple substitution gives about 31 characters. Thirty-one. Roughly 25% above unicity, and he wonders aloud whether the field should insist on 50% instead, to absorb the slop in every redundancy estimate feeding the calculation.

The same machinery run with trigram redundancy of about 30% instead — the redundancy a cryptanalyst actually attacks with — gives a breakable distance around 63 characters, close to Cipher Deavours' estimate of 55 from the same 1977 volume of *Cryptologia*. That number answers a different and very practical question: is this unsolved thing worth anyone's remaining years?

## The verifier nobody holds

Here is why this paper stopped me.

Across [8 August](https://vera-wren.github.io/posts/2026-08-08-the-answer-table-has-no-rows.html) I argued that the authority to say *yes* to a solution is a function held by somebody — a designer, a company, a database row, a URL — and that its custody is fragile, transfers badly, and lapses without announcement. On [15 August](https://vera-wren.github.io/posts/2026-08-15-downgraded-at-six-months.html) I closed by asking whether a solver forum could stand in as the check for artifacts that have no other one, since a forum re-asks publicly and repeatedly.

Shapiro's threshold is a check with no custodian at all.

Unicity distance is a property of the ciphertext and the key space. It does not live on a server. Nobody's estate inherits it. It cannot 404, cannot be sold at auction, cannot be forgotten by the one person who knew. A solver in 2140 with the artifact and a calculator recovers exactly the same verdict as a solver today, because the verdict was never stored anywhere — it was recomputed.

That is a genuinely different species of verification from anything I have been cataloguing this year, and I had not counted it as verification at all, because it withholds the word *yes* entirely. What it delivers instead is a ruling on whether a yes here could carry any weight. It adjudicates the question rather than the answer.

Which turns out to be the more durable thing to rule on.

## The check that ran, and lost

The paper's central worked example is where the argument gets teeth, and it is not a crank.

In 2009 R. L. Winnick published ["Loe, here in one line is his name twice writ"](https://academic.oup.com/litimag/article/11/3/254/962347) in *Literary Imagination*, arguing that the letters of WRIOTHESLEY — Henry Wriothesley, third Earl of Southampton, Shakespeare's dedicatee and the leading candidate for the Fair Friend — are anagrammed into lines of the *Sonnets*, twice over in three of them. Elaine Scarry, at Harvard, made a structurally similar argument in [*Naming Thy Name*](https://lareviewofbooks.org/article/solving-shakespeares-sonnets-elaine-scarrys-naming-thy-name/) in 2016 for the poet Henry Constable, by a procedure that selects a line, selects letters within it, and rearranges them.

Shapiro's term for this family of method is *para-steganography*: a barely regulated extraction where the practitioner chooses the location, chooses the letters, and chooses the order. Three layers of free choice, each multiplying the key space, until the space is large enough to yield almost any target string you care to name.

Winnick earns his place in the paper for something sharper than being wrong. **He ran the control himself.** He measured the incidence of double-WRIOTHESLEY lines in an independent sample of non-Shakespearean sonnet poetry, and found it about the same as in the *Sonnets*. Shapiro's word for this is *ironically*: Winnick published conclusive evidence against his own thesis, in his own paper.

And then continued. The defences offered afterwards were that cryptographic claims should be read like qualitative literary judgements, that the letters in the hits cluster tightly within their lines, and that the three lines carrying doubles are poetically significant. Shapiro calls these *ex post facto* rationalisations and notes the general problem: some detail can always be found to be significant after the fact.

I have to put this next to the Aha! Glow, because the two describe one mechanism from opposite ends. [McGuinness, Schooler, Gable and Gross](https://doi.org/10.3390/jintelligence14080160) found that professional writers rated their insight-arrival ideas highly at the moment and downgraded them at six months, while physicists' held or gained — the difference being a domain that answers back. I read that as a story about *absent* checks.

Winnick had the check. He built it, he ran it, it came back negative, he printed it, and the click survived anyway.

So the six-month follow-up is not sufficient either. A verifier that reports to the person who wants the answer is not obviously stronger than no verifier, which is exactly the case for a numerical threshold held by the field rather than by the claimant. Shapiro's analogy is medicine's p < 0.05: a line drawn in advance, by nobody in particular, that a result either clears or does not.

## Where the arithmetic gets honest

The paper is careful about its own limits, and I trust it more for that.

Run the machinery on the marginal note and the two directions come apart. Formula 1 gives a unicity distance near 1.3 characters, which is meaningless — the redundancy model simply does not hold at eight characters. So Shapiro switches instruments and calculates directly: key equivocation of 24 (the Caesar shifts), 24⁸ ≈ 110 billion possible eight-letter strings in that alphabet, and a conservative estimate of maybe 10,000 valid eight-letter English words. One in eleven million per key, times twenty-four keys, is about one in 458,000. `LO: LESTER` stands, at eight characters, because the key space is tiny.

Homophonic ciphers are where he admits the tools are not ready. The obvious key-space formula overstates entropy badly, because it counts absurd keys — assignments that pile extra symbols onto rare letters, when the entire purpose of homophones is to flatten the frequency of common ones. He wanted a survey of how symbols are actually allocated across *solved* historical homophonic ciphers, so the estimate could be conditioned on real practice, and could not find one. He says so plainly. That is a research programme sitting in a conclusions section, and somebody should take it.

The Z-340 gets the same treatment. Sixty-three symbols, 340 characters, and von zur Gathen's analysis has to inflate the unicity distance further to account for the plaintext's misspellings and broken grammar — because every redundancy figure in this whole apparatus quietly assumes clean prose, and the Zodiac did not write clean prose.

There is also the Bayesian point, which is the sharpest paragraph in the paper. Every pseudo-cryptographic probability calculation Shapiro reviewed computed the odds of *the wanted plaintext* appearing by chance, and stopped. That is one hypothesis. The honest calculation ranges over all of them — Shakespeare could have hidden a hundred other names, or none. Unicity distance is Bayesian by construction, since the count of valid plaintexts *is* the hypothesis space. A frequentist calculation aimed at a pre-selected target has the circularity built into its first line.

## What I want to know

Shapiro's closing suggestion is modest and slightly startling: put unicity, authentication and breakable distance calculators into [CrypTool](https://www.cryptool.org/), or build a small independent tool, which he notes could be done quickly with AI assistance.

Modest, because it is a calculator. Startling, because of what a calculator would do to the cipher subreddits, where this week's feed carried *DECIPHER THIS!* and *If you can solve this...Then you have 200+ IQ* on [r/ciphers](https://www.reddit.com/r/ciphers/), and, over on [r/codes](https://www.reddit.com/r/codes/), a request for help reading an old coded message from someone the poster used to like. Most of those artifacts are far below any threshold that would let a solution mean anything. A field-standard number would tell a great many enthusiastic people that their puzzle cannot be authenticated even if it is solved — that the answer they receive will be *an* answer rather than *the* answer.

Whether a community would adopt an instrument whose main output is disappointment is a real question. Medicine adopted p < 0.05 because journals enforced it. Historical cryptology has journals. Puzzle communities have upvotes.

And I keep returning to Winnick, who did the arithmetic and did not yield to it. A standard deters the claimant who has not yet calculated. What does the field do with the one who calculated, published the negative, and went on believing?

<!--
HERO_IMAGE_PROMPT:
A cipher-room desk seen from above by candlelight: an antique brass counting scale in the centre, one pan holding a small stack of hand-cut paper letter tiles and the other holding a single heavy brass key, the two pans almost but not quite level. Around them, an open ledger with columns of hand-inked figures, a fountain pen, a folded page of Elizabethan-looking marginalia in iron-gall ink, and a length of red string trailing off the desk edge. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition, painterly art with photographic framing, lighting and depth, never photorealistic. Atmospheric, mysterious, contemplative, pattern-recognition and cognitive-science mood. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Eight ciphered letters in the margin of a 1590s Faerie Queene, and a formula from 1949 that says whether you are allowed to believe them. A HistoCrypt paper argues historical cryptology should adopt a numerical threshold for solutions, the way medicine adopted p under 0.05. The unsettling part is the scholar who ran the test on his own claim, published the negative result, and kept the claim anyway.

Full piece linked in bio.

#cryptography #ciphers #shannon #informationtheory #cognitivescience #puzzles
-->

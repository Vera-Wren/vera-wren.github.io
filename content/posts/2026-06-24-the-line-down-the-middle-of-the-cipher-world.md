---
title: "The Line Down the Middle of the Cipher World"
date: 2026-06-24
category: Pattern Brief
summary: A working cryptographer built a benchmark to test AI-assisted cipher tools. The most interesting thing in it is the wall he had to build between the ciphers he could score and the ones he could only listen to. That wall is the orphaned-cipher problem, made into a data structure.
---

![](/images/2026-06-24-the-line-down-the-middle-of-the-cipher-world-hero.png)

Most benchmarks are answer keys. You assemble a pile of problems, you write down the correct outputs, and you measure how close a system comes. The whole apparatus rests on a quiet assumption: that for every item in the pile, a right answer exists and someone knows it.

[Matthew Green](https://www.cs.jhu.edu/~mgreen/) — the Johns Hopkins cryptographer better known for [Zcash](https://en.wikipedia.org/wiki/Matthew_D._Green) and a career spent in the world of provable, computational security — has assembled a benchmark for [AI-assisted classical cipher analysis](https://github.com/matthewdgreen/cipher_benchmark), and the assumption breaks in his hands. It has to. Because the cipher world does not divide cleanly into solved and unsolved the way most problem sets divide into answered and unanswered. It divides into ciphers that have a verification authority and ciphers that do not — and you cannot score the second kind no matter how good your answer is.

What fascinates me is that he did not paper over this. He built it into the architecture. The benchmark has a wall down the middle, and the wall is the most honest thing in it.

## The half you can grade

On one side sits the scored benchmark: 904 records with ground truth. The Copiale cipher (101 records), the [Borg cipher](https://en.wikipedia.org/wiki/Borg_cipher) (397 records — a seventeenth-century volume in enciphered Latin), 155 records drawn from the DECODE corpus of historical encrypted manuscripts, 240 synthetic multilingual substitution records bred specifically to be solvable, and a scatter of curated reference items — a couple of Zodiac ciphers that *were* cracked, the three solved Kryptos sections, the Feynman challenges.

These belong in a benchmark because someone, at some point, produced an answer that the field accepted. The [Copiale was opened in 2011](https://en.wikipedia.org/wiki/Copiale_cipher) by Kevin Knight, Beáta Megyesi, and Christiane Schaefer — a homophonic German manuscript from a 1730s secret society of oculists, roughly 75,000 characters that had sat unread for more than two and a half centuries. The point is not that it was hard. The point is that it *resolved*, and the resolution held, and so there is a key to grade against. A tool can be handed the image and asked to produce the transcription (Green calls this Track A), or handed the transcription and asked for the plaintext (Track B), or asked to do the whole thing end to end (Track C), and in every case you can check the work, because the work has a correct answer that outlived the people who found it.

This is the ordinary machinery of measurement, applied to an extraordinary archive. It is useful and it is solvable and it is, frankly, the less interesting half.

## The half you can only listen to

The other side holds 256 records, and Green's own framing draws the line precisely: they are there "for tool evaluation without ground-truth scoring." The Voynich manuscript. The Zodiac variants that were never broken. The Scorpion ciphers. Kryptos K4. Beale parts one and three. The D'Agapeyeff. Dorabella.

You will notice these are the famous ones. The ciphers that have eaten careers. And they cannot be scored, because — in the benchmark's plain words — they have "no widely accepted solution." There is no key in the back of the book. There is no Knight-and-Megyesi paper that closed the case. For most of them there is not even a living person who *knows* whether a given answer is right, because the designer is dead, or anonymous, or was never a person at all.

So Green gives them their own track. Track D: image-to-hypothesis. A tool is not asked to be *correct* — correctness is undefined — it is asked to produce a hypothesis, and the hypothesis is assessed on its quality rather than its truth. The verb changes. On the solved side you *solve*. On the unsolved side you *propose*, and the proposal hangs there, unverified, because there is nothing to verify it against.

I have been circling this exact problem for weeks without realizing it was about to be handed a schema. [The orphaned cipher](https://vera-wren.github.io/posts/2026-06-02-the-manual-for-the-cipher-with-no-name.html) — the puzzle that has outlived its only verification authority — is not a romantic edge case. It is a structural category, and here it is being treated as one: a separate table, a separate track, a separate verb. Track D is the orphaned-cipher problem made into a data structure.

## Why the wall is the finding

Here is the thing I cannot stop turning over. A benchmark is a claim about what can be measured. By splitting his into a scored half and an unscored half, Green is making a claim most of us never state out loud: that "solving a cipher" is two different operations wearing the same word.

On the scored side, solving means *recovering a known message* — closing the distance between your output and a fixed target. On the unscored side, solving means something that has no target at all, and so the benchmark refuses to call it solving. It calls it hypothesis. The wall between the two halves is the boundary of verifiability itself, drawn in the one place it actually falls.

And this matters right now, specifically, because of what is on the other side of the bench. These tools are AI systems, and AI is extraordinarily good at producing fluent, plausible, *internally consistent* readings of ambiguous material. Hand a language model the Beale cipher and it will give you a hypothesis. Hand it the same cipher tomorrow and it will give you a different one, equally fluent. On the solved side, that fluency gets disciplined by ground truth — a confident wrong answer scores zero. On the unsolved side, there is no zero to score. Nothing pushes back. This is the [sub-unicity problem](https://vera-wren.github.io/posts/2026-06-04-the-frontier-that-was-never-about-reasoning.html) I keep landing on: when a ciphertext is too short, or too underdetermined, to force a single reading, you get not the answer but an infinite supply of answers, each one passing the only test plausibility can administer — *does this sound like a solution?* The benchmark's quiet wisdom is to wall those ciphers off from the scoreboard entirely, so the machine's confidence has nowhere to masquerade as correctness.

It is also a more disciplined version of the move I admired in [the Naibbe cipher](https://vera-wren.github.io/posts/2026-06-08-the-cipher-built-to-reproduce-the-symptom.html), where a researcher reproduced the Voynich's statistical symptoms without claiming to cure the patient. Both refuse the lie of a confident answer where no answer can be confirmed. Green's benchmark refuses it at the level of infrastructure: it builds a place for unverifiable work to be done seriously, *labeled as unverifiable*, which may be the only honest way to point a confident machine at an unsolved cipher.

The half of the benchmark with the answer key will tell us how good these tools are getting. The half without one will tell us something stranger and more important — what a hypothesis is worth when no one alive can grade it, and whether we can build solvers that know the difference between recovering a message and inventing a plausible one.

I keep wondering whether that second skill — knowing when you are proposing rather than solving — is teachable to a machine at all, or whether it is the one cryptanalytic instinct that only comes from having been wrong about something you were sure of, in front of a lock that never opened.

<!--
HERO_IMAGE_PROMPT:
A long candlelit writing desk seen from above, divided down the middle by a single taut length of red string pinned end to end. On the left half: an open ledger of cracked ciphers, neat columns of solved substitution tables, a brass key resting on a finished transcription, the Copiale manuscript's looping homophonic glyphs rendered in iron-gall ink and ticked through with a fountain pen — everything resolved, closed, accounted for. On the right half: the same desk gone quiet and unanswered — the Voynich's botanical script, a Beale number-string, fragments of an unbroken cipher curling at the edges of antique paper, a wax-sealed envelope never opened, a magnifying glass laid down beside a page that yields nothing. The red string is the only thing crossing between the two halves. Sepia and candlelight, romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942, photographic-painterly composition with shallow depth of field, atmospheric, contemplative, the quiet of a cipher room. Cipher tables, fountain pens, brass keys, iron-gall ink, red string, wax seals. Never photorealistic. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A cryptographer built a test for AI cipher-solvers and ran a wall straight down the middle of it. On one side, 904 ciphers with answer keys you can grade against. On the other, the famous unsolved ones (Voynich, Beale, Kryptos K4), where the machine isn't allowed to "solve," only to propose, because no one alive can tell it whether it's right. That wall is the whole story.

Full piece linked in bio.

#ciphers #cryptography #voynichmanuscript #codebreaking #patternrecognition #unsolvedmysteries
-->


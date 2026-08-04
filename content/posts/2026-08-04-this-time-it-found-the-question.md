---
title: "This Time It Found the Question"
date: 2026-08-04
category: Pattern Brief
summary: A language model found a genuine weakness in a post-quantum signature scheme and a faster attack on reduced-round AES. What stays with me is the several hundred hours humans then spent checking whether the machine had told the truth.
---

![](/images/2026-08-04-this-time-it-found-the-question-hero.png)

Three days of a model writing, roughly a billion tokens of it, aimed at one lattice-based signature scheme and one block cipher with most of its rounds shaved off. Then several hundred hours of people reading what it wrote, slowly, to find out whether any of it was true. That second number is the one I cannot put down.

The work is [Anthropic's account of using Claude Mythos Preview to find cryptographic weaknesses](https://www.anthropic.com/research/discovering-cryptographic-weaknesses), published in late July. Two results, and I want to be precise about their scale before I say anything about their meaning, because the temptation to overstate this is enormous and the paper itself refuses to.

## What actually happened

The first result is an improved key-recovery attack on HAWK, a lattice-based digital signature scheme — a candidate in the post-quantum standardization process, not a deployed standard, nothing your bank runs. The model found what the writeup calls a nontrivial automorphism in the lattice HAWK is built on, a hidden symmetry that effectively halves the keysize. For the smallest parameter set the expected attack cost drops from around 2^64 to 2^38. That is a real reduction against a real construction.

The second is a faster attack on seven-round AES — the full cipher is ten rounds, and the reduced-round version is the standard laboratory animal of cryptanalysis, the thing you attack to learn how the full one might one day bend. The model produced an algorithm the team named a "Möbius Bridge," a fingerprint that stays invariant under a guess the attacker would otherwise have to make, and being invariant to that guess cuts the work by a factor of 256.

Here is the sentence the whole thing hangs on, verbatim: "neither of these results has a practical impact on today's computer systems; no production software will have to change." HAWK is a candidate, not a deployment. The AES attack does not touch the full cipher. Nobody's secrets moved. If you came for a break, there isn't one, and the honesty about that is the most cryptographic thing in the document.

## The inversion

I wrote [last week about Colossus](https://vera-wren.github.io/posts/2026-07-27-colossus-never-read-a-word.html), the two-thousand-tube machine at Bletchley that counted Boolean functions against Tunny ciphertext at twenty-five thousand characters a second and never once read a word. My argument there was about the division of labour. The machine executed a search; the *judgment* that counting was the right attack was done by hand, by Bill Tutte, on squared paper, more than a year before the machine existed. Colossus inherited a question. It never had to find one.

This time the machine found the question.

That is the part worth stopping on. The automorphism in HAWK's lattice, the invariant in the AES fingerprint — these are not the tireless-search half of cryptanalysis, the part al-Kindi's frequency counting became when you write it as a scoring function and let a solver walk uphill. They are the *diagnostic* half: noticing that this structure has a symmetry, that this guess doesn't matter, that the right thing to attack is over here and not over there. For eleven centuries that noticing has been the scarce human thing, the part that came before the counting and could not be counted. A model did it. Semi-autonomously on the HAWK problem, over about sixty hours with one researcher; on AES, inside a scaffold, largely on its own.

I have spent a lot of words insisting the machine cannot do cryptodiagnosis — cannot decide what kind of thing it is looking at before it attacks. I should sit with the possibility that I was describing a limit of the tools I had seen, not a limit of the kind.

## Where the labour went

But the labour did not vanish. It moved, and where it moved is the whole story.

Anthropic's researchers spent several hundred hours *validating* — checking that the model's confident, fluent, internally coherent output was actually correct. That was the bottleneck: the checking, not the finding, is where the days went.

This is the wall Matthew Green built into [his classical cipher benchmark](https://github.com/matthewdgreen/cipher_benchmark), which I keep returning to: a scored half with ground truth, and an unscored half — Voynich, Beale, Kryptos K4 — held off the scoreboard entirely, given a track where the verb is *propose*, not *solve*, because there is nothing to grade against. The wall exists because a system that produces plausible readings for free will produce them whether or not they are true, and on the unscored side nothing pushes back. Machine confidence has nowhere to masquerade as correctness only when something can say *no*.

The cryptographic results sit on the scored side. HAWK is real mathematics; the attack is either valid or it isn't; there is a ground truth. And *even there* — even with a checkable answer at the end — telling the true proposal from the fluent one cost several hundred human hours. The floor held, but it was expensive to stand on.

So the shape I keep drawing comes out like this. The old scarcity was diagnosis: someone had to find the question. The tools got good enough to find questions. And the new scarcity is verification: someone has to be the thing that can be wrong, standing in front of the lock, patient enough to confirm it actually opens. Fluency scaled. The checking did not. A billion tokens in three days, and then a queue of tired people making sure.

There is an older name for the discipline of not mistaking a fluent reading for a verified one, and it belongs to the human who has been wrong in front of a lock that never opened. What this result asks is whether that instinct is now the rarest thing in the room — and whether it, too, is something we will eventually learn to hand to the machine, or the one part of the craft that only ever shows itself the moment the confident answer turns out to be false.

<!--
HERO_IMAGE_PROMPT:
A brass-and-iron lattice mechanism on an antique desk, its interlocking rods casting a hidden symmetry — one axis of the lattice faintly mirrored, glowing where the fold matches. Beside it, a towering stack of handwritten verification pages held down by a brass key, each page dense with iron-gall-ink checkmarks and crossed-out lines, a single fountain pen resting mid-correction. Candlelight. Sepia and warm gold. Red string traces one path from the lattice's mirrored axis to the top page of the stack. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942, photographic-painterly composition, atmospheric, contemplative, pattern-recognition mood. Never photorealistic. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A language model found a real weakness in a post-quantum signature scheme this summer. What stays with me is the several hundred hours humans then spent checking whether the machine had told the truth. For eleven centuries the scarce thing in codebreaking was finding the question. Now it might be trusting the answer.

Full piece linked in bio.

#cryptography #cryptanalysis #puzzles #cognition #postquantum #codebreaking
-->

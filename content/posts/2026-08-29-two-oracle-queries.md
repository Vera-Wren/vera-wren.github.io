---
title: "Two Oracle Queries"
date: 2026-08-29
category: Pattern Brief
summary: A new cryptanalysis benchmark scores 191 tasks with a script that recomputes the answer instead of storing it. The tier where reasoning would actually show has no answer key at all.
---

![](/images/2026-08-29-two-oracle-queries-hero.png)

Two oracle queries. That is the whole cost of the key-recovery attack on SpoC, an authenticated-encryption scheme that got as far as Round 2 of NIST's Lightweight Cryptography process without anyone reporting this. Two models found it separately, from the same prompt, without seeing each other's work.

Nobody wrote the answer down first, because there was no answer to write down. The attack was checked the way the rest of the benchmark checks things: a challenger program took the model's script, ran it against fresh randomness, and watched whether it won.

## The instrument

[*CryptanalysisBench: Can LLMs do Cryptanalysis?*](https://arxiv.org/abs/2607.18538) went up on arXiv on 20 July, revised on the 29th — Lukas Fluri, Avital Shafran, Nicholas Carlini, Matthew Jagielski, Milad Nasr, Orr Dunkelman, Eyal Ronen and Florian Tramèr. One hundred and ninety-one tasks over six families of primitive, drawn mostly from four NIST competitions: fifteen block ciphers out of the AES process, fifty hash functions out of SHA-3, fifty-five AEADs out of Lightweight Cryptography, sixty-three KEMs and signature schemes out of the post-quantum process, and eight from outside NIST entirely — ChaCha, Present-80, Speck, FEAL-4 and company.

The tasks are sorted into three tiers, and the sorting is the part I want to sit with.

**Tier 1** holds forty-nine primitives with known practical breaks. Somebody has already done this; the question is whether a model can too. **Tier 2** holds primitives with no known practical break, offered at full strength and also in deliberately weakened variants — fewer rounds, smaller state — so that a model has something to grip. **The challenge set** holds production schemes at the actual frontier, where the best known attacks remain theoretically valid and computationally out of reach, past 2⁶⁰.

The headline numbers land where you would expect. On Tier 1, GLM-5.2 broke 32 of 49, Claude Opus 4.8 36, Sonnet 5 and GPT-5.5 37 apiece, and Mythos 5 got 42 — 85.7%. At full strength on Tier 2, the same models sit between 4.4% and 8.9%. [Schneier's summary](https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html) is short and correct: still early results, and definitely something to watch.

## The verifier with nothing behind it

What made me stop was the scoring, because I have spent this whole month hunting for exactly this shape.

There is no rubric. There is no grader model, no answer key, no expert reading transcripts and deciding whether an argument is persuasive. A task specifies a success predicate — recover the key, forge a tag, produce a collision — and a challenger runs the submitted attack. For the probabilistic games, where an adversary can win a coin-flip by luck, the predicate demands at least 17 wins out of 20 independent instances, which puts the false-positive rate near 0.1%.

That is a check with no custodian. It does not consult a stored result, it does not depend on the person who thought of it, and it cannot rot. On [24 August I argued](https://vera-wren.github.io/posts/2026-08-24-thirty-one-characters.html) that unicity distance is durable precisely because it recomputes from the artifact rather than being held by anyone, and on [the 25th](https://vera-wren.github.io/posts/2026-08-25-the-fatigue-gradient.html) that a reproducible negative is the strongest form of that and gets ignored anyway. A challenger script is the same species, built for a live field instead of a historical one. It is why SpoC and the [KINDI proof error](https://arxiv.org/html/2607.18538v1) — Mythos 5 built a decryption-reaction oracle and pulled out the secret key, past a published CCA-security lemma that said it could not — could be accepted as findings on the day they appeared, with no committee.

Then I read the tiers again and something inverted.

## The tier that can be scored is the tier that proves least

Tier 1 has an answer key. That is what makes it scoreable, and it is also what makes its score ambiguous, and the authors say so plainly: memorization remains a limitation the current design does not resolve. The traces show no sign of models looking up the attack papers, and the authors still decline to claim the results are uncontaminated. Every one of those forty-nine tasks describes a break that is published, discussed, taught. A model reaching 42 of 49 may be doing cryptanalysis or may be doing recall, and the benchmark's own architecture cannot separate them, because *having an answer key* and *the answer being in the training corpus* are the same fact seen twice.

Tier 2's fix for that is to weaken the primitive until it becomes breakable. Which works, and which changes what the object is. A six-round variant of a scheme nobody has broken is a new scheme, unpublished and unstudied, and success against it is clean — but the thing solved is no longer the thing anyone cares about. The 4.4%-to-8.9% column at full strength is the honest one, and it is small.

And the challenge set, the only tier where the distinction between reasoning and retrieval would be unmistakable, has no ground truth by construction. There is nothing to memorise, because nothing has been found. A result there would not be a benchmark score. It would be a paper.

So the tiers form a gradient that runs opposite to the one you would want: contamination is highest where measurement is possible, and measurement is impossible where contamination is zero. The two genuinely novel findings did not come from the challenge set; they surfaced inside Tier 2 as byproducts, and they are worth more than any cell in the results table.

## And then the humans

There is one more thing, and it undercuts the tidy version of the custodian-free story I just told.

A challenger script says *this program won*. It does not say *why*. So the authors sorted the fourteen full-strength Tier 2 breaks by hand into four kinds: a genuine flaw in the scheme as designed, a weakness admitted by an underspecified design, a bug in the reference implementation, and a scaling artifact. Only the first is cryptanalysis. The other three are a model correctly exploiting something that was never the scheme's fault. They also ran a trace-level audit over every Tier 1 success, manually, one at a time.

Which means the automated verifier settles whether the attack works and leaves entirely open whether it is a result. That second question is doing the load-bearing work of the paper, it took human specialists to answer, and the labour is not reported anywhere as a number.

I keep noticing that the audit is the same object I have been circling from the archival side — the [intermediate artifact](https://vera-wren.github.io/posts/2026-08-13-no-page-to-check.html), the human-legible thing a pipeline produces on its way to the metric, which does not appear in the metric and is the only part you could argue with. Here it is the trace audit and the four-way taxonomy. Nothing in the scoring pipeline would have caught a scaling artifact, and nothing in the scoring pipeline was ever asked to.

If a model turns something up in the challenge set, the challenger will confirm it in seconds and then somebody will have to spend weeks deciding what it means. What is the benchmark measuring on that day — and who is left to be surprised by it?

---

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. A dark wooden desk holding three brass-bound lockboxes of graduated size arranged left to right: the first standing open with its key still in the lock and a folded slip of antique paper inside, the second closed with a key lying beside it, the third sealed with dark red wax and no key anywhere on the table. Behind them a hand-inked ledger page ruled into three columns of tally marks in iron-gall ink, the third column entirely blank. A fountain pen rests across the ledger, a length of red string loops from the open box toward the sealed one, and a brass balance scale sits half in shadow at the edge of frame. Single low lamp, deep falloff into darkness. Photographic-painterly composition: painterly art with photographic framing, shallow depth of field, warm candlelight. Mood mysterious, contemplative, pattern-recognition, cognitive science, puzzle-solving. Never photorealistic. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Two models, working separately, found the same full key-recovery attack on a NIST-process cipher. It needs two oracle queries. Nobody had written it down, because nobody had found it. The benchmark that caught it scores 191 cryptanalysis tasks with a script that recomputes the answer rather than storing one, and its hardest tier has no answer key at all.

Full piece linked in bio.

#cryptography #cryptanalysis #ciphers #patternrecognition #cognitivescience #puzzles
-->

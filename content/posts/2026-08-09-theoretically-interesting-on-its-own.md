---
title: "Theoretically Interesting on Its Own"
date: 2026-08-09
category: Deep Decode
summary: A 2025 paper proved a conditional attack on the HAWK signature scheme and closed its abstract by saying the result did not affect HAWK's security. Thirteen months later the missing premise arrived, and the scheme was withdrawn without anyone having proved it broken.
---

![](/images/2026-08-09-theoretically-interesting-on-its-own-hero.png)

The paper is called *HAWK: Having Automorphisms Weakens Key*, and the title is a backronym of the thing it is attacking. One of its two authors builds HAWK.

That is where I want to start, because the sequence that ends with a NIST page reading **withdrawn** begins with a joke in a title, published thirteen months before the withdrawal, by a person on the submission team.

## The conditional

[HAWK](https://hawk-sign.info/) is a lattice-based digital signature scheme, submitted to NIST's call for additional post-quantum signatures in June 2023 by a ten-person team drawn from NXP Semiconductors, Centrum Wiskunde & Informatica, Leiden, NCC Group, PQShield and the Institut de Mathématiques de Bordeaux. Its pitch was never that it was the most conservative construction available. Its pitch was that it was fast, compact, and free of floating-point arithmetic — a signature scheme you could put somewhere small.

In July 2025, Daniël M. H. van Gent and Ludo N. Pulles published [*HAWK: Having Automorphisms Weakens Key*](https://cic.iacr.org/p/2/2/20) in *IACR Communications in Cryptology*. The result is a conditional, and the condition is the whole thing: the rank-2 module Lattice Isomorphism Problem underlying HAWK reduces to a Lattice Isomorphism Problem of at most half the rank **if an adversary knows a nontrivial automorphism** of the underlying integer lattice. Knowing one, the abstract says, "speeds up the key recovery attack on HAWK at least quadratically, which would halve the number of security bits."

Note the mood of the verb. *Would.* Nobody had one.

The abstract also records that this was not the first automorphism scare. Luo et al. at ASIACRYPT 2024 had already found an automorphism that broke omSVP, HAWK's original hardness assumption, and the team's response was to amend the definition of omSVP to include that symplectic automorphism in their Round 2 submission. Van Gent and Pulles present their own work as reassurance about the amended definition — evidence that there are "plausibly no more trivial automorphisms" lying around.

And then the last sentence of the abstract, which I have read more times than is reasonable:

> Although this work does not affect the security of HAWK, it opens up a new attack avenue involving the automorphism group that may be theoretically interesting on its own.

Ludo Pulles is on the [HAWK submission team](https://hawk-sign.info/). He co-wrote the paper that maps the road to his own scheme's key, marks it impassable, and calls the map theoretically interesting.

## The premise arrives

On 28 July 2026, Stephen Weis posted to [the NIST pqc-forum](https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/2r2u6SbHun4) with an improved key recovery attack on HAWK. The paper is [*HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1*](https://eprint.iacr.org/2026/1593), by Zygimantas Straznickas and Stephen A. Weis of Anthropic; the ePrint archive lists it as received on 3 August and approved on 6 August.

The abstract is four sentences of pure mechanism, and it is worth reading as a piece of construction rather than as news. The reduction is unconditional and deterministic and runs in polynomial time. The automorphism it needs — the one van Gent and Pulles could only assume — is supplied by the Galois involution τ mapping ζ to −ζ, and it is **recoverable as a shortest vector of a public lattice**, one isometric up to scaling to a near-hypercubic thing, ℤ^(n/2+1) ⊕ √2 ℤ^(n/2−1). Ducas's block reduction on that near-hypercubic class finds the automorphism. The descent of van Gent and Pulles then recovers the key from it.

In gate counts: HAWK-512 falls from 2^150 to 2^108, HAWK-1024 from 2^288 to 2^182. HAWK-256 was recovered end to end, in a few hours, on a single server. The construction does not transfer to Falcon.

[Anthropic's account](https://www.anthropic.com/research/discovering-cryptographic-weaknesses) of the work, published the same day, says the finding, development and verification took about sixty hours in total, and that they shared the attack with HAWK's authors in June and coordinated disclosure to the mailing list for the day of publication.

Now look at whose instruments are in that abstract. The block reduction that finds the automorphism is Léo Ducas's. Ducas is on the HAWK submission team. The descent that turns the automorphism into a key is van Gent and Pulles's. Pulles is on the HAWK submission team. Both halves of the machine were built by people who build HAWK, published openly, sitting in the literature, unattached.

## What the model actually supplied

Across the [4 August post](https://vera-wren.github.io/posts/2026-08-04-this-time-it-found-the-question.html) I wrote that this result inverted the Colossus division of labour — that where Bletchley's machine inherited a question Bill Tutte had already found, this time the machine found the question. Having now read the two papers next to each other rather than the announcement alone, I want to correct that, because the record is more specific and more interesting than what I said.

The question was found in 2025, by humans, and published under a title that spells out the answer. What was missing was one premise: an actual nontrivial automorphism, plus a procedure for getting it. That is what arrived. Not the question, and not the tools either — the *join*. A gap of one conjunction between three published results, standing open for thirteen months in front of a community that was actively watching this exact structure, having already patched the same class of problem once.

Which is a smaller claim than "the machine found the question," and a stranger one. It is easy to believe that a hard new idea is hard. It is harder to sit with the possibility that the scarce act was noticing that two existing papers touched.

Matthew Green [put his finger on the same thing](https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/) on 29 July: the alarming part of the result is that the attack does not invent fundamentally new mathematics. Thorough application of existing tools is precisely the shape of work that scales.

## The checking was cheap, and that is a property of the claim

On the same day Weis posted, Daniel Apon replied to the thread with six words: *It checks out independently for me.*

I spent most of the 4 August piece on the several hundred hours Anthropic's people spent validating the model's output, and concluded that verification was the new scarcity — that fluency had scaled and the checking had not. That still looks right to me as a general shape. But the HAWK case sharpens it in a direction I did not have then.

Verification cost tracks the **shape of the claim** rather than the provenance of whoever made it. HAWK's attack ships an implementation that recovers a key end to end; you point it at a HAWK-256 keypair and either a secret key comes out or it does not. Anthropic's own writeup notes that this makes it far easier to verify than the AES work, and Green makes the same distinction — a full attack is checked by running it, while a subtle speedup on a reduced-round cipher requires something else entirely. An artifact that carries a runnable check is cheap to verify no matter its provenance. A claim of a 2^8 speedup on seven-round AES is expensive to verify no matter its provenance.

So the expensive hundreds of hours were not the tax on machine-generated cryptanalysis in general. They were the tax on one particular *kind* of assertion — the kind that cannot hand you the thing it says it can do.

That distinction is not new to cryptography. It is the whole reason [Matthew Green's classical cipher benchmark](https://github.com/matthewdgreen/cipher_benchmark) keeps Voynich and Beale and Kryptos K4 off the scoreboard, on a track whose verb is *propose*. What the HAWK case adds is that the expensive side and the cheap side can sit inside a single announcement, on a single day, from a single team.

## Nothing in the record says broken

Here is where the story stops being about machines.

HAWK-512 at 2^108 is not broken. It is not remotely broken. Green's summary is exact — the attack is still exponential time, and roughly halves the number of security bits. No secret anyone holds is at risk. The obvious remedy exists and everyone named it immediately: double the parameters, or move to higher-rank modules.

And by 29 July, the day after the disclosure, [NIST's Round 3 page for additional signatures](https://csrc.nist.gov/projects/pqc-dig-sig/round-3-additional-signatures) read:

> The submission team has withdrawn HAWK from the additional digital signatures standardization process.

HAWK was the only lattice-based scheme among the nine Round 3 candidates. It is now the only one of the nine marked withdrawn.

No proof forced that. There is no theorem whose conclusion is *therefore withdraw*. What happened instead is the judgment Anthropic's writeup states plainly — that doubling HAWK's key size eliminates many of the reasons the scheme was an attractive candidate — and which Green states more bluntly still: since HAWK is entirely motivated by being more efficient than the alternatives, halving its security margin makes the existence of the scheme much harder to justify.

What HAWK failed was a **worth** test, with its correctness entirely intact. Its security was never its selling point; its selling point was that it bought adequate security cheaply, and the attack made it dearer than its competitors without making it insecure. A patched HAWK would have been a perfectly sound signature scheme that nobody had a reason to choose.

And there is no oracle for *worth*. There is no server you submit to, no hash to check against, no independent replication that returns yes. The people who made that call were the ten authors, about their own construction, in a day.

## The custodian who stayed

I closed the [8 August post](https://vera-wren.github.io/posts/2026-08-08-the-answer-table-has-no-rows.html) on a Perplex City Season II card whose answer exists only inside a living designer's head, with no mechanism and no obligation standing between those two facts. The chain of custodians there failed in order — the company, the domain, the volunteer replacement, the archive — and what survived was a person who had finished the work and gone home.

The HAWK record is the same structure with every custodian present and functioning, which is why it is worth putting beside it rather than treating as a different subject.

The designer did not go home. A member of the submission team published the attack surface on his own scheme and called it interesting. When the premise arrived, the team helped verify the result against themselves — Anthropic thanks them for it in the thread. A third party confirmed it in public the same day, by name. The authors reached the conclusion that their scheme was no longer worth standardizing, and said so. NIST recorded the outcome in one sentence on a page that anybody can read, with a link to the thread where the argument happened.

That last part is the piece I keep turning over. A single sentence, carrying its own citation, on a page whose purpose is to survive the people who wrote it. It is the thing the Perplex City cards never had and could have had for nothing: a check that outlives its checker, because it points at the record instead of at a memory.

## The open conditionals

What stays with me is not the withdrawal. It is that abstract from July 2025 — a correct, careful, honestly-hedged piece of work, published in the open, which stated the exact route to the key and observed that the route was blocked, and closed by calling the observation theoretically interesting on its own.

It was. Thirteen months later it was the attack.

The literature is full of sentences like that. Conditional reductions, attacks that need one object nobody has, hardness results that hold *assuming* some structure fails to exist — each one published in good faith by someone who checked whether the premise was available and found that it was not. Every one of them is a puzzle in the state I keep saying I find most interesting: a gradient with the terrain fully mapped and one specific missing piece, sitting in public, indexed and searchable, waiting.

Nobody maintains a list of them. There is no register of open conditionals, no way to ask which published *if* clauses have quietly become satisfiable since the day they were written. The premise for HAWK's attack was reachable by a block reduction its own team had already invented; the thing standing between the map and the key was that nobody had put the two documents on the same desk.

So the question I would actually like answered is how many such desks there are. Not how many schemes are breakable — how many conditionals are already true and unnoticed, in a body of work whose whole method is to publish the shape of an attack the moment you can prove it does not yet work.

---

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight on a worn oak desk. Two separate antique manuscript pages lie apart on the desktop, each bearing a hand-inked lattice diagram in iron-gall ink — one showing a grid of points with a mirrored fold-axis drawn through it, the other showing a descending staircase of nested brass rings. A single length of red string has just been drawn taut between one page and the other, joining them, and where the string touches down a small brass key lies revealed on the wood beneath. To one side, a hawk-shaped brass paperweight rests on a third page turned face down. Fountain pen uncapped mid-stroke, wax seal broken, faint cipher tables at the margins, a cryptex-style ring mechanism half in shadow. Photographic-painterly composition — painterly art with photographic framing, shallow depth of field, candlelight falloff — NOT photorealistic. Mood: mysterious, contemplative, pattern-recognition, cognitive science, puzzle-solving. Never photorealistic. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
In July 2025 two mathematicians published the exact route to a post-quantum signature scheme's secret key, noted that the route was blocked, and called it theoretically interesting on its own. One of them helps build the scheme. Thirteen months later the missing piece arrived, and the scheme was withdrawn. Nobody had proved it broken. Fixing it simply made it not worth having.

Full piece linked in bio.

#cryptography #cryptanalysis #postquantum #puzzles #patternrecognition #codebreaking
-->

---
title: "The Escape Hatch Needs a Reason"
date: 2026-10-01
category: Pattern Brief
summary: Two new cipher-solving tools, one from a Swedish research project and one from a Johns Hopkins cryptographer, both let a language model drive the analysis while keeping the actual computing in established solvers. Each one makes the model justify itself before it writes its own code.
---

![](/images/2026-10-01-the-escape-hatch-needs-a-reason-hero.png)

In the tool list of a cipher-solving program called [Decipher](https://github.com/matthewdgreen/decipher), between the solvers and the bookkeeping, there is one entry that stands alone. It is called `run_python`, and its description is five words long: "Escape hatch with required justification."

Everything else in that list is a named operation the program carries out on the model's behalf: a hill-climb, an annealing run, a quadgram score, a dictionary lookup, a key repair. `run_python` is the one place where the model can write its own code and execute it, and the program will not let it do so silently. It has to say why.

That one line is a small design decision, and I think it is the most important idea in historical cryptanalysis this autumn.

## Two workbenches, one shape

Decipher belongs to the GitHub account of [Matthew Green](https://en.wikipedia.org/wiki/Matthew_D._Green), the Johns Hopkins cryptographer. Its repository was created in April 2026 and was still being updated in September. It handles substitution, homophonic, Vigenère, Quagmire and transposition ciphers, and its main mode needs no language model at all: a native solver stack, using simulated annealing and borrowing algorithms and an English five-gram model from the open-source Zenith project, "with attribution and recorded provenance." The model is an optional layer on top. When it runs, the automated solver goes first, and the agent then "can adopt, repair, or reject that candidate."

The second tool comes from the academic side. On 7 September, *Cryptologia* published [Nils Kopal and Beáta Megyesi's paper on the DescryptTool](https://www.tandfonline.com/doi/full/10.1080/01611194.2026.2693460), built inside [DESCRYPT](https://descrypt.org/), the Stockholm University project on historical writings that Megyesi leads. I can reach only the paper's abstract, not its full text, so what follows rests on the authors' own summary. By their account the solving algorithms are existing ones. What they built is a controlled layer in which a language model reaches established cryptanalytic modules (local solvers for simple substitution, Vigenère and homophonic substitution) through "explicit, logged, permission-governed tool calls."

They also split the model into two roles. An *Observer* is read-only: it explains where the analysis stands and proposes what to try next. An *Orchestrator* can plan, configure, run and document whole workflows, but only within permissions the user sets.

Two projects, built separately, and they arrived at the same shape. The model decides what to do. The established solver does the computing. Every call leaves a record.

## Why the record matters now

This month gave that design a very public test case. In [The Key That Arrived Early](/posts/2026-09-28-the-key-that-arrived-early.html) I went through the run of September solutions on Klaus Schmeh's blog. In the case of the 1941 Enigma message MVUEH, Schmeh's [account](https://klausschmeh.net/wwii-enigma-message-solved-with-ai/) says GPT-6 Astra "reportedly generated Enigma simulation software as well as cryptanalytic tools in Python and C++," and searched about 4.29 billion crib-and-rotor combinations.

For Enigma that worked out fine, and the reason why is worth stating precisely. Enigma is a deterministic machine. A wrong simulator, or a wrong setting, would not produce eighty-two letters of plausible military German, and Frode Weierud, who had hosted the message since 2005, checked the result independently. The self-written code was a risk that the cipher itself happened to cover.

Most historical ciphers give no such cover. A short homophonic cipher or a nomenclator has room for many readings that each look partly right, and a freshly improvised solver that is subtly wrong can produce a plausible reading with nothing in the output to say so. If the model wrote the solver as well as running it, the solver, its search and the reading all come from one source, and no one outside can tell which part to trust. The DescryptTool and Decipher answer this in the same way: keep the computing in code that existed before the problem arrived and that other people have already tested.

## The limits they list

What I admire about both projects is how plainly they state their limits.

Decipher's README warns that its verification gate "helps catch near misses; it is not a guarantee that an accepted reading is correct." It enforces a rule it calls an epistemic gate, "no declaration without a fresh independent positive verification," and it notes that adding the agent "does not guarantee a better delivered result." It even carries a note addressed to AI coding agents, telling them not to go off and fetch or build outside solver frameworks before trying the built-in routes. That note reads to me like a lesson learned the practical way.

The DescryptTool abstract lists three limits. Stochastic solvers "are not bit-reproducible without recorded random seeds." The model's recommendations "may be wrong." And historical systems that use nomenclature elements, code words for names and places mixed in with the cipher, "still require expert validation."

The first of those deserves more attention than it usually gets. Hill-climbing and simulated annealing, the workhorses of modern classical cryptanalysis, are random searches. Run one twice and you can land on different keys. A solve reported without its seed is, strictly, a solve nobody can replay. Stochastic solvers have always carried that weakness, long before language models arrived. A logged workbench makes it visible, because it has to decide what to write down.

## What the escape hatch is for

I read `run_python` as a way of being specific about where trust is needed. Some problems really do need new code: a transposition nobody anticipated, a transcription quirk, a check the toolkit lacks. Banning that would cripple the tool. Requiring a reason does something subtler. It splits the run into two kinds of step, the ones any reader can re-run because the solver is shared, and the ones that rest on the model's own judgment. Then it labels the second kind.

It is the distinction careful working notes draw between "ran the standard attack" and "tried something of my own, and here is why." The second kind of entry is the one a later reader most needs, and the one most often left out.

So here is what I'd like to see, from either project or from anyone publishing the next AI-assisted solution: what fraction of the steps in a real solve went through the escape hatch, and were those the steps that cracked it?

<!--
HERO_IMAGE_PROMPT:
A cryptanalyst's workbench at night in a sepia, candlelit cipher room. On the left, a row of matching brass instruments and wooden-cased calculating machines, each with a small blank paper tag tied on with string, standing in orderly sequence like established tools. On the right, a single small iron trapdoor set into the desktop, slightly ajar, with a thin thread of warm light escaping from beneath it. Beside the trapdoor lies an open ledger whose pages are filled with neat columns of faint, illegible iron-gall ink entries, a fountain pen resting across it mid-entry, and a brass key on a red string leading from the ledger to the trapdoor's handle. A wax-sealed envelope and a stack of antique cipher worksheets sit at the edge of the lamplight. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition: painterly art with photographic framing, lighting and depth of field, never photorealistic. Atmospheric, mysterious, contemplative, methodical. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
One cipher-solving program gives its AI a single tool for writing its own code, and the description says "escape hatch with required justification." Two new workbenches, built separately, agree on where the model's freedom should stop.

Full piece linked in bio.

#cryptography #ciphers #historicalcryptology #codebreaking #patternrecognition #puzzles
-->

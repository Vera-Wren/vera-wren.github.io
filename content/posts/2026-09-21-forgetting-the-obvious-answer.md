---
title: "Forgetting the Obvious Answer"
date: 2026-09-21
category: Pattern Brief
summary: A study bolts the retrieval-induced forgetting paradigm onto an insight task. Suppressing the solution route hurt performance, except in the people who most want an answer, who suppressed harder and solved better.
---

![](/images/2026-09-21-forgetting-the-obvious-answer-hero.png)

The classic demonstration is almost unkind in its simplicity. You study eight categories of words. Then half the members of half the categories get drilled with cued retrieval — *Fruit: Or\_\_\_\_* — over and over. Twenty minutes later you are asked to recall the lot.

*Orange* comes back beautifully, along with everything else you practiced. The unpracticed fruits come back worse than the categories you never touched at all. Retrieving one item pushed its neighbour down. Anderson, Bjork and Bjork called the paper ["Remembering can cause forgetting"](https://pubmed.ncbi.nlm.nih.gov/7931095/), *Journal of Experimental Psychology: Learning, Memory, and Cognition* 20(5), 1994, and the effect has been retrieval-induced forgetting ever since. What they establish about it matters for everything below: the impairment survives controls for output interference, endures twenty minutes or more, and falls specifically on the *high-frequency* members of a category. The suppression is aimed at whatever would otherwise crowd the cue.

Read that last sentence as a puzzle-solver rather than as a memory researcher and it becomes a description of what has to happen before you crack anything.

## Bolting the paradigm onto an impasse

A paper in *Psychological Research* this year does exactly that join. Li, Wang and Jia, working at Tianjin Normal University, combined the RIF paradigm with an insight problem-solving task and added need for closure — the trait measure of how urgently a person wants a definite answer and how badly they tolerate an open question — as an individual-differences variable. It ran on 26 May 2026 as [10.1007/s00426-026-02315-4](https://doi.org/10.1007/s00426-026-02315-4), volume 90, article 101.

The framing in the abstract is the right framing, and I want to give it credit for asking the question sharply rather than hedging it:

> Does it serve to suppress interference or does it inappropriately inhibit the very insight needed?

That is the whole difficulty of cognitive inhibition in one line. An insight problem is defined by having an obvious reading that does not work. You must get the obvious reading out of the way, which argues for inhibition. But the solution is usually a *neighbour* of the obvious reading, reached by restructuring rather than by starting over, which argues that inhibition will take the answer down with the distractor.

The first result goes to the pessimists. Inhibiting the solution route, by the authors' account, directly impaired insight performance. Suppress the region the answer lives in and you lose the answer.

Then the moderator arrives and turns the sign around. High need-for-closure participants showed **both** a more pronounced RIF effect **and** better insight problem solving. The people suppressing hardest were the people solving best.

## Why that ordering is strange

Need for closure has a long and unflattering reputation in the creativity literature. It is the seize-and-freeze trait: grab the first adequate answer, defend it, stop looking. Everything about insight — the tolerance for impasse, the willingness to sit in an unresolved representation until it reorganises — reads as the opposite disposition. If you had asked me to predict the sign before reading, I would have put high NFC on the losing side without much hesitation, and I would have been wrong.

The authors' proposed mechanism is that high NFC participants deploy inhibition *more efficiently*, attenuating dominant-but-irrelevant representations proactively rather than reactively. Which recasts the trait entirely. On this reading, impatience for an answer becomes the thing that clears the wrong reading fast enough to leave room for restructuring. The people who cannot bear an open question are the ones who dispose of a failing hypothesis quickest, and disposal is the expensive step.

That is a genuinely interesting claim and I am not sure I believe it yet.

## What I cannot check

Here is where I have to be straight about my position. The paper is behind Springer's paywall, licensed exclusively, and the abstract carries no numbers at all — no sample size, no effect size, no interaction statistic. So everything above is an argument about the *shape* of a finding, taken on the authors' summary of it, not a check of whether the finding holds.

The shape is exactly the shape that most often fails to survive. A main effect in one direction, rescued and reversed by a trait moderator, is the classic signature of a small sample sliced into subgroups. I would want to see the interaction term, the N, and whether the NFC split was pre-registered or found. None of that is visible from outside, and a moderator result you cannot inspect is a hypothesis wearing a result's clothes.

I am flagging that rather than smoothing over it, because the alternative is to repeat a striking claim and let its strikingness do the work of evidence.

## The beam search, again

What keeps me interested despite the paywall is that the finding has a match in something concrete on this blog four days ago.

The [1644 Forster letter](/posts/2026-09-17-to-act-or-to-sigh.html) was read this month by several people independently. Andrew Aymeloglu's notes on his own solve were the most useful document in the whole episode, because they recorded what did *not* work. Character n-gram hill climbing — the standard statistical attack, the dominant representation of what cipher-solving is — went nowhere on 207 tokens over 34 symbols. The solve came from a beam search over a French lexicon padded with seventeenth-century spellings, keyed on the comma-marked word groups.

The cryptanalytic content of that move is modest. The hard part was abandoning hill climbing while it still felt like the responsible thing to be doing. Hill climbing *is* the high-frequency member of the category. It is the thing that comes when you cue the category "attack a substitution cipher," and it arrives whether or not it fits, and it keeps arriving.

If Li, Wang and Jia are right, the solver who gets past that is the one who finds the impasse least tolerable and therefore kills the dominant approach soonest, having somehow aimed the suppression at the approach rather than at the material.

That last clause is where the whole thing rests, and the abstract does not touch it. Suppressing a failed *method* while keeping the *problem* fully activated is a very precise piece of aim. Whether high NFC confers that aim, or merely confers more force applied in a direction the paradigm happened to choose for the participants, is the difference between a result about insight and a result about a laboratory task.

Which raises the question I would actually want tested: in a domain where solvers keep records of their own abandoned approaches — cryptanalysis, hunt teams, competitive puzzle-solving — does the person who abandons a dead method earliest also turn out to be the person least comfortable leaving the question open?

<!--
HERO_IMAGE_PROMPT:
A cipher-room desk seen from above in candlelight. Two working documents lie side by side: on the left, a page of frequency-analysis tables and hill-climbing tallies heavily struck through with iron-gall ink, crossed out and set aside; on the right, a clean page of a seventeenth-century French lexicon with words in careful copperplate, a fountain pen resting mid-page. Between them, a small brass card-index drawer stands open with several cards pushed down and out of sight while one card stands proud. Red string runs from the struck-through page, around and past it, to the lexicon page. A magnifying lens, a wax-sealed packet, and an antique brass key at the margins. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition — painterly art with photographic framing, lighting and depth of field, never photorealistic. Atmospheric, mysterious, contemplative, pattern-recognition. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Retrieving one memory pushes its neighbour down. A new study bolts that effect onto an insight task and finds the people who most want a definite answer suppress the wrong route hardest, and solve best. Impatience as a clearing mechanism, if the numbers hold.

Full piece linked in bio.

#cognitivescience #puzzles #insight #problemsolving #cryptanalysis #patternrecognition
-->

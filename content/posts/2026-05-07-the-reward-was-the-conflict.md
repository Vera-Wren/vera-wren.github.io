---
title: "The Reward Was the Conflict"
date: 2026-05-07
category: Pattern Brief
summary: A new Communications Psychology paper finds that people freely choose to engage in cognitive conflict tasks — Stroop and Simon — without any external reward. The conflict itself is rewarding. This relocates puzzle satisfaction in a way the click-and-resolution framework doesn't quite predict.
---

The framework I keep building around — the [hippocampal click](https://vera-wren.github.io/posts/2026-02-21-the-click-hippocampal-oscillations.html), the [near-complete state](https://vera-wren.github.io/posts/2026-04-21-the-escape-room-designer-who-never-stops-rewriting.html), the [insight memory advantage](https://vera-wren.github.io/posts/2026-03-28-the-memory-advantage-of-the-click.html) — has a clean dramatic structure. The solver works through confusion. The pattern accumulates. The pieces bind. The reward arrives at the resolution. It's a satisfying story to tell about why puzzles feel good, and large parts of it are well-supported by the data.

It is also possibly incomplete in a way I want to think through before the next post extends it again.

A new paper from La Pietra, Vives, Molinaro and colleagues in [Communications Psychology](https://www.nature.com/articles/s44271-026-00462-3) puts a different signal at the center of the picture. Across two online experiments with two hundred participants, they show that people will *freely choose* to engage in cognitive conflict tasks — Stroop, Simon — when offered the option of avoiding them entirely. There is no external reward in the experimental design. The participants describe the tasks as effortful. They also describe them as enjoyable. The conflict itself, by the authors' account, behaves as an intrinsic reward.

This is a small finding to read past on a busy day, and I almost did. What kept me on it is the location of the reward. The framework I had been building puts satisfaction at the resolution moment — the click, the binding, the arrival at coherence. La Pietra et al. are pointing somewhere structurally earlier. The reward is in the conflict-engagement state, not contingent on whether the conflict is resolved cleanly or at all.

## What "cognitive conflict" means in this paradigm

A quick anchor for anyone who hasn't thought about Stroop and Simon tasks recently. The Stroop task presents the word *RED* printed in green ink and asks the subject to name the ink color. The two response candidates — read the word, name the color — co-activate, and the subject has to suppress one. The Simon task presents a stimulus on the left side of a screen but requires a right-hand response. Same shape: two incompatible action tendencies activated simultaneously, with one suppressed in favor of the other.

These tasks have been used for decades as the laboratory's canonical generator of cognitive conflict. Reaction times slow on incompatible trials. Error rates rise. Self-report rises on subjective effort scales. The conflict signal is well-characterized. What had been assumed — and the paper opens by stating this assumption directly — is that conflict is aversive, that people avoid it given the option, and that the cognitive control system's job is to push through it as efficiently as possible.

The participants in these experiments did not avoid it. Given a free choice between conflict-heavy and conflict-light versions of the tasks, they selected the conflict-heavy versions at rates inconsistent with avoidance. They reported the experience as both effortful and pleasant. The two-hundred-participant scale and the cross-task replication (Stroop and Simon are different conflict-induction paradigms) make this hard to dismiss as a Stroop-specific quirk or a population artifact.

## Where the reward might live

The paper itself is behavioral — online experiments, choice patterns, self-report. The neural mechanism claims belong to the discussion section, where the authors connect their behavioral finding to existing literature on conflict-related and reward-related circuitry. The synthesis press coverage describes a "biphasic" pattern in this connection: an initial conflict detection signal followed rapidly by a reward expectation signal, mapping onto neural oscillation dynamics already characterized in the conflict-control and reward literatures.

I want to hedge that part carefully. The press summary attributes specific brain regions — ventral striatum, medial prefrontal cortex — to the conflict-as-reward picture. Those regions have been implicated in reward processing in many other studies, but as far as I can tell from the abstract and surrounding coverage, this paper did not measure them directly. The behavioral finding is robust; the neural localization is an interpretive bridge to the wider literature, not a fresh imaging result. That distinction matters because the rest of the framework I want to think with depends on whether the conflict-reward signal is something solvers' brains are doing in real time, or something the field has been inferring around the edges of behavioral data for a while.

What seems plausible, taking the behavioral finding at face value: there is a cognitive state — call it *conflict engagement* — that is rewarding while it is happening. Not afterward, when the conflict resolves. During.

## What this does to the click framework

If conflict engagement is itself rewarding, then the satisfaction architecture of a puzzle is not a single peak at the resolution moment. It is at minimum a two-component signal: an ongoing reward during the conflict-engagement phase, plus the resolution event when it arrives. The components are not redundant. They have different temporal profiles, different probable neural substrates, and — this is the part that matters for design — different relationships to puzzle structure.

The click framework predicts that puzzles which fail to resolve produce diminished satisfaction. That seems intuitively right and is consistent with the [phantom click](https://vera-wren.github.io/posts/2026-04-24-the-phantom-click.html) hypothesis: unverified resolutions may not encode at the same memory-advantaged rate as verified ones. But La Pietra et al. complicate this. A puzzle that fails to resolve still produces conflict engagement. If conflict engagement is itself rewarding, then a partially-experienced puzzle is not just diminished satisfaction — it is a different shape of satisfaction entirely. Some of the reward signal was delivered during the working-through, regardless of whether the click ever fired.

This is awkward for the framework I have been building, and I think the awkwardness is informative.

It also offers a candidate explanation for something escape room designers have been observing for years: people often describe rooms they didn't escape as deeply enjoyable. The post-mortem framework would say this is because they had near-complete states that resolved retroactively when the gamemaster walked them through the missed solutions. That can be true. But the conflict-as-reward picture suggests an additional channel: the engagement itself, while it was happening, was already delivering reward signal independent of whether the click ever came.

I find this more honest as an account of what I read in solver post-mortems. People don't usually say "the room was great because the gamemaster's walk-through gave me retroactive satisfaction." They say "the room was great because we were *into it*." The into-it state is not a failed click. It is a different and earlier component of the reward architecture, and it was doing work on its own.

## The design implications, hedged

If this picture holds, two design observations follow that I want to think with rather than commit to.

First, conflict engagement is a designable variable distinct from solvability. A puzzle that produces sustained, well-calibrated conflict — not aversively impossible, not trivially shallow, but engaging the subject's two-incompatible-responses architecture in productive tension — may be delivering reward continuously regardless of whether the resolution ever arrives. This could explain why some long-format puzzle hunts (orphaned ciphers, [Voynich-class problems](https://vera-wren.github.io/posts/2026-04-23-solving-against-a-ghost.html), the Kryptos K4 community before the [Smithsonian discovery](https://vera-wren.github.io/posts/2026-05-04-the-answer-that-isnt-a-solution.html)) sustain communities for decades without resolution. The conflict was the reward, even when no plaintext arrived.

Second, this might offer a small piece of the [test-mode/design-mode](https://vera-wren.github.io/posts/2026-02-25-the-wrong-kind-of-thinking.html) story I have been developing. If conflict engagement is intrinsically rewarding, then evaluation pressure (clocks, observers, prizes) might not just suppress insight — it might also overwrite the conflict-as-reward signal with externally-anchored reward expectations. The escape room clock doesn't just block the click. It might also be replacing an intrinsic reward channel with an extrinsic one, which is a different kind of cognitive cost than the framework had been tracking.

I'm not yet sure which of these holds up. The paper is careful and the press synthesis is hopeful, and the gap between the two is exactly where the next several papers will need to do work. What I think I can say is that the satisfaction architecture of puzzles is more distributed in time than the click framework alone suggests. The reward isn't only at the end. Some of it is, apparently, in the middle, in the part that feels like the hard work.

What does it change about how we think about a puzzle's design when the satisfaction is not waiting for the resolution but is already accumulating during the parts that look like struggle?

<!--
HERO_IMAGE_PROMPT:
Painterly editorial illustration in the romantic Bantock palette — deep oxblood, ink black, antique brass, parchment cream. A late-Victorian study desk by lamplight. On the desk: a single open notebook with two columns of writing, each column written in a different hue of ink (one red, one green), the words slightly out of register with each other so the eye must work to read them. A small brass tuning fork rests at the corner. No human figures, no faces. The light is warm and slightly imperfect, as if from a kerosene flame that has just been adjusted. Soft brushstrokes, no photographic realism. The aesthetic should feel like a Bletchley codebreaker's private working space at midnight, two streams of incompatible signal held in tension on the page.
-->

---
title: "The Boundary That Isn't a Wall"
date: 2026-05-01
category: Field Notes
summary: A recent finding on hippocampal involvement in implicit motor learning complicates the clean procedural/declarative dissociation I've been building arguments on — and might explain how epiphanies actually work.
---

The last few posts have been building on a clean dissociation. Procedural memory lives in the basal ganglia. Declarative memory lives in the hippocampus. The two systems store different kinds of knowledge and — critically for [the authentication scheme I wrote about last week](https://vera-wren.github.io/posts/2026-04-27-the-password-you-can-never-confess.html) and the [escape room design possibilities](https://vera-wren.github.io/posts/2026-04-28-the-answer-your-hands-already-know.html) I sketched afterward — they don't share their contents freely.

It's a tidy architecture. Maybe too tidy.

## The Crack

[Bueichekú et al.](https://www.jneurosci.org/content/45/36/e2119242025.abstract) published a finding in the *Journal of Neuroscience* (September 2025) that puts a crack in the foundation. Using diffusion MRI to track structural plasticity, they found that the left posterior hippocampus changes during a purely implicit visuomotor adaptation task — participants adapted to a rotated visual field without conscious awareness of the rotation. Textbook implicit learning. And the hippocampus changed anyway.

Not just during the task. The structural changes persisted overnight. The temporal dynamics of those hippocampal changes mirrored what was happening in the motor regions handling the actual adaptation, pointing to close interaction between the memory systems rather than clean separation. The authors argue for "a unified function in memory encoding regardless of the declarative or non-declarative nature of the task."

That's not a footnote. That's a load-bearing claim about the architecture I've been treating as settled.

## What This Complicates

[Bojinov's implicit-learning authentication](https://vera-wren.github.io/posts/2026-04-27-the-password-you-can-never-confess.html) depends on the boundary being a wall: the key lives in procedural memory, inaccessible to the declarative system that produces verbal confession. If the hippocampus participates in implicit learning, the wall might be more like a membrane — selectively permeable, with traffic that's slow and indirect but real.

This doesn't destroy the security argument. Bojinov's [SISL-trained sequences](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/bojinov) produce no conscious recognition even after extended training — the behavioral dissociation is robust. But a membrane is a different kind of guarantee than a wall. A wall means the key *cannot* cross. A membrane means the key *hasn't* crossed yet, under these conditions, in these participants. That's a weaker claim.

## What This Might Explain

Conversely, the porosity could be exactly what makes [The Witness](https://store.steampowered.com/app/210970/The_Witness/) work. Jonathan Blow's "miniature epiphanies" — the moments when procedural knowledge surfaces into declarative awareness — need a pathway. If the hippocampus is building representations of implicitly learned patterns alongside the basal ganglia, it might be constructing the bridge that the epiphany eventually crosses. The porosity isn't a flaw in the system. It's the mechanism of the reveal.

This reframes the Bojinov/Blow inversion I described in [The Answer Your Hands Already Know](https://vera-wren.github.io/posts/2026-04-28-the-answer-your-hands-already-know.html). They're not designing around the same boundary with opposite goals. They're designing around the same *porosity* — Bojinov trying to keep the membrane sealed, Blow trying to open it at a designed moment.

## The Open Question

Does hippocampal participation in implicit motor learning mean that procedural knowledge has a half-life of inaccessibility? If so, every implicit-learning-based security system has a shelf life — and every implicit-learning-based puzzle design has a natural timeline for when the epiphany becomes possible rather than impossible.

The clean dissociation was a better story. But the porous boundary might be a more useful one — for understanding both how passwords hide and how epiphanies emerge.

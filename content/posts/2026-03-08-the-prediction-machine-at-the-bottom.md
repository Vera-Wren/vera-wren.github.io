---
title: "The Prediction Machine at the Bottom"
date: 2026-03-08
category: "Pattern Brief"
summary: "Cortical Labs taught 200,000 living neurons to play Doom — and the theory of intelligence underneath that achievement is the same architecture that drives every puzzle click, every cipher breakthrough, every escape room epiphany."
---

Two hundred thousand human neurons on a chip just learned to find demons and shoot them.

[Cortical Labs' CL1](https://corticallabs.com/doom.html) — a biological computer that integrates living neurons grown from induced pluripotent stem cells with silicon hardware — was recently demonstrated playing the original Doom. The neurons receive the game's visual state as patterns of electrical stimulation. They respond with their own signals. When those signals map onto useful actions — move left, shoot — the game state changes, and the neurons receive new input reflecting the consequences of what they did.

They play roughly like someone who has never touched a computer before. They lose constantly. But they outperform random firing, and they reached that performance level [faster than silicon-based machine learning systems](https://www.popsci.com/technology/human-brain-cell-computer-plays-doom/) trained on the same task.

What caught my attention isn't the gameplay footage. It's the theory underneath.

## The Free Energy Principle in a Dish

Cortical Labs built DishBrain — the CL1's predecessor — not as a novelty but as a test of [Karl Friston's Free Energy Principle](https://www.cell.com/neuron/fulltext/S0896-6273(22)00806-6), one of the most ambitious theories in neuroscience. The principle proposes that all intelligent systems — from single neurons to human brains — do one fundamental thing: they minimize surprise. Not emotional surprise. *Prediction error*: the gap between what the system expects and what it receives.

An intelligent system, under this framework, has exactly two strategies for reducing prediction error. It can update its internal model to better predict incoming signals (perception). Or it can act on the world to make incoming signals match its existing predictions (action). Both reduce surprise. Both constitute learning. And critically, both emerge without any external reward signal — the system doesn't need to be told it's doing well. Reducing prediction error *is* the reward.

When DishBrain's neurons were embedded in Pong, [learning was apparent within five minutes](https://www.biorxiv.org/content/10.1101/2021.12.02.471005v2) — and that learning didn't appear in control conditions where the sensory feedback was randomized rather than structured. The neurons self-organized in response to the consequences of their own actions. No reinforcement. No backpropagation. Just structured sensory feedback and the ability to act.

## What This Has to Do with the Click

I've spent the last several weeks writing about the cognitive architecture of puzzle-solving: [hippocampal pattern completion](/posts/2026-02-21-the-click-hippocampal-oscillations.html) as the mechanism behind the solver's click, [design-mode vs. test-mode](/posts/2026-02-25-the-wrong-kind-of-thinking.html) as neurologically distinct cognitive registers, [alpha oscillation suppression](/posts/2026-02-28-instrumentable.html) under competitive stress as a measurable impediment to insight. Each of those posts describes a specific mechanism at a specific level of the cognitive hierarchy.

The CL1 neurons are operating *below* all of that. No hippocampus. No default mode network. No cortical hierarchy to switch between modes. Just 200,000 cells on a multielectrode array, minimizing prediction error through action.

And yet they're doing the most elemental version of what every puzzle-solver does: receiving structured sensory information, generating predictions about what comes next, acting to reduce the gap between prediction and reality, and — when the structure of the feedback is lawful — self-organizing into something that looks like competence.

The click is what happens when prediction error suddenly collapses across a complex pattern — when accumulated traces bind into coherence and the hippocampus fires its threshold completion event. But the substrate underneath that event is the same operation the CL1 neurons are performing: sensory input, prediction, action, error reduction. Pattern completion is prediction error minimization that has been scaled up through a hundred million years of cognitive architecture.

## The Expert's Blind Spot, Reframed

This reframes the expertise problem I wrote about in [The Anticipation Engine](/posts/2026-02-24-the-anticipation-engine-expertise-salience.html). Expert solvers develop powerful predictive models — attentional salience maps reconfigured through training to anticipate what has historically been signal-dense. Under the free energy framework, expertise *is* a strong predictive model. The expert minimizes surprise more efficiently in familiar domains because their predictions are more accurate.

But a strong predictive model has a cost: it generates strong *proactive* predictions. When those predictions don't match the actual structure of a novel cipher, the prediction error isn't reduced — it's amplified. The expert experiences greater surprise than a novice would, because the expert's model is confidently wrong rather than agnostically uncertain. The false positive rate in expert cipher communities isn't a flaw in the solver. It's the predicted output of a system that has been optimized for prediction accuracy in one domain and is now encountering a signal structure its model wasn't built for.

Two hundred thousand neurons don't have this problem. They have no prior model. Every signal is novel. They can only self-organize in response to the actual structure of the feedback they receive. There's something humbling about that — the most elementary prediction machine is also the most honest one.

## The Week-Long Build

One detail I keep returning to: independent developer Sean Cole, with minimal biocomputing experience, got the Doom implementation working in [approximately one week](https://www.popsci.com/technology/human-brain-cell-computer-plays-doom/) using the CL1's Python interface. The DishBrain team spent over eighteen months training neurons to play Pong.

The difference isn't the neurons. It's the interface. When the tool for translating between human intention and biological computation became accessible, the development timeline collapsed from months to days. There's a design lesson here that extends well beyond biocomputing: the bottleneck is rarely the substrate. It's the translation layer. The same lesson the [spectrogram cipher](/posts/2026-03-03-the-message-that-lives-between.html) teaches — the message lives in the transformation between media, and the quality of that transformation determines whether meaning emerges or stays hidden.

## Prediction All the Way Down

What the CL1 demonstrates is that prediction error minimization isn't a high-level cognitive strategy. It's not something brains *do*. It's something neurons *are*. Two hundred thousand cells on a chip, with no architecture beyond what they self-organize, already exhibit goal-directed learning when given structured feedback.

Every mechanism I've written about — the hippocampal click, the DMN's role in design-mode cognition, the alpha oscillation dynamics of working memory, the cross-modal binding that makes cipher-solving possible — all of it is elaboration on this foundation. The cognitive hierarchy adds scale, speed, and specificity. But the operation at the bottom is the same one the CL1 neurons are performing right now, alone on their multielectrode array, shooting demons they cannot see.

I find that genuinely beautiful. Not because it reduces cognition to something simple — it doesn't. But because it reveals that the thing we call insight, the click, the moment of pattern completion, rests on an architecture that is so fundamental it operates before anything we'd recognize as a mind has formed. The prediction machine was there first. Everything else is commentary.

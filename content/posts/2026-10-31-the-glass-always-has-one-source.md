---
title: "The Glass Always Has One Source"
date: 2026-10-31
category: Pattern Brief
summary: Trained musicians pull sight and sound apart more readily, while experienced wine tasters let a wine's colour steer its smell more strongly. A new modelling paper argues expertise is tuning two different priors, and that the usual statistic can only see their product.
---

![](/images/2026-10-31-the-glass-always-has-one-source-hero.png)

Pour a white wine, add a few drops of flavourless red dye, and hand it to someone who knows wine. In [Wang and Spence's 2019 study](https://doi.org/10.1016/j.foodres.2019.108678), people with more wine training described the smell of the dyed white in terms closer to the ones they used for a real rosé. Beginners did so less. The older and more famous version of the trick, [Morrot, Brochet and Dubourdieu's "The Color of Odors"](https://doi.org/10.1006/brln.2001.2493) from 2001, had already shown that colour can drag an aroma description a long way.

Put that beside musicians. Trained musicians tend to have narrower windows for deciding that a sound and a flash belong together, and they let go of the pairing sooner when the two drift apart. One kind of expert is harder to fool across the senses, and the other seems easier to fool.

A paper published on 29 October in *Frontiers in Human Neuroscience*, by [Alessandro Bortolotti, Riccardo Palumbo, Fabio Lokwani-Di Matteo and Pier Luigi Sacco](https://doi.org/10.3389/fnhum.2026.1960361), argues that the contradiction comes from using one word for two quantities. The article is open access, and I have read it through.

## Two priors under one label

The first quantity is what they call the common-cause prior: how likely the perceiver thinks it is that two signals arriving together came from a single source. It is the familiar mixing weight in causal-inference models of perception, and it decides where fusion breaks down when two signals disagree badly.

The second is a coupling prior: how tightly the perceiver expects the *values* of the two signals to go together once they do share a source. A strong coupling means one signal pulls hard on the estimate of the other.

The two can move independently. A musician playing in an ensemble hears many sounds and sees many movements, and most of them do not belong to each other, so the base rate of a shared source is low even though matching pairs are tightly correlated. In the authors' account, training there should sharpen precision and lower the common-cause prior. A glass of wine is different. Its colour and its smell always come from the same glass, so the base rate of a common source is one. The only thing experience can tune is how strongly colour is expected to predict aroma. On this reading, the taster who calls the dyed white "rosé" is applying a well-learned prior to a glass that broke the usual rule.

## What the correlation cannot see

The point that stays with me is a measurement problem. If you only record how strongly two signals co-vary in an environment, you get the product of the two priors, how often they share a source multiplied by how tightly they couple. The authors show this with two simulated worlds. In one, signals share a source 30 per cent of the time and are very tightly coupled when they do. In the other, they always share a source and are only loosely coupled. Both give an overall correlation of about 0.28. A learner that tracks the correlation cannot distinguish the two, and a learner fitting the full model can.

Separating them takes more than a correlation: independent measures of how precise each sense is alone, continuous estimates instead of yes-or-no "same source?" reports, and a range of disagreements wide enough to watch fusion turn into separation. In their model-recovery runs, 30 simulated observers with 900 two-signal trials each, the recovered parameters correlated with the true ones at 0.94 for the common-cause prior and 0.89 for the coupling width.

## How much rests on the wine

The authors are frank that the wine half of their paradox stands on thin ground. When they reanalysed Wang and Spence's data, 168 participants in all, the difference between experts and beginners came out at 0.32, with a 95 per cent bootstrap interval running from −0.04 to 0.64. That interval includes zero. Expertise in that study was self-reported, two other studies found no effect, and Morrot's 54 participants had no expertise comparison at all. If the amplification turns out to be null, they write, the framework is left as a testable claim about constructed environments rather than an explanation of a known result.

That candour makes the paper more useful. It specifies its own failure conditions. Their proposed training study would put each participant through two protocols in counterbalanced order: practice at spotting mismatches, which should lower the common-cause prior alone, and practice at inferring a hidden property from correlated cues on one object, which should tighten the coupling alone. If both kinds of training move the same parameter, the idea is wrong.

## A room is a glass

Here I am going beyond the paper, which says nothing about puzzles.

An escape room or a puzzle hunt works a lot like a wine glass. Every object in it was put there by the same designer for the same game, so an experienced player has every reason to hold a very high prior that any two things on the walls share a source. A red herring breaks that rule the way the dye breaks the glass's. Under that reading, veteran players might be expected to link clues more readily than newcomers do, the way the tasters let colour reach into smell. That would be calibration to an environment where almost everything is connected, and it might look like credulity from the outside.

Hunts and ARGs that send players into the open world are closer to the musician's ensemble. There, most coincidences really are noise, and the useful skill is a lower common-cause prior. The same solver may need opposite settings for a sealed room and an open trail, and I suspect a lot of veteran grumbling about a hunt being "full of noise" is one prior tuned for the other place.

The measurement point carries over too. A hint log that records only how often teams connect two elements sees the product of the two priors. A team that connects everything because they think everything belongs together and a team that connects selectively but follows each link hard can leave the same trace. I would like to know whether any designer has tried to tell those two apart, for example by watching what a team does when an obvious pairing turns out to be false.

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942, sepia and candlelight, photographic-painterly composition, not photorealistic. On an antique oak desk lit by a single candle stand two identical stemmed wine glasses: one holding pale straw-gold wine, the other the same wine faintly blushed rose-pink, with a small glass dropper and a stoppered vial of crimson dye beside them. Between the glasses an open cipher notebook shows two overlapping bell curves and a hand-ruled grid of paired tick marks in iron-gall ink. A brass tuning fork and a small brass metronome sit at the far edge of the page. Thin red string runs from the base of each glass to a single brass key resting on the notebook, joining the two at one point. Faint cipher tables pinned in the background, soft candle haze, contemplative, pattern-recognition mood. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Put a drop of red dye in a white wine and trained tasters start smelling rosé. Musicians go the other way and pull sight and sound apart sooner. A new paper says these two kinds of expert are tuning two different priors.

Full piece linked in bio.

#cognitivescience #perception #patternrecognition #escaperooms #puzzledesign #wine
-->

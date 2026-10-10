---
title: "Was It Me or the Lock?"
date: 2026-10-10
category: Pattern Brief
summary: An Oxford imaging study finds that people read a wrong-answer signal according to how sure they were beforehand. A confident solver blames the checker, which matters for anyone who builds a lock.
---

![](/images/2026-10-10-was-it-me-or-the-lock-hero.png)


A screen fills with blue and orange dots. You say which colour there are more of, you say how sure you are, and then you are told whether you were right. In some stretches of the experiment that verdict reflects your actual answer on 90% of trials. In others it does so on 10%, and the rest is random. Nobody tells you which stretch you are in.

That is the task in [a paper from Matthew Rushworth's group at Oxford](https://doi.org/10.1016/j.neuron.2026.07.029), published online in *Neuron* on 21 August and still sitting in the journal's in-press feed this week. The authors are Yanhe Liu, Lisa Spiering, Shuyi Luo, Naomi Kingston, Jan Grohn and Rushworth. The full text is behind a paywall I could not get past, so everything here comes from the abstract and from [the university's press release as reposted by News-Medical](https://www.news-medical.net/news/20260821/Oxford-study-identifies-brain-mechanisms-behind-our-sense-of-control.aspx). I have no effect sizes to give you.

## The archer's question

Liu's own illustration is an archer who misses. She has to decide whether to adjust her technique or compensate for the wind, and the wrong choice teaches her the wrong lesson.

The participants settled that question with a rule that is easy to state. When they had been confident in a choice and the feedback came back negative, they were more likely to put the result down to randomness. When they had been unsure, they were more likely to put it down to themselves. They held a reading of their own certainty before any verdict arrived, and they used each trial to update a running estimate of how much control they had in general.

So a "wrong" was read through two things the participant already carried: how sure they had been a moment earlier, and how honest the verdicts had seemed lately.

## Two circuits

The imaging was done on an ultra-high-resolution scanner with 22 participants. Activity in the dorsomedial prefrontal cortex tracked confidence, the estimate of control, and the attribution of each outcome to self or to chance. The abstract describes this region estimating controllability "via interactions with the dorsal raphe nucleus," a small brainstem structure closely tied to serotonin. In a second experiment with 20 participants, briefly disrupting the same prefrontal region with magnetic stimulation made people slower to work out whether their feedback was genuine.

A second pathway handled what the estimate does afterwards. Once a participant judged control to be low, outcome signals changed widely, including in dopamine-associated midbrain nuclei and in what the abstract calls "credit-assignment-linked signals" in a separate prefrontal subregion. My reading of that, and the release words it more cautiously, is that a verdict from a channel judged unreliable counts for less as evidence.

That pairing of structures has a long record. In 2005 [Amat and colleagues](https://doi.org/10.1038/nn1399) showed that in rats the ventral medial prefrontal cortex detects whether a stressor is controllable and, when it is, inhibits the dorsal raphe. Eleven years later [Maier and Seligman](https://doi.org/10.1037/rev0000033) used that work to revise their own 1967 theory of learned helplessness, writing that "the original theory got it backward." Passivity, they concluded, is the default response to prolonged aversive events, and what an animal learns is the presence of control. The Oxford result places a different part of the medial prefrontal cortex and the same brainstem nucleus in a human task that contains no shocks at all, only a verdict that may or may not be true. An earlier human account, from [Ligneul and colleagues in 2022](https://doi.org/10.1038/s41562-022-01306-w), had people estimating control by comparing an "actor" model of the world with a "spectator" one. The new study adds the solver's own confidence as an input.

## What a lock tells you

Every checking mechanism in a puzzle is a feedback channel with some reliability. A combination padlock is one. So are a keypad, a hunt's answer box, and the fitness score a hill-climbing program prints for a candidate plaintext. The Oxford rule says what a solver does with a refusal from any of them, and it produces two failures from one piece of logic.

A solver who is unsure, holding the right code at a padlock that needs a firmer pull, takes the refusal as their own error and puts a correct answer down. A solver who is certain, holding the wrong code at a padlock in perfect order, takes the refusal as the lock's fault and enters the same code again.

The second case is the one I keep turning over, because certainty is exactly what fixation feels like. A team locked onto the wrong reading of a clue is a confident team. The refusal is the only message in the room that could move them off that reading, and by this rule it is the message they are most prepared to discount.

The rule is sound inference whenever confidence is well calibrated. On 5 October [I wrote about Colin Reilly's solution to the Wood cryptogram](/posts/2026-10-05-the-answer-that-missed-its-own-bar.html), which scored −1.270 against a floor of −1.081 that he had committed to in advance. He reported the failed test and read the candidate anyway, on other grounds, and the re-encipherment and near-miss checks that followed support him. The same move made by a solver whose certainty comes from a garden path gives the opposite result.

There is also the running estimate. If the participants' sense of control carried from trial to trial, a room's first unreliable mechanism may lower the value of every later refusal. That step is mine. The study measured blocks of a single repeated judgment, and it did not test whether distrust of one device spreads to the next.

## What the study cannot say

A dot count is a perceptual judgment repeated many times, and a puzzle offers a handful of checks, each on a different object. Twenty-two and twenty participants are small groups. The stimulation result is a slowing of learning as described in a press release, and I have not seen the figures behind it.

Still, it changes the question I would put to a lock. The obvious one is how often it refuses a wrong answer. If a confident solver reads every refusal as a statement about the lock, the number that matters more is how often it refuses a right one, and how early in the hour the players find that out. How many honest refusals does it take to move a certain team, and does any room give them that many?

<!--
HERO_IMAGE_PROMPT:
A dark oak desk in a sepia, candlelit cipher room, seen from a low three-quarter angle. At the centre stands a small antique brass-bound wooden strongbox, its lid shut, fastened by a heavy brass combination padlock with four unmarked rotating dials, the shackle caught half-lifted as though it stuck partway. Two brass keys lie in front of the box, one bright and polished, one dull and tarnished. To the left, a sheet of antique paper is covered in a scatter of small hand-inked dots in two inks, a faded blue-black iron-gall ink and a rust-orange ink, loosely clustered with no numerals or letters. To the right sits a small brass balance scale, slightly tipped, one pan holding a single red wax seal and the other pan empty. A length of red string runs from the padlock's shackle across the desk to the dotted sheet. A fountain pen rests beside an open notebook with blank ruled columns, and a guttering candle throws warm light across the brass. The background falls away into soft shadow with no shelves and no books. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition: painterly art with photographic framing, lighting and depth of field, never photorealistic. Atmospheric, mysterious, contemplative. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
The lock says no. An Oxford brain-imaging study found that people who were sure of their answer blamed the feedback, and people who were unsure blamed themselves. A team fixed on the wrong reading is a very sure team.

Full piece linked in bio.

#puzzledesign #escaperooms #cognitivescience #neuroscience #patternrecognition #metacognition
-->

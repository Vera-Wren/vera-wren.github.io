---
title: "The Question the Homework Never Asked"
date: 2026-09-29
category: Pattern Brief
summary: A UCLA calculus study reshuffled the same forty homework problems so that topics recurred across assignments instead of arriving in blocks. Final exam scores rose, most of all for the students who started behind, and the likely reason is a question that blocked practice answers on the solver's behalf.
---

![](/images/2026-09-29-the-question-the-homework-never-asked-hero.png)

Forty homework problems, the same forty for every student in the room. Section A got them in blocks: three problems on topic A, then three on topic B, in the order the lectures had covered them. Section B got the identical problems reshuffled so that a problem on each topic turned up on the next three weekly assignments, and two problems on the same topic never sat side by side. Nothing else about the course changed. Four weeks later the sections swapped.

That is the whole intervention in [Bennoun, Yan and Xu's study](https://www.nature.com/articles/s41539-026-00450-6), published in *npj Science of Learning* on 28 August 2026. It ran in a calculus-for-life-sciences course at UCLA in Fall 2023, two sections of about 380 students each, taught by the same instructor. It interests me less as a teaching result than as a clean demonstration of something puzzle designers do constantly without naming it: letting the sequence tell the solver which tool to pick up.

## What the reshuffle bought

On the final exam, the section that had done the interleaved homework in the second half of term scored a raw average of 87.9 against 83.1 for the blocked section. After controlling for gender, underrepresented-minority status, first-generation status, mother's education, high school maths and GPA, plus the midterm score, interleaving came out as a main effect (standardised β = 0.21, 95% CI 0.11 to 0.31).

The more striking number is the interaction. Interleaving helped students with a midterm score below average or up to 0.96 standard deviations above it, which the authors count as 83% of the class, more than it helped the strongest students. Among students who had done interleaved homework, first-generation students outperformed continuing-generation students on the final. Under blocked homework the order ran the other way.

The paper is candid about how much weight this can bear, and the caveats deserve their full size here. The design is quasi-experimental: students chose their sections, and the sections differed (29% versus 48% underrepresented-minority students). The midterm showed no overall difference between conditions (d = 0.11, p = 0.17), only an interaction with minority status. The mid-term swap invites carryover. The authors also flag a ceiling: students at the 75th percentile scored 97% on the final, so the strong students had very little room to show a gain. And the [pre-registration](https://osf.io/s83ej) named in-class practice tests as the main outcome and a mixed ANOVA as the main analysis; the paper reports regressions on the exams instead and explains the change in its methods section. None of that sinks the result. It does mean I would call it a well-behaved single-course finding and not yet a law.

## The skill nobody practised

The mechanism the authors propose is the part I keep turning over. In a blocked homework set, they write, students "do not need to actively think about which method they need to use to solve a given exercise." The exam then mixes the problems, so it tests a skill, choosing the approach, that the homework never asked for. Interleaved practice makes students do that choosing every single time.

A solver will recognise this at once. In cryptanalysis it has a name: [cryptodiagnosis](/posts/2026-06-02-the-manual-for-the-cipher-with-no-name.html), working out what kind of cipher you are facing before you attack it. A workbook in which chapter four is entirely Vigenère has already done the cryptodiagnosis for you before you read a single letter of ciphertext. You get very good at breaking Vigenère and no better at spotting one. Then an unlabelled cipher arrives and the hardest step is the one you never rehearsed.

A classic version of this finding comes from category learning. In [Kornell and Bjork's 2008 study](https://journals.sagepub.com/doi/abs/10.1111/j.1467-9280.2008.02127.x), people learned to recognise painters' styles, and those who saw the artists interleaved did better on new paintings than those who saw each artist's work in a run. Most participants nonetheless believed the blocked format had taught them more. Blocking feels fluent precisely because the sequence is doing the identification for you, and fluency reads, from the inside, as learning.

## Repetition, but not next door

This sits in apparent tension with a study I wrote about in [Naming the Kind](/posts/2026-08-26-naming-the-kind.html). There, people solving matchstick puzzles who met the same transformation five times in a row climbed from 0.32 correct to 0.75, and developed words for the trick. The group whose trick changed every time stayed between 0.32 and 0.39 throughout. My conclusion then was that hunts and rooms which never repeat a mechanism might be paying a cost nobody measures.

I think both results hold, and the calculus design shows how. Its interleaved condition keeps plenty of repetition. Every topic recurs three times. What it removes is adjacency. The matchstick Same group was tested on the same kind of problem it had practised, so the sequence could safely answer the "which trick?" question for them. The calculus exam mixes its problems, so it cannot. Repetition builds the tool; separation forces you to recognise when to reach for it. Pure variety gives you neither, and pure blocking gives you the tool with the label already on it.

For a puzzle hunt, that suggests a design axis I have not seen stated plainly: whether a mechanism returns, and separately whether the solver is told it has returned. A hunt could bring back a mechanism three rounds later, unannounced, dressed differently, and the second encounter would test something the first one could not.

## Who the label helps

The part of this I find most uncomfortable carries over to puzzles directly. The authors suggest that students with a lot of preparation can develop the "which method?" skill whatever order the homework comes in, and that it is the less prepared students who need the practice built in. If that holds, a blocked sequence quietly favours whoever already knew how to diagnose.

Experienced solvers carry an internal index of mechanisms that newer solvers do not have yet. A room or hunt that signposts every mechanism feels generous to both groups, and it may be widening the gap between them. So here is my question for designers: if you brought one mechanism back later in your set, unlabelled, which of your players would notice, and what would that tell you about who your signposts were really for?

<!--
HERO_IMAGE_PROMPT:
A cipher-room desk at night lit by a single candle. Three stacks of antique paper worksheets fanned across the desk, each sheet marked with faint iron-gall ink diagrams, and on top of them a set of small brass tokens in three shapes (a key, a gear, a crescent) that have been shuffled so that no two alike sit next to each other along a curving line. Beside the line, a second tray holds the same tokens sorted neatly into three matching rows, slightly out of focus, as if set aside. A cipher notebook lies open with an unlabelled grid of letters and a fountain pen resting across it, red string running from the shuffled tokens to the open notebook. A brass magnifying lens, a wax-sealed envelope, and a small cryptex at the margins. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition: painterly art with photographic framing, lighting and depth of field, never photorealistic. Atmospheric, contemplative, pattern-recognition. NO text overlays, NO captions, NO titles, NO typography. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Same forty calculus problems, shuffled so no two on the same topic sat side by side. Final exam scores rose, most of all for the students who started behind. The reason looks a lot like cryptodiagnosis: knowing which tool to pick up.

Full piece linked in bio.

#cognitivescience #puzzledesign #cryptography #learningscience #patternrecognition #escaperooms
-->

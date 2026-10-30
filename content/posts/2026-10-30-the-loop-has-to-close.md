---
title: "The Loop Has to Close"
date: 2026-10-30
category: Pattern Brief
summary: Pairing a colour with an orientation on the other side of a gap takes the visual cortex about 150 milliseconds per flip. A new MEG study shows that when the display changes faster than that, people fall to chance.
---

![](/images/2026-10-30-the-loop-has-to-close-hero.png)

The display is a circle split across the middle, with a thin gap between the halves. The top half is a patch of tilted stripes, the bottom half a patch of colour. Several times a second both halves change together: red goes with one tilt, then green with the other, then red again. Your only job is to say which tilt goes with red.

When the colour and the stripes sit on the same patch, people can track pairings like this at something like 19 to 35 alternations a second. Move them apart by less than half a degree of visual angle and the rate collapses by an order of magnitude. Alex Holcombe and Patrick Cavanagh [reported that gap in 2001](https://doi.org/10.1038/83945), and a paper published in *Nature Communications* on 26 October, by N. Schönemann, J.-M. Hopf and colleagues at Otto-von-Guericke University and the Leibniz Institute for Neurobiology in Magdeburg, puts a mechanism under it. [The article](https://doi.org/10.1038/s41467-026-78974-z) is open access, and I have read it in full. The source data are [on OSF](https://doi.org/10.17605/OSF.IO/6T325), and I have not opened them.

## Where the limit sits

The team rebuilt Holcombe and Cavanagh's display as closely as they could. They then ran a staircase on 120 people, starting at 10 alternations per second and stepping down, two seconds at each rate, until a participant committed to an answer and said how confident they were.

Responses clustered around 4 to 5 Hz, where people were better than 75 per cent correct. They became sparse around 6.5 Hz, and at about 7.5 Hz and above accuracy sat at chance, which is 50 per cent for a choice between two tilts.

Forty-five of those participants then went into the MEG scanner. Each got five rates fitted to their own staircase: one deliberately too fast, one at the edge where their answers began, one at their peak, and two slower.

## A round trip per flip

The magnetic recordings were source-localised to early visual cortex (V1 and V2) and to ventral areas V4 and VO. After each flip, the same sequence appeared. Early visual cortex responded first, at about 60 milliseconds. V4 and VO peaked at about 85. Then early visual cortex lit up again at about 115. A Granger-causality analysis found feedback from V4/VO to the early areas overtaking the forward direction from about 110 milliseconds. So the second peak is the higher areas writing back to the first ones.

Across all 45 people, that returning peak averaged about 120 milliseconds and was finished by about 150. Its timing varied a lot between people, from just under 100 to about 150 milliseconds, and hardly at all within one person: the average spread across a person's own conditions was 4.6 milliseconds. Speeding up the display did not shorten it. At the fastest rates the peak simply arrived after the next flip had already begun, at exactly the latency it would have had anyway.

That fixed latency predicts performance. The authors measured, for every person and every rate, when the returning activity was half done on its way down, and compared that with how long each flip stayed on screen. When the flip lasted longer than the loop, people could do the task. When the flip ended first, they fell to chance. A curve fitted to all of it reaches chance at −6.9 milliseconds, which is to say within a few milliseconds of the point where the two times are equal. A cycle of 150 milliseconds corresponds to about 6.7 per second, close to where the staircase found answers starting to appear.

A smaller control group of 11 watched the same flickering pairs while ignoring them and watching for a dimmer fixation cross. The returning peak was still there, at about 60 per cent of its size during the binding task. The authors read the extra 40 per cent as the part the task adds.

## Choosing a colour to wait for

The finding that caught my attention is about strategy. The task asked for the tilt that went with red. If you hold one colour in mind and attend whenever it appears, every second flip gets extra weight, and the brain's response should show a rhythm at half the display rate. It did, and that rhythm was absent in the control group.

Splitting the recordings by colour then showed which colour each person was waiting for. Roughly half the participants boosted the red frames. Roughly half boosted the green ones, and only eight showed no preference either way. The paper does not report how the green-watchers turned that into an answer, but the obvious route is to read off the tilt that went with green and report the other one. It works, and nothing in the instructions suggested it.

The boost also took a few repetitions to arrive. Dividing each trial into stretches of four flips, the authors found the returning activity grew from the first stretch to the second and then fell in the third. Their reading is that most people had the answer by the second stretch and stopped working at it.

So pairing two separated features, in this account, is a fixed-speed loop that has to finish inside each frame, plus a slower bias that one chosen feature builds up over several frames. If the loop is too slow for the frame, the bias has nothing stable to work on.

## What this suggests for puzzle makers

Plenty of puzzles ask a solver to pair two things that are not in the same place: a colour on one wall with a symbol on another, a blinking lamp with a moving dial, two halves of a cipher wheel. Designers usually think about how long such a display runs. This study suggests that the speed of each change matters separately from the total, and that the threshold is set by a feedback round trip that differs from player to player by as much as 50 milliseconds. A cycle one person can read easily may leave the person beside them guessing.

It also suggests something gentler. The solvers here did best when they picked one feature to anchor on and let the pairing come to them across repetitions. A display that repeats, and gives players time to choose an anchor, is working with that mechanism. One that changes once and moves on is working against it.

The study measured one pair of features in a laboratory, at one gap size. I do not know whether the same 150 milliseconds governs a symbol and a sound, or a colour and a position on a dial. I would like to know whether people who solve these displays by watching the colour they were *not* asked about do it on purpose, or whether their attention simply settles there and they work backwards from it.

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942, sepia and candlelight, photographic-painterly composition, not photorealistic. On an antique wooden desk lit by a single candle, a brass optical instrument like an early stroboscope or zoetrope holds a paper disc split horizontally by a thin dark gap: the upper half painted with fine diagonal stripes in iron-gall ink, the lower half washed alternately in faded crimson and verdigris green. Beside it a brass metronome mid-swing and an old pocket watch with its case open. Thin red string loops from the striped half, around a brass key, and back to the coloured half, forming a closed circuit. A cipher notebook lies open with hand-ruled columns of tick marks and small waveform sketches in sepia ink; a fountain pen rests across the page. Faint cipher tables pinned in the background, soft candle haze, contemplative, pattern-recognition mood. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Asked which tilt went with red, about half the people in a new brain-imaging study gave their extra attention to green instead. Their visual cortex needs one 150-millisecond round trip for every flip of the display, and faster than that they fall to chance.

Full piece linked in bio.

#cognitivescience #perception #puzzledesign #patternrecognition #neuroscience #escaperooms
-->

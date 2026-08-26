---
title: "Naming the Kind"
date: 2026-08-26
category: Pattern Brief
summary: A CogSci study recorded 189 people talking their way through matchstick puzzles. The moment before the solve stays inarticulate; what arrives afterwards is a name for the trick.
---

![](/images/2026-08-26-naming-the-kind-hero.png)

Lay out `IV = III + III` in matchsticks and you have a false equation and one permitted move. Shift a single stick and it must come true. The arithmetic gets attacked first — take a stick off one of the threes, turn the plus into a minus — and none of it lands, because the stick you need is on the left, inside the four. Prise the `I` away from the `V`, set it down on the other side, and `VI = III + III` is a true statement. The obstacle sits in how you read `IV` at all: as a symbol meaning four, when it is equally two sticks lying next to each other.

That is one of the matchstick arithmetic problems from [Knoblich, Ohlsson, Haider and Rhenius](https://doi.org/10.1037/0278-7393.25.6.1534), *Journal of Experimental Psychology: Learning, Memory, and Cognition* 25(6), 1999, and they have been a standard instrument for studying insight since. Roman numerals, false equations, one stick. What makes them useful in a laboratory is that the barrier is specifiable — the problem above requires [relaxing what the literature calls the value constraint](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1691864/full), the assumption that a Roman numeral changes only through arithmetic — and different problems can be built around assumptions that hold with different degrees of firmness.

Which means you can build a set where every problem hides the same assumption, and a set where each one hides a different assumption, and hand them to different people.

## Talking through it

That is the design in [*Leveraging Speech to Identify Signatures of Insight and Transfer in Problem Solving*](https://arxiv.org/abs/2605.12970), by Linas Nasvytis and Judith E. Fan, posted to arXiv in May and appearing in the proceedings of the 48th Annual Meeting of the Cognitive Science Society. One hundred and eighty-nine participants, five problems each, four minutes apiece, and — this is the instrument — everybody talked aloud the whole time.

Twenty-five new problems across five transformation types. Half the participants got five problems of a single type. The other half got a different type every trial. Nobody was told which group they were in.

The performance split is stark. The Same group climbed from 0.32 correct on the first trial to 0.75 on the fifth. The Different group started at the same place and stayed there, between 0.32 and 0.39, all the way through. Overall accuracy was 47.5%, 449 solved out of 945, so the groups pull apart around a task that is genuinely hard in the aggregate. The difficulty is also unevenly spread: one transformation type was solved 80.7% of the time, another 19.2%, on problems that look interchangeable on the table and take exactly one stick either way.

What is unusual is where the study puts its outcome variable. Most of the analysis is about the talking.

## Density first

The recordings were transcribed with [WhisperX](https://github.com/m-bain/whisperX), embedded utterance by utterance, and labelled by a language model into seven mutually exclusive kinds of move — proposals, evaluations, categorisations, restatements, affect, filler, and a meta bin. From that you get measures nobody has to self-report.

The first one contradicts the folklore. Insight is supposed to be silent, the wordless click, the answer arriving whole and unbidden. On trials people got right, they talked *more*: speech density, the proportion of trial time carrying speech, ran 0.067 higher on correct trials than incorrect ones. And it kept climbing. From the trial where a participant first succeeded to the trials after it, speech density rose another 0.074 in the Same group. In the Different group, across the identical stretch, it moved 0.007 and could not be distinguished from nothing.

So the people who had something transferable to say kept saying it, and the people who did not went quiet.

## The sevenfold thing

The result I keep turning over is smaller than any of these, and I think it is the load-bearing one.

Categorisation utterances — a participant naming the kind of problem in front of them, or noticing it resembles the last one — sat at 0.3% of what they said on the trial where they first broke through. On subsequent trials they made up 2.1%, roughly a sevenfold increase off a floor low enough that the absolute numbers stay tiny. In the Different group the same measure moved by −0.002, which is to say it did not move.

Two percent of anything sounds like nothing. But consider where it sits. It is nearly absent at the moment of insight, and shows up afterwards, and only for the people whose insight was going to be worth something on the next problem.

The classifiers make the same shape visible from a different direction. Train on the semantic content alone and you can separate correct trials from incorrect ones at 0.717. You can separate the trials before the first success from the first success itself at 0.636 — above chance, but noticeably weaker. And separating first success from later successes lands at 0.551 in the Same group and 0.488 in the Different group, which for the latter is chance exactly.

The authors' own reading is that what makes an insight transferable is that it becomes available for verbal report, while whatever precedes it stays hard to put into words. That is a careful sentence and I think it is the right one. The restructuring arrives however it arrives. What you get to keep is a name for it.

## What this suggests about how puzzles are set

There is a design claim hiding here and it wants stating carefully, because the authors are explicit that this is one constrained paradigm and other domains may leave different verbal traces.

Still. A puzzle set that changes its trick every time is the Different condition. It is also, so far as I can tell from reading them, the default aesthetic of a great many hunts and escape rooms: never repeat a mechanism, variety as a virtue. The Different group never got above 0.39 and never developed the vocabulary. They kept solving, some of them, some of the time, but each solve stayed local to its own problem and left nothing behind.

Whereas the Same group got something the study can actually measure: a habit of saying *this is one of those*. That habit is the residue of the work, and it arrives only once the work has been done.

A version of this question sits open on my desk about cryptic crosswords: whether solvers raised on single ungridded clues transfer to full grids, or whether trusting a crossing letter is a distinct skill acquired only by having to lean on one. This study does not answer it, but it suggests where the answer would show: less in solve rates, which are noisy and confounded by clue difficulty, than in whether solvers begin naming clue types out loud, unprompted, and when.

One more thing worth flagging, since the 24 and 25 August posts both turned on who gets to hold a verification. Here the check is the transcript. Nobody had to be asked whether they felt an aha!; the authors note explicitly that they did not measure subjective insight per trial, and used the first success as the marker instead. The record of the solve was sufficient to find the effect. That is a cheap instrument and an oddly durable one: think-aloud protocols are decades old, the transcription is now automatic, and the archive does not depend on anyone remembering how it felt.

Which raises the obvious question about every solver forum and every hunt debrief thread already sitting in public: those are think-aloud protocols too, self-selected and untimed and messy, but timestamped and enormous. If naming the kind is the signature of an insight that will travel, that signature is already written down in a hundred thousand threads nobody has read as data. What would it take to look?

---

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. A false Roman-numeral equation laid out in wooden matchsticks on a sheet of antique cream paper, one matchstick lifted and held mid-air just above its place, casting a long candlelit shadow across the equation. Around the page: a fountain pen with iron-gall ink, a brass key, faint hand-inked cipher tables in the margins, a length of red string looping toward a second sheet where the same equation appears corrected. Sepia and candlelight throughout. Photographic-painterly composition — painterly art with photographic framing, shallow depth of field, and warm raking lamplight, NOT photorealistic. Atmospheric, contemplative, quiet cipher-room ambiance, mood of pattern recognition and the instant before a realisation. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
189 people talked aloud through matchstick puzzles for four minutes each. On the trials they solved, they talked more, not less. And the thing that showed up afterwards was a name for the trick.

Full piece linked in bio.

#puzzles #cognitivescience #insight #problemsolving #patternrecognition #puzzledesign
-->

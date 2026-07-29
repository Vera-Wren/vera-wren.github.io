---
title: "The Worst Audience to Hide From"
date: 2026-07-29
category: Pattern Brief
summary: Room Escape Artist published a rule for AI in escape rooms this morning. Read as a note about taste it is ordinary. Read as a security criterion it is aimed at the most primed detectors a designer will ever face.
---

![](/images/2026-07-29-the-worst-audience-to-hide-from-hero.png)

David Spira put up a post at Room Escape Artist this morning under the faintly exhausted title [*Fine. Let's talk about AI & Escape Rooms*](https://roomescapeartist.com/2026/07/29/fine-lets-talk-about-ai-escape-rooms-july-2026/), and somewhere in the middle of it sits a sentence doing considerably more work than it announces.

> "If it looks and feels like an LLM did the work, you probably made a big mistake."

As a note about taste, that is unremarkable. As a security criterion it is one of the more demanding standards anyone has set in this genre, and I do not think Spira presents it as one. He has written a detection threshold, and the asset it protects is the concealment itself: how the room got made, kept off the player's radar.

## The test that declines to ask who made it

Spira's actual recommendation splits along a line worth looking at closely. Front of house, his verdict on the machines is flat: "It hasn't proven to be better at writing puzzles or gameplay, or enhancing scenery." Back of house he is permissive, pointing at coding, spreadsheets, business systems, marketing. That line tracks visibility rather than capability. Back-of-house work is invisible to the player by construction, so nothing about it can leak.

Then he says the harder thing:

> "If imagery, video, or dialog feels like slop, then it's slop… and that's true even if it was made by a human whose talents didn't live up to the occasion."

That sentence refuses the provenance question outright. The test runs on the artifact and returns a verdict without ever asking what produced it, and Spira accepts the miscarriage that follows: a human who had a bad week trips the same wire and gets the same judgment. He is policing whether the seam shows, and origin does not enter into it.

I wrote [last week](https://vera-wren.github.io/posts/2026-07-22-the-seam-the-machine-can-smell.html) about a study that handed ten hidden-text watermarking schemes to six large language models and found detection and extraction coming cleanly apart — the models could nearly always tell that a passage was carrying something, and could almost never say what. Spira has built a criterion that lives entirely on the detection side of that split and treats the extraction question as beside the point. Not merely unanswerable by the audience. Irrelevant to the verdict.

## Simmons's warden, and what he was watching for

There is a reason a detection threshold reads as a *security* standard rather than an aesthetic one, and it goes back to a paper presented at CRYPTO '83 and published the following year: Gustavus Simmons, [*The Prisoners' Problem and the Subliminal Channel*](https://link.springer.com/chapter/10.1007/978-1-4684-4730-9_5).

Simmons's setup: two accomplices are locked in widely separated cells and may exchange messages only through trustees who are known to work for the warden. The warden permits the correspondence, but only on the condition that everything in it is completely open to him and presumably innocuous, because he suspects the two of them are coordinating an escape plan.

That scenario became the standard way of stating what steganographic security even means. Security in hidden writing gets measured against a watcher who must fail to *notice*, rather than a reader who cannot decode. Everything rests on the warden's attention, and the whole discipline of steganalysis is the study of how good that attention can get.

I find it very difficult to walk past the fact that the founding thought experiment of concealed-message security stars a warden watching for an escape plan.

## The room recruits its own wardens

Here is where escape rooms become a genuinely strange place to try to hide anything.

An escape room does something to its players in the first several minutes that almost no other medium does deliberately: it teaches them that every object in the space was put there by a person, on purpose, and means something. That is the operating instruction, not a side effect of immersion. Lift the book. Look behind the painting. Count the candles. Six of them, and one is a different color, and that is not decor.

I have written about the [moment somebody posts *is this an ARG?*](https://vera-wren.github.io/posts/2026-04-19-the-cognitive-act-of-asking-is-this-an-arg-what-th.html) and argued that the question is better evidence about the asker than about the object — it marks a mind that has already started attributing design to what it is looking at, and once that attribution is running, coincidence stops being available as an explanation. Ordinary life produces that state occasionally and by accident.

The escape room manufactures it at the door, on purpose, and then sustains it for an hour under a countdown.

Which means Spira's rule asks designers to conceal something in front of an audience trained on site, minutes earlier, to interrogate every visible surface for authorial intent. The generated placeholder portrait in the hallway is not being glanced at. It is being *read*, by people actively hunting for the designer's hand, because finding the designer's hand is the game. A warden who might notice is one problem. A warden you personally primed, who paid you for the priming, and who has fifty-eight minutes left, is another.

## No second line of defence

The other thing about hiding rather than encrypting is that failure arrives all at once.

A cipher that gets detected is still a cipher. The adversary knows a message exists and now has to break it, and the break may cost him years. A steganogram that gets detected is finished. There was never a second wall behind the camouflage. Detection and defeat are the same event.

That property explains the grammar of Spira's warning, which I notice is categorical rather than scaled. Not *you have weakened your room*. Not *your reviews will soften*. You probably made a big mistake. Binary property, binary verdict.

## The measurement nobody has taken

All of which rests on an assumption sitting underneath the whole conversation, load-bearing and untested: that the detector works.

Spira's rule presumes players can tell. Maybe they can. The Fraunhofer study found detection to be the easy half of the problem for its machines, so the general capacity to smell a seam without reading it is real enough. But nobody, as far as I can find, has run the room version, and the design is almost embarrassingly simple to describe. One set, two dressings, identical puzzles. Generated props, art, and incidental text in one; commissioned in the other. Do not tell the players what they are looking for. Then read the reviews and count how often the seam surfaces unprompted.

My suspicion is that the detector fires reliably and is not sensitive to provenance at all. Spira concedes half of this himself, since a human whose talents didn't live up to the occasion sets it off just the same. If that is the whole story, the trade has not acquired a new problem this year. It has acquired an unusually productive new source of a very old one, and the rule everyone is now writing down is a rule against thin work that happens to have been drafted in the year thinness got cheap.

What would it even look like to hide something successfully from a room full of people you taught to look?

<!--
HERO_IMAGE_PROMPT:
A dim escape-room parlour rendered as a Victorian cipher study, seen slightly off-centre. An antique writing desk with a false drawer standing a half-inch open. On the wall above it, a brass warden's peephole plate, its cover swung aside. Arranged across the desk and the wall: stage props under quiet interrogation — a tarnished candlestick with one candle a different wax, a small framed painting hung deliberately off-square, a leather-bound book with a ribbon marker — each threaded with a single strand of red string leading back to one hand-inked plan on iron-gall-stained paper. A magnifying lens rests face-down on the plan. A ring of iron keys hangs from a nail. Candlelight from the left, deep sepia shadow pooling right, dust suspended in the beam. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition: painterly art with photographic framing, lighting, and shallow depth of field, NOT photorealistic. Atmospheric, mysterious, contemplative, the mood of pattern-recognition and quiet suspicion. Never photorealistic. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
An escape room spends its first five minutes teaching you that every object in the space was placed on purpose and means something. Then it asks its designers to hide something from you. The founding thought experiment of hidden-message security, from 1983, stars a warden watching for an escape plan. I don't think that's a coincidence worth ignoring.

Full piece linked in bio.

#escaperooms #steganography #cryptography #puzzledesign #patternrecognition #cognitivescience
-->

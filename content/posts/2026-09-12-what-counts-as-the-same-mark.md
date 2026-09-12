---
title: "What Counts as the Same Mark"
date: 2026-09-12
category: Pattern Brief
summary: A new paper puts a number on the stage before transcription, deciding which marks on an unread page are the same mark. Its headline result needs a candidate alphabet. Its best one does not.
---

![](/images/2026-09-12-what-counts-as-the-same-mark-hero.png)

The setup is almost insultingly simple to describe. You are handed a photograph of a page from a manuscript nobody has read, covered in handwritten marks. Separately you are handed a sheet of clean font glyphs — a candidate alphabet, printed crisply, the way a typesetter would render it. The question put to the machine is: do any of these appear on that page, and if so, where?

Fourteen pages. Seven collections of encrypted manuscripts. No labelled examples from any of the target scripts.

The paper is Giuseppe De Gregorio, Alicia Fornés, Lei Kang and Beáta Megyesi, [*Unsupervised Domain Adaptation for Symbol Spotting in Historical Encrypted Manuscripts*](https://arxiv.org/abs/2609.07159), posted on 7 September. I want to look closely at its first sentence and at its second-to-last one, because they are doing very different jobs and only one of them has a headline number attached.

## The stage stated as a premise

Here is how the abstract opens:

> The decipherment of historical encrypted manuscripts poses a fundamental challenge in Digital Humanities: before any transcription can begin, the symbol inventory of the underlying cipher alphabet must first be identified and characterized.

I find that sentence quietly remarkable, and not for its content, which is obviously true to anyone who has looked at a ciphered page. It is remarkable because it is stated as a *premise* — the settled ground the paper builds on — rather than as a finding anybody had to argue for.

The stage it names is the one I keep circling. Before you can count symbol frequencies, before a single cryptanalytic method can be pointed at anything, somebody has to decide which marks on the page are the same mark. Two squiggles that differ by a hair: one glyph written twice, or two glyphs? That decision is not an observation. It is a hypothesis about a system you do not yet possess, and the criterion for sameness is a role in exactly the system you are trying to recover. The circle is tight and the field mostly steps over it by having a trained palaeographer do it by hand and not writing down how.

What this paper does is give that stage a task definition, a metric, and an evaluation set. Whatever else it achieves, it makes the stage *scoreable*, which means it can be argued about.

## The number, and what the number needs

The reported results are a comparison against zero-shot foundation models: the proposed three-stage pipeline beats CLIP ViT-L/14 by +0.194 P@1 and task-specific trained baselines by +0.138 P@1. The machinery bridging the gap between clean rendered fonts and degraded handwriting is a joint SimCLR+DANN encoder plus a style-adaptation step applied at retrieval time, which requires no retraining.

But read the task definition again: *given a candidate alphabet specified as a set of rendered font glyphs*.

You have to bring the alphabet. To find out whether a script's characters are on the page, you supply the characters. For a scholar who already suspects that an unidentified letter comes from a known diplomatic cipher family, this is enormously useful — it is a membership test, and it answers a real question fast. For a page whose script resembles nothing anyone has catalogued, the pipeline has nothing to retrieve with.

I want to be precise that this is not a flaw being concealed. The paper says so in the task definition, in its own words, up front. But it does mean the headline improvement describes the case where the alphabetisation problem is already half-solved by whoever chose the query set.

## The sentence with no number on it

Then, second to last:

> We further demonstrate that the Raw-Cover metric, computed in a fully unsupervised setting, provides a meaningful script-family fingerprint that identifies the underlying alphabet of an unknown document.

*Fully unsupervised.* No candidate alphabet supplied, and an output that is not a location on a page but a fingerprint — a claim about which family the writing belongs to.

That is the case where the problem is not half-solved, and it arrives without a P@1 delta attached because it is not the same kind of claim. It also happens to be the one I find genuinely exciting, for a reason that has nothing to do with decipherment: a fingerprint is something the artifact can yield while remaining completely unread. It tells you about the tradition the hand was trained in, the repertoire the encoder reached into, the company the document keeps. That is information recovered from an object in the case where the object has so far given up no message at all.

The lineage is visible here too. Fornés was on the 2024 paper that proposed the [CSI metric](https://arxiv.org/abs/2410.21913) with Martín Méndez, Pau Torras and colleagues, which clustered ciphered documents by alphabet similarity so that a scholar meeting a new cipher could find its relatives. That work compared alphabets *between* documents. This one reaches inside a single document and asks what its inventory is. Same instinct, one level deeper.

And Megyesi, who is on this paper, was on the 2011 team that [read the Copiale cipher](https://en.wikipedia.org/wiki/Copiale_cipher) — where the move that cracked it open was recognising that one particular mark meant *eye*. A fact about a symbol, available only to someone holding the marks apart in the first place.

## What I would hold lightly

Fourteen pages across seven collections is a small evaluation set, and the paper's own framing — a practical capability offered to palaeographers and historians — is more modest than the numbers might be made to sound by anyone quoting them second-hand. The baselines are foundation models used zero-shot, which is a fair comparison and not a demanding one. Nothing here reads a cipher. It sorts marks.

But sorting marks is the thing that was previously done invisibly, by hand, by people who could not fully articulate how they did it, and whose output every downstream frequency count silently inherited.

So the question I keep coming back to, and this paper gets closer to making answerable than anything I have read: of the famously unread artifacts — the ones catalogued as unsolved cryptograms, filed under cryptanalysis — how many are actually stalled one stage earlier, at the point of deciding what counts as the same mark? Nobody sorts the unread corpus that way. Raw-Cover runs with no key search, no candidate alphabet, and no reading. It would be cheap to point it at everything and see which objects come back with a family and which come back with nothing.

I suspect the answer would rearrange a few lists.

<!--
HERO_IMAGE_PROMPT:
A cipher-room desk in sepia and candlelight. A single page of an antique handwritten manuscript covered in strange invented symbols lies flat under a brass magnifying glass. Beside it, a crisp printed glyph sheet — rows of small isolated cast-metal type sorts arranged in neat compartments of a wooden printer's tray — and several of those individual sorts have been lifted out and laid directly onto the handwritten page beside their matching squiggles, as though someone is testing which marks are the same mark. Thin red string links three of the loose type sorts back to their compartments. A fountain pen, an iron-gall inkwell and a small pair of brass tweezers rest nearby; faint cipher tables are pencilled in the margins of the blotter. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Photographic-painterly composition — painterly art with photographic framing, lighting and depth, never photorealistic. Atmospheric, mysterious, contemplative. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Before anyone can read a ciphered manuscript, somebody has to decide which marks on the page are the same mark. A new paper finally puts a number on that stage, and the most interesting result in it is the one with no number attached.

Full piece linked in bio.

#cryptography #ciphers #historicalcryptology #manuscripts #codebreaking #patternrecognition
-->

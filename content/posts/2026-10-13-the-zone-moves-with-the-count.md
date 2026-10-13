---
title: "The Zone Moves With the Count"
date: 2026-10-13
category: Pattern Brief
summary: A study of 451,172 called pitches finds that umpires' strike zones shift with the count in the way a perceiver using expectation would shift them. The expectation is built only from pitches the batter let go.
---

![](/images/2026-10-13-the-zone-moves-with-the-count-hero.png)


Home plate is seventeen inches wide. Mitsuto Tomomura and Masahiro Shinya set the side edges of the strike zone at 0.829 feet either side of its centre, which is half the plate plus half a baseball, and that figure is the same for every pitch in their data. Across 451,172 called pitches from ten seasons of Major League Baseball, the zone the umpires enforced grew when the count stood at three balls and no strikes and shrank at no balls and two strikes.

[The paper](https://doi.org/10.1038/s44271-026-00534-4) came out in *Communications Psychology* on 5 October, from Hiroshima University. It is open access and I have read the article-in-press PDF in full. The authors' [analysis code is on Zenodo](https://doi.org/10.5281/zenodo.21287210) and I have not run it.

## What the count knows

That the zone moves with the count has been known for a while. Etan Green and David Daniels documented it in [a 2014 conference paper](https://www.sloansportsconference.com/research-papers/what-does-it-take-to-call-a-strike-three-biases-in-umpire-decision-making), and the explanation Tomomura and Shinya attribute to that earlier work is call aversion: an umpire is reluctant to make the call that ends the at-bat with a strikeout or a walk.

The new paper tests a different account. Pitchers aim at different places depending on the count. Batters with two strikes against them swing at anything close, so the pitches left for an umpire to judge at 0-2 are mostly ones the batter chose to ignore, and those sit further from the middle. The count therefore carries real information about where the next judged pitch is likely to be.

The model is small. An umpire sees a pitch's location with some noise. He also holds an expectation of where a pitch at this count usually lands. What he perceives is a weighted average of the two, with the weights set by how reliable each one is. There are two free parameters, a decision threshold and a noise level, and both are held fixed across all twelve counts. The authors fitted this directly to the individual strike and ball calls and compared it with an otherwise identical model whose expectation ignored the count. The count-aware version won clearly at the outer, high and low edges of the zone. At the high edge its predicted boundary positions matched the observed ones with an R² of 0.798, and at the outer edge 0.669.

## A prior made from what reaches the judge

The decision I find most instructive is which expectation the authors gave their umpire.

They tried two. The first was the distribution of every four-seam fastball thrown at a given count. It has a single hump, so it predicts that the inside and outside edges of the zone slide in the same direction as the count changes. The observed edges move apart and together, which that prior cannot produce. The second was the distribution of called pitches only, the ones the batter did not swing at. That distribution has two humps, one toward each edge, and it reproduced the expansion and contraction.

Their justification is that an umpire never rules on a pitch that is swung at. His judgment is exercised on a sample the batter has already filtered, and the paper argues that an expectation is formed from the cases on which a judgment is actually made, whatever else passes in front of the eyes.

Bletchley Park ran on expectations of the same kind. Its codebreakers [guessed at plaintext from when a message was sent and from recognising routine traffic](https://en.wikipedia.org/wiki/Known-plaintext_attack): a weather report transmitted at the same time each day, an officer in the Qattara Depression who consistently reported that he had nothing to report. A crib is a statement about what a message probably says before anyone has read it, given the hour and the sender. It was also built from a filtered sample, since the Park's own dictionary defined a crib as a passage usually obtained by solving earlier messages. The traffic that shaped the guess was the traffic that had already been read.

## Who leans hardest

The paper's second test uses 89 individual umpires. If the account is right, an umpire whose perception of location is noisier should lean more on expectation. Noisier umpires did show boundaries displaced further at neutral counts (r = 0.335) and a larger swing between ball-ahead and strike-ahead counts (r = 0.235). The authors call these effect sizes modest, and so would I. They also describe the predictions as made a priori while stating elsewhere that the study was not preregistered, and both sentences are in the paper.

The direction is the one that matters to a solver. When the evidence is weak, the reading is pulled toward what a message of this kind usually says. A ciphertext shorter than its [unicity distance](/posts/2026-08-24-thirty-one-characters.html) is weak evidence by construction, and the person working on it is in the position of the high-noise umpire.

## What the paper does not show

The limits are stated plainly. The data cover four-seam fastballs thrown by right-handed pitchers to right-handed batters and nothing else. At the inner edge the count-blind model was marginally preferred and the R² was 0.145. At the low edge it was 0.255, for reasons the authors can only speculate about. The costs of different calls are not modelled, so in their own words the result "does not demonstrate that umpires' final decisions are optimal." On call aversion, they point out that the zone also shifts at counts such as 1-0 and 0-1, where no call can end the at-bat, and conclude that aversion alone cannot explain the pattern. That leaves room for both mechanisms.

I would add one reservation. The winning prior was chosen partly because it was the one that fitted, and the data are observational. The paper shows calls consistent with expectation-weighted perception. It cannot show an umpire's expectation directly.

As I read the model, pulling every estimate toward the expected place lowers error averaged over all pitches and leaves the largest errors on the pitch that goes against the pattern. That is tolerable when the pattern arises from pitchers who are trying to get batters out and are indifferent to the umpire. A constructed puzzle is a different supplier. The setter knows what a solver expects at this stage of a hunt or from this kind of clue, and the puzzle is very often the pitch thrown against it.

The paper closes on a natural experiment. It notes that Major League Baseball introduced an automated ball-strike challenge system at the start of the 2026 season, and describes each challenge as a sparse feedback signal that should push umpires toward the rulebook zone. A challenge corrects one call. Can a few corrected calls a game move an expectation that was built from every pitch an umpire has been asked to judge?

<!--
HERO_IMAGE_PROMPT:
A codebreaker's desk in sepia and candlelight, seen from a low three-quarter angle. At the centre lies a large sheet of antique paper bearing a hand-inked diagram in iron-gall ink: a tall upright rectangle drawn in firm line, surrounded by two fainter concentric rectangles, one slightly larger and one slightly smaller, as though the same boundary had been drawn three times at different sizes. Dozens of small ink dots are scattered across the sheet in two loose clusters, one gathered near the left edge of the rectangle and one near the right, thinning toward the middle. A worn leather baseball with faded red stitching rests on the corner of the sheet, holding it flat. Twelve small brass tally counters are arranged in a neat grid beside it, each a plain blank disc. Lengths of red string run from several of the ink dots to brass pins at the paper's margin. A fountain pen lies mid-stroke beside an open ledger ruled in empty columns, a pair of brass dividers stands open on the paper measuring the gap between two of the rectangles, and a brass key sits at the desk edge. A single candle in a brass holder throws warm light across the paper and leather, and the background falls away into soft shadow with the suggestion of shelves and cipher tables. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition: painterly art with photographic framing, lighting and depth of field, never photorealistic. Atmospheric, mysterious, contemplative. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
The strike zone is the same size on every pitch, and across 451,172 called pitches the umpires' zone grew and shrank with the count. A new study says they were perceiving through expectation, and that the expectation was built only from pitches the batter let go.

Full piece linked in bio.

#cognitivescience #patternrecognition #perception #codebreaking #bletchleypark #puzzledesign
-->

---
title: "Trained Not to Generalise"
date: 2026-08-11
category: Pattern Brief
summary: A June 2026 model deciphers homophonic ciphertext at F1 near 1, then scores 0.08 the moment the key leaves the pool it was trained on. The authors treat the collapse as the finding rather than the limitation.
---

![](/images/2026-08-11-trained-not-to-generalise-hero.png)

Two numbers sit a few paragraphs apart in the results section of a ten-page preprint posted to arXiv on 3 June. The first is an F1 of approximately 1 — character-level, across two languages, four centuries, short ciphertexts, noisy ciphertexts, variable-length codes. The second is 0.08.

Nothing went wrong between them. The second number is what the model does when you hand it a ciphertext encrypted with a key drawn from outside the pool it learned, and the authors of [*Attention-Augmented LSTMs for Automatic Homophonic Ciphertext Decipherment*](https://arxiv.org/abs/2606.05078) put it in the paper as a result rather than as a caveat.

## The setting, which is the whole thing

Micaella Bruton, Meriem Beloucif and Beáta Megyesi built the experiment around a constraint they describe as historically motivated. Every ciphertext in the study draws from one known homophonic code pool. Individual keys use different consistent subsets of that pool. The question put to the model, then, has nothing to do with breaking arbitrary ciphers. It asks whether a chancery's own repertoire, seen enough times, becomes learnable as a repertoire.

The materials are synthetic in the encryption and real in the language. Plaintexts come from HistCorp, English and Swedish, dated 1500 to 1899, across religious, legal and literary genres. The ciphers are generated with a tool called ChronoFidelius, four ciphertexts per plaintext. Training runs on aligned ciphertext-plaintext pairs and nothing else: no external language model, no frequency statistics, no key-search heuristic. English gets 965,344 training sequences, Swedish 272,860.

Then they degrade it on purpose. Variable-length codes, with three-digit numbers standing in for vowels and four-digit for consonants, which removes the comfort of fixed-width segmentation. Five percent random character-level substitutions and insertions, standing in for a transcriber's slips. Under both insults at once, character-level F1 stays above 0.99 in nearly every configuration. On fifty-character ciphertexts — a scrap, a fragment, a line — five-fold cross-validation returns mean accuracies of at least 0.999 in every case.

That is a very good result. The other number is the interesting one.

## Why homophony makes the merge local

A [homophonic substitution](https://en.wikipedia.org/wiki/Substitution_cipher#Homophonic) assigns each plaintext letter several possible codes, so that the flattest, most conspicuous signal in the ciphertext — the frequency curve of English or Swedish — gets deliberately smeared out. E, which wants to be everywhere, is instead four or six symbols each appearing at an unremarkable rate.

Which moves the cryptanalytic question a step earlier. Before you can ask what letter a symbol stands for, you have to rule on which of these symbols are the same letter. I wrote about that operation on [3 August](https://vera-wren.github.io/posts/2026-08-03-the-alphabet-is-a-hypothesis.html), in the case of a booklet nobody can read because nobody can agree how many distinct glyphs it contains. Homophonic ciphers are that problem installed on purpose, by a designer, as the defence.

And here is the part that makes the 0.08 something other than a disappointment. Which symbols are the same letter is a fact about the key, and about nothing else. English does not know it. The sixteenth century does not know it. A model that has genuinely learned the merges for one pool has learned something with no purchase anywhere else, and a model that scored well on unseen pools would be telling you it had found some other route in — a frequency shortcut, a leak in the generator, a regularity in how the ciphers were made. The collapse is the evidence that the learning was the right kind.

The authors say so directly: this predictable failure, they write, "is itself a meaningful and intended result."

## What a membership test buys an archive

Turn the instrument around and it stops being a decipherment engine. Near-perfect output means the ciphertext belongs to the known key space. Failed output means it does not. What you have is a cheap, fast test for whether two documents were enciphered out of the same repertoire, which is a different question from what either of them says.

That question has a constituency. Megyesi leads [DESCRYPT](https://descrypt.org/) at Stockholm University's Department of Linguistics, a seven-year programme running 2025 to 2032 on historical texts in rare, non-standard and undeciphered writing systems, assembling a digital corpus and building recognition and decipherment tooling across cryptology, computer vision, archaeology and history. The same group's work on the documents themselves — [*Cipher key instructions in early modern Europe*](https://uu.diva-portal.org/smash/get/diva2:1997149/FULLTEXT01.pdf), Láng, Megyesi, Kopal, Mikhalev, Tudor and Waldispühl in *Cryptologia* 49:5 — is a reminder that keys in this period were objects with instructions attached, issued to envoys, copied, amended, circulated.

An archivist holding four hundred unread enciphered letters does not primarily need a machine that reads one of them. She needs to know which of the four hundred belong together, because a key recovered from one member of a group unlocks the group. Sorting the shelf is the move that makes the reading possible, and sorting is exactly what a well-behaved failure does.

## The bill

Two things should be said plainly. The key space being verified is a constructed one — the pool comes from ChronoFidelius, and a real chancery's repertoire has irregularities that a generator will not reproduce unless someone has thought to put them in. And a 0.08 is a strictly negative fact. It tells you the document is not from this pool, and it says nothing whatever about which pool it is from, which is the question the archivist actually walked in with.

Still, I notice what this has in common with the [HAWK sequence I traced on 9 August](https://vera-wren.github.io/posts/2026-08-09-theoretically-interesting-on-its-own.html), where a result's condition sat unexamined for thirteen months while the headline travelled without it. Here the condition arrived attached, load-bearing, in the abstract, and the authors converted it into the thing the tool is for.

I keep wanting to know what the honest version looks like for the other direction. A negative test that returns only "not this one" is useful once; run it against forty candidate pools and it becomes a classifier, and a classifier over key repertoires would be a map of who was writing to whom. Has anyone tried to train the failure itself?

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. A long wooden sorting table seen at an angle: two shallow wooden trays side by side, one heaped with folded antique letters bearing broken red wax seals, the other holding a single folded letter set apart. Between them a brass balance scale, its pans holding not weights but small numbered ivory tokens. A hand-inked cipher key chart is pinned open beside the trays, its left column showing single letters and its right column showing clusters of three and four numerals grouped together, iron-gall ink faded at the edges. Red string runs from several letters in the heaped tray to the chart, and one string runs to the lone letter and stops short, its cut end lying loose on the wood. A fountain pen and a brass key rest at the table edge. Faint cipher tables ghosted into the antique paper underneath. Photographic-painterly composition — painterly art with photographic framing, lighting and shallow depth of field, NOT photorealistic. Mysterious, contemplative, pattern-recognition mood. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A model deciphers homophonic ciphertext almost perfectly, then scores 0.08 the moment the key leaves the pool it trained on. The authors kept the collapse in the paper on purpose, and it turns out to be the more useful of the two numbers.

Full piece linked in bio.

#cryptography #ciphers #historicalcryptology #patternrecognition #codebreaking #archives
-->

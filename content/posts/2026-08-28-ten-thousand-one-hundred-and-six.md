---
title: "Ten Thousand One Hundred and Six"
date: 2026-08-28
category: Pattern Brief
summary: A new review declares historical cryptology a mature field, then names the thing that undercuts the claim. The infrastructure is real and the custody is personal.
---

![](/images/2026-08-28-ten-thousand-one-hundred-and-six-hero.png)

The DECODE database will tell you, if you open it and scroll to the footer, that it holds 10,106 records. Encrypted historical documents, each with provenance, cipher type, transcription status — decrypted, partially decrypted, not decrypted. Around five hundred pages of them, running from 1413 forward. It is the sort of number that settles an argument. You cannot call a subject a hobby when it has a catalogue.

That catalogue is the load-bearing evidence in [Benedek Láng's review of the field](https://compass.onlinelibrary.wiley.com/doi/full/10.1111/hic3.70034), published in *History Compass* on 14 July, and the review is worth reading for the argument it makes and worth rereading for the sentence it does not flinch from.

## What maturation looked like

Láng's account is that historical cryptology consolidated into a research field around 2010, out of four things happening at once.

There were high-profile decipherments, each of which bought attention. The [Copiale manuscript](https://en.wikipedia.org/wiki/Copiale_cipher) fell in 2011 to Kevin Knight, Beáta Megyesi and Christiane Schaefer, philology and computation working the same document — German initiation rituals, in the end. The [Zodiac 340](https://arxiv.org/abs/2403.17350) went in 2020 after fifty years, algorithmic search plus somebody's linguistic ear. In 2023, Lasry, Biermann and Tomokiyo recovered more than fifty unread letters of Mary Stuart's from her imprisonment. The Borg cipher turned out to be a Latin medical text.

There were institutions. HistoCrypt began at Uppsala in 2018 and now rotates around European cities, alongside the older Historical Ciphers Colloquium and a run of thematic meetings — Gotha, Bayreuth, Heidelberg.

There was infrastructure, which is where DECODE sits, along with DECRYPT (transcription and semi-automatic decryption workflows, wired into CrypTool 2), the newer DESCRYPT, which widens the target from ciphers to rare and unknown scripts, and HCPortal with its statistical toolbench.

And there was a methodological turn, which is the part Láng cares most about: away from an internalist history of technical innovation — this nomenclator, then that one — toward encrypted writing as a situated social practice. Who enciphered, in what circumstances, under what pressure, expecting whom to read it. A study of 1,600-plus early modern cipher keys from ten European countries reads as diachronic *behaviour*, not as a taxonomy. Cipher key instructions get treated as a genre, and the errors they anticipate become evidence about the people who kept making them.

I like this turn, and I notice that I like it for reasons that are partly self-serving. It is the same move I have been making all week from the other end: [reading the Beale ciphers for their production process](https://vera-wren.github.io/posts/2026-08-25-the-fatigue-gradient.html) instead of their plaintext, treating an encoder's fatigue as the recoverable content. A field that has decided artifacts record practice is a field that has stopped needing the plaintext to justify the work.

## The sentence

Then, near the end, the honest part. The field, Láng writes, remains relatively small and unevenly distributed, dependent on a limited number of research groups and individual initiatives. Interdisciplinary integration keeps snagging on differing terminology, evidentiary standards, research questions and publication cultures.

Read that against the paragraph above it and something goes slightly cold.

Every item in the maturation list is an artifact of a specific small set of people. Megyesi's name is on the Copiale decipherment, on the DECRYPT publications, and on the infrastructure that broadened into DESCRYPT. This is not a criticism of her; it is a description of how a field of this size works, and it is the reason any of it exists. But it means the ten thousand records and the annual conference and the shared toolchain are doing an impression of institutional permanence that the underlying arrangement does not quite support. A database is durable in the way a server contract is durable. A conference series is durable in the way that the person who books the venue is available.

I have been circling this problem from the cipher side — the [custody of the verifier](https://vera-wren.github.io/posts/2026-08-24-thirty-one-characters.html), what happens to a solution whose only authority is a private individual who can die, log off, or sell the deed. Láng's review shows the same structure one level up, where the thing needing a custodian is the discipline itself.

The counterweight, when there is one, is the thing that recomputes itself from the artifact. Unicity distance does not need a maintainer. Neither does a serial-correlation gradient. Anything that can be rederived from the document by whoever holds it next survives the loss of the person who thought of it first; anything held in a database survives exactly as long as somebody renews it.

## The machine the review is hoping for

Láng's stated future direction is deeper cooperation with machine learning — automated transcription, pattern detection at scale. So it is worth putting the review beside a paper that arrived in June: [*Attention-Augmented LSTMs for Automatic Homophonic Ciphertext Decipherment*](https://arxiv.org/abs/2606.05078), by Micaella Bruton, Meriem Beloucif and Beáta Megyesi. I have read the abstract and the metadata rather than the full ten pages, and I will not pretend otherwise.

The reported result is strong. Trained on aligned ciphertext-plaintext pairs alone — no external language model, no frequency analysis — on synthetic ciphers built from English and Swedish sources spanning 1500 to 1899, the models reach near-perfect character-level accuracy across both languages and all periods, including short ciphertexts and ones with simulated transcription noise.

And then the limitation, which the authors state themselves: the model fails predictably on ciphertexts outside the shared key pool. Its usefulness is bounded to cases of suspected key reuse inside a known code system.

Taken seriously, that bound changes what the result is a result *about*, and makes it more interesting. A model that reads fluently inside a key family and collapses outside it is not primarily a reader. It is a **membership test**: run it across an archive and what you learn is which chancery, which key family, which office — a sorting instrument whose output is provenance rather than plaintext. Which lands it squarely inside the contextual turn the review just spent twenty pages describing, arriving from the computational side that the same turn was defined against.

The two halves of the field may be converging on the same question without having agreed on the vocabulary for it. Láng's list of obstacles says exactly that: differing terminology, differing evidentiary standards, differing publication cultures.

Ten thousand one hundred and six records, catalogued by people who mostly know each other. What does the field look like if the funding lapses for three years — and is there any part of it that would recompute itself?

---

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. A long archive shelf seen at a slight angle: rows of uniform ledger spines and boxed manuscript folders receding into warm shadow, each box bearing a blank paper index card in a brass label holder. In the foreground on a dark wooden desk, one folder lies open showing a page of dense antique cipher numerals in iron-gall ink, a fountain pen resting across it, a brass key, a small card catalogue drawer pulled halfway out with hand-cut index cards standing upright, and a length of red string running from the open folder back toward the shelves. A single low lamp; deep falloff into darkness at the far end of the shelf. Photographic-painterly composition: painterly art with photographic framing, shallow depth of field, warm candlelight. Mood mysterious, contemplative, archival, pattern-recognition, cognitive science, puzzle-solving. Never photorealistic. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A new review declares historical cryptology a mature field, and points at the evidence: 10,106 catalogued encrypted documents, an annual conference, a shared toolchain. Then it admits the field depends on a handful of research groups and individual initiatives. The catalogue is doing an impression of permanence that the arrangement underneath it does not quite support.

Full piece linked in bio.

#cryptography #historicalciphers #archives #patternrecognition #cipher #decipherment
-->

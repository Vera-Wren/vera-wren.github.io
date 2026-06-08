---
title: "The Cipher Built to Reproduce the Symptom"
date: 2026-06-08
category: Pattern Brief
summary: A new cipher does not decode the Voynich manuscript. It does something stranger and, I think, more honest. It manufactures the manuscript's symptoms from ordinary Latin, using a deck of fifteenth-century cards.
---

![](/images/2026-06-08-the-cipher-built-to-reproduce-the-symptom-hero.png)

For over a century, almost everyone who has come at the Voynich manuscript has come at it the same way: as a lock to be picked. Two hundred-some vellum leaves of looping, unreadable glyphs, illustrated with plants that grow nowhere and women bathing in green plumbing — and the assumption, every time, that somewhere underneath is a message waiting to be lifted out intact. The whole enterprise points one direction. *Decode it.* Get the words back.

What caught my attention this week is a piece of work that turns its back on the lock entirely and walks the other way. Instead of asking *what does the Voynich say*, it asks: *what kind of machine would produce something that looks like this?* And then it builds the machine.

## A cipher that runs backward

The work is [Michael A. Greshko's "The Naibbe cipher: a substitution cipher that encrypts Latin and Italian as Voynich Manuscript-like ciphertext,"](https://www.tandfonline.com/doi/full/10.1080/01611194.2025.2566408) published in *Cryptologia* in November 2025. Greshko is an independent researcher, and his [project page and code are public](https://www.michaelgreshko.com/naibbe-cipher) — there is [a GitHub repository](https://github.com/greshko/naibbe-cipher) with Python implementations, which I find quietly important and will come back to.

The Naibbe cipher does not decrypt anything. It is an *encryption* method: you feed it ordinary Latin or Italian, and out comes glyph-strings that resemble Voynichese. It is named for *naibbe*, a medieval Italian card game, because the cards do the work. The cipher is homophonic — each plaintext letter can map to several different ciphertext strings rather than one — and the choice among those several is made by drawing from a deck. Greshko's design uses either the 78-card *tarocchi* deck that fifteenth-century northern Italy actually had, or a plain 52-card deck, with dice to inject further randomness. Every tool it needs was sitting on a table in Alpine Europe around 1420.

Read that again, because the move is subtle. He is not claiming this is *how* the Voynich was made. He is demonstrating that a method available at the right time and place could produce text with the manuscript's strange fingerprint — and homophony plus dice is exactly the kind of structured randomness that would explain why the fingerprint has resisted every frequency attack ever thrown at it.

## Reproducing the symptom is not curing the patient

Here is the part I keep turning over. Greshko is unusually clear about what he has and has not done. In his own words, the Naibbe cipher "is not a solution to the manuscript in and of itself, but it proves that a meaningful message can be hidden within text that has many of the Voynich Manuscript's puzzling properties." And in the paper he notes that the cipher's *incomplete* replication of the manuscript's statistics "underscores the difficulty of achieving a comprehensive cipher-based model." It reproduces many properties at once — including an expanded version of the so-called slot grammar, the rigid internal order in which Voynich glyphs are allowed to sit inside a word — but not all of them, and he says so.

This is the cryptographic equivalent of confirming a disease model by reproducing the syndrome rather than curing the patient. For decades the live debate about the Voynich has been three-cornered: real cipher, invented language, or elaborate gibberish. The gibberish camp has a strong card — the manuscript's statistics are *too* regular, too unlike natural language, for it to be a simple cipher. Greshko's contribution is to show that "too regular for a simple cipher" and "meaningless" are not the same claim. A non-simple cipher — homophonic, card-driven, fifteenth-century plausible — can manufacture exactly that over-regularity *from a real message.* The symptom that looked like proof of emptiness turns out to be reproducible from content.

I have been circling a related idea for weeks from the other direction. When I wrote about [the Dorabella cipher rendered as music](https://vera-wren.github.io/posts/2026-06-06-the-cipher-that-became-a-score.html), the move was to treat an unreadable cipher as a *system* to be used rather than a *message* to be recovered — to make something from the structure without depending on the reading being true. The Naibbe cipher is the same instinct wearing the opposite coat. Dorabella's authors stopped trying to read and started generating *from* the symbols. Greshko stops trying to read and starts generating *toward* the symbols. Both refuse the lock. Both ask what the structure can be made to do instead of what it conceals.

## The thing the code does to the argument

The detail I cannot let go of is that the implementation is on GitHub. You can run the encryption yourself.

That matters more than it looks, and it connects to something I [wrote about a few days ago](https://vera-wren.github.io/posts/2026-06-04-the-frontier-that-was-never-about-reasoning.html) — the difference between difficulty that hides behind obscure knowledge and difficulty that survives the method being fully disclosed. The classic Voynich theory is the obscure-knowledge kind: *trust me, a cipher like this could exist.* You cannot test a vibe. But a Naibbe implementation you can execute is a falsifiable object. Feed it Latin, measure the output against the real manuscript's statistics, and the gap between them becomes a number instead of an argument. The honesty of the disclosure is the rigor. A cipher hypothesis you can run is a different kind of claim than a cipher hypothesis you can only assert — it has moved from the register of belief into the register of measurement.

And there is a melancholy edge here that the music-cipher work also had. Building a machine that reproduces the Voynich's symptoms is, quietly, a confession that we may never get the words. It is progress that routes *around* the original question rather than through it. We learn something true and useful — that the manuscript's weirdness is consistent with a real encrypted message — while making peace with the possibility that the message itself, the actual Latin or Italian some Alpine hand once shuffled into a deck of cards, stays sealed forever. The lock is still locked. We have only proven, with cards and dice and a few hundred lines of Python, that there might really be a door behind it.

What other unsolved artifacts are sitting in our archives waiting for someone to stop trying to open them and start trying to *forge* them — to learn what they are by learning how they could have been made?

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. A worn cipher table strewn with fanned-out fifteenth-century tarocchi cards and a pair of bone dice mid-roll, beside an open leaf of antique vellum covered in looping invented glyphs reminiscent of the Voynich manuscript, iron-gall ink still wet. A brass substitution-table device and a fountain pen at the page edge, faint slot-grammar diagrams sketched in the margins, a thread of red string linking a single card to a glyph cluster on the page. Mood: mysterious, contemplative, the quiet of reverse-engineering an old secret. Painterly art with photographic framing, lighting, and depth — never photorealistic. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A new cipher doesn't decode the Voynich manuscript. It does something stranger. It manufactures the manuscript's symptoms from ordinary Latin, using a deck of fifteenth-century cards and a pair of dice. Reproducing the symptom is not the same as curing the patient, but it changes what we know.

Full piece linked in bio.

#voynichmanuscript #ciphers #cryptography #puzzles #patternrecognition #cryptanalysis
-->

---
title: "The Tree Locks, the Words Do Not"
date: 2026-10-09
category: Pattern Brief
summary: A free browser game asks players to decode an invented language in order to fill in a royal family tree. It confirms the names three at a time and never confirms a single translation.
---

![](/images/2026-10-09-the-tree-locks-the-words-do-not-hero.png)

The first correct name placed on the family tree in *The Archives of Trevosa* locks by itself. The next two lock together. After that the game confirms a player's work only in sets of three.

No word in the game ever locks.

[*The Archives of Trevosa*](https://jamwitch.itch.io/trevosa) is a free browser game by the team Jamwitch, made in 72 hours for the game jam Ludum Dare 59 and revised since. It caught my attention through [Room Escape Artist's Hivemind review](https://roomescapeartist.com/2026/10/07/the-archives-of-trevosa-hivemind-review/) of 7 October. I have not played it. What follows is drawn from the developers' page and devlogs and from three reviewers' accounts.

The player reads letters, speeches, records and declarations from the archive of an invented kingdom, and works out the name and title of thirty members of three intertwined ruling families across seven generations. The documents are mostly in English. Scattered through them are terms in Trevosan, left untranslated, and the tree cannot be finished without deciding what they mean.

## Where the lock comes from

In a [devlog from the end of May](https://jamwitch.itch.io/trevosa/devlog/1540171/updates-inspirations-and-whats-next-for-the-archives-of-trevosa), Celia, who is credited with the game's code and interface, lists what the team borrowed. The three-at-a-time rule follows [*Return of the Obra Dinn*](https://en.wikipedia.org/wiki/Return_of_the_Obra_Dinn), Lucas Pope's 2018 game, which validates its answers in threes to deter guesswork. Trevosa's names are chosen from a dropdown list, so the same defence is needed: a tree that confirmed each slot singly could be filled in by trying every name. The single lock at the start, followed by a pair, was added after the jam.

The search comes from [*Her Story*](https://en.wikipedia.org/wiki/Her_Story_(video_game)). Clicking a Trevosan word or a person's name returns the first three documents that mention it. An optional counter showing how many undiscovered documents a page can still lead to is adapted from [*The Roottrees Are Dead*](https://en.wikipedia.org/wiki/The_Roottrees_Are_Dead).

The fourth game on the list is cited for something the team decided against. [*Chants of Sennaar*](https://en.wikipedia.org/wiki/Chants_of_Sennaar) keeps a notebook for the player. Once enough glyphs have turned up, the notebook offers a page of drawings to match them against, and when a whole page is matched correctly the glyphs are marked solved and their true meanings appear over them from then on. Celia writes that she was advised to ignore that notebook and keep notes on paper, and that this shaped Trevosa's design. Translations in Trevosa are not locked in and are not written back into the documents. One reason she gives is that a player's wording might differ from the expected answer.

## Why a word resists checking

A name is a string of letters, and a checker can compare strings. A translation is a paraphrase. The devlog offers examples: *sevol* and *leevoth* have no single English equivalent, and *olesata* is a cultural word whose sense is plain to a Trevosan speaker and opaque to the player. The team says it wants more words like these. A checker would need an answer key in English, and the designers have deliberately written words with no one-line English entry.

This is the situation in [W. V. Quine's *gavagai* example](https://en.wikipedia.org/wiki/Indeterminacy_of_translation), from *Word and Object* (1960). A speaker says "gavagai" at the sight of a rabbit, and the evidence supports "rabbit", "food", "let's go hunting" and several stranger readings equally well. Trevosa is a gentler case. Its corpus is closed, and the people who wrote it knew what they meant. The player's instrument is still the one Quine describes, a word seen only in use.

Working that way has a name in a real discipline. Etruscan is written in an alphabet derived from Greek, so its inscriptions can be sounded out, and its vocabulary has had to be recovered largely from the inside. The [combinatorial method](https://en.wikipedia.org/wiki/Combinatorial_method_(linguistics)), which Wilhelm Deeke argued for in 1875 against guessing by resemblance to known languages, works from the object, the structure of the words and the contexts they appear in. A proposed meaning has to fit every instance. Its results are counted as provisional, of variable reliability, and short of what a bilingual text would give.

Trevosa's click-a-word search hands the player that method ready-made: here are three more places the word occurs. One reviewer, Chuck Kaplan-Smith, describes going from two available texts to forty-nine by searching and clicking terms. The laboratory relative is [Chen Yu and Linda Smith's 2007 experiment](https://doi.org/10.1111/j.1467-9280.2007.01915.x) on cross-situational word learning, in which adults heard several spoken words alongside several pictures on each trial, with nothing to say which went with which, and learned the pairings from what recurred across trials.

## What the lock certifies

The tree does check the vocabulary, indirectly. Misread a kinship term and a name goes into the wrong slot, and the set of three does not lock. What follows is my own reading of the design, since no source measures it. A lock certifies three names. It does not say which readings of which words put them there, and a word that never bears on anyone's position in the tree is never tested by anything.

The reviews carry traces of this. Kaplan-Smith writes that many specifics still eluded him after he had finished, and that his spells of confusion lengthened and came close to frustration near the end. Matthew Stein says his most satisfying revelation came just past the formal ending, when the game left him with the question of what it all meant. In the comments under the game, players argue over the meanings of *solaam* and *nyscet*. Celia's reply sends them back to re-read the game's final note. She does not supply a gloss.

I wrote in [Fourteen Hours on One Grid](/posts/2026-09-16-fourteen-hours-on-one-grid.html) about what a free checker does to a puzzle when it names the rule that broke. *Chants of Sennaar* gives the dictionary a checker of that kind. Trevosa gives the dictionary to the player and keeps its checker for the genealogy, where an answer can be right or wrong. I think that is the better match to what translating is. It has a cost, which the reviewers report honestly, and the game page showed a rating of 4.9 from about 1,500 ratings when I looked.

An expanded version is [planned for Steam](https://jamwitch.itch.io/trevosa/devlog/1636165/the-archives-of-trevosa-is-coming-to-steam-with-publisher-inner-pocket) with sixty family members, two new families with their own cultures and words, and a lexicon for the player's notes. The designers know which Trevosan words a player must understand to place a name and which only colour the story. Does that proportion change when the tree doubles? And if a word was never put under a lock, has the player who finished the tree solved it?

<!--
HERO_IMAGE_PROMPT:
A dark oak desk in a sepia, candlelit cipher room, seen from a low three-quarter angle. Spread across the desk is a large sheet of antique paper carrying a hand-inked family tree in iron-gall ink: about thirty small oval medallions arranged in seven descending rows, joined by fine ruled lines, every medallion blank inside with no writing. Three neighbouring medallions near the top are each closed with a small brass padlock and a dab of red sealing wax, and taut red string links those three to one another. The remaining medallions are open and unsealed. To the left of the tree sits a stack of loose manuscript leaves and unrolled scrolls covered in rows of abstract invented glyphs that resemble no real alphabet, a few glyphs circled in faded ink. An open notebook lies beside them with blank ruled columns and a fountain pen resting mid-page. A small brass key, a brass magnifying lens, a ribbon bookmark in dull red and a guttering candle sit at the edge of the light. The background falls away into warm shadow with no shelves and no books. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition: painterly art with photographic framing, lighting and depth of field, never photorealistic. Atmospheric, mysterious, contemplative. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A free browser game asks you to decode an invented language to finish a royal family tree. It confirms the names in threes. It never tells you whether a single word you translated was right.

Full piece linked in bio.

#puzzledesign #deductiongames #linguistics #cognitivescience #patternrecognition #decipherment
-->

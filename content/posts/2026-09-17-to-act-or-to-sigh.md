---
title: "To Act, or to Sigh"
date: 2026-09-17
category: Pattern Brief
summary: A 1644 cipher letter on a public unsolved list was read by two AI-assisted solvers on the same day, then turned out to have been read twice before. All four readings agree on the key. They disagree only where the cipher checks nothing.
---

The letter ends in plain French. After two hundred-odd cipher symbols and a few stretches of cleartext, Sir Richard Forster writes that the reader should weigh whether it is better *d'agir, ou de soupir*: to act, or to sigh. Then the date, 13 May 1644.

Or perhaps the word is *soubir*, which would make it *subir*, to endure. "To act or to endure" is the better sentence. It is also a different piece of advice.

That word was never enciphered. Anyone could read it. And after four separate decipherments of this letter, it is the part nobody can settle.

## The letter on the list

Forster was treasurer of Queen Henrietta Maria's household. The letter survives among his papers in the departmental archives of the Val-d'Oise, and Karen Britland described it in ["Reading between the lines: royalist letters and encryption in the English civil wars"](https://doi.org/10.1111/criq.12072), *Critical Quarterly* 55(4), 2013, as a cipher nobody had read. The recipient is unknown. Britland suggested the queen, who had come to Exeter ill and pregnant that spring and would soon leave for France.

Satoshi Tomokiyo reposted the transcription on [his blog](https://cryptiana.blogspot.com/2021/09/an-unsolved-letter-of-richard-forster.html) in September 2021 and carried the letter on his [Unsolved Historical Ciphers](https://cryptiana.web.fc2.com/code/unsolved.htm) page. His transcription follows Britland's printed one, line breaks and all, and ends with *soupir*.

## Two solvers, one Monday

On 14 September 2026, two decipherments appeared. Robert Pitt, who describes himself as a software engineer experimenting with modern AI, published [forster-cipher](https://github.com/robertpitt/forster-cipher). Andrew Aymeloglu published [his reading](https://github.com/aaymeloglu/unsolved-ciphers/tree/main/forster-1644) in a repository that, by its own account, was started after the news that Claude Fable 5.1 had read Urquhart's Cyphral Distich, to see whether an agent plus a person checking its work could get further down the list. Tomokiyo's page now marks the entry **Solved**, crediting Pitt and noting that Aymeloglu uploaded his solution almost at the same time.

The two keys agree. The system is a homophonic substitution mixing letters and numbers: *e* can be `0` or `2`, *t* can be `8`, `50` or `b`, and so on. The plaintext is spiritual counsel. There is no cause for scruple about failing God, it says; take the ways of prudence to preserve your life, so that you can make of it a greater sacrifice through further service.

Aymeloglu's notes on how he got there interested me most. Character n-gram hill climbing, the standard statistical attack, went nowhere on 207 tokens over 34 symbols. What worked was a beam search over a French lexicon padded with seventeenth-century spellings (*ie* for *je*, *u* for *v*, *mesmes*, *subiet*), using the comma-marked word groups. The repository puts it bluntly: neither of the two things that carried the solve was cryptanalytic cleverness. What carried it was knowing where the words broke and what French looked like in 1644.

## Then the inbox

Pitt wrote to Britland. His update of 15 September reports her reply: George Lasry had sent her a decipherment after the article came out, and Norbert Biermann had independently reached the same solution. Pitt changed his repository's description to acknowledge them and says plainly that it makes no claim to the first decipherment.

So this cipher had been read at least twice before this week. At least one of those readings went to the scholar who had asked the question. Neither reached the list that recorded the question as open.

[Two days ago](https://vera-wren.github.io/posts/2026-09-15-solved-in-1858.html) the Richelieu letters turned out to be solved in an 1858 printed edition that no cipher catalogue indexed. The Forster answer sat somewhere harder still to search: private correspondence. The independent review in Aymeloglu's repository, written the day before Britland's reply surfaced, had drawn the line exactly where it belonged. "No known published solution," it said, was the defensible claim, and a private solve could not be excluded. It was the right sentence to write.

## Where four readers disagree

Pitt's update prints a small table of the earlier reading next to his own, and it is the most useful thing in either repository.

The earlier reading opens *aucune voie de scrupule* where Pitt has *aucun subiet*. It gives *preveu seulement* where both new solutions give *prenez seulement*. And it ends on *soupir*.

Look where those differences fall. *Prenez seulement* is one of the positions where the key breaks: the symbol there decodes to *d*, which gives *sdulement*, and both new solvers repair it by hand. Aymeloglu finds three such positions in 207. Pitt counts four, because he also emends *conceruer*, while Aymeloglu keeps it as a real period spelling and cites a 1623 archival transcription that uses *concerver*. The last disagreement is the cleartext word at the end.

Everywhere else, four readers agree. The review in Aymeloglu's repository shows why. It withheld each of the 37 cipher groups in turn and asked the other 36 to predict it. They recovered 195 of the 207 letters, and they reproduced exactly the three defective positions. Most of this cipher is overdetermined. Every `0` in the letter is checked by every other `0`, and a wrong value for `16` would wreck *dieu*, *perfection* and *multiplication* all at once. A homophonic key repeats itself across the whole letter, and each repetition is a check.

A slip has no such support. Neither does a word written in the clear. *Soupir* appears once, bound to no symbol, and nothing else in the letter can vote on it. The enciphered sentences are held in place by their own redundancy, while the unenciphered one is held in place by a single printed page.

## One page underneath

That page is the catch. Every modern reader here worked from the same transcription, Britland's typeset one, as copied by Tomokiyo. Pitt and Aymeloglu both say the manuscript was not checked, and Aymeloglu lists the archive's reference, MS 68.H.8, as not digitized. As for *soubir*, both repositories get it from the article's abstract. By their account, Britland's printed transcription reads *soupir* and her abstract reads *soubir*: one scholar, two spellings of the ending, on two different pages.

So the convergence is real, and I think it should be read at its actual size. Four people using different methods landed on one key. That settles the key. It cannot settle anything the transcription got wrong, because all four inherited the transcription. Their independence is independence of method, drawn from a single source of evidence. Whether those three bad symbols are Forster's slips or a copyist's, and whether the queen's treasurer counselled someone to endure or to sigh, is waiting in a bundle in Pontoise.

I find it moving that the one uncertain word is also the whole question the letter was sent to answer. The cipher protected the reasoning. The choice itself was left in plain sight, and it is the part that has worn thinnest.

What would a catalogue of solved ciphers need to record, beyond the word "Solved," so that the next reader could see which parts the key has checked and which parts nothing ever has?

<!--
HERO_IMAGE_PROMPT:
A single seventeenth-century letter on aged antique paper lies on a dark wooden cipher-room desk in sepia and candlelight, its lines a mix of iron-gall ink numerals and small letter-symbols, with one short line of plain handwriting at the bottom lit more brightly than the rest, as though a candle has been pulled close to it. Around the letter, four separate hand-ruled key tables on different papers (a parchment slip, a notebook page, a folded sheet, a card) are laid in a loose ring, each joined to the letter by a strand of red string, all four strings converging on the ciphered lines and none reaching the plain line at the bottom. A brass magnifying glass rests over the plain line. In the soft background, a tied archive bundle of papers with a faded ribbon and a wax seal, and a closed wooden archive box. A fountain pen and a brass key at the edge of the frame. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Photographic-painterly composition, painterly art with photographic framing, lighting and depth, never photorealistic. Atmospheric, contemplative, mysterious. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
A 1644 cipher letter to someone in mortal danger has now been read by four different solvers, and all four agree on the key. The word they cannot agree on was never enciphered at all: act, or sigh?

Full piece linked in bio.

#ciphers #cryptography #codebreaking #historicalciphers #englishcivilwar #patternrecognition
-->

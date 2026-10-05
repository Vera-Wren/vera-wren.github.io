---
title: "The Answer That Missed Its Own Bar"
date: 2026-10-05
category: Pattern Brief
summary: A 21-letter cipher from 1950, written to be read only after its author's death, was solved on 3 October. The correct answer failed the acceptance test its solver had committed in advance.
---

![](/images/2026-10-05-the-answer-that-missed-its-own-bar-hero.png)

HIER BIN ICH TOTSIENS TEW.

Twenty-one letters: "here I am" in German, a goodbye in Afrikaans, and three initials. T. E. Wood, a solicitor in Bournemouth, enciphered them in 1950 and printed the result in the *Proceedings* of the [Society for Psychical Research](https://en.wikipedia.org/wiki/Society_for_Psychical_Research) as FVAMI NTKFX XWATB OIZVV X. His plan was to die and then send the key back through a medium. A message opened that way would be a greeting from a man who, on the evidence of the key, was still somewhere.

The key was found on the evening of 3 October 2026 by a search through printed books. Klaus Schmeh [confirmed the solution the next day](https://klausschmeh.net/woods-cryptogram-from-the-crypt-another-top-50-crypto-mystery-solved/), and the solver, Colin Reilly, a UX designer near Seattle new to codebreaking, has published [a full account](https://creilly11235.github.io/wood-cryptogram-1950/) along with [the code and run history](https://github.com/creilly11235/wood-cryptogram-1950). One line of that account caught my attention more than the plaintext did. The correct answer failed the acceptance test he had written for it.

## A test borrowed from Thouless

Wood was copying [Robert Thouless](https://en.wikipedia.org/wiki/Robert_H._Thouless), the Cambridge psychologist who wrote *Straight and Crooked Thinking*. In 1948 Thouless published enciphered passages whose keys he meant to transmit after his death. The cipher was there as an experimental control. A medium might have been shown a sealed message in advance, but nobody could have been shown a key that existed in one head only.

The method Wood borrowed works on words. Take a passage of text and drop any word that has already appeared. Add up the letters of each remaining word (A is 1, B is 2), reduce the total modulo 26, and the result is the shift for one letter of the message. Wood added two hints: the key passage was in a foreign-language book anyone could obtain, and the message would be in more than one language.

Thouless's own passages all fell without help from the other side. One went within weeks. Another went to James Gillogly and Larry Harnisch, who published in *Cryptologia* in 1996 under the title [Cryptograms from the Crypt](https://www.tandfonline.com/doi/abs/10.1080/0161-119691885004). The last went in 2019 to [Richard Bean](https://scienceblogs.de/klausis-krypto-kolumne/2019/08/16/richard-bean-solves-another-top-50-crypto-mystery/), who ran the word-sum method across thousands of Project Gutenberg books. Wood's stayed open, at number 35 on Schmeh's list of unsolved messages.

## Keys on a shelf

It stayed open for a reason Thouless himself had pointed out. With a free choice of key letters, any ciphertext in this system can be turned into any message of the same length. At twenty-one letters there seemed to be no way of telling a solution from a coincidence. Readers of [Thirty-One Characters](/posts/2026-08-24-thirty-one-characters.html) will recognise the problem: the message is shorter than the length at which a reading starts to vouch for itself.

Reilly's project, by its own notes, believed this at first. The correction came on 17 September. Wood's key is a run of consecutive words in a published book. The candidate keys are therefore the starting points in real books, and that is a list one can walk along.

The first sweeps scored every decryption for how English it looked, across 129 books and then 3,977 texts. Before trusting a blank result, the project planted known messages under random book keys, and 97 of 100 came back ranked first. Wood's did not come back at all. The write-up reports that twelve of a hundred random ciphertexts scored better than his best.

Two changes on 3 October opened it. Candidates were scored across seven languages, with the language free to change at any word boundary, and nineteen Bibles were added to the shelves. The repository's commit history shows the multilingual rules going in at 9:33 that evening, Pacific time, and the solve being committed sixteen minutes later.

The key is Matthew 6:9 to 11 in the [1912 Luther Bible](https://www.bibel-online.net/text/luther_1912/matthaeus/6/): *Unser Vater in dem Himmel*, and on through twenty-one distinct words to *uns*. A few minutes earlier the project had typed in the Lord's Prayer by hand in the familiar church wording, which begins *Vater unser*, and got garbage. The same prayer in another wording is another key.

## The bar it missed

The rule committed before the Bible run required a candidate's score to clear a threshold set by the planted test messages. HIERBINICHTOTSIENSTEW scored −1.270 against a floor of −1.081. Under a second version of the arithmetic, a string of nonsense scored slightly higher.

The reason is in the output. The scorer knew seven languages and Afrikaans was not one of them. It had no notion of a signature either. It read the end of the message as TOT SIEN STEW.

The instrument had been built around an expectation of what the message would look like, and two of the message's three parts sat outside it. What Reilly did next is the part I admire. He reported the failed test, and then he read the candidate anyway, because it was the best of 26.7 million under Thouless's rule with junk in second place. After that came the checks: a standalone script that re-enciphers the plaintext to Wood's exact ciphertext, a second model reviewing independently, near-miss keys that all fail, and a control with 500 random signatures in place of TEW, seven of which also found a match. Of that last test he says it was designed after the hit, so it "shows rarity, not proof."

What follows is my own reading and not his. The threshold did its narrow job, which was to stop the search from declaring a solve by itself. The claim is carried by something the scorer could not see: two constraints Wood printed in 1950 and a signature he did not mention, all met by one of the best-known passages in a foreign-language book that any English town could supply. I find that persuasive. I also notice that it is a person's judgment standing where the number was supposed to stand, and the number had been written down first.

## A slip in the showcase

One more thing came out of the checking. To demonstrate the method in 1948, Thouless enciphered THERE IS NO DEATH with Hamlet's soliloquy as the key. The fourteenth key word is *suffer*, whose letters sum to 75, which reduces to 23 and so to W. Thouless printed U, and his printed ciphertext follows the U. By Reilly's account the error has sat in the *Proceedings* for seventy-eight years. Wood's twenty-one sums, presumably done by hand, contain no mistake.

## The date nobody has

Reilly is plain that a key found on a bookshelf says nothing either way about survival. What remains is Wood's own request. He asked anyone who attempted the cipher to report the result to the Society, even a negative one, and he promised the Society particulars of himself and word, through his executors, of when he died.

Wood was born in Yorkshire in 1887 and had practised law in Burma. Neither write-up gives the year of his death. The experiment needed that date before the cipher could mean anything, and if a folder survives in the Society's archive, it is the one part of the test still unread.

<!--
HERO_IMAGE_PROMPT:
A large antique leather-bound Bible lying open on a dark oak desk in a sepia, candlelit cipher room, its pages filled with dense blurred blackletter-style marks that are abstract and entirely illegible, a faded silk ribbon marking the place. Across the lower page lies a narrow strip of aged paper carrying a single row of twenty-one small ink marks, each one an indistinct smudge of iron-gall ink. A thin red string runs from the open page to a sealed envelope closed with dark red wax, and a brass key rests on the envelope. Beside them stands a brass balance scale with one pan slightly lower than the other, a small brass weight in the higher pan and a folded slip of paper in the lower. A fountain pen, an hourglass with its sand run out, and a single guttering candle sit at the edge of the light, with shelves of old book spines receding into shadow behind. Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. Photographic-painterly composition: painterly art with photographic framing, lighting and depth of field, never photorealistic. Atmospheric, mysterious, contemplative. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
In 1950 a solicitor published 21 enciphered letters and promised to send the key back after his death. The key turned up this weekend on a bookshelf, and the right answer failed the test its own solver had set for it.

Full piece linked in bio.

#cryptography #ciphers #codebreaking #historicalcryptology #patternrecognition #cognitivescience
-->

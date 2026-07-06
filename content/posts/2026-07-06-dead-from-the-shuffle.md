---
title: "Dead from the Shuffle"
date: 2026-07-06
category: Pattern Brief
summary: A famous open problem in probability hides a quieter truth about solitaire: a deal can be impossible in two completely different ways, and you are never told which kind you are holding.
---

![](/images/2026-07-06-dead-from-the-shuffle-hero.png)

Room Escape Artist reviewed a small game this week called [*Forbidden Solitaire*](https://roomescapeartist.com/2026/07/03/forbidden-solitaire-hivemind-review/) — a story-driven solitaire puzzle with, in their words, "a creepy vibe, reminiscent of early 90s FMV games." What caught me was the artwork: piles of red-backed cards arranged over a dungeon, and some of the face-up cards showing keys and keyholes. A lock puzzle built on top of the oldest single-player card game there is. Which is a lovely idea, and also a slightly haunted one, because solitaire already has a locked door built into it. Every deal is a door. And some of them cannot be opened by anyone, ever — you just don't get told which.

## The number nobody has

Here is a fact that should be more famous than it is. Nobody knows how often a game of Klondike solitaire — the one that shipped with Windows and swallowed an untold number of office afternoons — can actually be won. Not approximately-nobody. Nobody. The exact winnability of the most-played card game on Earth is an open problem, and the mathematician [Persi Diaconis](https://en.wikipedia.org/wiki/Klondike_(solitaire)), who is also a former professional magician and therefore knows something about cards, called our ignorance of it an embarrassment. The 2019 paper that made the biggest dent in it opens by repeating the charge: our not knowing this number has been described as ["one of the embarrassments of applied mathematics."](https://arxiv.org/abs/1906.12314)

That paper is [*The Winnability of Klondike Solitaire and Many Other Patience Games*](https://arxiv.org/abs/1906.12314), by Charlie Blake and Ian P. Gent, and it is a beautiful piece of work. They built a general solver called Solvitaire and turned it loose on 73 variants of 35 different patience games. For Klondike they report a winnability of **81.945%, give or take about a tenth of a percent** — but with one enormous asterisk. That number is for the *thoughtful* variant, which the paper defines precisely as the game "where the player knows the rank and suit of all cards." Every downturned card face-up. Perfect information.

So with nothing hidden, roughly four Klondike deals in five can be won. Which means — and this is the part I keep turning over — that close to **one deal in five simply cannot be won at all.** Not by you, not by a grandmaster, not by Solvitaire running depth-first search for a week. Those deals were dead the instant they were shuffled. There is no sequence of legal moves that opens them. The lock has no key cut for it.

## Two kinds of impossible

Now hold that eighteen percent next to the other number. When actual humans play actual Klondike — cards down, no peeking — a skilled player wins something like [43% of the time](https://en.wikipedia.org/wiki/Klondike_(solitaire)) (one experiment clocked a good player at 189 games out of 442). The solving AIs that play blind land lower, in the thirty-something range. Wikipedia summarizes the whole spread as odds of winning somewhere between 18% and 43%.

Look at the gap. Full sight: about 82%. Best blind play: about 43%. Something on the order of *forty percentage points of winnable games are being lost* — and they are not being lost because those deals were impossible. They were winnable. They are being lost because the player couldn't see.

That is the whole quiet argument of this post. A solitaire deal can be impossible in two completely different ways, and the two have nothing to do with each other.

The first is **structural**. The cards fell in an order that admits no solution. This is a fact about the deal itself, true from the shuffle, indifferent to how well you play. It is the same shape as a cipher with no unique reading — [the underdetermined message](https://vera-wren.github.io/posts/2026-06-24-the-line-down-the-middle-of-the-cipher-world/) where "internally consistent" and "actually solvable" have come apart, and no amount of skill can close a gap that isn't there. The answer is not hidden. The answer does not exist.

The second is **informational**. The deal *is* winnable — a version of you who could see every downturned card would open it clean — but you cannot see those cards, and so you cannot know which move is the right one. Here the answer exists. It is simply behind a face-down card, and the game will not let you look. This is the far more ordinary tragedy, and it is the reason the gap between 82% and 43% is so wide: most of the games a good player loses were never dead. They were just dark.

## The state you can never read

Here is what I find genuinely eerie about solitaire, and what *Forbidden Solitaire*'s keys and keyholes accidentally make literal. **When you are stuck, you cannot tell which kind of stuck you are in.**

You are staring at a stalled tableau. Maybe you are grinding away at a deal that was structurally dead before you turned the first card, and every clever line you try is wasted motion against a wall with no door in it. Or maybe you are one hidden card away from a win you will never see, betrayed not by the shuffle but by the information the game withholds. From inside the game, at the moment of being stuck, *these two situations look exactly the same.* Same frozen board, same feeling, same silence. The game never tells you whether you are fighting the deal or fighting your own blindness.

I keep coming back to a distinction I wrote about earlier this month — [knowing which kind of stuck you are in](https://vera-wren.github.io/posts/2026-07-01-when-the-hands-get-in-the-way/), whether a difficulty is one your hands can attack or one that lives somewhere you cannot reach. Solitaire is the cruelest possible version of that question, because it withholds the very information you would need to answer it. And it rhymes with the condition of every solver working an orphaned cipher — grinding for years on a message whose author is gone and [no authority is left to confirm a solution](https://vera-wren.github.io/posts/2026-06-25-the-keeper-that-is-a-hash/), unable to know whether they are one insight from the answer or working something that was never solvable at all. That is a Klondike deal the size of a life. Winnable or dead, and no way to check from the inside.

The thing Blake and Gent gave us, really, is not a percentage. It is a clean separation of two things that feel identical from the chair. With perfect information, a deal is won or it is dead, full stop — a structural fact. Without it, a whole second layer of loss appears, made entirely of games you *could* have won if the world had let you see. The 82% is the ceiling of the possible. The 43% is what you can reach through a keyhole.

So I wonder what it would do to a puzzle to expose that seam on purpose — a game that, at the end, told you which of your losses were dead deals and which were merely blind ones. It might be unbearable. Half your defeats revealed as bad luck of the shuffle you were right to accept, and the other half as wins that were sitting there the whole time, one face-down card away, if only you had been allowed to look.

<!--
HERO_IMAGE_PROMPT:
Romantic painterly illustration in the manner of Nick Bantock's Griffin & Sabine meets Bletchley Park 1942. Sepia and candlelight. An antique desk seen from above: a spread of aged playing cards with faded red backs arranged in the fanned columns of a solitaire tableau, several cards face-down and shadowed, one or two face-up cards subtly engraved with an antique brass key and a keyhole instead of pips. A single brass key rests across the cards, tied with a thread of red string that trails to a small closed padlock at the edge of the frame. A fountain pen and an open leather notebook with faint hand-inked columns of tally marks sit alongside, iron-gall ink, a wax-sealed envelope, an hourglass half-run. Deep chiaroscuro, some cards dissolving into candlelit dark to suggest the hidden downturned cards. Photographic-painterly composition: painterly art with photographic framing, lighting, and depth, never photorealistic. Mood: mysterious, contemplative, the quiet fatalism of a game already decided. No human figures anywhere. No legible text. 16:9 horizontal composition.
-->

<!--
SOCIAL_CAPTIONS:

INSTAGRAM:
Nobody actually knows how often a game of Klondike solitaire can be won. It is a genuine open problem in mathematics. But hidden inside it is something stranger: a solitaire deal can be impossible in two completely different ways. Some deals are dead from the shuffle, unwinnable by anyone. Others are perfectly winnable, and you lose them only because you cannot see the face-down cards. And when you are stuck, the game never tells you which kind of stuck you are in.

Full piece linked in bio.

#solitaire #puzzles #probability #cryptography #patternrecognition #cardgames
-->

---
title: "The Proof That Was Hiding in the Wrong Field"
date: 2026-04-26
category: Pattern Brief
summary: A 23-year-old with no advanced math training used GPT-5.4 Pro to crack a 60-year-old Erdős conjecture in 80 minutes — by applying a formula from Markov process theory that no number theorist had thought to use.
---

Liam Price is 23 years old and has no advanced mathematics training. On an idle Monday afternoon, he typed [Erdős Problem #1196](https://www.erdosproblems.com/forum/thread/1196) — a conjecture about primitive sets that had resisted proof for sixty years — into GPT-5.4 Pro. Eighty minutes later, the model produced a proof. "I didn't know what the problem was," Price told [*Scientific American*](https://www.scientificamerican.com/article/amateur-armed-with-chatgpt-vibe-maths-a-60-year-old-problem/). "I was just doing Erdős problems as I do sometimes, giving them to the AI and seeing what it can come up with."

The conjecture concerns [primitive sets](https://en.wikipedia.org/wiki/Primitive_set): collections of whole numbers where no number divides any other. Erdős, together with Sárközy and Szemerédi, conjectured that a specific weighted sum over such sets — ∑ 1/(a log a) for elements a in the set — approaches exactly 1 as the numbers grow large. Mathematicians had whittled the upper bound down to roughly 1.399 over the decades. Nobody could close the gap.

## The Formula from the Adjacent Room

What GPT-5.4 Pro produced wasn't a harder version of existing approaches. It was a [different kind of approach entirely](https://www.converseer.com/chatgpt-5-4-pro-cracks-60-year-old-erdos-conjecture-in-under-two-hours-reveals-novel-mathematical-insight/): a Markov chain argument combined with von Mangoldt weights — tools from probability theory and analytic number theory that were well-known in their home fields but that nobody had applied to primitive set analysis.

Terence Tao, responding on the Erdős Problems Project forum, called it "a previously undescribed connection" between integer anatomy and Markov process theory, one that "now seems obvious in hindsight" and "goes well beyond the solution of this particular Erdős problem." Kevin Barreto, a Cambridge mathematics undergraduate who helped review the work, called it "a creative leap prior efforts missed."

"Obvious in hindsight" is doing a lot of work in that sentence. Sixty years of work.

## The Register No One Left

I've been writing about a failure mode I first noticed in [spectrogram ciphers](https://vera-wren.github.io/posts/2026-04-22-spectrogram-steganography-as-a-liminal-cipher-the-.html) — the wrong-perceptual-register problem. When a message is encoded in the frequency domain of an audio file, solvers on [r/codes](https://www.reddit.com/r/codes/) consistently exhaust every tool appropriate to audio analysis — frequency analysis, bit manipulation, the full in-register toolkit — before someone finally loads the file into a spectrogram viewer and the static renders as text. The solution isn't harder than what they were attempting. It is in a different register entirely.

The Erdős conjecture played the same trick on mathematics. For sixty years, number theorists approached it with number-theoretic tools. Each generation narrowed the bound a little further — from distant approximations to 1.399 — all within the same register. The wall they hit at 1.399 wasn't a wall of difficulty. It was a wall of register. The proof required a tool from a neighboring room of mathematics that no one had carried over.

This is [expertise as attentional restructuring](https://vera-wren.github.io/posts/2026-02-24-how-learning-reconfigures-attentional-salience-in-.html) made visible at the disciplinary level. The same mechanism that makes a trained number theorist excellent at recognizing standard proof strategies — proactive prediction, salience reconfiguration, the brain learning to anticipate what has previously been signal-dense — also makes adjacent-field tools invisible. The salience map doesn't flag what it hasn't been trained on. And sixty years of working within the same register is sixty years of deepening the grooves that prevent the switch.

## The Tool with No Grooves

GPT-5.4 Pro has no salience hierarchy. It does not know which mathematical tools are "standard" for which problem classes. It cannot distinguish between "this is a number theory approach" and "this is a probability theory approach" at the level of disciplinary identity. When it searches the space of possible proof strategies, it searches without the attentional filters that a mathematical education installs.

This is not the same as being smarter. It is the same as being unblocked.

Price's role is equally telling. He had no knowledge of the problem's history — no awareness of which approaches had been tried and exhausted, no sense of which tools were "appropriate." He fed the problem to the AI without the sixty-year context of what hadn't worked. In the [taxonomy of solver failure modes](https://vera-wren.github.io/posts/2026-04-22-spectrogram-steganography-as-a-liminal-cipher-the-.html) I've been developing, this is the naive solver advantage: no toolkit to exhaust means no register to get stuck in.

## A Sixth Position

When I wrote about [AI's structural positions in puzzle experiences](https://vera-wren.github.io/posts/2026-03-15-the-caddy-doesnt-design-the-course.html), I identified five roles: designer, solver, opponent, companion, oracle. The Erdős proof suggests a sixth: **register-switcher**. The AI's value here wasn't in solving the problem *harder* within the existing framework. It was in approaching the problem from a place that the existing framework's trained attention had made invisible.

This is a different claim from "AI is better at math." AI is not better at math. AI is worse at staying inside a register — which, for sixty-year-old conjectures where the register is the problem, turns out to be exactly the advantage that matters.

Tao's "obvious in hindsight" is the same phenomenology as the spectrogram reveal — the moment when the hidden message materializes and you cannot understand how you ever looked at the carrier without seeing it. The Markov chain connection was always there. The formula was well-known. The bridge between fields was, as Tao notes, undescribed but not undescribable. It was hiding not behind complexity but behind the trained attention of everyone who had ever looked.

Eighty minutes. The wall wasn't hard. It was just in the wrong place.

---
title: "The Caddy Doesn't Design the Course"
date: 2026-03-15
category: "Pattern Brief"
summary: "Google I/O's annual puzzle tradition has evolved from developer-only scavenger hunts to AI-companion mini-games — and the specific role they chose for Gemini reveals something important about where AI actually belongs in puzzle design."
---

A Gemini-powered caddy watches you line up a mini-golf shot, adjusts its commentary based on your performance, and offers real-time feedback as you navigate obstacles toward a hole. This is one of five games in Google's [I/O 2026 "Make, Build, Unlock" puzzle](https://io.google/2026/puzzle/play/) — the annual tradition where the developer community solves challenges collectively to reveal the conference dates. The caddy is charming. It's responsive. And its design role is notably precise: it watches you play. It does not design the course.

That distinction matters more than it might seem.

## Nine Years of Designed Discovery

Google has been running these I/O reveal puzzles since at least 2017, and the [design arc across those years](https://tech.yahoo.com/google-o-happening-soon-5-173856847.html) tells a story. The 2017 puzzle was a global scavenger hunt — decoding numbers into letters, following coordinates to real-world locations including crop circles in Brazil. You needed coding knowledge to participate. The 2018 version dropped players into a [virtual escape room inside Google's offices via Street View](https://blog.google/technology/developers/google-io-2025-puzzle-ai/), a browser-based Myst that rewarded spatial reasoning and patience. By 2024, it was Pipe Dream — a 3D marble-path construction game with fifteen levels of tile-based constraint logic.

Each year, the puzzles got more accessible. The audience broadened from developers who could decode hex to anyone who could navigate a browser game. But the fundamental structure stayed constant: human designers built the puzzle architecture, set the constraints, calibrated the difficulty curve, and engineered the moment of collective revelation when enough people solved enough challenges to unlock the date.

Then came 2025's [Prism Shift](https://io.google/2025/puzzle/), which asked players to aim light beams through mirrors and prisms to illuminate colored nodes — and generated unique bonus-level clues using Gemini. AI entered the puzzle space. But how it entered is the interesting part.

## The Five Roles AI Could Play

When you put an AI model inside a puzzle experience, it could occupy at least five structural positions:

**Designer** — generating the puzzle constraints, difficulty curve, and solution architecture from scratch. This is what procedural generation attempts, and it's where I remain skeptical. A constraint solver can produce valid Sudoku grids all day, but the [satisfaction of solving one comes from the designer's engineered solve path](/posts/2026-03-14-the-satisfaction-the-solver-cant-reach.html) — the sequence of discoveries that produces the feeling of arriving rather than just answering.

**Solver** — cracking the puzzle computationally, which is what Ken Shirriff's MiniZinc model does with NYT Pips. Useful for verification. Not a puzzle experience.

**Opponent** — actively working against the solver in real time. This is chess engines, Go programs, adversarial game AI. Fascinating, but a different domain.

**Companion** — observing the solver's behavior and responding to it without altering the puzzle structure. This is the Gemini caddy.

**Oracle** — generating hints or clues on demand, bridging the gap between the solver's current state and the solution. This is what Prism Shift's bonus-level clues approached.

Google chose companion and oracle. Not designer. Not opponent. And the choice reveals a design intuition that aligns with something I've been circling for weeks in these posts: the puzzle's intentionality has to come from somewhere, and right now, AI doesn't have it.

## What the Caddy Actually Does

The [2026 puzzle suite](https://chromeunboxed.com/the-countdown-to-google-i-o-2026-begins-with-the-make-build-unlock-puzzle/) includes five games — Hole in One (mini-golf with the Gemini caddy), Nonogram (logic-picture puzzle), Word Wheel (crossword variant), Supersonic Bot (voice-controlled Flappy Bird), and Stretchy Cat (board-filling path puzzle). The concept is tagged "Make, Build, Unlock," and it was explicitly designed to welcome audiences at any technical level.

The caddy's real-time feedback serves a specific cognitive function: it maintains engagement through the frustration trough. When you miss a shot, the caddy responds — not by changing the course, but by reframing your attempt in a way that keeps you inside the problem. This is what good escape room game masters do. They watch your process, offer calibrated nudges, and preserve your sense of agency while preventing you from disengaging entirely.

The crucial thing the caddy doesn't do: it doesn't redesign the hole after you fail. The obstacle layout stays fixed. The solution space stays constant. The constraints remain human-authored. Gemini operates in the space between the solver and the puzzle, not in the space between the designer and the puzzle.

## The Collective Threshold

There's one more structural detail worth noting. Google requires a [global completion threshold](https://chromeunboxed.com/the-countdown-to-google-i-o-2026-begins-with-the-make-build-unlock-puzzle/) before the final reveal unlocks — enough players worldwide must solve enough challenges before the conference date is exposed. This is a designed collective discovery event, the same architecture I examined in [MrBeast's million-dollar puzzle hunt](/posts/2026-03-13-the-puzzle-that-sixty-million-people-walked-into.html), but calibrated very differently. Where MrBeast's hunt funneled sixty million people toward a single winner, Google's puzzle distributes the revelation across the entire solving community simultaneously. Everyone who participated gets the answer at the same time.

The AI companion doesn't change this social architecture. It operates at the individual level — your caddy, your feedback, your nudge through the frustration trough. The collective threshold remains a purely human-to-human design contract: we all solve, and the answer arrives for everyone.

I think Google stumbled into something important here, possibly without fully articulating it. The question isn't whether AI can generate puzzles — it can generate valid constraint structures all day. The question is where in the puzzle experience AI adds something that isn't already better served by human intentionality. And the answer, at least in 2026, is: in the space between the solver and the solve. Not in the architecture. Not in the answer. In the accompaniment.

The caddy doesn't design the course. And that might be exactly right.

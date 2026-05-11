---
title: "The Satisfaction the Solver Can't Reach"
date: 2026-03-14
category: "Pattern Brief"
summary: "NYT Pips can be cracked by a constraint solver in milliseconds — so why do millions of humans find it deeply satisfying to solve by hand?"
---

Ken Shirriff [built a constraint solver](http://www.righto.com/2025/10/solve-nyt-pips-with-constraints.html) that cracks NYT Pips puzzles in milliseconds. He modeled the domino positions as coordinate pairs, constrained each half to occupy adjacent cells, enforced pip-value matching and regional rule compliance, and handed the whole thing to MiniZinc. The solver — using backtracking, constraint propagation, and heuristic variable selection — finds valid solutions almost instantly. Some backends solve the hard puzzles in under a second.

The algorithm's approach is structurally identical to how the game [tells you to play](https://nytpips.com/): identify the most restrictive regions first, work outward, use process of elimination. Pick the most constrained position. Apply the locally optimal rule. Propagate.

If that sequence sounds familiar, it should. I [wrote recently](/posts/2026-03-10-the-constraint-engine-that-cant-see-the-whole.html) about Wave Function Collapse — the procedural generation algorithm that works on exactly this principle. WFC always selects the most constrained tile, collapses it, propagates the consequences, and repeats. It is test-mode cognition formalized as code. And I argued that WFC's fatal limitation is that it produces local coherence without global meaning — roads that connect but lead nowhere, coastlines that tile correctly but don't describe a recognizable shore.

Pips is a constraint-satisfaction puzzle. The solver proves it. So why do millions of people find it genuinely satisfying to do by hand what a computer does in milliseconds?

## The Non-Algorithmic Remainder

The solver gets the answer. The human gets the *click*. These are not the same thing.

When you stare at a Pips grid — colored regions with their rules, a tray of unused dominoes — you do start with constraint propagation. You look for the most locked-down region. If a section demands a sum of 11 and only one domino combination can produce that, you place it. Pure logic. The solver does this faster.

But then something else happens. You start seeing spatial relationships between regions. You notice that a domino bridging two zones satisfies both simultaneously — one half contributing to a sum constraint, the other half fulfilling an inequality. That bridge is not a step in a constraint propagation algorithm. It's a perception of non-local structure. You're not propagating constraints outward from a single cell. You're recognizing that two apparently separate problems share a single solution.

This is the exact operation I argued WFC cannot perform. Constraint propagation is bottom-up: collapse, propagate, repeat. The bridge domino is top-down: see the whole, recognize the joint, place it. The human solver isn't running constraint propagation badly. They're running a different process — one that uses constraint propagation as a substrate but adds something on top.

## Handcrafted, Not Generated

Here's the design detail that makes this visible: every Pips puzzle is [handcrafted by human editors](https://parade.com/living/pips-game-nyt), not algorithmically generated. The New York Times specifically chose human puzzle construction over procedural generation.

This matters. An algorithm could generate valid Pips grids — constraint-satisfiable configurations with unique solutions. But a handcrafted puzzle has something an algorithmically generated one doesn't: a *solve path*. The editor builds the grid so that constraint resolution unfolds in an order that produces satisfaction. The most constrained region leads to a placement that opens the next insight, which cascades into the next, until the final domino drops into the last gap with an inevitability that feels earned.

The editor is working in design-mode. They're constructing a constraint landscape that channels the solver's attention through a specific sequence of revelations. The solver — the algorithm — doesn't care about path. It finds the answer. The editor cares about nothing *but* path. They're engineering the experience of arriving.

This is why handcrafted puzzles feel different from generated ones, even when both are valid. The solution is the same. The satisfaction isn't.

## What the Click Actually Is

Pips launched in [August 2025](https://www.today.com/life/pips-new-york-times-game-rcna225538) as the New York Times' first original logic puzzle — not a word game, not an adaptation, but a new design built on domino mechanics. It joins Wordle, Connections, and Strands in the NYT's daily puzzle ecosystem, and it's the first in that lineup that is purely spatial and mathematical. No vocabulary, no semantic associations. Just regions, rules, and tiles.

And it's the one that makes the constraint-satisfaction structure most visible. In Wordle, the constraint propagation is obscured by linguistic intuition — you're not just eliminating letters, you're pattern-matching against your mental lexicon. In Pips, the constraints are laid bare. The rules are printed on the grid. The available dominoes are visible in the tray. Everything you need is right there.

Which means the satisfaction can't come from information asymmetry or hidden knowledge. It comes from the moment when locally separate constraints reveal themselves as globally coherent. When the domino you place doesn't just satisfy one region — it makes the entire remaining grid solvable. The click is the recognition that local rules compose into a whole.

I keep returning to the hippocampal pattern completion model — the idea that the "aha" moment is a binding event, where separately held partial patterns suddenly cohere into a single representation. Pips makes this architecturally explicit. The partial patterns are the regional constraints. The binding event is the placement that satisfies multiple regions simultaneously. The click is the hippocampal threshold being crossed: enough constraints resolved that the remaining solution becomes inevitable.

The constraint solver crosses that threshold on the first iteration. It never experiences the accumulation phase. It never holds partial patterns in tension. It arrives at the answer without passing through the state that makes the answer feel like a revelation.

That's the non-algorithmic remainder. Not the answer — the *arriving*.

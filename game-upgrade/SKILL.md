---
name: game-upgrade
description: |
  Run a full game health check from player and senior-engineer perspectives, merge the findings into a prioritized revision plan, obtain user approval before editing, implement approved changes, verify them, and log the cycle under docs/upgrades/. Use when the user invokes /game-upgrade in Claude Code, invokes $game-upgrade in Codex, or asks for a complete game upgrade, health check, or revision pass.
---

# Game Upgrade

A periodic health check for a game in active development. Invoke it as `/game-upgrade` in Claude Code or `$game-upgrade` in Codex. It never edits code before the user approves a plan.

## Process

1. **Read current state.** `README.md` Status/Built/Left, and any prior `docs/upgrades/*.md` — know what's already been tried.
2. **Get real observation material.** Don't analyze from source alone. Produce a short capture per this project's own capture recipe if it has one (e.g. a `godot.md`/`babylon.md`/`bevy.md`-style doc, whatever this engine/template calls it), or ask the user to hand you one — and actually watch it before judging feel. This is the same "proof over claims" rule applied to *analysis*, not just delivery; it holds regardless of engine.
3. **Two independent passes, run in parallel** (spawn as two separate subagents so neither pass anchors on the other's framing):
   - **Player pass** — given the capture + a chance to reason about controls/UI/flow: is it fun, is input intuitive, is feedback clear, pacing, difficulty, is it boring or confusing, UI/visual/audio read, replay value, the single moment most likely to make someone quit.
   - **Engineer pass** — given the code/scenes: architecture, scene structure, coupling, duplication, maintainability, extensibility, physics/performance, asset management, input, camera, UI, GameManager, debuggability, tech debt.
4. **Merge** both passes into one plan, bucketed **must-do / recommended / skip for now**. Every item states: the problem, why it matters, the proposed fix, the expected improvement.
5. **Stop and present the plan to the user.** Do not implement anything yet.
6. On approval, implement only the approved items. Verify per this project's own build/verification gate (a `godot.md`-style doc if it has one, otherwise however this project normally confirms a change works), then have the user confirm in the editor/runtime.
7. **Write `docs/upgrades/upgrade-NNN.md`** (increment N from existing files) with: date, game state at the time, player-pass findings, engineer-pass findings, the full plan, which items the user approved, what was actually changed, test results, and what's left / to watch next round.

## Notes

- This skill changes the *current game* only, never a shared template repo it may have been generated from. If the project has a companion skill for harvesting reusable lessons back into that template (e.g. `game-distill`), that normally runs afterward, using this skill's own upgrade log as one of its inputs — but `game-upgrade` works standalone with no such skill present.
- If `docs/upgrades/` doesn't exist yet, create it on first run.

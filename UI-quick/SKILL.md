---
name: UI-quick
description: |
  Get a decent, good-looking UI into a game or app in minutes, not hours — the MVP path: speed and "good enough, license-clean, ready to use" over bespoke design. Covers both game-engine UI (Godot: Kenney CC0 asset packs, or a ready-made Godot Theme built from them) and web/app UI (React: shadcn/ui + tweakcn; framework-agnostic: DaisyUI), plus a zero-dependency pure-code path (Godot StyleBoxFlat / Tailwind tokens) for when no external asset should be added. Distinct from `pick-ui-library` (which library for a specific component like toasts/charts, not visual skin), `ui-quality` (reviewing/critiquing existing UI against design checklists), and `frontend-ui-engineering` (React code architecture patterns) — this skill is about sourcing the actual visual "skin". For a custom/bespoke look worth spending real money, time, or heavy iteration on, use `UI-pro` instead.
---

# UI Quick

Get real, good-looking UI into a project fast by sourcing from known-good, license-clean, pre-designed places — not by hand-crafting a look from scratch, and not by picking blind. Unlike `sound-quick` (Claude cannot hear audio, so it must trust category-match or community rating), **Claude can actually see a rendered UI** — always finish by capturing a screenshot of the applied result and looking at it before calling the work done. Trust-but-verify, the same rule this template already applies everywhere else.

## Priority order

### 1. Identify the target: game engine or web/app

- **Game engine (Godot confirmed; likely generalizes to others)** → `references/kenney-ui-packs.md`.
- **Web/app (React or Tailwind-based)** → `references/web-ui-kits.md`.
- **Neither fits** (unusual engine, no Tailwind, a from-scratch custom look) → drop to the pure-code path below, or escalate to `UI-pro`.

### 2A. Godot / game engine path

Two options, in speed order:

1. **Fastest: a ready-made Theme resource.** `references/kenney-ui-packs.md` documents "Kenney's UI Theme for Godot" — a CC0, pay-what-you-want `.tres` already wired from Kenney's UI Pack for Godot 4.x. Apply it as the project's default theme or to the UI root, done. Note it doesn't cover dialogs/tabs/tree — leave those default or style them yourself.
2. **Raw asset pack, more control:** download Kenney's "UI Pack" (or a themed sibling pack — RPG/Sci-Fi/Adventure/Pixel, see the reference doc) directly, and wire pieces into `StyleBoxTexture`s yourself (9-slice margins per Godot's texture import settings). More setup than option 1, worth it when the ready-made theme's coverage or look doesn't fit.

Copy chosen files into the project's real asset directory — if this project has a `godot.md`-style convention doc, follow its asset-layout rule; otherwise the common Godot default is everything under `assets/` (e.g. `res://assets/ui/`) — matching the same discipline `sound-quick` uses for audio files. Tell the user exactly which pack/file was used and that it's CC0.

### 2B. Web/app path

`references/web-ui-kits.md` has the full comparison. Short version: **shadcn/ui + a tweakcn theme** for a React project you'll keep customizing; **DaisyUI** for non-React or maximum speed. Don't introduce a second styling system into a project that already committed to one of these.

### 3. Pure-code path (zero new dependencies/assets)

Valid when the project's own convention forbids external assets (check this project's `godot.md`-style doc if it has one — some Godot projects/templates have a house rule to build everything from primitives at build time), or when neither 2A/2B fits.

**Godot — `StyleBoxFlat` Theme, authored in the project's scene-builder script** (no textures, no plugin):
- Rounded corners: `CornerRadiusTopLeft`/`TopRight`/`BottomLeft`/`BottomRight` — 8–12px reads as "clean modern flat" for a normal-DPI UI; adjust to the project's actual resolution.
- A subtle border instead of a flat fill: `BorderWidthLeft/Top/Right/Bottom` (2–3px) + `BorderColor` a shade lighter/darker than the fill, not pure black/white.
- Depth without a texture: `ShadowSize` + `ShadowColor` (low alpha, e.g. 0.25–0.35) reads as a soft drop shadow.
- **Every interactive control needs distinct `normal`/`hover`/`pressed`/`focus` StyleBoxFlats** — a Button that only gets a font override (no StyleBox at all) renders as Godot's bare default flat-gray box with no hover feedback beyond the engine's built-in subtle tint, which most players won't even notice. This is the single most common "placeholder-looking" tell — fix it even if nothing else changes.
- Reference numbers (not a drop-in file, just calibration): the Godot Editor's own 4.6+ default theme (formerly the separate "godot-minimal-theme" project) documents ~4–5px corner radius, a dark base (~#272727) + one accent color, contrast 0.3–0.35 as a clean baseline — that's an editor-chrome theme, not something to literally import into a game, but the numbers transfer as a starting point.
- `StyleBoxFancy` (a small Godot addon, MIT) extends `StyleBoxFlat` with gradients combined with rounded corners if the stock resource can't express the look — an addon dependency, not zero-dependency, so only reach for it if plain `StyleBoxFlat` genuinely can't do it.

**Web — Tailwind utility classes + a real token palette**, no component library. Use `ui-quality`'s color/contrast method if that skill is installed; otherwise pick 1 accent + a neutral scale with a consistent hue bias, and check text-on-background contrast against WCAG AA (4.5:1 for body text) rather than picking colors ad hoc.

### Why this isn't split into a separate "0-dependency" skill

Considered and rejected: asset-pack-vs-pure-code is an *implementation choice within* the same "get UI done fast" job, not a different task needing separate triggering — exactly like `sound-quick` already folds its own procedural-synthesis fallback (tier 3) into one skill rather than splitting it out. Split by **effort/cost tier** instead (this file vs. `UI-pro`), matching the `sound-quick`/`sound-pro` precedent this pair is modeled on.

## What NOT to do

- Don't mix two different visual packs/styles on one screen (e.g. Kenney's flat "UI Pack" buttons next to "UI Pack - Adventure" panels) — inconsistency reads worse than plain unstyled controls.
- Don't claim to have "picked the best-looking option by eye" when the real method was category/reputation match (same honesty rule as `sound-quick`) — say what was actually used and why.
- Don't skip the verification screenshot. A theme/pack that fails to import correctly (wrong path, missing font fallback, broken 9-slice margins) looks like success in the diff and broken in the running app — a project's own `godot.md`/`run`-style build-verification convention, where one exists, exists precisely because "it compiled" isn't proof; follow it if present, otherwise verify with your own screenshot regardless.
- Don't introduce a second component/styling system into a project that already has one working.

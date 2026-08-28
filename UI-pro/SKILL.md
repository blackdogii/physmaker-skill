---
name: UI-pro
description: |
  The resource-intensive counterpart to `UI-quick`: spend real money, human time, and/or a large Claude token budget to get UI that's custom-fit to the project instead of a pre-made pack/theme. Five tracks — paid premium asset kits (game engines, one-time cost), AI UI generation (web/React, v0.dev, subscription), custom-generated game UI art via this project's `asset-gen` skill if it has one, or any equivalent image-generation skill otherwise (per-image API cost), Claude-driven iterative visual refinement (token-heavy, no external cost), and human designer commission (money + turnaround time, Claude only writes the brief and integrates the result). Use when `UI-quick`'s packs/themes don't fit the project's visual identity, or the UI is a signature moment (a game's title screen, a product's core screen) worth the extra cost.
---

# UI Pro

Where `UI-quick` picks the closest pre-made option, this skill spends more to get something closer to exactly right. Pick the track that matches which resource the user is actually willing to spend — don't default to the most expensive one.

## Hard boundary — money, API keys, and human labor

Same rule as `sound-pro`: Claude does not acquire, hold, or pay for API access, marketplace purchases, or freelancer payments on the user's behalf.

- **API-key tracks (v0.dev, `asset-gen`'s or an equivalent image skill's APIs)**: the user creates their own account, generates their own key, and puts it in their own environment — never pasted into chat, never written into project files or memory. If the key isn't present when this skill is invoked, stop and say which env var is needed and where to get it.
- **Marketplace purchase (itch.io, Envato)**: Claude can search, evaluate, and recommend a specific listing, but the user completes the actual purchase/download themselves (these sites need a logged-in checkout Claude cannot and should not perform). State the price before recommending a purchase.
- **Human commission (Fiverr/Upwork)**: Claude drafts the brief; the user posts it, selects a freelancer, and pays them. Claude's role resumes at integrating the delivered files.
- **Before any paid/costly action**, state the estimated cost and get explicit confirmation — this is a real-money or real-labor action, same bar as any other consequential action.

## Track 1 — Paid premium asset kits (game engines)

The official Godot Asset Library is free-only (verified 2026-08-23) — paid Godot/game UI kits live on marketplaces instead:

- **itch.io** (https://itch.io/game-assets/tag-godot/tag-user-interface and similar tag combinations for other engines) — mixed free/paid, typically $3–20 one-time per kit, huge range of styles (fantasy, sci-fi, minimalist, RPG). Search, screenshot the preview images the listing shows, present 2–3 candidates with price + style to the user rather than picking one unilaterally — this is a taste decision, not a technical one.
- **Envato Elements** — subscription ($16.50+/mo as of last general knowledge, **re-verify current price at https://elements.envato.com/pricing before quoting it**) — unlimited downloads across a huge UI-kit library while subscribed; only worth it if the user already has or wants a subscription for other assets too, not just for one UI kit.
- Workflow: search → shortlist 2–3 with screenshots/prices → user picks and buys → integrate the same way `UI-quick`'s Kenney path does (9-slice into `StyleBoxTexture`s or an included ready `Theme` if the kit ships one).

## Track 2 — AI UI generation for web apps (v0.dev)

- **v0 by Vercel** (https://v0.dev) — generates React + Tailwind UI from a text prompt, including full pages and interactive states, with a visual "Design Mode" editor and GitHub sync.
- **Pricing (verified 2026-08-23, re-verify at https://v0.dev/pricing before relying on it)**: Free tier exists (reported as ~$5/mo in credits, or a 200-credit/10-generation-per-day variant depending on current plan structure — the exact mechanic has changed before, confirm live), Premium ~$20/mo, Team/Business tiers above that. Token-based cost per generation as of a Feb-2026 pricing change — complex prompts cost more.
- State the tier/cost expectation to the user before generating anything beyond what the free tier obviously covers.
- Output is real React/Tailwind source, not an image — reads naturally into a project already using `UI-quick`'s shadcn/ui path (v0's output style is close to shadcn's conventions).
- Alternatives mentioned in passing, not independently verified this pass: Galileo AI, Uizard — check current state before recommending over v0 if the user specifically wants a comparison.

## Track 3 — Custom game UI art via `asset-gen` (only if this project has it)

Some game projects/templates have their own `asset-gen` skill (Gemini/Grok image generation, GLB models, background removal) for producing visual assets from text prompts. **If this project has it**, it's the fastest path to bespoke game UI art:

- Generate custom panel/button/icon textures via `asset-gen`'s image path (a real per-image API cost — confirm spend with the user before the first generation, per that skill's own existing rule).
- Import the result as a 9-slice `StyleBoxTexture` the same way a Kenney texture would be used, or as flat icon sprites.
- Don't duplicate `asset-gen`'s own workflow/pricing details here — invoke it directly for the generation step; this track exists only to point at it as the "custom AI art for game UI" option, since `asset-gen` (or an equivalent general-purpose image-gen skill) typically doesn't have game-UI-specific prompt guidance of its own.
- **If this project has no `asset-gen` (or equivalent) skill, this track simply isn't available** — fall back to Track 1, 2, or 4. Don't treat its absence as an error.

## Track 4 — Claude-driven iterative visual refinement (tokens, no external cost)

The zero-dollar, high-token track: no new asset or paid API, just many capture → critique → adjust cycles until the UI clears a real quality bar. This is the same loop this project has already used successfully for gameplay VFX tuning (screenshot a change, compare against the prior frame, adjust the value, re-screenshot) — extended to UI chrome:

1. Capture the current UI (per the target engine/framework's normal screenshot method — Godot: `--write-movie` a few frames per this project's `godot.md` capture recipe if it has one, otherwise just `--write-movie` with sensible defaults; web: a browser screenshot tool).
2. Critique it against a real rubric, not vibes — for Godot, use `UI-quick`'s pure-code `StyleBoxFlat` checklist (rounded corners, border, shadow, all 4 button states) as the rubric; for web, use `ui-quality`'s rubric if that skill is installed, otherwise this baseline: consistent surface/border/shadow treatment across all states, icon sizing and alignment, spacing rhythm (one scale, not ad-hoc pixel values), and every interactive state (default/hover/focus/active/disabled) actually styled, not just default.
3. Adjust the specific values the critique flagged — not a wholesale re-do each round.
4. Re-capture and compare directly against the previous round's screenshot (not just "does it look fine now" — actually diff what changed).
5. Stop when a round produces no more findings against the rubric, not after a fixed number of rounds.

This is expensive in tokens (each round is a real render + inspection cycle) but produces a genuinely bespoke, project-fitted result with zero new licensing/dependency surface — the right choice when the user has token budget to spend but not money, or when neither a pre-made pack nor an AI generator's output style fits the project.

## Track 5 — Human designer commission

- Fiverr/Upwork for a custom Figma UI kit, icon set, or full screen design.
- Claude's role: write a clear, specific brief (target platform, screen inventory, visual references/mood, required states, delivery format) for the user to post; after delivery, integrate the provided assets/specs into the project. Claude does not do the visual design itself in this track — that's the point of paying a human.
- If the delivered file is a Figma design (not ready assets), **Locofy** or **Anima** can bridge Figma → code for web projects — mention as an option, verify current capability/pricing before committing the user to one.

## Workflow

1. Ask (or infer from context) which resource the user actually wants to spend: money, time, or tokens — don't assume the most expensive track.
2. Pick the matching track above.
3. For any paid step, state the cost and get confirmation before it happens.
4. Deliver the result the same way `UI-quick` does: tell the user exactly what was used/generated/purchased, from where, and verify it renders correctly with a real screenshot — never claim success from the diff alone.

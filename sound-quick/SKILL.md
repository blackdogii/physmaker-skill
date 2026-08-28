---
name: sound-quick
description: |
  Fast, no-listening-required sourcing of ready-to-use CC0/royalty-free sound effect files for a game or UI's MVP/prototype pass — button clicks, hit/impact sounds, coin/powerup/laser sci-fi cues, error/confirm chimes, footsteps. Pulls from pre-curated Kenney.nl CC0 packs first (professionally vetted, filename-categorized, zero auth, zero license risk), Freesound.org CC0-filtered top-rated results second. Never claims to have "listened and picked the best" — Claude cannot hear audio; selection is by category-match or community rating, and the skill says so. Use when the user wants working sound effects quickly for a first playable/MVP, not a bespoke or hero-moment sound.
---

# Sound Quick

Get a decent, legally-clean sound effect into the project in minutes, not hours. This is the MVP path: speed and "good enough, CC0, zero license risk" over bespoke quality. For a hand-crafted signature sound (a boss's roar, a game's title-screen sting), use `sound-pro` instead.

## Hard boundary — be honest about what this skill can't do

Claude has no audio-listening capability. This skill never says "I listened to 5 candidates and picked the best one" — that would be fabricated. What it actually does is:
- Match the requested sound *category* to a pre-vetted, professionally-designed CC0 pack (Kenney) — the designer already did the quality control across the whole pack, so picking by filename category is a legitimate substitute for auditioning.
- Or sort Freesound results by community rating/download count and take the top CC0-licensed result — trusting the crowd's ears, not Claude's.
- Always tell the user which specific file was used and where it came from, so they can swap it in ten seconds if it doesn't fit.

## Priority order

### 1. Kenney.nl CC0 packs (default — try this first)

No account, no API key, no attribution required (CC0). Packs are downloaded once, cached locally, and files are picked by filename category — verified working as of 2026-08-23 (see `references/kenney-packs.md` for the exact download URLs and the full verified filename vocabulary per pack).

Workflow:
1. Check `references/kenney-packs.md` for a pack whose category vocabulary matches the need (e.g. "button click" → Interface Sounds pack, `click_*`; "explosion/hit" → Impact Sounds pack, `impact*_heavy`; "power-up/laser" → Digital Audio pack, `powerUp`/`laser`/`zap*`).
2. If the pack isn't already cached under the project's scratch/cache dir, download its zip (`curl -sL <url> -o pack.zip`) and unzip it.
3. Pick the file(s) matching the wanted category. If several numbered variants exist (`click_001.ogg` … `click_005.ogg`), default to `_001`; only try others if the user specifically asks for a different flavor.
4. Copy the chosen file into the project's actual audio asset directory (ask if unclear — e.g. `public/sounds/`, `assets/audio/`, a Godot project's `res://audio/`), renaming it to something descriptive for the project (not the Kenney filename) if that matches project convention.
5. Tell the user exactly which pack + filename was used and that it's CC0 (crediting Kenney is appreciated but not required).
6. **If the download URL in the reference doc 404s** (Kenney occasionally reissues packs with a new hash), re-resolve it: fetch `https://kenney.nl/assets/<pack-slug>` and find the current zip link, then update the reference doc with the corrected URL so the next run doesn't hit the same dead link.

Packs verified and cataloged so far: Interface Sounds, Impact Sounds, Digital Audio (see the reference doc). Kenney has dozens more (UI Audio, RPG Audio, and others under kenney.nl/assets — filter by "Audio" category) — if none of the cataloged three fit, browse `https://kenney.nl/assets/category:Audio`, fetch the relevant pack page for its real download URL, download and inspect its filenames the same way, and append the new pack + its verified vocabulary to `references/kenney-packs.md` so it's cataloged for next time.

### 2. Freesound.org (fallback — when Kenney has nothing close)

Freesound needs a free account + API token (instant, no approval wait, from `freesound.org/apiv2/apply`) — the user needs to do this once and give Claude the token (as an env var, e.g. `FREESOUND_API_TOKEN`; never ask the user to paste it into chat, and never store it in project files).

- Search: `GET https://freesound.org/apiv2/search/text/?query=<keyword>&filter=license:"Creative Commons 0"&sort=rating_desc&token=<token>` — the CC0 filter is not optional, other Freesound licenses require attribution or forbid commercial use and this skill must not silently pull those in.
- Take the top-rated result. Token auth is enough to fetch the **preview** (lossy mp3, usually fine for a game SFX); the full-quality original download requires OAuth2 (a real login flow) — only bother with that if the user specifically wants master-quality and is willing to do the OAuth dance.
- Same reporting rule as above: tell the user which sound (with its Freesound page URL) was used, and that it's CC0.

### 3. `sfx.ts`-style live synthesis (last resort / zero-dependency fallback)

If neither source has anything close (or the project genuinely can't have any external binary assets — e.g. a code-golf/13kb game jam entry), fall back to procedural Web Audio synthesis: short oscillator envelopes for tonal UI cues, filtered white-noise bursts for impact/percussive sounds. This project's own wedding-website `src/scripts/sfx.ts` is a working reference implementation of this pattern (tone() + noiseBurst() primitives) — reuse that structure rather than reinventing it. Zero external files, zero license concerns, but inherently "electronic/retro" sounding — say so if the user seems to want something more organic/realistic and suggest step 1/2 instead.

## What NOT to do

- Don't pull a non-CC0 Freesound result without flagging the license and getting explicit confirmation — CC-BY needs attribution tracked somewhere, CC-BY-NC forbids commercial games.
- Don't claim a file was "quality-checked by listening" — say what selection method was actually used (category match / community rating).
- Don't download a whole Kenney pack repeatedly for the same project — cache it locally on first use.

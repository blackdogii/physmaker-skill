# Kenney.nl UI asset packs — verified catalog (game engines)

All CC0 (public domain), free for personal/educational/commercial use, no attribution required. Same trusted source `sound-quick` uses for audio — Kenney's packs are professionally designed as a coherent set, so picking the matching pack is a legitimate substitute for auditioning dozens of scattered individual assets.

Download links include a content hash that changes when Kenney reissues a pack — if a link 404s, re-resolve by fetching `https://kenney.nl/assets/<slug>` and reading the current link off the page, then update this file.

## UI Pack (the flagship — verified 2026-08-23)

- Page: https://kenney.nl/assets/ui-pack
- Zip: https://kenney.nl/media/pages/assets/ui-pack/f651646eab-1718203990/kenney_ui-pack.zip
- 870 PNG files (plus `Vector/` SVG source, 2 `.ttf` fonts, 6 `.ogg` click/switch/tap sounds)
- Structure: `PNG/<Color>/<Density>/<file>.png` — 6 color variants (**Blue, Green, Grey, Red, Yellow, Extra**) × 2 densities (**Default**, **Double** = @2x), all pixel-identical layouts across colors so swapping the `<Color>` folder re-themes everything with zero re-wiring.
- Verified base-name vocabulary (82 unique names per color folder):
  - **Buttons** (30 variants): `button_{rectangle,round,square}_{flat,gloss,gradient,line,border}` and the same 5 again prefixed `depth_` (a pressed/3D look) — i.e. every shape × flat/gloss/gradient/line/border, with or without the depth treatment.
  - **Checkboxes/radio**: `check_round_color`, `check_round_grey`, `check_round_grey_circle`, `check_round_round_circle`, `check_square_color[_checkmark|_cross|_square]`, `check_square_grey[_checkmark|_cross|_square]`.
  - **Sliders**: `slide_hangle` (the draggable handle), `slide_{horizontal,vertical}_{color,grey}[_section|_section_wide]`.
  - **Arrows**: `arrow_{basic,decorative}_{n,s,e,w}[_small]`.
  - **Misc**: `star.png`.
  - **`Extra/` color folder specifically** also holds: `divider.png`, `divider_edges.png`, `icon_{arrow_down,arrow_up,play,repeat}_{dark,light,outline}.png`, `input_{outline_rectangle,outline_square,rectangle,square}.png`.
- Fonts: `Font/Kenney Future.ttf`, `Font/Kenney Future Narrow.ttf` — a rounded, friendly display face; pair with a real body font for long text.
- Sounds: `Sounds/{click-a,click-b,switch-a,switch-b,tap-a,tap-b}.ogg` — matches `sound-quick`'s Interface Sounds pack in spirit; use either, don't need both.
- **No dedicated "panel" background texture in this pack** — build panel backgrounds from a `button_*_flat`/`button_*_depth_flat` piece (9-sliced) or from a plain `StyleBoxFlat`; don't assume a panel asset exists here.
- Best for: clean flat/rounded "casual mobile game" look, any genre. This is the default first pick.

## Kenney's UI Theme for Godot (verified 2026-08-23) — the fastest Godot-specific path

- Page: https://azagaya.itch.io/kenneys-ui-theme
- A community-made, **CC0-licensed**, pay-what-you-want (free is a valid price) Godot `Theme` `.tres` resource built directly from the UI Pack above — i.e. someone already did the StyleBoxTexture/9-slice wiring for you.
- Two downloads: "for Godot 3.x" and **"for Godot 4.x"** (51 kB) — use the 4.x one for any current project.
- Covers: buttons, checkboxes, sliders, line edit, progress bar, and other standard controls. Explicitly does **not** cover dialogs/popups, tabs, or tree — style those yourself (StyleBoxFlat, see the pure-code path in SKILL.md) or leave them default.
- Apply: drop the downloaded `.tres` into the project (e.g. `res://themes/kenney_ui_theme.tres`), then either set it as the project's default theme (Project Settings → GUI → Theme → Custom) or assign it to a root `Control`/`CanvasLayer`'s `Theme` property (in this project's build-script convention, that's `root.Theme = GD.Load<Theme>("res://themes/kenney_ui_theme.tres");` in the relevant `BuildX.cs`) so every child Button/Panel/LineEdit inherits it automatically.
- **Verify the actual download link by visiting the itch.io page at use-time** — itch.io doesn't expose a stable direct zip URL the way Kenney's own site does; this skill can't `curl` it unattended the way Kenney packs are downloaded, so either ask the user to download it once (a few clicks, no account needed) or use browser automation if available.

## Other Kenney UI packs — known to exist, not yet downloaded/cataloged

Verify vocabulary the same way (fetch the asset page for the real zip link, download, `unzip`, inspect filenames) before relying on a specific filename from these:

- **UI Pack (RPG Expansion)** — https://kenney.nl/assets/ui-pack-rpg-expansion — 85 assets, adds RPG-flavored pieces (parchment-style panels, ornate frames) on top of the base UI Pack.
- **UI Pack - Adventure** — https://kenney.nl/assets/ui-pack-adventure — 130 assets, a different (non-flat) visual style from the base pack — don't mix the two styles in one screen.
- **UI Pack - Sci-Fi** — https://kenney.nl/assets/ui-pack-sci-fi — angular/glowing sci-fi HUD look.
- **UI Pack - Pixel Adventure** / **Pixel UI Pack** (750 assets) — pixel-art style, for a retro/8-bit game — don't use with a smooth-shaded 3D game (mismatched art direction).
- **Input Prompts** — https://kenney.nl/assets/input-prompts — keyboard/mouse/gamepad button icons (for control legends/hints), a good pairing with any of the above.

## Style-matching rule

Pick **one** pack/color and use it for every UI surface in the project — mixing "UI Pack" flat buttons with "UI Pack - Adventure"'s different bevel style reads as visibly inconsistent, worse than plain unstyled controls. If the project's game already has an established palette (e.g. this project's Snow/Grass/Desert route colors), pick the Kenney color variant closest to it, or recolor via a shader/material tint rather than mixing packs.

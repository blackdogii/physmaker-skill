# Web/app UI component + theme sources — verified catalog

Unlike the Kenney game-asset packs, none of these are "download a zip once" — they're installed as dependencies or copy-paste source. Verify the install command still matches current docs at use-time (these ecosystems move fast); the license/positioning facts below are stable.

## shadcn/ui — default pick for a React project (verified 2026-08-23)

- Site: https://ui.shadcn.com
- **Not a component library you `npm install` and import from** — it's a CLI (`npx shadcn@latest add button`) that copies the actual component source (React + Tailwind + Radix primitives) into your own `src/components/ui/`. You own and can edit every line; no black-box dependency to fight later.
- License: MIT. Framework: React only (a Vue/Svelte port exists community-side but isn't the canonical project).
- Ships with a real, considered default visual style out of the box (not just unstyled primitives) — this is why it beats hand-rolling Tailwind classes for MVP speed: the taste work is already done.
- **tweakcn** (https://tweakcn.com) — the most popular free shadcn/ui theme generator/registry. Browse pre-made themes (each is a set of CSS variables), preview live, copy the variables into the project's `globals.css`/theme file. This is the fast way to get a *distinctive* look instead of every shadcn project looking identical — genuinely worth a pass before shipping the stock default.
- Best for: any React (Next.js, Vite+React, Remix) project where the UI will be hand-customized further — dashboards, admin panels, SaaS apps, forms-heavy apps.

## DaisyUI — default pick when speed beats ownership, or the project isn't React

- Site: https://daisyui.com
- A Tailwind CSS **plugin** — adds semantic component classes (`btn`, `card`, `modal`, …) on top of Tailwind utilities. Framework-agnostic (works in plain HTML, Vue, Svelte, React, anything using Tailwind) — no JS framework required at all.
- Zero JS dependency footprint (unlike shadcn's Radix-based interactive components) — purely CSS classes.
- **35 built-in themes**, switchable at runtime via a `data-theme` attribute — the fastest way to reskin an entire app without touching component markup. Good for prototypes, admin panels, internal tools, or anywhere the exact pixel-level design isn't the differentiator.
- Trade-off vs shadcn: you don't own/see the component internals the way shadcn's copy-paste model gives you — faster to start, less to customize later without fighting the plugin's class API.
- Best for: non-React projects, fastest possible MVP, or when 35 ready themes covers the actual need better than one hand-tuned shadcn theme would.

## Choosing between them

| Situation | Pick |
| --- | --- |
| React project, will iterate on the design over time | shadcn/ui + tweakcn theme |
| Non-React project, or genuinely just need it done fast | DaisyUI |
| Need a dashboard/charts-heavy admin UI specifically | Either, but check `pick-ui-library` skill first for chart library (recharts/Liveline) — this skill covers visual UI kit sourcing, not the component-library-per-task decisions that skill already owns |
| Project already uses one of these | Stick with it — don't introduce a second styling system into one project |

## Higher-effort web sources (still free/cheap, more setup than the above)

- **Flowbite** (https://flowbite.com) — Tailwind component library with a free tier + paid Figma/Pro blocks; a middle ground between DaisyUI's simplicity and a full custom build.
- **Once UI** (https://once-ui.com) — a more opinionated, design-forward Next.js system with a strong out-of-box aesthetic; smaller ecosystem than shadcn/DaisyUI so expect more edge cases.

If none of the above fit (a genuinely unusual visual direction, or a non-web/non-Godot stack this reference doesn't cover), fall back to the pure-code path in `SKILL.md`, or escalate to `UI-pro` for an AI-generated or paid custom option.

---
name: high-quality-presentation-workflow
description: Govern the end-to-end creation of high-quality presentations through source verification, evidence boundaries, slide narrative design, visual-system approval, representative sample approval, per-slide production, independent visual QA, speaker notes, and final PPTX or HTML validation. Use when Codex must create or substantially redesign a professional slide deck, PowerPoint, PPTX, web presentation, academic talk, teacher workshop, research briefing, course presentation, project report, or AI/science-education deck where visual quality, factual accuracy, Traditional Chinese, traceability, and delivery reliability matter.
---

# High-quality presentation workflow

Create the presentation as a governed production project. Treat content, narrative, visual design, QA, and delivery as separate responsibilities.

## Route the artifact

1. Load the format-specific skill before production:
   - Native `.pptx`: use `presentations:Presentations`.
   - High-design HTML deck: use `guizang-ppt-skill` when appropriate.
   - Generated raster visuals: use `imagegen` only after the visual direction is approved.
   - Source PDFs: use `pdf:pdf` to extract and visually inspect them.
2. Preserve the user's requested output format. Do not silently replace PPTX with HTML or image-based slides.
3. If a required format skill or renderer is unavailable, report the missing dependency and propose a specific fallback before production.

## Apply the quality formula

Evaluate every deck against six dimensions:

`quality = content credibility × narrative clarity × visual consistency × page readability × QA rigor × delivery reliability`

Treat a near-zero score in any dimension as a release blocker.

## Follow the gated workflow

### Gate 1 — source and outline approval

1. Read all supplied sources before choosing a visual style.
2. Separate source-supported claims, adjacent evidence, presenter recommendations, and unresolved uncertainty.
3. Never invent data, quotations, citations, researchers, classroom outcomes, or experimental photographs.
4. Define the communication job in one sentence.
5. Draft a slide-by-slide outline. Each slide must contain a takeaway title, audience-facing core message, supporting evidence or boundary, slide role, layout intent, and speaker-note purpose.
6. Ask the user to approve the outline before full visual production when the deck is complex, research-based, or longer than five slides.

Read [references/core-workflow.md](references/core-workflow.md) for the overall control flow. For research-heavy or externally sourced decks, also read [references/content-and-evidence.md](references/content-and-evidence.md).

### Gate 2 — visual system and representative sample

1. Define one visual system: palette, typography, image language, spacing, density, and icon treatment.
2. Vary layouts by function. Do not repeat one card grid across the deck.
3. Produce one representative content slide—not only the cover.
4. Inspect the sample at full size and thumbnail size.
5. Ask for approval before producing the full deck when the visual direction requires material judgment.
6. Record the approved sample, renderer, model/backend, dimensions, and quality settings. Keep them stable throughout production.

Read [references/visual-system.md](references/visual-system.md) before proposing or approving the visual direction.

### Gate 3 — per-slide production and independent QA

1. Create a self-contained job for each slide. Include exact visible text, evidence boundary, layout intent, required assets, prohibited additions, output path, and notes intent.
2. Do not let a slide generator research or complete missing facts.
3. Keep generation and acceptance separate. Reinspect every candidate independently.
4. Check every slide for exact title and Traditional Chinese; factual and citation accuracy; topology, arrows, sequence, and labels; missing or invented key points; clipping, overlap, contrast, density, and thumbnail readability; and consistency with the approved visual system.
5. Repair local defects with the same renderer or backend. Regenerate only when local repair cannot preserve quality.
6. Compare multiple candidates on correctness first, then visual polish.

For resumable production, use [references/job-and-state.md](references/job-and-state.md). For detailed inspection and repair decisions, use [references/qa-and-repair.md](references/qa-and-repair.md).

### Gate 4 — deck-level QA, notes, and delivery

1. Render all slides and build a contact sheet.
2. Inspect visual rhythm, layout diversity, density balance, terminology, and narrative continuity.
3. Write Traditional Chinese speaker notes for every slide. Notes must explain the claim, guide attention, add limits or context, and bridge to the next slide—not read the slide aloud.
4. Validate that the final artifact opens; page count and 16:9 dimensions are correct; no overflow, placeholder, or missing asset remains; note count matches slide count; and the PPTX package or HTML navigation is valid.
5. Deliver only after all blockers are resolved.

Read [references/delivery-validation.md](references/delivery-validation.md) before packaging the final artifact.

## Use the bundled utilities

Initialize a governed production workspace:

```powershell
python scripts/init_deck_workspace.py <project-directory> --deck-name "Deck title" --slide-count 10 --format pptx
```

Check that the approved sample and all slide records are ready for assembly:

```powershell
python scripts/validate_deck_state.py <project-directory>
```

Validate a produced PowerPoint package:

```powershell
python scripts/validate_pptx.py <deck.pptx> --expected-slides 10 --require-notes --aspect-ratio 16:9
```

These utilities validate production state and package structure. They do not replace visual inspection of rendered slides or a contact sheet.

## Enforce hard prohibitions

- Do not start full production before content and visual direction are aligned.
- Do not use a repeated three-card layout as the default solution.
- Do not create fake data, diagrams, quotations, citations, student work, or classroom photographs.
- Do not let attractive visuals overstate the source evidence.
- Do not trust the producing agent's PASS without independent inspection.
- Do not change image backend, model, dimensions, or quality after sample approval without explicit reason and renewed visual review.
- Do not assemble the final deck while any slide is pending, blocked, missing, or unverified.

## Keep the user in the loop

For complex work, communicate at the outline proposal, visual-system proposal, representative sample, full-deck QA result, and final delivery. Keep decisions explicit and resumable.

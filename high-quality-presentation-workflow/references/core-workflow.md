# Core workflow reference

## Contents

- Evidence model
- Slide outline contract
- Layout-role rules
- Sample approval criteria
- Per-slide QA checklist
- Final release checklist

## Evidence model

Classify every material claim as one of:

1. **Source-supported** — directly supported by supplied material or an authoritative cited source.
2. **Adjacent evidence** — relevant evidence from another population, context, discipline, or task; label the transfer limit.
3. **Presenter recommendation** — a teaching, design, or implementation judgment; do not present it as research fact.
4. **Unresolved** — insufficient evidence or ambiguity; omit, qualify, or ask the user.

Retain precise author names, years, DOI values, units, sample sizes, and limitations when they affect interpretation. Put full citations in notes when visible-slide density would suffer.

## Slide outline contract

Each slide record must include:

```yaml
slide_number: 1
takeaway_title: "A complete sentence stating the point"
role: "cover | problem | concept | process | comparison | evidence | case | framework | close"
core_message: "One audience-facing idea"
key_points:
  - "Exact point 1"
evidence_boundary: "What may and may not be claimed"
layout_intent: "The visual relationship the page must show"
required_assets: []
prohibited_content: []
speaker_note_intent: "What the presenter adds verbally"
```

Avoid unresolved references such as “as mentioned earlier.” Every production job must be understandable on its own.

## Layout-role rules

Use a shared design system while changing composition by slide function:

- Cover: one proposition and one visual metaphor.
- Problem: surface appearance versus internal gap.
- Concept: hierarchy, bridge, spectrum, or relationship.
- Process: linear timeline, cycle, or staged workflow with explicit arrow direction.
- Comparison: matched columns, matrix, or before/after structure.
- Evidence: claim-led exhibit with visible evidence boundary.
- Case: context, intervention, observation, and limit.
- Framework: clear dimensions, roles, or assessment logic.
- Close: synthesis and an actionable next step.

Do not use the same modular card silhouette for three consecutive slides. Use large type, restrained copy, stable alignment, and enough contrast to remain readable as a thumbnail.

## Sample approval criteria

- [ ] Exact Traditional Chinese and correct terminology.
- [ ] Credible information density.
- [ ] Title readable at thumbnail size.
- [ ] Layout expresses the intended relationship.
- [ ] Palette, typography, icon language, and imagery can scale to the full deck.
- [ ] No fake data, fake people, fake classroom evidence, watermark, or decorative filler.
- [ ] Renderer/backend, model, dimensions, and quality are recorded.

## Per-slide QA checklist

- [ ] Title is exact and states a takeaway.
- [ ] All visible Chinese is Traditional Chinese.
- [ ] Names, dates, numbers, units, quotations, and citations are correct.
- [ ] Arrow direction, sequence, hierarchy, and labels are correct.
- [ ] No required key point is missing.
- [ ] No unsupported information was added.
- [ ] Important text is not clipped, distorted, or obscured.
- [ ] Contrast and density support projection and thumbnail reading.
- [ ] Layout role matches the content relationship.
- [ ] Visual style matches the approved sample.
- [ ] Speaker-note intent is covered.

## Final release checklist

- [ ] Every slide is present, accepted, and rendered.
- [ ] Contact sheet shows coherent rhythm and varied functional layouts.
- [ ] Speaker notes exist for every slide.
- [ ] Output opens successfully and uses the requested format.
- [ ] Page count, aspect ratio, notes, media, and package structure are valid.
- [ ] No placeholder, temporary path, draft marker, or missing asset remains.
- [ ] Known image-based or editability limitations are disclosed.
- [ ] Final path and verification result are reported.

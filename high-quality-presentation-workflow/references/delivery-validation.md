# Delivery and validation

## Speaker notes

Write Traditional Chinese notes for every slide. As a practical target, use roughly 150–400 Chinese characters when the talk format needs a full script; shorten when the user requests cue notes.

Each note should:

- explain the claim rather than read the slide;
- tell the speaker where to direct attention;
- add evidence limits, examples, or teaching context;
- bridge to the next slide;
- preserve exact citations that were omitted visually.

## PPTX checks

Verify:

- the file opens and the ZIP package has no corrupt members;
- page count and requested aspect ratio are correct;
- slide XML count equals the intended deck count;
- notes-slide count equals slide count when notes are required;
- required media is embedded and no temporary path remains;
- rendered slides have no overflow, placeholder, clipping, or missing asset;
- the final contact sheet has passed deck-level review;
- SHA-256 is recorded when traceable delivery matters.

Run `scripts/validate_pptx.py` for structural checks. Structural success does not prove visual quality.

## HTML checks

Verify the entry file opens locally, all assets resolve, keyboard and touch navigation work, slide count is correct, viewport scaling is stable, text remains selectable when required, and no development-only dependency or absolute local path remains.

## Disclosure

State whether the deck is native/editable, hybrid, or image-based. Image-based PowerPoint can preserve appearance but limits editing, search, accessibility, and text extraction. Never describe it as fully editable.

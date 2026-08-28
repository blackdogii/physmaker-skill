# Slide jobs and production state

## Workspace contract

Use one directory for each production:

```text
project/
├── sources/
├── outline/
├── style/
├── jobs/
├── candidates/
├── approved/
├── renders/
├── qa/
├── output/
├── deck_spec.json
├── state.json
└── speech.md
```

Run `scripts/init_deck_workspace.py` to create this structure without overwriting existing files.

## Self-contained slide job

Create one JSON or Markdown job per slide. Include:

- slide number and role;
- exact visible title and body text;
- core message and evidence boundary;
- layout intent and arrow or reading direction;
- required assets and their source identifiers;
- prohibited additions;
- approved style and renderer settings;
- candidate and approved output paths;
- speaker-note intent.

Do not use phrases such as “same as before” or “continue the previous slide.” A job must remain understandable if processed independently.

## State model

Use these slide states:

- `pending`: job not dispatched;
- `dispatched`: production started;
- `candidate`: candidate exists but is not accepted;
- `recorded`: independently accepted and approved path recorded;
- `blocked`: cannot proceed without a decision or missing input.

Use `pending` or `accepted` for the representative sample. Assembly is forbidden unless the sample is `accepted` and every slide is `recorded`.

Record the candidate, approval decision, QA report, renderer/backend, and repair history. Do not treat a producer's self-reported PASS as acceptance.

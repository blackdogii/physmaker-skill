from __future__ import annotations

import argparse
import json
from pathlib import Path


ALLOWED_STATUSES = {"pending", "dispatched", "candidate", "recorded", "blocked"}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate presentation production state before assembly.")
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--allow-incomplete", action="store_true")
    args = parser.parse_args()

    project_dir = args.project_dir.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    try:
        spec = load_json(project_dir / "deck_spec.json")
        state = load_json(project_dir / "state.json")
    except ValueError as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 1

    expected_count = spec.get("slide_count")
    slides = state.get("slides", {})
    if not isinstance(expected_count, int) or expected_count < 1:
        errors.append("deck_spec.json must contain a positive integer slide_count")
    elif len(slides) != expected_count:
        errors.append(f"Expected {expected_count} slide records, found {len(slides)}")

    if state.get("sample", {}).get("status") != "accepted":
        warnings.append("Representative sample is not accepted")

    for number, record in sorted(slides.items()):
        status = record.get("status")
        if status not in ALLOWED_STATUSES:
            errors.append(f"Slide {number} has invalid status: {status!r}")
            continue
        job = record.get("job")
        if not job or not (project_dir / job).is_file():
            warnings.append(f"Slide {number} job is missing")
        if status != "recorded":
            warnings.append(f"Slide {number} is {status}, not recorded")
            continue
        approved = record.get("approved")
        qa_report = record.get("qa_report")
        if not approved or not (project_dir / approved).is_file():
            errors.append(f"Slide {number} recorded without an approved artifact")
        if not qa_report or not (project_dir / qa_report).is_file():
            errors.append(f"Slide {number} recorded without a QA report")

    if spec.get("speaker_notes_required") and not (project_dir / "speech.md").is_file():
        errors.append("speech.md is required but missing")

    if warnings and not args.allow_incomplete:
        errors.extend(warnings)

    result = {
        "valid": not errors,
        "project_dir": str(project_dir),
        "expected_slides": expected_count,
        "recorded_slides": sum(1 for record in slides.values() if record.get("status") == "recorded"),
        "errors": errors,
        "warnings": warnings if args.allow_incomplete else [],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())

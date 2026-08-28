from __future__ import annotations

import argparse
import json
from pathlib import Path


DIRECTORIES = (
    "sources",
    "outline",
    "style",
    "jobs",
    "candidates",
    "approved",
    "renders",
    "qa",
    "output",
)


def write_json_if_missing(path: Path, payload: dict) -> bool:
    if path.exists():
        return False
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a governed presentation workspace.")
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--deck-name", required=True)
    parser.add_argument("--slide-count", type=int, required=True)
    parser.add_argument("--format", choices=("pptx", "html"), required=True)
    parser.add_argument("--language", default="zh-TW")
    parser.add_argument("--aspect-ratio", default="16:9")
    args = parser.parse_args()

    if args.slide_count < 1:
        parser.error("--slide-count must be at least 1")

    project_dir = args.project_dir.resolve()
    project_dir.mkdir(parents=True, exist_ok=True)
    for directory in DIRECTORIES:
        (project_dir / directory).mkdir(exist_ok=True)

    slides = {
        f"{number:02d}": {
            "status": "pending",
            "job": f"jobs/slide-{number:02d}.json",
            "candidate": None,
            "approved": None,
            "qa_report": None,
        }
        for number in range(1, args.slide_count + 1)
    }
    spec = {
        "deck_name": args.deck_name,
        "format": args.format,
        "language": args.language,
        "aspect_ratio": args.aspect_ratio,
        "slide_count": args.slide_count,
        "speaker_notes_required": args.format == "pptx",
        "visual_system": {
            "renderer": None,
            "backend": None,
            "dimensions": None,
            "quality": None,
        },
    }
    state = {"sample": {"status": "pending", "approved_path": None}, "slides": slides}
    outline = {"communication_job": "", "slides": []}

    created = []
    for filename, payload in (
        ("deck_spec.json", spec),
        ("state.json", state),
        ("outline.json", outline),
    ):
        if write_json_if_missing(project_dir / filename, payload):
            created.append(filename)

    speech_path = project_dir / "speech.md"
    if not speech_path.exists():
        speech_path.write_text(f"# {args.deck_name}｜講者備註\n", encoding="utf-8")
        created.append("speech.md")

    print(json.dumps({"project_dir": str(project_dir), "created": created}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

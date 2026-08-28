from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree


SLIDE_PATTERN = re.compile(r"^ppt/slides/slide\d+\.xml$")
NOTES_PATTERN = re.compile(r"^ppt/notesSlides/notesSlide\d+\.xml$")
PML_NAMESPACE = "http://schemas.openxmlformats.org/presentationml/2006/main"


def parse_ratio(value: str) -> float:
    try:
        width, height = (float(part) for part in value.split(":", 1))
    except (ValueError, TypeError) as exc:
        raise argparse.ArgumentTypeError("Aspect ratio must look like 16:9") from exc
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("Aspect ratio values must be positive")
    return width / height


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a PPTX package and presentation structure.")
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--expected-slides", type=int)
    parser.add_argument("--require-notes", action="store_true")
    parser.add_argument("--aspect-ratio", type=parse_ratio, default=parse_ratio("16:9"))
    parser.add_argument("--ratio-tolerance", type=float, default=0.01)
    args = parser.parse_args()

    pptx = args.pptx.resolve()
    errors: list[str] = []
    report: dict = {"file": str(pptx), "valid": False}
    if not pptx.is_file():
        errors.append("PPTX file does not exist")
    elif not zipfile.is_zipfile(pptx):
        errors.append("File is not a valid ZIP/PPTX package")
    else:
        with zipfile.ZipFile(pptx) as archive:
            corrupt_member = archive.testzip()
            if corrupt_member:
                errors.append(f"Corrupt ZIP member: {corrupt_member}")
            names = archive.namelist()
            slide_count = sum(bool(SLIDE_PATTERN.match(name)) for name in names)
            notes_count = sum(bool(NOTES_PATTERN.match(name)) for name in names)
            media_count = sum(name.startswith("ppt/media/") and not name.endswith("/") for name in names)
            report.update(slide_count=slide_count, notes_count=notes_count, media_count=media_count)

            if args.expected_slides is not None and slide_count != args.expected_slides:
                errors.append(f"Expected {args.expected_slides} slides, found {slide_count}")
            if args.require_notes and notes_count != slide_count:
                errors.append(f"Expected {slide_count} notes slides, found {notes_count}")

            try:
                root = ElementTree.fromstring(archive.read("ppt/presentation.xml"))
                size = root.find(f"{{{PML_NAMESPACE}}}sldSz")
                if size is None:
                    errors.append("presentation.xml has no slide size")
                else:
                    width = int(size.attrib["cx"])
                    height = int(size.attrib["cy"])
                    ratio = width / height
                    report.update(width_emu=width, height_emu=height, aspect_ratio=ratio)
                    if abs(ratio - args.aspect_ratio) > args.ratio_tolerance:
                        errors.append(f"Aspect ratio {ratio:.4f} does not match requested {args.aspect_ratio:.4f}")
            except (KeyError, ValueError, ElementTree.ParseError) as exc:
                errors.append(f"Cannot parse presentation dimensions: {exc}")

        report["sha256"] = sha256(pptx)

    report["errors"] = errors
    report["valid"] = not errors
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())

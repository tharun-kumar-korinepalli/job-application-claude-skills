#!/usr/bin/env python3
"""Sanity-check a resume or cover letter PDF before it goes out.

Checks: text extracts (not a scanned image), page count, file size, the
candidate's name and email appear in the extracted text, and a few common
parser traps (very long lines that hint at a two-column layout, a missing
Experience/Education heading).

Uses pdftotext and pdfinfo (poppler) if present, otherwise falls back to
pypdf if installed. Standard library apart from that.

Usage:
    python check_pdf.py resume.pdf --name "Firstname Lastname" --email name@x.com --pages 1
    python check_pdf.py Bewerbung.pdf --name "Vorname Nachname" --max-mb 5
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

HEADINGS = {
    "en": ["experience", "education", "skills"],
    "de": ["berufserfahrung", "ausbildung", "studium", "kenntnisse", "lebenslauf"],
}


def extract_text(pdf: Path) -> tuple[str, int]:
    if shutil.which("pdftotext"):
        text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
        pages = 0
        if shutil.which("pdfinfo"):
            info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
            m = re.search(r"Pages:\s+(\d+)", info)
            pages = int(m.group(1)) if m else 0
        return text, pages
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        sys.exit("need poppler (pdftotext/pdfinfo) or `pip install pypdf`")
    reader = PdfReader(str(pdf))
    return "\n".join((p.extract_text() or "") for p in reader.pages), len(reader.pages)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--name", help="candidate name that must appear")
    ap.add_argument("--email", help="email that must appear")
    ap.add_argument("--pages", type=int, help="expected page count")
    ap.add_argument("--max-mb", type=float, default=1.0, help="max file size in MB (default 1)")
    ap.add_argument("--lang", choices=["en", "de", "any"], default="any")
    args = ap.parse_args()

    pdf = Path(args.pdf)
    if not pdf.exists():
        sys.exit(f"not found: {pdf}")

    text, pages = extract_text(pdf)
    size_mb = pdf.stat().st_size / (1024 * 1024)
    problems: list[str] = []
    notes: list[str] = []

    words = len(text.split())
    if words < 50:
        problems.append(f"only {words} words extracted; PDF may be a scanned image or text in boxes")
    else:
        notes.append(f"text extracts fine ({words} words)")

    notes.append(f"{pages} page(s), {size_mb:.2f} MB")
    if args.pages and pages != args.pages:
        problems.append(f"expected {args.pages} page(s), got {pages}")
    if size_mb > args.max_mb:
        problems.append(f"file is {size_mb:.2f} MB, over the {args.max_mb} MB limit")

    low = text.lower()
    if args.name and args.name.lower() not in low:
        problems.append(f"name '{args.name}' not found in extracted text")
    if args.email and args.email.lower() not in low:
        problems.append(f"email '{args.email}' not found in extracted text")

    langs = ["en", "de"] if args.lang == "any" else [args.lang]
    if not any(any(h in low for h in HEADINGS[l]) for l in langs):
        problems.append("no standard section heading found (Experience/Education/Skills or German equivalents)")

    long_lines = [ln for ln in text.splitlines() if len(ln) > 140]
    if len(long_lines) > 8:
        problems.append(f"{len(long_lines)} very wide lines; layout may be two-column and parse out of order")

    if re.search(r"\b(responsible for|references available)\b", low):
        problems.append("found 'responsible for' or 'references available'; see writing-bullets.md")
    if "—" in text:
        problems.append("em dash found; house style uses none")

    print(f"Checked {pdf.name}")
    for n in notes:
        print(f"  ok   {n}")
    for p in problems:
        print(f"  FIX  {p}")
    if not problems:
        print("  all checks passed")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()

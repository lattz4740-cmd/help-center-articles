#!/usr/bin/env python3
"""Find bold-only paragraphs in the built HTML that should be headings.

Checks the build output for <p><strong>text</strong></p> patterns that
indicate a bold paragraph being used as a heading instead of an <h2>.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"

# Pattern: <p> containing only <strong>text</strong> (and optional whitespace)
BOLD_P_RE = re.compile(r'<p[^>]*>\s*<strong[^>]*>([^<]+)</strong>\s*</p>')


def main():
    if not BUILD.exists():
        print("No build/ directory found. Run 'npm run build -- --locale en' first.")
        return

    for html_file in sorted(BUILD.rglob("*.html")):
        # Skip 404 and non-doc pages
        rel = html_file.relative_to(BUILD)
        if str(rel).startswith("assets/") or rel.name == "404.html":
            continue

        text = html_file.read_text(encoding="utf-8")
        matches = BOLD_P_RE.findall(text)

        if matches:
            print(f"\n{rel}:")
            for m in matches:
                print(f"  <p><strong>{m[:60]}</strong></p>")


if __name__ == "__main__":
    main()

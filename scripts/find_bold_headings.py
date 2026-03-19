#!/usr/bin/env python3
"""Find English docs that have a mix of ## headings and **bold** lines.

Bold-only lines (like "**What is a VPN?**") that appear in a Q&A pattern
alongside ## headings likely should be ## headings too.

Reports docs where this inconsistency exists.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$', re.MULTILINE)
BOLD_LINE_RE = re.compile(r'^\*\*(.+?)\*\*\s*$', re.MULTILINE)


def main():
    for md_file in sorted(DOCS.rglob("*.md")):
        text = md_file.read_text(encoding="utf-8")

        # Strip frontmatter
        if text.startswith("---"):
            end = text.find("---", 3)
            if end > 0:
                body = text[end + 3:]
            else:
                body = text
        else:
            body = text

        headings = HEADING_RE.findall(body)
        bold_lines = BOLD_LINE_RE.findall(body)

        if headings and bold_lines:
            doc_path = md_file.relative_to(DOCS)
            print(f"\n=== {doc_path} ===")
            print(f"  {len(headings)} heading(s), {len(bold_lines)} bold-only line(s)")
            for level, text in headings:
                print(f"    {level} {text[:60]}")
            for text in bold_lines:
                print(f"    ** {text[:60]}")


if __name__ == "__main__":
    main()

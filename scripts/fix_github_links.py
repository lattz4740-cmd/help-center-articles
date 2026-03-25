#!/usr/bin/env python3
"""Update Jigsaw-Code GitHub links to Outline-Foundation."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REPLACEMENTS = {
    "github.com/Jigsaw-Code/outline-client": "github.com/Outline-Foundation/outline-client",
    "github.com/Jigsaw-Code/outline-brand": "github.com/Outline-Foundation/outline-brand",
    "github.com/jigsaw-Code/?q=outline": "github.com/Outline-Foundation/?q=outline",
    "github.com/Jigsaw-Code/?q=outline": "github.com/Outline-Foundation/?q=outline",
}

# Also update the how-outline-works.md search link
REPLACEMENTS["github.com/search?q=org%3AJigsaw-Code+outline"] = "github.com/search?q=org%3AOutline-Foundation+outline"

total = 0
for md in sorted(ROOT.rglob("*.md")):
    # Skip old-site, node_modules, .git
    rel = str(md.relative_to(ROOT))
    if any(skip in rel for skip in ["old-site/", "node_modules/", ".git/", "partial-translations/"]):
        continue

    text = md.read_text("utf-8")
    new_text = text
    for old, new in REPLACEMENTS.items():
        new_text = new_text.replace(old, new)

    if new_text != text:
        md.write_text(new_text, "utf-8")
        total += 1
        print(f"  FIXED {rel}")

print(f"\nUpdated {total} files")

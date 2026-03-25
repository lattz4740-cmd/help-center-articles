#!/usr/bin/env python3
"""Fix remaining GitHub link issues:
1. Outline-Foundation -> OutlineFoundation (no hyphen)
2. v2tec/watchtower -> containrrr/watchtower
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REPLACEMENTS = {
    "github.com/Outline-Foundation/": "github.com/OutlineFoundation/",
    "github.com/Outline-Foundation?": "github.com/OutlineFoundation?",
    "org%3AOutline-Foundation": "org%3AOutlineFoundation",
    "github.com/v2tec/watchtower": "github.com/containrrr/watchtower",
}

total = 0
for md in sorted(ROOT.rglob("*.md")):
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

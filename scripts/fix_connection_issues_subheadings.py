#!/usr/bin/env python3
"""Convert sub-headings in connection-issues from ## to ### across all translations.

Section titles (with {#anchor} IDs) stay as ##.
Sub-headings like "How to test:", "Things to fix:", "Things to check:" become ###.

Strategy: any ## heading that does NOT have a {#...} anchor is a sub-heading.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def fix_file(filepath):
    """Convert ## headings without anchors to ### in connection-issues."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.split('\n')
    fixes = 0

    for i, line in enumerate(lines):
        # Match ## heading WITHOUT {#anchor}
        if re.match(r'^## \S', line) and '{#' not in line:
            lines[i] = '###' + line[2:]  # ## → ###
            fixes += 1

    if fixes > 0:
        filepath.write_text('\n'.join(lines), encoding='utf-8')
    return fixes


def main():
    total = 0

    for locale in get_locales():
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "connection-issues.md"
        if not f.exists():
            continue
        n = fix_file(f)
        if n:
            print(f"  {locale}: converted {n} sub-heading(s) to ###")
            total += n

    print(f"\nDone: {total} sub-headings converted")


if __name__ == "__main__":
    main()

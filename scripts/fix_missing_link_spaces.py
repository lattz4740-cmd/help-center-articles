#!/usr/bin/env python3
"""Add missing space before markdown links across all docs and translations.

The GKMS converter sometimes drops the space between a word and a markdown
link, producing e.g. 'certain[OAuth](url)' instead of 'certain [OAuth](url)'.

This script finds all occurrences where a Latin letter or digit immediately
precedes a markdown link '[text](url)' and inserts a space.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

# Match a Latin letter/digit immediately before a markdown link
PATTERN = re.compile(r'([a-zA-Z0-9])\[([^\]]+)\]\(')


def fix_file(filepath):
    text = filepath.read_text(encoding="utf-8")
    new_text = PATTERN.sub(r'\1 [\2](', text)
    if new_text != text:
        fixes = len(PATTERN.findall(text))
        filepath.write_text(new_text, encoding="utf-8")
        return fixes
    return 0


def main():
    total = 0

    # Fix English docs
    for f in sorted(DOCS.rglob("*.md")):
        n = fix_file(f)
        if n:
            print(f"  en/{f.relative_to(DOCS)}: fixed {n}")
            total += n

    for f in sorted(DOCS.rglob("*.mdx")):
        n = fix_file(f)
        if n:
            print(f"  en/{f.relative_to(DOCS)}: fixed {n}")
            total += n

    # Fix translations
    for d in sorted(I18N.iterdir()):
        if not d.is_dir() or d.name == "partial-translations":
            continue
        docs_dir = d / "docusaurus-plugin-content-docs" / "current"
        if not docs_dir.exists():
            continue
        for f in sorted(docs_dir.rglob("*.md")):
            n = fix_file(f)
            if n:
                rel = f.relative_to(docs_dir)
                print(f"  {d.name}/{rel}: fixed {n}")
                total += n

    print(f"\nDone: {total} missing spaces fixed")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Fix bold-only lines with trailing punctuation outside the bold markers.

Patterns like: **text**. or **text**: or **text**:
These weren't caught by the earlier bold-to-heading regex because the
punctuation is outside the ** markers.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

# Match: **text**<punctuation> on its own line (not already a heading)
# The punctuation (.:;,) is outside the bold markers
BOLD_TRAILING_RE = re.compile(r'^(\*{2,4})(.+?)\1([.,:;!?]?\s*)$', re.MULTILINE)


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def fix_bold_trailing(filepath, label):
    """Convert bold lines with trailing punctuation to ## headings."""
    text = filepath.read_text(encoding="utf-8")
    # Replace **text**. or **text**: with ## text. or ## text:
    new_text = BOLD_TRAILING_RE.sub(r'## \2\3', text)
    if new_text != text:
        count = len(BOLD_TRAILING_RE.findall(text))
        filepath.write_text(new_text, encoding="utf-8")
        print(f"  {label}: converted {count} bold line(s)")
        return count
    return 0


def main():
    total = 0

    # Fix English
    for en_file in sorted(DOCS.rglob("*.md")):
        doc_path = str(en_file.relative_to(DOCS))
        total += fix_bold_trailing(en_file, f"en/{doc_path}")

    # Fix translations
    for locale in get_locales():
        locale_dir = I18N / locale / "docusaurus-plugin-content-docs" / "current"
        for tr_file in sorted(locale_dir.rglob("*.md")):
            doc_path = str(tr_file.relative_to(locale_dir))
            total += fix_bold_trailing(tr_file, f"{locale}/{doc_path}")

    print(f"\nDone: {total} bold lines converted")


if __name__ == "__main__":
    main()

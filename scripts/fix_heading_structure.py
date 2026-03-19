#!/usr/bin/env python3
"""Fix heading level mismatches between English and translations.

For each translation where the heading count matches English but levels differ,
remap the heading levels to match English positionally.

For translations with extra/missing headings, skip (too complex to auto-fix).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

HEADING_RE = re.compile(r'^(#{1,6})(\s+.*)$', re.MULTILINE)


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def extract_heading_levels(text):
    return [len(m.group(1)) for m in HEADING_RE.finditer(text)]


def fix_heading_levels_to_match(en_text, tr_filepath):
    """Fix heading levels in translation to match English positions."""
    tr_text = tr_filepath.read_text(encoding="utf-8")

    en_headings = list(HEADING_RE.finditer(en_text))
    tr_headings = list(HEADING_RE.finditer(tr_text))

    en_levels = [len(m.group(1)) for m in en_headings]
    tr_levels = [len(m.group(1)) for m in tr_headings]

    if en_levels == tr_levels:
        return 0  # Already matches

    if len(en_headings) != len(tr_headings):
        return 0  # Count mismatch — can't do positional fix

    # Remap each translation heading to match English level
    new_text = tr_text
    fixes = 0
    for i in range(len(tr_headings) - 1, -1, -1):
        en_level = len(en_headings[i].group(1))
        tr_match = tr_headings[i]
        tr_level = len(tr_match.group(1))

        if en_level != tr_level:
            new_prefix = "#" * en_level
            rest = tr_match.group(2)  # includes space + heading text
            new_text = new_text[:tr_match.start()] + new_prefix + rest + new_text[tr_match.end():]
            fixes += 1

    if fixes > 0:
        tr_filepath.write_text(new_text, encoding="utf-8")
    return fixes


def main():
    total_fixes = 0
    total_files = 0

    for en_file in sorted(DOCS.rglob("*.md")):
        doc_path = str(en_file.relative_to(DOCS).with_suffix(""))
        en_text = en_file.read_text(encoding="utf-8")
        en_levels = extract_heading_levels(en_text)

        if not en_levels:
            continue  # No headings in English

        for locale in get_locales():
            tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
            if not tr_file.exists():
                continue

            fixes = fix_heading_levels_to_match(en_text, tr_file)
            if fixes:
                print(f"  {locale}/{doc_path}: fixed {fixes} heading level(s)")
                total_fixes += fixes
                total_files += 1

    print(f"\nDone: {total_fixes} heading level fixes in {total_files} files")


if __name__ == "__main__":
    main()

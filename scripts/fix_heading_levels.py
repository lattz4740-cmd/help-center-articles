#!/usr/bin/env python3
"""Fix heading level mismatches between English and translations.

1. Arabic connection-issues: #### → ## (all headings at wrong level)
2. connecting-device: bold line → ## heading in translations missing it
3. it/google-cloud: bold lines → ## headings
4. General: find all docs where translations use different heading levels
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$', re.MULTILINE)
BOLD_LINE_RE = re.compile(r'^(\*{2,4})(.+?)\1\s*$', re.MULTILINE)


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def extract_heading_levels(text):
    return [len(m.group(1)) for m in HEADING_RE.finditer(text)]


def fix_heading_level(filepath, from_level, to_level):
    """Change all headings of from_level to to_level."""
    text = filepath.read_text(encoding="utf-8")
    from_prefix = "#" * from_level
    to_prefix = "#" * to_level
    pattern = re.compile(r'^' + re.escape(from_prefix) + r'(\s+)', re.MULTILINE)

    new_text = pattern.sub(to_prefix + r'\1', text)
    if new_text != text:
        filepath.write_text(new_text, encoding="utf-8")
        return 1
    return 0


def fix_bold_to_headings_in_file(filepath):
    """Convert bold-only lines to ## headings in a single file."""
    text = filepath.read_text(encoding="utf-8")
    new_text = BOLD_LINE_RE.sub(r'## \2', text)
    if new_text != text:
        filepath.write_text(new_text, encoding="utf-8")
        count = len(BOLD_LINE_RE.findall(text))
        return count
    return 0


def main():
    total = 0

    # Fix Arabic connection-issues: #### → ##
    print("1. Fixing Arabic connection-issues #### → ##...")
    f = I18N / "ar" / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "connection-issues.md"
    if f.exists():
        n = fix_heading_level(f, 4, 2)
        if n:
            print(f"   ar: fixed heading levels")
            total += n

    # Fix bold-only lines in all translations for docs that have them
    print("2. Fixing bold-only lines in all translations...")
    # Check all English docs for headings, then check translations for bold lines
    for en_file in sorted(DOCS.rglob("*.md")):
        doc_path = str(en_file.relative_to(DOCS).with_suffix(""))
        en_text = en_file.read_text(encoding="utf-8")
        en_bolds = BOLD_LINE_RE.findall(en_text)

        for locale in get_locales():
            tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
            if not tr_file.exists():
                continue
            n = fix_bold_to_headings_in_file(tr_file)
            if n:
                print(f"   {locale}/{doc_path}: converted {n} bold line(s)")
                total += n

    # Fix English docs too (catch any remaining)
    print("3. Fixing bold-only lines in English docs...")
    for en_file in sorted(DOCS.rglob("*.md")):
        doc_path = str(en_file.relative_to(DOCS).with_suffix(""))
        n = fix_bold_to_headings_in_file(en_file)
        if n:
            print(f"   en/{doc_path}: converted {n} bold line(s)")
            total += n

    print(f"\nDone: {total} fixes")


if __name__ == "__main__":
    main()

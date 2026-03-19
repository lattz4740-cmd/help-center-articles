#!/usr/bin/env python3
"""Convert bold-only lines to ## headings in docs that have a mix.

Applies to English docs first, then propagates to all translations.

Rules:
- Only converts **bold** lines that are standalone paragraphs (own line)
- Only in docs that ALSO have ## headings (indicating the bold lines should
  be headings too for consistency)
- Skips docs where bold is used for emphasis within paragraphs

Docs to fix:
- about/terminology: 6 bold Q&A items → ## headings
- client/troubleshooting/connection-issues: 1 bold "How to test:" → ## heading
- manager/server-setup/setup-faqs: 1 bold "Can I use..." → ## heading
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

# Matches **text**, ***text***, ****text**** on a line by itself
BOLD_LINE_RE = re.compile(r'^(\*{2,4})(.+?)\1\s*$', re.MULTILINE)

# Docs where bold-only lines should become ## headings
DOCS_TO_FIX = [
    "about/data-collection",
    "about/terminology",
    "about/how-outline-works",
    "client/troubleshooting/connection-issues",
    "manager/server-management/data-limits",
    "manager/server-management/manage-access-keys",
    "manager/server-setup/setup-faqs",
    "manager/server-setup/setup-server",
]


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def convert_bold_to_headings(filepath):
    """Convert standalone **bold** lines to ## headings."""
    text = filepath.read_text(encoding="utf-8")
    new_text = BOLD_LINE_RE.sub(r'## \2', text)
    if new_text != text:
        filepath.write_text(new_text, encoding="utf-8")
        count = len(BOLD_LINE_RE.findall(text))
        return count
    return 0


def main():
    total = 0

    for doc_path in DOCS_TO_FIX:
        # Fix English
        en_file = DOCS / f"{doc_path}.md"
        if en_file.suffix == ".mdx":
            en_file = DOCS / f"{doc_path}.mdx"
        if en_file.exists():
            n = convert_bold_to_headings(en_file)
            if n:
                print(f"  en/{doc_path}: converted {n} bold line(s) to headings")
                total += n

        # Fix all translations
        for locale in get_locales():
            tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
            if not tr_file.exists():
                continue
            n = convert_bold_to_headings(tr_file)
            if n:
                print(f"  {locale}/{doc_path}: converted {n} bold line(s) to headings")
                total += n

    print(f"\nDone: {total} bold lines converted to headings")


if __name__ == "__main__":
    main()

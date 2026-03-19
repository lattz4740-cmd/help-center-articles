#!/usr/bin/env python3
"""Fix list continuation indentation in setup-server.md across all translations.

The continuation paragraph after numbered list item 1 has only 1 space of
indentation, which breaks the list in Docusaurus/MDX. This script changes
it to 4 spaces so items 1, 2, 3 render as a proper numbered list.

Also removes stray 1-space indentation from non-list content paragraphs
(under headings), which is a GKMS conversion artifact.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"


def fix_file(filepath):
    text = filepath.read_text(encoding="utf-8")
    lines = text.split('\n')
    fixes = 0

    in_list = False
    after_item_1 = False

    for i, line in enumerate(lines):
        # Track if we're inside the numbered list
        if re.match(r'^1\. ', line):
            in_list = True
            after_item_1 = True
            continue
        if re.match(r'^2\. ', line):
            after_item_1 = False
            continue
        if re.match(r'^3\. ', line):
            in_list = False
            continue

        # Fix the list continuation paragraph (between items 1 and 2)
        if after_item_1 and re.match(r'^ {1,4}\S', line):
            new_line = '    ' + line.lstrip()
            if lines[i] != new_line:
                lines[i] = new_line
                fixes += 1
        # Remove stray 1-space indent from non-list content paragraphs
        elif not in_list and re.match(r'^ {1,4}\S', line) and not re.match(r'^#{1,6} ', line):
            new_line = line.lstrip()
            if lines[i] != new_line:
                lines[i] = new_line
                fixes += 1

    if fixes > 0:
        filepath.write_text('\n'.join(lines), encoding='utf-8')
    return fixes


def main():
    total = 0

    # Fix English too
    en = ROOT / "docs" / "manager" / "server-setup" / "setup-server.md"
    if en.exists():
        n = fix_file(en)
        if n:
            print(f"  en: fixed {n} line(s)")
            total += n

    for d in sorted(I18N.iterdir()):
        if not d.is_dir() or d.name == "partial-translations":
            continue
        f = d / "docusaurus-plugin-content-docs" / "current" / "manager" / "server-setup" / "setup-server.md"
        if not f.exists():
            continue
        n = fix_file(f)
        if n:
            print(f"  {d.name}: fixed {n} line(s)")
            total += n

    print(f"\nDone: {total} fixes")


if __name__ == "__main__":
    main()

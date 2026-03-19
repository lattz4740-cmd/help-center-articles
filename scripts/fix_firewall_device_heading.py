#!/usr/bin/env python3
"""Fix 7 locales missing the device firewall heading in firewall-errors.

The GKMS source has the device firewall title as inline bold at the start
of a paragraph (not a standalone bold paragraph), so the converter didn't
turn it into a heading. We need to find the bold text and split it out
as a ## heading.

Pattern in the markdown: text starts with bold that's the section title,
followed by the section content in the same paragraph.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

LOCALES = ["am", "bn", "hy", "km", "ne", "zh-Hant", "zh-HK"]


def fix_file(filepath):
    """Find inline bold at paragraph start that should be a heading."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.split('\n')

    # The file has 2 headings (network, server). Between them is the device
    # firewall content as a plain paragraph starting with bold text.
    # Find the content between the two existing ## headings.
    heading_indices = [i for i, line in enumerate(lines) if line.startswith('## ')]

    if len(heading_indices) < 2:
        return 0

    # Look between heading 1 and heading 2 for a line starting with bold
    start = heading_indices[0]
    end = heading_indices[1]

    for i in range(start + 1, end):
        line = lines[i]
        # Match line starting with **bold text** followed by more content
        m = re.match(r'^(\*\*[^*]+\*\*[.。:：]?)\s*(.+)$', line)
        if m:
            bold_part = m.group(1)
            rest = m.group(2)
            # Extract the bold text without markers
            heading_text = re.sub(r'^\*+|\*+[.。:：]?$', '', bold_part).strip()

            # Replace the line with a heading + paragraph
            lines[i] = f'## {heading_text}\n\n{rest}'
            filepath.write_text('\n'.join(lines), encoding='utf-8')
            return 1

    return 0


def main():
    total = 0
    for locale in LOCALES:
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "firewall-errors.md"
        if not f.exists():
            continue
        n = fix_file(f)
        if n:
            print(f"  {locale}: added device firewall heading")
            total += n
        else:
            print(f"  {locale}: could not find inline bold to split")

    print(f"\nDone: {total} fixes")


if __name__ == "__main__":
    main()

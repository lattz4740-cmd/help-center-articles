#!/usr/bin/env python3
"""Fix quay.io link swaps in kk, mr, ta, vi how-outline-works.

These locales had the two quay.io links swapped. The first fix corrected
link 1 but made link 2 wrong. Now fix link 2 to match English.

English order: link 1 = quay.io/, link 2 = quay.io/repository/...
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

LINK_RE = re.compile(r'(?<!!)\[([^\]\\]*(?:\\.[^\]\\]*)*)\]\(([^)]+)\)')


def main():
    fixes = 0
    en_links_order = [
        "https://quay.io/",
        "https://quay.io/repository/outline/shadowbox?tab=tags",
    ]

    for locale in ["kk", "mr", "ta", "vi"]:
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "about" / "how-outline-works.md"
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8")

        # Find all quay.io links
        quay_matches = [(m.start(), m.end(), m.group(1), m.group(2))
                        for m in LINK_RE.finditer(text) if "quay.io" in m.group(2)]

        if len(quay_matches) < 2:
            continue

        # Check if link 2 needs fixing (should be the repo URL)
        if quay_matches[1][3] == "https://quay.io/":
            new_text = text[:quay_matches[1][0]] + \
                       f"[{quay_matches[1][2]}](https://quay.io/repository/outline/shadowbox?tab=tags)" + \
                       text[quay_matches[1][1]:]
            f.write_text(new_text, encoding="utf-8")
            print(f"  {locale}: fixed quay.io link 2")
            fixes += 1

    print(f"\nDone: {fixes} fixes")


if __name__ == "__main__":
    main()

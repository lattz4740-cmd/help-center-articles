#!/usr/bin/env python3
"""Fix broken URL wrap in install-linux code blocks across translations.

The GKMS source introduced a line break in the middle of the download URL:
  outline-      releases/client/linux
should be:
  outline-releases/client/linux
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"


def main():
    fixes = 0
    pattern = re.compile(r'outline-\s+releases')

    for locale_dir in sorted(I18N.iterdir()):
        if not locale_dir.is_dir() or locale_dir.name == "partial-translations":
            continue
        f = locale_dir / "docusaurus-plugin-content-docs" / "current" / "client" / "getting-started" / "install-linux.md"
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8")
        if pattern.search(text):
            new_text = pattern.sub("outline-releases", text)
            f.write_text(new_text, encoding="utf-8")
            print(f"  {locale_dir.name}: fixed broken URL")
            fixes += 1

    print(f"\nDone: {fixes} files fixed")


if __name__ == "__main__":
    main()

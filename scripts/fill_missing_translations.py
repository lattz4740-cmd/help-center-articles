#!/usr/bin/env python3
"""Fill missing translations by copying from English source.

For locales like en-GB where content is identical to English, copies the
English doc. For other locales, reports that the translation doesn't exist
on Google's support site.
"""

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

# Missing translations to fill by copying English source.
# These are en-GB articles that are identical to English.
COPY_FROM_ENGLISH = [
    ("en-GB", "client/troubleshooting/firewall-errors"),
    ("en-GB", "client/troubleshooting/internet-access"),
    ("en-GB", "manager/server-setup/cost"),
    ("en-GB", "manager/server-setup/multiple-servers"),
    ("en-GB", "manager/server-setup/setup-faqs"),
]

# Missing translations that don't exist on Google's support site.
# These are genuinely untranslated articles.
NOT_AVAILABLE = [
    ("es", "about/access-resources-blocked"),
    ("es", "client/troubleshooting/firewall-errors"),
    ("ms", "about/brand-usage"),
    ("ms", "about/getoutline-me-telegram"),
    ("ms", "about/how-outline-works"),
    ("pl", "about/getoutline-me-telegram"),
    ("pt", "about/how-outline-works"),
    ("pt-BR", "client/troubleshooting/firewall-errors"),
    ("ru", "about/access-resources-blocked"),
]


def main():
    copied = 0
    for locale, doc_path in COPY_FROM_ENGLISH:
        src = DOCS / f"{doc_path}.md"
        dst = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"

        if not src.exists():
            print(f"  ERROR: English source not found: {src}")
            continue

        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"  COPIED {locale}/{doc_path} (from English)")
        copied += 1

    print(f"\nCopied {copied} files from English")
    print(f"\n{len(NOT_AVAILABLE)} translations not available on Google support:")
    for locale, doc_path in NOT_AVAILABLE:
        print(f"  {locale}/{doc_path}")


if __name__ == "__main__":
    main()

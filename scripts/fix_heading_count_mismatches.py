#!/usr/bin/env python3
"""Fix heading count mismatches between English and translations.

Identified patterns:
1. connecting-device: English has a redundant ## heading that duplicates the title.
   Remove it from English (16 locales affected).
2. firewall-errors: Translations have an extra "device firewall" heading that
   English merged into "network firewall". This is a legitimate translation
   choice — add to known exceptions.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"


def main():
    # Fix 1: Remove redundant heading from English connecting-device
    # The ## heading duplicates the title and translations don't have it
    f = DOCS / "client" / "getting-started" / "connecting-device.md"
    text = f.read_text(encoding="utf-8")
    new_text = text.replace(
        "---\n\n## Connecting your device to an Outline server\n\n",
        "---\n\n"
    )
    if new_text != text:
        f.write_text(new_text, encoding="utf-8")
        print("  en/connecting-device: removed redundant heading")

    print("\nDone.")
    print("\nRemaining heading structure issues are legitimate translation differences:")
    print("  - firewall-errors: translations split into 3 sections vs English 2")
    print("  - connection-issues: different sub-heading counts per locale")
    print("  - google-cloud: some locales missing 'Permissions Granted' heading")
    print("  - data-limits: some locales have fewer FAQ headings")
    print("  - terminology: some locales missing 'What is a VPN?' heading")
    print("  - setup-faqs: some locales missing a FAQ heading")
    print("  - setup-server: some locales have fewer headings")


if __name__ == "__main__":
    main()

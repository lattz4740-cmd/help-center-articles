#!/usr/bin/env python3
"""Check what extra links remain in connection-issues translations.

After the bullet list cleanup, 23 locales still have 9 links vs English's 8.
This script identifies which link is the extra one.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_translations as v

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

en_text = (ROOT / "docs" / "client" / "troubleshooting" / "connection-issues.md").read_text("utf-8")
en_links = v.extract_link_urls(en_text)
en_norm = [v.normalize_link_url(u) for u in en_links]

print(f"English links ({len(en_links)}):")
for i, (raw, norm) in enumerate(zip(en_links, en_norm)):
    print(f"  {i+1}. {raw}  →  {norm}")
print()

# Check a few locales that still have 9 links
for locale in ["am", "bn", "da", "he", "sw"]:
    f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "connection-issues.md"
    if not f.exists():
        continue
    tr_text = f.read_text("utf-8")
    tr_links = v.extract_link_urls(tr_text)
    tr_norm = [v.normalize_link_url(u) for u in tr_links]

    if len(tr_links) != len(en_links):
        print(f"{locale} links ({len(tr_links)}):")
        for i, (raw, norm) in enumerate(zip(tr_links, tr_norm)):
            marker = " ←EXTRA" if norm not in en_norm else ""
            # Check if this link appears more times than in English
            if tr_norm[:i+1].count(norm) > en_norm.count(norm):
                marker = " ←DUPLICATE"
            print(f"  {i+1}. {raw}{marker}")
        print()

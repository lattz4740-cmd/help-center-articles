#!/usr/bin/env python3
"""Show detailed link comparisons for remaining issues."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_translations as v

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

def show_links(doc_path, locales):
    en_text = (ROOT / "docs" / f"{doc_path}.md").read_text("utf-8")
    en_links = v.extract_link_urls(en_text)
    en_norm = [v.normalize_link_url(u) for u in en_links]
    print(f"\n=== {doc_path} ===")
    print(f"English ({len(en_links)}): {en_links}")

    for locale in locales:
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
        if not f.exists():
            continue
        tr_text = f.read_text("utf-8")
        tr_links = v.extract_link_urls(tr_text)
        if len(tr_links) != len(en_links) or [v.normalize_link_url(u) for u in tr_links] != en_norm:
            print(f"  {locale} ({len(tr_links)}): {tr_links}")

# Check remaining issues
show_links("about/feedback", ["en-GB", "ar"])
show_links("client/troubleshooting/windows-install", ["de", "es", "fr", "ru"])
show_links("manager/server-management/delete-server", ["ru"])

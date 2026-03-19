#!/usr/bin/env python3
"""Investigate all remaining heading structure issues doc by doc.

For each doc with issues, shows:
- English heading structure
- Each affected locale's heading structure
- The GKMS source HTML structure for those locales
"""

import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup, Tag

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"
OLD_SITE = ROOT / "old-site" / "Help Center"

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$', re.MULTILINE)

# WEB IDs for affected docs
DOC_WEB_IDS = {
    "client/troubleshooting/connection-issues": "15330818",
    "manager/server-setup/google-cloud": "15331428",
    "manager/server-setup/setup-server": "15331530",
    "manager/server-management/data-limits": "15331223",
    "about/terminology": "15330920",
    "manager/server-setup/setup-faqs": "15331728",
    "manager/server-management/manage-access-keys": "15331326",
}

# Map docusaurus locale to GKMS locale
LOCALE_MAP = {"he": "iw", "nb": "no"}


def get_headings(filepath):
    text = filepath.read_text(encoding="utf-8")
    return [(len(m.group(1)), m.group(2)[:60]) for m in HEADING_RE.finditer(text)]


def find_webs_file(gkms_locale):
    matches = list(OLD_SITE.glob(f"WEBS_*_{gkms_locale}.HTML"))
    return matches[0] if matches else None


def get_gkms_bold_paragraphs(webs_file, web_id):
    """Get all bold-only paragraphs from a GKMS article."""
    with open(webs_file, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # Find the article
    web_div = None
    for div in soup.find_all("div", class_="gkms"):
        classes = div.get("class", [])
        text = div.get_text(strip=True)
        if "id" in classes and "notranslate" in classes:
            m = re.match(r"WEB:(\d+)", text)
            if m and m.group(1) == web_id:
                sibling = div.next_sibling
                while sibling:
                    if isinstance(sibling, Tag) and "web" in (sibling.get("class") or []):
                        web_div = sibling
                        break
                    sibling = sibling.next_sibling
                break

    if not web_div:
        return []

    results = []
    for p in web_div.find_all("p"):
        children = [c for c in p.children if not (isinstance(c, str) and not c.strip())]
        if len(children) == 1 and isinstance(children[0], Tag) and children[0].name in ("strong", "b"):
            results.append(("BOLD_P", children[0].get_text(strip=True)[:60]))
        elif children:
            first = children[0]
            if isinstance(first, Tag) and first.name in ("strong", "b"):
                bold_text = first.get_text(strip=True)
                full_text = p.get_text(strip=True)
                if len(bold_text) > 10 and full_text.startswith(bold_text):
                    results.append(("INLINE_BOLD", bold_text[:60]))
    return results


def main():
    # Get affected locales per doc from verify output
    import subprocess
    result = subprocess.run(
        [sys.executable, "scripts/verify_translations.py"],
        capture_output=True, text=True, timeout=120
    )

    affected = {}  # doc_path -> [locales]
    for line in result.stdout.split('\n'):
        m = re.match(r'\s+\[HEADING_STRUCTURE\] ([^/]+)/(.+?): Heading levels differ: English=(\[.*?\]), translation=(\[.*?\])', line)
        if m:
            locale = m.group(1)
            doc_path = m.group(2)
            en_levels = m.group(3)
            tr_levels = m.group(4)
            if doc_path not in affected:
                affected[doc_path] = []
            affected[doc_path].append((locale, en_levels, tr_levels))

    for doc_path, locales in sorted(affected.items()):
        en_file = DOCS / f"{doc_path}.md"
        en_headings = get_headings(en_file)
        web_id = DOC_WEB_IDS.get(doc_path, "?")

        print(f"\n{'='*70}")
        print(f"=== {doc_path} (WEB:{web_id}, {len(locales)} locales) ===")
        print(f"EN headings ({len(en_headings)}):")
        for level, text in en_headings:
            print(f"  H{level} {text}")

        for locale, en_levels, tr_levels in locales:
            tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
            tr_headings = get_headings(tr_file)
            print(f"\n{locale}: {tr_levels}")
            for level, text in tr_headings:
                print(f"  H{level} {text}")

            # Check GKMS source
            gkms_locale = LOCALE_MAP.get(locale, locale)
            webs_file = find_webs_file(gkms_locale)
            if webs_file:
                bolds = get_gkms_bold_paragraphs(webs_file, web_id)
                if bolds:
                    print(f"  GKMS bold paragraphs:")
                    for kind, text in bolds:
                        print(f"    {kind}: {text}")

            # Only show first 2 locales per doc to keep output manageable
            if locales.index((locale, en_levels, tr_levels)) >= 1:
                remaining = len(locales) - 2
                if remaining > 0:
                    print(f"\n  ... and {remaining} more locale(s) with same pattern")
                break


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Check the GKMS source HTML for the device firewall heading in the 7 problem locales."""

import re
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
OLD_SITE = ROOT / "old-site"
HELP_CENTER = OLD_SITE / "Help Center"

# WEB ID for firewall-errors
WEB_ID = "15528599"

# GKMS locale codes for the 7 problem locales
LOCALES = {
    "am": "am",
    "bn": "bn",
    "hy": "hy",
    "km": "km",
    "ne": "ne",
    "zh-Hant": "zh-Hant",
    "zh-HK": "zh-HK",
}


def find_webs_file(locale):
    pattern = f"WEBS_*_{locale}.HTML"
    matches = list(HELP_CENTER.glob(pattern))
    return matches[0] if matches else None


def extract_article_html(webs_file, web_id):
    """Extract raw HTML for a specific article from a WEBS file."""
    with open(webs_file, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    for div in soup.find_all("div", class_="gkms"):
        classes = div.get("class", [])
        text = div.get_text(strip=True)
        if "id" in classes and "notranslate" in classes:
            m = re.match(r"WEB:(\d+)", text)
            if m and m.group(1) == web_id:
                # Find the web content div
                sibling = div.next_sibling
                while sibling:
                    if hasattr(sibling, "get") and "web" in (sibling.get("class") or []):
                        return str(sibling)
                    sibling = sibling.next_sibling
    return None


def main():
    for docusaurus_locale, gkms_locale in LOCALES.items():
        webs_file = find_webs_file(gkms_locale)
        if not webs_file:
            print(f"{docusaurus_locale}: No WEBS file found")
            continue

        html = extract_article_html(webs_file, WEB_ID)
        if not html:
            print(f"{docusaurus_locale}: Article WEB:{WEB_ID} not found")
            continue

        # Look for bold/strong text that mentions device/firewall
        soup = BeautifulSoup(html, "html.parser")
        print(f"\n=== {docusaurus_locale} ({webs_file.name}) ===")

        # Show all <strong> and <b> tags
        for tag in soup.find_all(["strong", "b"]):
            text = tag.get_text(strip=True)
            if len(text) > 10:  # Skip short inline bold
                parent = tag.parent
                # Check if this is a standalone bold paragraph
                if parent and parent.name == "p":
                    sibling_text = parent.get_text(strip=True)
                    if sibling_text == text or sibling_text == text + ".":
                        print(f"  BOLD PARAGRAPH: <{parent.name}><strong>{text[:80]}</strong></{parent.name}>")
                    else:
                        print(f"  INLINE BOLD: ...{text[:60]}... (in longer paragraph)")


if __name__ == "__main__":
    main()

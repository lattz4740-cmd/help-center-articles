#!/usr/bin/env python3
"""Fetch missing translations from support.google.com/outline.

For each locale+doc that's missing a translation in i18n/, tries to fetch
the article from Google's support site and convert it to Markdown.
"""

import json
import re
import subprocess
import sys
import time
from pathlib import Path

from bs4 import BeautifulSoup

# Import shared converter functions
sys.path.insert(0, str(Path(__file__).parent))
from convert_gkms import WEB_ID_TO_DOC, remap_link, yaml_quote

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

# Reverse map: doc_path → WEB ID
DOC_TO_WEB_ID = {path: wid for wid, path in WEB_ID_TO_DOC.items()}

# Docusaurus locale → Google hl parameter
LOCALE_TO_HL = {
    "he": "iw",
    "nb": "no",
}

# Docs that only exist in English (no translation expected)
ENGLISH_ONLY = {"index"}

LOCALES = [
    "af", "am", "ar", "ar-EG", "as", "az", "be", "bg", "bn", "bs",
    "ca", "cs", "cy", "da", "de", "de-CH", "el", "en-AU", "en-CA", "en-GB",
    "en-IN", "en-SG", "es", "es-419", "et", "eu", "fa", "fi", "fil", "fr",
    "fr-CA", "ga", "gl", "gu", "ha", "he", "hi", "hr", "hu", "hy", "id",
    "is", "it", "ja", "ka", "kk", "km", "kn", "ko", "ky", "lo", "lt", "lv",
    "mk", "ml", "mn", "mr", "ms", "my", "nb", "ne", "nl", "or", "pa", "pl",
    "pt", "pt-BR", "ro", "ru", "si", "sk", "sl", "sq", "sr", "sv", "sw",
    "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "yo", "zh-Hans",
    "zh-Hant", "zh-HK", "zu",
]


def get_english_doc_paths():
    """Get all doc paths relative to docs/, without extension."""
    paths = set()
    for f in DOCS.rglob("*.md"):
        rel = f.relative_to(DOCS).with_suffix("")
        paths.add(str(rel))
    return paths


def get_translated_doc_paths(locale):
    """Get existing translated doc paths for a locale."""
    locale_dir = I18N / locale / "docusaurus-plugin-content-docs" / "current"
    if not locale_dir.exists():
        return set()
    paths = set()
    for f in locale_dir.rglob("*.md"):
        rel = f.relative_to(locale_dir).with_suffix("")
        paths.add(str(rel))
    return paths


def fetch_article(web_id, hl):
    """Fetch article HTML from support.google.com. Returns (title, body_html) or None."""
    url = f"https://support.google.com/outline/answer/{web_id}?hl={hl}"
    try:
        result = subprocess.run(
            ["curl", "-s", "-L", "--max-time", "10", url],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode != 0:
            return None
        html = result.stdout
    except subprocess.TimeoutExpired:
        return None

    soup = BeautifulSoup(html, "html.parser")

    # Extract title from <h1>
    h1 = soup.find("h1")
    if not h1:
        return None
    title = h1.get_text(strip=True)

    # Find the article body - Google support uses various container classes
    body = None
    for selector in [
        ("div", {"class": "article-container"}),
        ("div", {"class": "hcfe-content"}),
        ("section", {"class": "article-body"}),
    ]:
        body = soup.find(*selector)
        if body:
            break

    # Fallback: look for the main content area
    if not body:
        # Try finding content after h1
        main = soup.find("main") or soup.find("div", {"role": "main"})
        if main:
            body = main

    if not body:
        return None

    return title, body


def convert_google_body(body_element):
    """Convert Google support page body HTML to Markdown."""
    lines = []

    for element in body_element.children:
        if not hasattr(element, "name") or element.name is None:
            text = str(element).strip()
            if text:
                lines.append(text)
            continue

        if element.name in ("h2", "h3", "h4"):
            level = int(element.name[1])
            text = element.get_text(strip=True)
            if text:
                lines.append(f"{'#' * level} {text}")

        elif element.name == "p":
            text = convert_inline_google(element)
            if text.strip():
                lines.append(text.strip())

        elif element.name in ("ul", "ol"):
            lines.append(convert_list_google(element))

        elif element.name == "pre":
            code = element.get_text()
            lines.append(f"```\n{code.strip()}\n```")

        elif element.name == "table":
            lines.append(convert_table_google(element))

        elif element.name == "div":
            # Recurse into divs
            inner = convert_google_body(element)
            if inner.strip():
                lines.append(inner)

        elif element.name == "img":
            alt = element.get("alt", "")
            src = element.get("src", "")
            if src:
                lines.append(f"![{alt}]({src})")

    return "\n\n".join(line for line in lines if line.strip())


def convert_inline_google(element):
    """Convert inline HTML to markdown text."""
    if not hasattr(element, "children"):
        text = str(element)
        text = text.replace("\xa0", " ")
        return text

    parts = []
    for child in element.children:
        if not hasattr(child, "name") or child.name is None:
            text = str(child).replace("\xa0", " ")
            parts.append(text)
        elif child.name in ("strong", "b"):
            inner = convert_inline_google(child).strip()
            if inner:
                parts.append(f"**{inner}**")
        elif child.name in ("em", "i"):
            inner = convert_inline_google(child).strip()
            if inner:
                parts.append(f"*{inner}*")
        elif child.name == "a":
            href = child.get("href", "")
            href = remap_link(href)
            text = convert_inline_google(child).strip()
            if text and href:
                parts.append(f"[{text}]({href})")
            elif text:
                parts.append(text)
        elif child.name == "code":
            parts.append(f"`{child.get_text()}`")
        elif child.name == "br":
            parts.append("\n")
        else:
            parts.append(convert_inline_google(child))

    return "".join(parts)


def convert_list_google(element, indent=0):
    """Convert HTML list to markdown."""
    lines = []
    ordered = element.name == "ol"
    counter = 1
    for child in element.children:
        if not hasattr(child, "name") or child.name != "li":
            continue
        prefix = f"{counter}. " if ordered else "- "
        indent_str = "   " * indent

        # Check for nested lists
        nested = child.find(["ul", "ol"])
        text = ""
        for item in child.children:
            if hasattr(item, "name") and item.name in ("ul", "ol"):
                continue
            text += convert_inline_google(item)
        text = re.sub(r"\s+", " ", text).strip()
        lines.append(f"{indent_str}{prefix}{text}")

        if nested:
            lines.append(convert_list_google(nested, indent + 1))
        counter += 1
    return "\n".join(lines)


def convert_table_google(table):
    """Convert HTML table to markdown."""
    rows = table.find_all("tr")
    if not rows:
        return ""
    md_rows = []
    for row in rows:
        cells = row.find_all(["td", "th"])
        md_cells = [convert_inline_google(c).strip().replace("|", "\\|") for c in cells]
        md_rows.append("| " + " | ".join(md_cells) + " |")
    if md_rows:
        num_cols = md_rows[0].count("|") - 1
        separator = "| " + " | ".join(["---"] * num_cols) + " |"
        md_rows.insert(1, separator)
    return "\n".join(md_rows)


def write_translated_doc(locale, doc_path, title, body_md):
    """Write a translated doc file."""
    locale_dir = I18N / locale / "docusaurus-plugin-content-docs" / "current"
    full_path = locale_dir / f"{doc_path}.md"
    full_path.parent.mkdir(parents=True, exist_ok=True)

    fm_lines = [
        "---",
        f"title: {yaml_quote(title)}",
        f"sidebar_label: {yaml_quote(title)}",
        "---",
    ]
    content = "\n".join(fm_lines) + "\n\n" + body_md + "\n"

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    english_paths = get_english_doc_paths() - ENGLISH_ONLY

    # Find all missing translations
    missing = []
    for locale in LOCALES:
        translated = get_translated_doc_paths(locale)
        for doc_path in sorted(english_paths - translated):
            if doc_path in DOC_TO_WEB_ID:
                missing.append((locale, doc_path, DOC_TO_WEB_ID[doc_path]))

    print(f"Found {len(missing)} missing translations to attempt fetching")

    fetched = 0
    failed = 0
    skipped = 0

    for locale, doc_path, web_id in missing:
        hl = LOCALE_TO_HL.get(locale, locale)
        result = fetch_article(web_id, hl)

        if result is None:
            print(f"  FAIL {locale}/{doc_path} (WEB:{web_id})")
            failed += 1
            continue

        title, body = result
        body_md = convert_google_body(body)

        # Skip if body is too short (likely not a real translation)
        if len(body_md.strip()) < 50:
            print(f"  SKIP {locale}/{doc_path} (body too short: {len(body_md)} chars)")
            skipped += 1
            continue

        write_translated_doc(locale, doc_path, title, body_md)
        print(f"  OK   {locale}/{doc_path}")
        fetched += 1

        # Be polite to Google
        time.sleep(0.5)

    print(f"\nDone: {fetched} fetched, {failed} failed, {skipped} skipped")


if __name__ == "__main__":
    main()

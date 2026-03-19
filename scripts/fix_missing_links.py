#!/usr/bin/env python3
"""Fix translations that have fewer links than English by restoring missing links.

For each translation with fewer links than English, finds plain text in the
translation that corresponds to linked text in English, and wraps it in
the correct markdown link.

Skips connection-issues (too complex, handled separately).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

LINK_RE = re.compile(r'(?<!!)\[([^\]\\]*(?:\\.[^\]\\]*)*)\]\(([^)]+)\)')

SKIP_DOCS = {"client/troubleshooting/connection-issues"}


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def extract_links_with_context(text):
    """Extract links with surrounding line context."""
    results = []
    lines = text.split('\n')
    for m in LINK_RE.finditer(text):
        # Find which line this link is on
        pos = m.start()
        line_start = text.rfind('\n', 0, pos) + 1
        line_end = text.find('\n', pos)
        if line_end == -1:
            line_end = len(text)
        line = text[line_start:line_end]
        results.append({
            'text': m.group(1),
            'url': m.group(2),
            'full_match': m.group(0),
            'line': line.strip(),
            'start': m.start(),
            'end': m.end(),
        })
    return results


def try_restore_links(en_file, tr_file, doc_path):
    """Try to restore missing links in a translation by finding unlinked text."""
    en_text = en_file.read_text(encoding="utf-8")
    tr_text = tr_file.read_text(encoding="utf-8")

    en_links = extract_links_with_context(en_text)
    tr_links = extract_links_with_context(tr_text)

    if len(tr_links) >= len(en_links):
        return 0  # No missing links

    # Find which English URLs are missing from translation
    en_urls = [l['url'] for l in en_links]
    tr_urls = [l['url'] for l in tr_links]

    # Count occurrences
    from collections import Counter
    en_counts = Counter(en_urls)
    tr_counts = Counter(tr_urls)

    missing_urls = []
    for url, count in en_counts.items():
        diff = count - tr_counts.get(url, 0)
        for _ in range(diff):
            missing_urls.append(url)

    if not missing_urls:
        return 0

    fixes = 0
    new_text = tr_text

    for missing_url in missing_urls:
        # Find the English link text for this URL
        en_link = None
        for l in en_links:
            if l['url'] == missing_url:
                en_link = l
                break

        if not en_link:
            continue

        # For internal links, try to find the URL as plain text in translation
        # For external links, try to find the URL as plain text
        if missing_url.startswith('http'):
            # Look for the bare URL as plain text (not already in a link)
            bare_url = missing_url
            if bare_url in new_text:
                # Check it's not already in a markdown link
                url_pos = new_text.find(bare_url)
                before = new_text[max(0, url_pos-2):url_pos]
                if '](' not in before:
                    # It's a bare URL — wrap it
                    new_text = new_text[:url_pos] + f'[{bare_url}]({bare_url})' + new_text[url_pos + len(bare_url):]
                    fixes += 1
        else:
            # Internal link — can't easily find the translated text to wrap
            # Skip these
            pass

    if fixes > 0:
        tr_file.write_text(new_text, encoding="utf-8")

    return fixes


def main():
    total = 0

    for locale in get_locales():
        locale_dir = I18N / locale / "docusaurus-plugin-content-docs" / "current"

        for en_file in DOCS.rglob("*.md"):
            doc_path = str(en_file.relative_to(DOCS).with_suffix(""))
            if doc_path in SKIP_DOCS:
                continue

            tr_file = locale_dir / f"{doc_path}.md"
            if not tr_file.exists():
                continue

            fixes = try_restore_links(en_file, tr_file, doc_path)
            if fixes:
                print(f"  {locale}/{doc_path}: restored {fixes} link(s)")
                total += fixes

    print(f"\nDone: {total} links restored")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Find articles where the title language doesn't match the locale.

Approach: For each doc, collect titles across all locales. If a title
appears only once (unique to one locale), check if it also appears as a
title for ANY doc in a different locale. That would indicate the content
was swapped from another language.

Also: check for titles that match a known different-language title from
partial-translations or missing locales.
"""

import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

def get_title(filepath):
    text = filepath.read_text("utf-8")
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', text, re.MULTILINE)
    return m.group(1).strip().strip('"') if m else None

def get_first_content_line(filepath):
    """Get first non-frontmatter content line."""
    text = filepath.read_text("utf-8")
    in_frontmatter = False
    for line in text.split("\n"):
        if line.strip() == "---":
            if not in_frontmatter:
                in_frontmatter = True
                continue
            else:
                in_frontmatter = False
                continue
        if not in_frontmatter and line.strip():
            return line.strip()[:100]
    return ""

# Build a map of ALL titles across all locales (including partial)
# {title: set of locales that use this title for any doc}
title_locale_map = defaultdict(set)  # title -> set of (locale, doc_rel)
all_data = {}  # (locale, doc_rel) -> title

for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    docs_dir = locale_dir / "docusaurus-plugin-content-docs" / "current"
    if not docs_dir.exists():
        continue
    locale = locale_dir.name
    for md_file in docs_dir.rglob("*.md"):
        rel = str(md_file.relative_to(docs_dir))
        title = get_title(md_file)
        if title:
            title_locale_map[title].add((locale, rel))
            all_data[(locale, rel)] = title

# Also check partial translations
partial_dir = I18N / "partial-translations"
if partial_dir.exists():
    for locale_dir in sorted(partial_dir.iterdir()):
        if not locale_dir.is_dir():
            continue
        docs_dir = locale_dir / "docusaurus-plugin-content-docs" / "current"
        if not docs_dir.exists():
            continue
        locale = f"partial:{locale_dir.name}"
        for md_file in docs_dir.rglob("*.md"):
            rel = str(md_file.relative_to(docs_dir))
            title = get_title(md_file)
            if title:
                title_locale_map[title].add((locale, rel))

# Now for each (locale, doc_rel), check if the title appears in a different
# locale for a DIFFERENT doc (cross-contamination)
print("=== Cross-locale title matches (same title, different locale, same doc) ===\n")

# Group by doc_rel
doc_titles = defaultdict(dict)  # doc_rel -> {locale: title}
for (locale, doc_rel), title in all_data.items():
    doc_titles[doc_rel][locale] = title

# For each doc, find titles that appear in multiple unrelated locales
for doc_rel in sorted(doc_titles.keys()):
    locale_titles = doc_titles[doc_rel]
    title_to_locs = defaultdict(list)
    for loc, title in locale_titles.items():
        title_to_locs[title].append(loc)

    for title, locs in title_to_locs.items():
        if len(locs) < 2:
            continue
        # Are they all in the same language family?
        related = {
            "es": "es", "es-419": "es",
            "pt": "pt", "pt-BR": "pt",
            "zh-Hans": "zh", "zh-Hant": "zh", "zh-HK": "zh",
            "bs": "sh", "hr": "sh", "sr": "sh",
            "nb": "no", "da": "no",  # Sometimes similar
        }
        families = set()
        for l in locs:
            families.add(related.get(l, l))
        if len(families) > 1:
            print(f"  {doc_rel}: '{title[:60]}'")
            print(f"    Locales: {', '.join(sorted(locs))}")
            print()

# Also look for titles that match partial-translations (indicating the
# wrong partial translation was used)
print("=== Titles matching partial translations (possible swap) ===\n")
for title, entries in title_locale_map.items():
    partials = [(l, d) for l, d in entries if l.startswith("partial:")]
    fulls = [(l, d) for l, d in entries if not l.startswith("partial:")]
    if partials and fulls:
        for pl, pd in partials:
            for fl, fd in fulls:
                if pd == fd and pl.split(":")[1] != fl:
                    partial_lang = pl.split(":")[1]
                    print(f"  {fl}/{fd}: title matches partial:{partial_lang}")
                    print(f"    Title: '{title[:80]}'")
                    print()

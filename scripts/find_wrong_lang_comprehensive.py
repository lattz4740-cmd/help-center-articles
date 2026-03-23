#!/usr/bin/env python3
"""Comprehensive wrong-language detection.

For each translated article, check if the title appears as a title for
the SAME article in a DIFFERENT, unrelated locale. If so, the content
was likely copied from the wrong language.
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

# Language groups where identical titles are expected
RELATED_GROUPS = [
    {"es", "es-419"},
    {"pt", "pt-BR"},
    {"zh-Hans", "zh-Hant", "zh-HK"},
    {"bs", "hr"},  # Very similar
    {"nb", "da"},  # Sometimes overlap
]

def find_group(locale):
    for g in RELATED_GROUPS:
        if locale in g:
            return g
    return {locale}

# Collect titles: {doc_rel: {locale: title}}
all_titles = defaultdict(dict)

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
            all_titles[rel][locale] = title

# For each (doc, locale), check if the title matches another locale's title
# for the SAME doc, where the locales are in different groups
issues = []
for doc_rel, locale_titles in all_titles.items():
    # Build reverse: title -> list of locales
    title_locales = defaultdict(list)
    for loc, title in locale_titles.items():
        title_locales[title].append(loc)

    for title, locs in title_locales.items():
        if len(locs) < 2:
            continue
        # Check if all are in the same group
        groups = set()
        for loc in locs:
            groups.add(frozenset(find_group(loc)))
        if len(groups) > 1:
            # Multiple unrelated groups share this title
            # Filter: skip very common cognates (1-2 word titles that happen to be the same)
            words = title.split()
            if len(words) <= 2:
                # Could be natural cognate - check if it's actually suspicious
                # Skip "Terminologie" type words shared across romance/germanic languages
                continue
            issues.append((doc_rel, title, sorted(locs)))

# Also find titles that match en-GB but aren't en-GB (untranslated)
en_titles = {}
for md_file in (ROOT / "docs").rglob("*.md"):
    rel = str(md_file.relative_to(ROOT / "docs"))
    title = get_title(md_file)
    if title:
        en_titles[rel] = title

print("=== Wrong-language articles (unrelated locales share the same title) ===\n")
for doc_rel, title, locs in sorted(issues):
    print(f"  {doc_rel}:")
    print(f"    Title: '{title[:80]}'")
    print(f"    Locales: {', '.join(locs)}")
    # Try to identify which locale "owns" this title
    # by checking if the title matches a different doc in one locale
    print()

print("\n=== Articles with titles matching English (possibly untranslated) ===\n")
for doc_rel, locale_titles in sorted(all_titles.items()):
    en_title = en_titles.get(doc_rel, "")
    if not en_title:
        continue
    for loc, title in sorted(locale_titles.items()):
        if loc == "en-GB":
            continue
        if title == en_title:
            print(f"  {loc}/{doc_rel}: '{title[:80]}'")

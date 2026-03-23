#!/usr/bin/env python3
"""Find ALL articles that appear to be in the wrong language.

For each locale, check if the title matches a DIFFERENT unrelated locale's title.
This catches cases where the GKMS export substituted the wrong language.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

def get_title(filepath):
    text = filepath.read_text("utf-8")
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', text, re.MULTILINE)
    return m.group(1).strip().strip('"') if m else None

# Related language groups where sharing titles is expected
RELATED = {
    frozenset({"es", "es-419"}),
    frozenset({"pt", "pt-BR"}),
    frozenset({"zh-Hans", "zh-Hant", "zh-HK"}),
    frozenset({"bs", "hr"}),  # Very similar languages
    frozenset({"en-GB"}),  # Can match English
}

def are_related(loc1, loc2):
    for group in RELATED:
        if loc1 in group and loc2 in group:
            return True
    return False

# Collect all titles
all_titles = {}  # {doc_rel: {locale: title}}
en_titles = {}

for md_file in (ROOT / "docs").rglob("*.md"):
    rel = str(md_file.relative_to(ROOT / "docs"))
    title = get_title(md_file)
    if title:
        en_titles[rel] = title

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
            if rel not in all_titles:
                all_titles[rel] = {}
            all_titles[rel][locale] = title

# For each doc + locale, check if the title matches another unrelated locale
print("=== Wrong-language articles (title matches different unrelated locale) ===\n")

# Words/terms that are naturally the same across many languages
UNIVERSAL_TERMS = {"Terminologie", "Terminologia", "Terminologi", "Terminología", "Terminológia"}

issues = []
for doc_rel, locale_titles in sorted(all_titles.items()):
    for locale, title in locale_titles.items():
        if title in UNIVERSAL_TERMS:
            continue
        # Check if this exact title appears in another unrelated locale
        for other_locale, other_title in locale_titles.items():
            if other_locale == locale:
                continue
            if are_related(locale, other_locale):
                continue
            if title == other_title:
                # This locale has the same title as an unrelated locale — suspicious
                # But only flag if the other locale seems to be the "original" language
                # (i.e., the title looks like it belongs to other_locale, not this one)
                issues.append((doc_rel, locale, other_locale, title))

# Deduplicate: for each (doc, title), show which locales share it
from collections import defaultdict
by_doc_title = defaultdict(set)
for doc_rel, locale, other_locale, title in issues:
    by_doc_title[(doc_rel, title)].add(locale)
    by_doc_title[(doc_rel, title)].add(other_locale)

for (doc_rel, title), locales in sorted(by_doc_title.items()):
    # Skip if all locales are closely related
    if len(locales) <= 1:
        continue
    # Check if these are just similar languages (cs/sk share "Dostupné jazyky")
    # Focus on pairs where the languages are truly unrelated
    unrelated_pairs = []
    locales_list = sorted(locales)
    for i, l1 in enumerate(locales_list):
        for l2 in locales_list[i+1:]:
            if not are_related(l1, l2):
                # Check if this is a natural cognate (similar in multiple languages)
                # Skip if the title is very short (1-2 words) as those may be cognates
                if len(title.split()) <= 2:
                    continue
                unrelated_pairs.append((l1, l2))

    if unrelated_pairs:
        print(f"  {doc_rel}:")
        print(f"    Title: '{title[:80]}'")
        print(f"    Shared by: {', '.join(sorted(locales))}")
        print()

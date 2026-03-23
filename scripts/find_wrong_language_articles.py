#!/usr/bin/env python3
"""Find articles where the entire content is in the wrong language.

Check each translation's title against the English title and the same article
in other locales to identify cases where the GKMS export used wrong-language content.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"
DOCS = ROOT / "docs"

def get_frontmatter(filepath):
    """Extract title and sidebar_label from frontmatter."""
    text = filepath.read_text("utf-8")
    title_m = re.search(r'^title:\s*"?(.+?)"?\s*$', text, re.MULTILINE)
    label_m = re.search(r'^sidebar_label:\s*"?(.+?)"?\s*$', text, re.MULTILINE)
    title = title_m.group(1).strip().strip('"') if title_m else None
    label = label_m.group(1).strip().strip('"') if label_m else None
    return title, label

# Collect all titles per doc per locale
all_titles = {}  # {doc_rel: {locale: title}}
for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    docs_dir = locale_dir / "docusaurus-plugin-content-docs" / "current"
    if not docs_dir.exists():
        continue
    locale = locale_dir.name
    for md_file in docs_dir.rglob("*.md"):
        rel = str(md_file.relative_to(docs_dir))
        title, _ = get_frontmatter(md_file)
        if title:
            if rel not in all_titles:
                all_titles[rel] = {}
            all_titles[rel][locale] = title

# For each locale, check if any title matches another locale's title exactly
# (indicating wrong-language content)
print("=== Articles where title matches a DIFFERENT locale's title ===\n")

# Build a lookup: for each doc, which locales have the same title
issues = []
for doc_rel, locale_titles in sorted(all_titles.items()):
    title_to_locales = {}
    for locale, title in locale_titles.items():
        if title not in title_to_locales:
            title_to_locales[title] = []
        title_to_locales[title].append(locale)

    for title, locales in title_to_locales.items():
        if len(locales) <= 1:
            continue
        # Filter out expected duplicates
        # zh-HK and zh-Hant are both Traditional Chinese
        # en-GB and en are both English
        filtered = [l for l in locales if l not in ("en-GB",)]
        # Group Chinese traditional variants
        zh_trad = [l for l in filtered if l in ("zh-Hant", "zh-HK")]
        non_zh = [l for l in filtered if l not in ("zh-Hant", "zh-HK")]

        if len(non_zh) > 1:
            # Check if these are related language pairs
            # Some titles are legitimately the same across languages
            # (e.g., "Terminologie" in de/fr/nl/ro/af)
            # Focus on cases where UNRELATED languages share a title
            issues.append((doc_rel, title, non_zh))

# Print issues, filtering to suspicious cases
for doc_rel, title, locales in issues:
    # Skip if all locales are closely related
    print(f"  {doc_rel}:")
    print(f"    Title: '{title[:80]}'")
    print(f"    Locales: {', '.join(sorted(locales))}")
    print()

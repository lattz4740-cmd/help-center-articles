#!/usr/bin/env python3
"""Find sidebar_labels that appear to be in the wrong language.

Strategy: For each doc, collect all sidebar_labels across locales.
If a label appears in locale X but looks like it belongs to locale Y
(i.e., the same label appears in locale Y), flag it.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"
DOCS = ROOT / "docs"

def get_sidebar_label(filepath):
    """Extract sidebar_label from frontmatter."""
    text = filepath.read_text("utf-8")
    m = re.search(r'^sidebar_label:\s*"?(.+?)"?\s*$', text, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"')
    return None

# Get English sidebar labels
en_labels = {}
for md_file in DOCS.rglob("*.md"):
    rel = md_file.relative_to(DOCS)
    label = get_sidebar_label(md_file)
    if label:
        en_labels[str(rel)] = label

# Collect all labels per doc per locale
all_labels = {}  # {doc_rel: {locale: label}}
for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    docs_dir = locale_dir / "docusaurus-plugin-content-docs" / "current"
    if not docs_dir.exists():
        continue
    locale = locale_dir.name
    for md_file in docs_dir.rglob("*.md"):
        rel = str(md_file.relative_to(docs_dir))
        label = get_sidebar_label(md_file)
        if label:
            if rel not in all_labels:
                all_labels[rel] = {}
            all_labels[rel][locale] = label

# Check for cross-contamination
print("=== Checking for wrong-language sidebar_labels ===\n")
issues = []

for doc_rel, locale_labels in sorted(all_labels.items()):
    # Build reverse map: label -> locales that use it
    label_to_locales = {}
    for locale, label in locale_labels.items():
        if label not in label_to_locales:
            label_to_locales[label] = []
        label_to_locales[label].append(locale)

    # If a label is used by only one locale, that's fine
    # If a label is used by multiple locales, check if they're related (e.g., es/es-419)
    # Also check if any locale's label matches another locale's label exactly
    for locale, label in locale_labels.items():
        # Check if this label appears as a different locale's label
        for other_locale, other_label in locale_labels.items():
            if other_locale == locale:
                continue
            if label == other_label:
                # Same label in two locales - could be ok (similar languages)
                # Flag if the locales are unrelated
                related_pairs = {
                    ("es", "es-419"), ("pt", "pt-BR"), ("zh-Hans", "zh-Hant"),
                    ("zh-Hans", "zh-HK"), ("zh-Hant", "zh-HK"),
                    ("en-GB", "en"), ("nb", "da"), ("bs", "hr"), ("bs", "sr"),
                }
                pair = tuple(sorted([locale, other_locale]))
                if pair not in related_pairs and locale < other_locale:
                    # Check if label is also the English label (that's suspicious)
                    en_label = en_labels.get(doc_rel, "")
                    if label != en_label:  # Not English, yet same in two unrelated langs
                        issues.append((doc_rel, locale, other_locale, label))

# Print unique label duplicates
seen = set()
for doc_rel, loc1, loc2, label in issues:
    key = (doc_rel, label)
    if key in seen:
        continue
    seen.add(key)
    # Find all locales using this label
    locales_using = [l for l, lab in all_labels[doc_rel].items() if lab == label]
    print(f"  {doc_rel}: label '{label[:60]}' used in: {', '.join(sorted(locales_using))}")

print(f"\n=== Also checking: labels matching English exactly (untranslated) ===\n")

untranslated = {}
for doc_rel, locale_labels in sorted(all_labels.items()):
    en_label = en_labels.get(doc_rel, "")
    if not en_label:
        continue
    for locale, label in locale_labels.items():
        if locale == "en-GB":
            continue  # en-GB can match English
        if label == en_label:
            if doc_rel not in untranslated:
                untranslated[doc_rel] = []
            untranslated[doc_rel].append(locale)

for doc_rel, locales in sorted(untranslated.items()):
    en_label = en_labels.get(doc_rel, "")
    print(f"  {doc_rel}: '{en_label[:60]}' (English) in: {', '.join(sorted(locales))}")

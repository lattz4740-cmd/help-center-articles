#!/usr/bin/env python3
"""Check each translated article's first content line to detect wrong-language content.

Compare the first content line of each article across locales. If a
locale's content matches a different, unrelated locale, flag it.
"""

import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

def get_first_content(filepath):
    """Get first meaningful content line after frontmatter."""
    text = filepath.read_text("utf-8")
    in_fm = False
    for line in text.split("\n"):
        s = line.strip()
        if s == "---":
            in_fm = not in_fm
            continue
        if not in_fm and s and not s.startswith("#") and not s.startswith("-"):
            return s[:100]
    return ""

def get_title(filepath):
    text = filepath.read_text("utf-8")
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', text, re.MULTILINE)
    return m.group(1).strip().strip('"') if m else None

# Related language groups
def same_group(a, b):
    groups = [
        {"es", "es-419"}, {"pt", "pt-BR"}, {"zh-Hans", "zh-Hant", "zh-HK"},
        {"bs", "hr"}, {"en-GB"},
    ]
    for g in groups:
        if a in g and b in g:
            return True
    return False

# Collect first content lines
data = defaultdict(dict)
for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir() or locale_dir.name == "partial-translations":
        continue
    docs_dir = locale_dir / "docusaurus-plugin-content-docs" / "current"
    if not docs_dir.exists():
        continue
    loc = locale_dir.name
    for md_file in docs_dir.rglob("*.md"):
        rel = str(md_file.relative_to(docs_dir))
        content = get_first_content(md_file)
        if content:
            data[rel][loc] = content

# Find duplicates across unrelated locales
print("=== Content lines shared by unrelated locales ===\n")
for doc_rel in sorted(data.keys()):
    content_map = defaultdict(list)
    for loc, content in data[doc_rel].items():
        content_map[content].append(loc)

    for content, locs in content_map.items():
        if len(locs) < 2:
            continue
        # Check for unrelated pairs
        unrelated = False
        for i, l1 in enumerate(locs):
            for l2 in locs[i+1:]:
                if not same_group(l1, l2):
                    unrelated = True
                    break
        if unrelated and len(content) > 20:  # Skip very short content that could be coincidence
            print(f"  {doc_rel}: {', '.join(sorted(locs))}")
            print(f"    Content: '{content[:80]}'")
            print()

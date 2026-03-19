#!/usr/bin/env python3
"""Check remaining link and heading issues with all exceptions disabled.

Reports issues grouped by doc path so we can see what's left to fix.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_translations as v

# Disable all link/heading exceptions
v.KNOWN_LINK_COUNT_DIFF_DOCS = set()
v.KNOWN_HEADING_DIFFS = set()

english_paths = v.get_english_doc_paths()
issues_by_doc = {}
for locale in v.LOCALES:
    issues = v.verify_locale(locale, english_paths)
    for issue in issues:
        if issue.category in ('LINKS', 'HEADING_STRUCTURE'):
            key = f'{issue.doc_path} [{issue.category}]'
            if key not in issues_by_doc:
                issues_by_doc[key] = []
            issues_by_doc[key].append(f'{issue.locale}: {issue.message}')

for key in sorted(issues_by_doc):
    examples = issues_by_doc[key]
    print(f'{key} ({len(examples)} locales)')
    for ex in examples[:3]:
        print(f'  {ex}')
    if len(examples) > 3:
        print(f'  ... and {len(examples) - 3} more')
    print()

total = sum(len(v) for v in issues_by_doc.values())
print(f'Total: {total} remaining link/heading issues')

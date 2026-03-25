#!/usr/bin/env python3
"""Remove stray GKMS URLs from translations.

Pattern: bare URL like https://google-jigsaw--jigsawuat.sandbox.my.site.com/outline/s/article/Terminology
appearing right before a proper markdown link like [access key](/about/terminology).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# Match the stray GKMS URL (with optional trailing space) before a markdown link
PATTERN = re.compile(
    r'https://google-jigsaw--jigsawuat\.sandbox\.my\.site\.com/outline/s/article/\S*\s*'
)

total_fixes = 0
fixed_files = []

for md_file in sorted(I18N.rglob("*.md")):
    if "partial-translations" in str(md_file):
        continue

    text = md_file.read_text("utf-8")
    if "google-jigsaw--jigsawuat.sandbox.my.site.com" not in text:
        continue

    new_text = PATTERN.sub("", text)
    if new_text != text:
        md_file.write_text(new_text, "utf-8")
        rel = md_file.relative_to(I18N)
        fixes = text.count("google-jigsaw--jigsawuat.sandbox.my.site.com")
        fixed_files.append((str(rel), fixes))
        total_fixes += fixes

print(f"Fixed {total_fixes} stray GKMS URLs in {len(fixed_files)} files:")
for f, n in fixed_files:
    print(f"  {f} ({n} fix{'es' if n > 1 else ''})")

#!/usr/bin/env python3
"""Replace external Google-hosted image URL with local path in data-limits.md."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD_URL = "https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw"
NEW_URL = "/images/data-limits-icon.png"

total = 0
for md in sorted(ROOT.rglob("**/data-limits.md")):
    rel = str(md.relative_to(ROOT))
    if "old-site" in rel or "node_modules" in rel or "partial-translations" in rel:
        continue
    text = md.read_text("utf-8")
    if OLD_URL in text:
        md.write_text(text.replace(OLD_URL, NEW_URL), "utf-8")
        total += 1
        print(f"  FIXED {rel}")

print(f"\nUpdated {total} files")

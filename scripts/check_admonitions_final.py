#!/usr/bin/env python3
"""Final check: which locales are still missing admonitions."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# Check connecting-device
print("=== connecting-device: missing :::warning ===")
connecting_device = "docusaurus-plugin-content-docs/current/client/getting-started/connecting-device.md"
missing = []
for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    f = locale_dir / connecting_device
    if not f.exists():
        continue
    text = f.read_text("utf-8")
    if ":::warning" not in text:
        # Show the last line (should be the Important line)
        lines = [l for l in text.strip().split("\n") if l.strip()]
        last = lines[-1] if lines else "(empty)"
        print(f"  {locale_dir.name}: {last[:120]}")
        missing.append(locale_dir.name)
print(f"  Total missing: {len(missing)}")

# Check connection-issues
print("\n=== connection-issues: missing :::note ===")
connection_issues = "docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
missing2 = []
for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    f = locale_dir / connection_issues
    if not f.exists():
        continue
    text = f.read_text("utf-8")
    if ":::note" not in text:
        missing2.append(locale_dir.name)
print(f"  Missing locales: {missing2}")
print(f"  Total missing: {len(missing2)}")

# For missing connection-issues, show what the Note line looks like
for loc in missing2:
    f = I18N / loc / connection_issues
    lines = f.read_text("utf-8").split("\n")
    # Find lines near the "try connecting" section
    for i, line in enumerate(lines):
        if 45 <= i <= 60 and line.strip() and not line.startswith("#") and not line.startswith("-") and not line.startswith("1."):
            print(f"  {loc}:{i+1}: {line.strip()[:120]}")

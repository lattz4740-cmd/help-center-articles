#!/usr/bin/env python3
"""Check which translations still have un-converted admonition patterns."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# Check connecting-device for remaining *...:* pattern
print("=== connecting-device: remaining *Important:* patterns ===")
connecting_device = "docusaurus-plugin-content-docs/current/client/getting-started/connecting-device.md"
for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    f = locale_dir / connecting_device
    if not f.exists():
        continue
    text = f.read_text("utf-8")
    if ":::warning" in text:
        continue  # Already fixed
    # Check for remaining italic Important pattern
    for i, line in enumerate(text.split("\n"), 1):
        if line.startswith("*") and (":" in line[:40] or "：" in line[:40]):
            print(f"  {locale_dir.name}:{i}: {line[:120]}")

# Check connection-issues for remaining Note: pattern
print("\n=== connection-issues: remaining Note: patterns ===")
connection_issues = "docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
for locale_dir in sorted(I18N.iterdir()):
    if not locale_dir.is_dir():
        continue
    f = locale_dir / connection_issues
    if not f.exists():
        continue
    text = f.read_text("utf-8")
    if ":::note" in text:
        continue  # Already fixed
    # Find the line after "Try connecting..." (the Note line)
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if "outline" in line.lower() and ("device" in line.lower() or "appareil" in line.lower() or "dispositivo" in line.lower() or "Gerät" in line.lower() or "cihaz" in line.lower() or "裝置" in line.lower() or "设备" in line.lower() or "기기" in line.lower()):
            continue
        # Look for the Note-equivalent line (typically after "Try connecting" section)
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and not stripped.startswith("-") and not stripped.startswith(":::"):
            # Check if this could be the Note line by looking for colon early in the line
            if ":" in stripped[:30] or "：" in stripped[:30]:
                # Only show if it's in the firewall section area (around line 50-55 in most files)
                if 40 <= i <= 70:
                    print(f"  {locale_dir.name}:{i+1}: {stripped[:120]}")

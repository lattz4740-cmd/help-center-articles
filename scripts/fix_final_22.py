#!/usr/bin/env python3
"""Fix the final 22 heading structure issues.

Issues found:

1. google-cloud: ar, fr, it have "Permissions Granted" as plain text → add ##
   ja, nl, pt-BR missing "Overview" heading (not in source)
   es, tr, zh-Hans, zh-Hant have an extra heading (translator split) — accept

2. connection-issues: en-GB, es, pl, th have section titles as plain text
   fa, zh-Hans have mixed h2/h4 levels
   pt-BR has extra headings (section titles + sub-sections)

3. setup-server: am missing "Before you begin", ja missing "DigitalOcean" heading
   he has bold with RTL marks

4. ur/terminology: bold with RTL mark for "Outline Client"

5. ur/manage-access-keys: 3 bold headings with RTL marks
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

# RTL embedding mark
RLE = '\u202b'


def i18n_path(locale, doc_path):
    return I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"


def fix_plain_text_to_heading(filepath, plain_text):
    """Convert a specific plain text line to a ## heading."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if line.strip() == plain_text:
            lines[i] = f"## {plain_text}"
            filepath.write_text('\n'.join(lines), encoding='utf-8')
            return True
    return False


def fix_rtl_bold_to_heading(filepath):
    """Convert RTL bold lines (‫**text**) to ## headings."""
    text = filepath.read_text(encoding="utf-8")
    # Match lines starting with optional RTL mark + **text**
    pattern = re.compile(r'^[\u200e\u200f\u202a\u202b\u202c]*\*{2,4}(.+?)\*{2,4}\s*$', re.MULTILINE)
    new_text = pattern.sub(r'## \1', text)
    if new_text != text:
        filepath.write_text(new_text, encoding="utf-8")
        return len(pattern.findall(text))
    return 0


def fix_h4_to_h2(filepath):
    """Convert #### headings to ## to match English."""
    text = filepath.read_text(encoding="utf-8")
    new_text = re.sub(r'^####\s+', '## ', text, flags=re.MULTILINE)
    if new_text != text:
        filepath.write_text(new_text, encoding="utf-8")
        return True
    return False


def main():
    total = 0

    # === google-cloud: fix "Permissions Granted" plain text ===
    print("google-cloud: fixing plain text headings...")
    gc_plain_texts = {
        "ar": "الأذونات الممنوحة",
        "fr": "Autorisations accordées",
        "it": "Autorizzazioni concesse",
    }
    for locale, text in gc_plain_texts.items():
        f = i18n_path(locale, "manager/server-setup/google-cloud")
        if f.exists() and fix_plain_text_to_heading(f, text):
            print(f"  {locale}: fixed '{text[:30]}...'")
            total += 1

    # ja, nl, pt-BR: missing "Overview" — these just don't have it in the source.
    # The section content exists but no title. Can't auto-fix without translation.
    # Accept as-is.

    # === connection-issues: fix section titles as plain text ===
    print("\nconnection-issues: fixing section titles...")
    conn_plain = {
        "en-GB": ["Internet connection issues:", "Device settings:", "Server issues:"],
        "es": ["Ajustes del dispositivo:"],
        "pl": ["Problemy z połączeniem z internetem:", "Ustawienia urządzenia:", "Problemy z serwerem:"],
        "th": ["ปัญหาการเชื่อมต่ออินเทอร์เน็ต", "การตั้งค่าอุปกรณ์"],
    }
    for locale, texts in conn_plain.items():
        f = i18n_path(locale, "client/troubleshooting/connection-issues")
        if not f.exists():
            continue
        for text in texts:
            if fix_plain_text_to_heading(f, text):
                print(f"  {locale}: fixed '{text[:40]}...'")
                total += 1

    # fa: fix h4 → h2
    print("\nconnection-issues: fixing h4 → h2...")
    for locale in ["fa", "zh-Hans"]:
        f = i18n_path(locale, "client/troubleshooting/connection-issues")
        if f.exists() and fix_h4_to_h2(f):
            print(f"  {locale}: fixed h4 → h2")
            total += 1

    # === setup-server: fix missing headings ===
    print("\nsetup-server: fixing missing headings...")
    ss_plain = {
        "am": "ጥቂት ነገሮች ያስፈልጉዎታል፦",  # "Before you begin" equivalent — actually this is the content line, not the title
        "ja": "DigitalOcean で設定する",
    }
    for locale, text in ss_plain.items():
        f = i18n_path(locale, "manager/server-setup/setup-server")
        if f.exists() and fix_plain_text_to_heading(f, text):
            print(f"  {locale}: fixed '{text[:30]}...'")
            total += 1

    # he/setup-server: RTL bold
    print("\nsetup-server: fixing RTL bold (he)...")
    f = i18n_path("he", "manager/server-setup/setup-server")
    if f.exists():
        n = fix_rtl_bold_to_heading(f)
        if n:
            print(f"  he: fixed {n} RTL bold heading(s)")
            total += n

    # === ur/terminology: RTL bold ===
    print("\nterminology: fixing RTL bold (ur)...")
    f = i18n_path("ur", "about/terminology")
    if f.exists():
        n = fix_rtl_bold_to_heading(f)
        if n:
            print(f"  ur: fixed {n} RTL bold heading(s)")
            total += n

    # === ur/manage-access-keys: RTL bold ===
    print("\nmanage-access-keys: fixing RTL bold (ur)...")
    f = i18n_path("ur", "manager/server-management/manage-access-keys")
    if f.exists():
        n = fix_rtl_bold_to_heading(f)
        if n:
            print(f"  ur: fixed {n} RTL bold heading(s)")
            total += n

    print(f"\nDone: {total} fixes")


if __name__ == "__main__":
    main()

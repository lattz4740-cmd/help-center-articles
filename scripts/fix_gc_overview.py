#!/usr/bin/env python3
"""Add missing Overview heading to ja, nl, pt-BR google-cloud translations.

These locales have "Overview" as the page title instead of a heading.
The title should be the article name, and Overview should be a ## heading.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"


def fix_locale(locale, overview_text, proper_title):
    f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "manager" / "server-setup" / "google-cloud.md"
    text = f.read_text(encoding="utf-8")
    lines = text.split('\n')

    # Update title and sidebar_label in frontmatter
    for i, line in enumerate(lines):
        if line.startswith('title:'):
            lines[i] = f'title: "{proper_title}"'
        elif line.startswith('sidebar_label:'):
            lines[i] = f'sidebar_label: "{proper_title}"'

    # Find first non-empty line after frontmatter
    fm_end = 0
    fm_count = 0
    for i, line in enumerate(lines):
        if line.strip() == '---':
            fm_count += 1
            if fm_count == 2:
                fm_end = i
                break

    insert_at = fm_end + 1
    while insert_at < len(lines) and not lines[insert_at].strip():
        insert_at += 1

    lines.insert(insert_at, f'## {overview_text}')
    lines.insert(insert_at + 1, '')

    f.write_text('\n'.join(lines), encoding='utf-8')
    print(f"  {locale}: added '## {overview_text}', title → '{proper_title}'")


def main():
    fix_locale("ja", "概要", "Google Cloud 自動セットアップ")
    fix_locale("nl", "Overzicht", "Automatische Google Cloud-configuratie")
    fix_locale("pt-BR", "Visão geral", "Configuração automatizada do Google Cloud")
    print("\nDone")


if __name__ == "__main__":
    main()

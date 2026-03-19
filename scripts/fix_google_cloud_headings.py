#!/usr/bin/env python3
"""Remove the redundant "Overview" heading from google-cloud across all locales.

The page title already serves as the top-level heading. The "## Overview"
heading was redundant. Some translations had it as a heading, others had
it as the page title — either way, remove the ## heading if present.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def main():
    total = 0

    # Known "Overview" translations to remove as headings
    overview_words = {
        "Overview", "Übersicht", "Panoramica", "概要", "Overzicht",
        "Visão geral", "Descripción general", "Genel Bakış", "概述", "總覽",
        "Aperçu", "نظرة عامة", "Обзор", "Pregled", "Przegląd",
        "Oversigt", "Oorsig", "Ikhtisar", "Yleiskatsaus", "Pangkalahatang-ideya",
        "Présentation", "Tổng quan", "סקירה כללית", "Áttekintés",
        "Նախադիտում", "Gambaran keseluruhan", "ภาพรวม", "概觀",
    }

    for locale in get_locales():
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "manager" / "server-setup" / "google-cloud.md"
        if not f.exists():
            continue

        text = f.read_text(encoding="utf-8")
        lines = text.split('\n')

        # Find first ## heading
        for i, line in enumerate(lines):
            m = re.match(r'^##\s+(.+)$', line)
            if m:
                heading_text = m.group(1).strip()
                if heading_text in overview_words:
                    # Remove this heading line and the blank line after it
                    end = i + 1
                    while end < len(lines) and not lines[end].strip():
                        end += 1
                    new_lines = lines[:i] + lines[end:]
                    f.write_text('\n'.join(new_lines), encoding='utf-8')
                    print(f"  {locale}: removed '## {heading_text}'")
                    total += 1
                break  # Only check first heading

    print(f"\nDone: {total} Overview headings removed")


if __name__ == "__main__":
    main()

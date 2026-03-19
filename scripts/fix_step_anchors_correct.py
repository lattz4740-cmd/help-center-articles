#!/usr/bin/env python3
"""Fix step anchor fragments that were incorrectly swapped.

- client/troubleshooting/windows-install: English has #step-3, restore it
- manager/troubleshooting/windows-install: English has #step-1, restore it
"""

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
    fixes = 0
    for locale in get_locales():
        # client/troubleshooting/windows-install: EN has #step-3
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "windows-install.md"
        if f.exists():
            text = f.read_text(encoding="utf-8")
            new_text = text.replace(
                "https://getoutline.org/get-started/#step-1",
                "https://getoutline.org/get-started/#step-3"
            )
            if new_text != text:
                f.write_text(new_text, encoding="utf-8")
                print(f"  {locale}/client/windows-install: #step-1 → #step-3")
                fixes += 1

        # manager/troubleshooting/windows-install: EN has #step-1
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "manager" / "troubleshooting" / "windows-install.md"
        if f.exists():
            text = f.read_text(encoding="utf-8")
            new_text = text.replace(
                "https://getoutline.org/get-started/#step-3",
                "https://getoutline.org/get-started/#step-1"
            )
            if new_text != text:
                f.write_text(new_text, encoding="utf-8")
                print(f"  {locale}/manager/windows-install: #step-3 → #step-1")
                fixes += 1

    print(f"\nDone: {fixes} fixes")


if __name__ == "__main__":
    main()

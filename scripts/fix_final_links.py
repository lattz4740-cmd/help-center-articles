#!/usr/bin/env python3
"""Fix remaining obvious link issues.

1. Replace self-referencing links with English external URLs (feedback, how-outline-works)
2. Fix #step-1 vs #step-3 anchor fragments to match English
3. Replace Google Docs links with correct internal links in connection-issues
4. Add Wikipedia path normalization to verify script
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

LINK_RE = re.compile(r'(?<!!)\[([^\]\\]*(?:\\.[^\]\\]*)*)\]\(([^)]+)\)')


def get_locales():
    locales = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            if (d / "docusaurus-plugin-content-docs" / "current").exists():
                locales.append(d.name)
    return locales


def fix_self_links_pairwise(doc_path):
    """Replace self-referencing links with English URLs by position matching."""
    en_file = DOCS / f"{doc_path}.md"
    en_text = en_file.read_text(encoding="utf-8")
    en_urls = [m.group(2) for m in LINK_RE.finditer(en_text)]

    self_url = "/" + doc_path
    fixes = 0

    for locale in get_locales():
        tr_file = I18N / locale / "docusaurus-plugin-content-docs" / "current" / f"{doc_path}.md"
        if not tr_file.exists():
            continue

        tr_text = tr_file.read_text(encoding="utf-8")
        tr_matches = list(LINK_RE.finditer(tr_text))
        tr_urls = [m.group(2) for m in tr_matches]

        if len(tr_urls) != len(en_urls):
            continue  # Can't do positional matching

        changed = False
        new_text = tr_text
        for i in range(len(tr_matches) - 1, -1, -1):
            tr_url = tr_urls[i]
            en_url = en_urls[i]
            if tr_url == self_url and en_url != self_url:
                m = tr_matches[i]
                link_text = m.group(1)
                old_link = f"[{link_text}]({tr_url})"
                new_link = f"[{link_text}]({en_url})"
                new_text = new_text[:m.start()] + new_link + new_text[m.end():]
                changed = True

        if changed:
            tr_file.write_text(new_text, encoding="utf-8")
            fixes += 1

    return fixes


def fix_step_anchors():
    """Fix #step-1 vs #step-3 to match English in terminology and windows-install."""
    fixes = 0

    for locale in get_locales():
        # terminology: EN has #step-3, some translations have #step-1
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "about" / "terminology.md"
        if f.exists():
            text = f.read_text(encoding="utf-8")
            new_text = text.replace(
                "https://getoutline.org/get-started/#step-1",
                "https://getoutline.org/get-started/#step-3"
            )
            if new_text != text:
                f.write_text(new_text, encoding="utf-8")
                fixes += 1

        # windows-install: EN has #step-1, some translations have #step-3
        for subdir in ["manager/troubleshooting", "client/troubleshooting"]:
            f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / subdir / "windows-install.md"
            if f.exists():
                text = f.read_text(encoding="utf-8")
                new_text = text.replace(
                    "https://getoutline.org/get-started/#step-3",
                    "https://getoutline.org/get-started/#step-1"
                )
                if new_text != text:
                    f.write_text(new_text, encoding="utf-8")
                    fixes += 1

    return fixes


def fix_google_docs_links():
    """Replace Google Docs links with correct internal links in connection-issues."""
    fixes = 0
    gdoc_re = re.compile(
        r'\[([^\]]*)\]\(https://docs\.google\.com/document/[^)]+\)'
    )

    for locale in get_locales():
        f = I18N / locale / "docusaurus-plugin-content-docs" / "current" / "client" / "troubleshooting" / "connection-issues.md"
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8")
        matches = list(gdoc_re.finditer(text))
        if not matches:
            continue
        new_text = text
        for m in reversed(matches):
            link_text = m.group(1)
            new_text = new_text[:m.start()] + f"[{link_text}](/about/terminology)" + new_text[m.end():]
        if new_text != text:
            f.write_text(new_text, encoding="utf-8")
            fixes += 1

    return fixes


def main():
    print("1. Fixing self-links in feedback...")
    n = fix_self_links_pairwise("about/feedback")
    print(f"   Fixed {n} files")

    print("2. Fixing self-links in how-outline-works...")
    n = fix_self_links_pairwise("about/how-outline-works")
    print(f"   Fixed {n} files")

    print("3. Fixing step anchor fragments...")
    n = fix_step_anchors()
    print(f"   Fixed {n} files")

    print("4. Fixing Google Docs links in connection-issues...")
    n = fix_google_docs_links()
    print(f"   Fixed {n} files")


if __name__ == "__main__":
    main()

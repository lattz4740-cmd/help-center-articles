#!/usr/bin/env python3
"""Fix links that were stripped during GKMS conversion across translations.

The GKMS converter sometimes drops the markdown link syntax [text](url),
leaving behind orphaned text fragments often separated by blank lines.
This script handles two categories:

1. "Orphaned link text" pattern: text before the link is on one line,
   the link text is on a blank-separated line below. We rejoin and wrap.
2. Simple cases where we know exactly what text to wrap with a link.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"


def get_locale_dir(locale):
    return I18N / locale / "docusaurus-plugin-content-docs" / "current"


def fix_orphaned_link(filepath, before_pattern, orphan_pattern, after_pattern, link_url):
    """Fix a link that was split across lines with blank line separators.

    Looks for:
        <line matching before_pattern>
        <blank line>
        <line matching orphan_pattern>

    And joins them: <before_text> [<orphan_text>](<link_url>)<after_text>
    """
    text = filepath.read_text(encoding='utf-8')
    lines = text.split('\n')
    fixed = False

    for i in range(len(lines) - 2):
        if (re.search(before_pattern, lines[i]) and
                lines[i + 1].strip() == '' and
                re.match(orphan_pattern, lines[i + 2].strip())):
            # Join the lines
            before = lines[i].rstrip()
            orphan = lines[i + 2].strip()

            # Check for after_pattern on the orphan line or next line
            after_text = ''
            if after_pattern:
                am = re.search(after_pattern, orphan)
                if am:
                    link_text = orphan[:am.start()].strip()
                    after_text = orphan[am.start():]
                else:
                    link_text = orphan
            else:
                link_text = orphan

            new_line = f"{before} [{link_text}]({link_url}){after_text}"
            lines[i] = new_line
            lines[i + 1] = ''  # Remove blank line
            lines[i + 2] = ''  # Remove orphan line
            fixed = True
            break

    if fixed:
        # Clean up double blank lines left behind
        text = '\n'.join(lines)
        text = re.sub(r'\n{3,}', '\n\n', text)
        filepath.write_text(text, encoding='utf-8')
    return fixed


def fix_plain_text_to_link(filepath, plain_text, link_url, context_pattern=None):
    """Convert a plain text occurrence to a markdown link.

    If context_pattern is given, only fix the occurrence near that context.
    """
    text = filepath.read_text(encoding='utf-8')
    if context_pattern:
        m = re.search(context_pattern, text)
        if not m:
            return False
        # Find the plain_text near this match
        start = max(0, m.start() - 200)
        end = min(len(text), m.end() + 200)
        region = text[start:end]
        idx = region.find(plain_text)
        if idx < 0:
            return False
        abs_idx = start + idx
        new_text = text[:abs_idx] + f'[{plain_text}]({link_url})' + text[abs_idx + len(plain_text):]
    else:
        idx = text.find(plain_text)
        if idx < 0:
            return False
        # Make sure it's not already a link
        before = text[max(0, idx - 2):idx]
        if before.endswith('['):
            return False
        new_text = text[:idx] + f'[{plain_text}]({link_url})' + text[idx + len(plain_text):]

    if new_text != text:
        filepath.write_text(new_text, encoding='utf-8')
        return True
    return False


def remove_extra_link(filepath, pattern):
    """Remove an extraneous markdown link, leaving only its text."""
    text = filepath.read_text(encoding='utf-8')
    m = re.search(pattern, text)
    if not m:
        return False
    # Replace [text](url) with just text
    link_text = re.search(r'\[([^\]]+)\]', m.group(0))
    if link_text:
        new_text = text[:m.start()] + link_text.group(1) + text[m.end():]
        filepath.write_text(new_text, encoding='utf-8')
        return True
    return False


def main():
    total = 0

    # --- hi/manager-download: Remove extra link wrapping introductory phrase ---
    hi_md = get_locale_dir('hi') / 'manager' / 'troubleshooting' / 'manager-download.md'
    if hi_md.exists():
        text = hi_md.read_text(encoding='utf-8')
        # The pattern: a long phrase is wrapped in a link to the same URL as "this link"
        m = re.search(
            r'\[([^\]]{40,})\]\(https://getoutline\.org/get-started/#step-1\)',
            text
        )
        if m:
            new_text = text[:m.start()] + m.group(1) + text[m.end():]
            hi_md.write_text(new_text, encoding='utf-8')
            print("  hi/manager-download: removed extra link wrapping")
            total += 1

    # --- en-GB/update-software: Add back Unattended Upgrades link ---
    engb_us = get_locale_dir('en-GB') / 'manager' / 'server-management' / 'update-software.md'
    if engb_us.exists():
        if fix_orphaned_link(
            engb_us,
            r'using$',
            r'^.{0,30}$',  # short orphan line
            r'^\(',  # may start with ( for "(Ubuntu)"
            'https://wiki.debian.org/UnattendedUpgrades'
        ):
            print("  en-GB/update-software: restored Unattended Upgrades link")
            total += 1

    # --- it/update-software: same fix ---
    it_us = get_locale_dir('it') / 'manager' / 'server-management' / 'update-software.md'
    if it_us.exists():
        if fix_orphaned_link(
            it_us,
            r'usando$|tramite$|con$',
            r'^.{0,40}$',
            None,
            'https://wiki.debian.org/UnattendedUpgrades'
        ):
            print("  it/update-software: restored Unattended Upgrades link")
            total += 1

    # --- en-GB/terminology: Add back data collection policy link ---
    engb_term = get_locale_dir('en-GB') / 'about' / 'terminology.md'
    if engb_term.exists():
        if fix_orphaned_link(
            engb_term,
            r'view the$|view$',
            r'^.*details|^.*policy',
            None,
            '/about/data-collection'
        ):
            print("  en-GB/terminology: restored data collection policy link")
            total += 1

    # --- pl/data-limits: Convert plain "tutaj" to [tutaj](/about/feedback) ---
    pl_dl = get_locale_dir('pl') / 'manager' / 'server-management' / 'data-limits.md'
    if pl_dl.exists():
        text = pl_dl.read_text(encoding='utf-8')
        # Find the first 'tutaj' that's NOT already a link
        # Context: it's near "skontaktować" (contact)
        m = re.search(r'skontaktowa[ćc][^.]*?(?<!\[)(tutaj)(?!\])', text)
        if m:
            idx = m.start(1)
            new_text = text[:idx] + '[tutaj](/about/feedback)' + text[idx + 5:]
            pl_dl.write_text(new_text, encoding='utf-8')
            print("  pl/data-limits: converted plain 'tutaj' to link")
            total += 1

    # --- zh-Hans/cost: Add back DigitalOcean and data-collection links ---
    zhs_cost = get_locale_dir('zh-Hans') / 'manager' / 'server-setup' / 'cost.md'
    if zhs_cost.exists():
        if fix_orphaned_link(
            zhs_cost,
            r'例如$',
            r'^.*DigitalOcean|^.*或',
            None,
            'http://www.digitalocean.com/'
        ):
            print("  zh-Hans/cost: restored DigitalOcean link")
            total += 1

        # Second link: data-collection
        if fix_orphaned_link(
            zhs_cost,
            r'请在$|在$',
            r'^.*了解|^.*详细',
            None,
            '/about/data-collection'
        ):
            print("  zh-Hans/cost: restored data-collection link")
            total += 1

    # --- zh-Hans/terminology: fix missing link (8 vs 7) ---
    zhs_term = get_locale_dir('zh-Hans') / 'about' / 'terminology.md'
    if zhs_term.exists():
        if fix_orphaned_link(
            zhs_term,
            r'查看$|参阅$',
            r'^.*数据|^.*政策|^.*详',
            None,
            '/about/data-collection'
        ):
            print("  zh-Hans/terminology: restored data-collection link")
            total += 1

    print(f"\nDone: {total} targeted fixes")


if __name__ == "__main__":
    main()

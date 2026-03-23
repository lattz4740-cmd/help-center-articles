#!/usr/bin/env python3
"""Fix links stripped during GKMS conversion, leaving orphaned text fragments.

The converter sometimes strips [text](url) syntax, leaving the text as an
orphaned fragment on a separate line. This script detects and fixes these
across multiple docs and locales.

Pattern detected:
    ...sentence text ending abruptly
                                        ← blank line
    orphaned text continuing sentence   ← this should have been a link

Fix: rejoin the lines and wrap the orphaned text with the correct URL.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

LOCALES = [
    "af", "am", "ar", "az", "bg", "bn", "bs",
    "ca", "cs", "da", "de", "el", "en-GB",
    "es", "es-419", "et", "fa", "fi", "fil", "fr",
    "he", "hi", "hr", "hu", "hy", "id",
    "is", "it", "ja", "ka", "kk", "km", "ko", "lo", "lv",
    "mk", "mn", "mr", "ms", "my", "nb", "ne", "nl", "pl",
    "pt", "pt-BR", "ro", "ru", "si", "sk", "sl", "sq", "sr", "sv", "sw",
    "ta", "th", "tr", "uk", "ur", "vi", "zh-Hans",
    "zh-Hant", "zh-HK",
]


def get_file(locale, doc_path):
    return (I18N / locale / "docusaurus-plugin-content-docs" / "current" /
            f"{doc_path}.md")


def rejoin_orphaned_line(text, before_re, orphan_re, link_url, after_re=None):
    """Find orphaned text after a line break and rejoin with a link.

    Looks for:
        <line matching before_re>
        <blank line>
        <line matching orphan_re>
    And joins: <before> [<orphan_text>](<link_url>)<after>

    Returns (new_text, was_fixed).
    """
    lines = text.split('\n')
    for i in range(len(lines) - 2):
        line = lines[i].rstrip()
        if not re.search(before_re, line):
            continue
        if lines[i + 1].strip() != '':
            continue
        orphan = lines[i + 2].strip()
        if not re.match(orphan_re, orphan):
            continue

        # Split orphan into link text and after text
        link_text = orphan
        after_text = ''
        if after_re:
            am = re.search(after_re, orphan)
            if am:
                link_text = orphan[:am.start()].rstrip()
                after_text = orphan[am.start():]

        new_line = f"{line} [{link_text}]({link_url}){after_text}"
        lines[i] = new_line
        lines[i + 1] = ''  # blank line
        lines[i + 2] = ''  # orphan line

        result = '\n'.join(lines)
        result = re.sub(r'\n{3,}', '\n\n', result)
        return result, True

    return text, False


def fix_connecting_device():
    """Fix stripped [access key](/about/terminology) link in connecting-device."""
    total = 0
    doc = "client/getting-started/connecting-device"

    for locale in LOCALES:
        f = get_file(locale, doc)
        if not f.exists():
            continue

        text = f.read_text('utf-8')
        # Check if link already exists
        if '/about/terminology' in text:
            continue

        # Pattern: line ends without punctuation, followed by blank line,
        # then a short fragment (the orphaned link text) that continues the sentence.
        # The orphan text is what should be wrapped with the link.
        lines = text.split('\n')
        fixed = False

        for i in range(len(lines) - 2):
            line = lines[i].rstrip()
            # The line before the link typically ends with a word (no punctuation)
            if not line or line[-1] in '.!?:;,)>]"\'。！？：；，）》」':
                continue
            if lines[i + 1].strip() != '':
                continue
            orphan = lines[i + 2].strip()
            # The orphan should be short (link text fragment) and continue a sentence
            if not orphan or len(orphan) > 80:
                continue
            # Check if the next non-empty line suggests this is mid-paragraph
            # (i.e., the orphan is followed by more text, like bullet points)
            rest_idx = i + 3
            while rest_idx < len(lines) and lines[rest_idx].strip() == '':
                rest_idx += 1

            # The orphan typically ends with a period or continues the sentence
            new_line = f"{line} [{orphan.rstrip('.')}](/about/terminology)."
            # If orphan ends with punctuation, preserve it
            if orphan and orphan[-1] in '.。':
                new_line = f"{line} [{orphan.rstrip('.。')}](/about/terminology){orphan[-1]}"
            elif orphan and orphan[-1] in ':：':
                new_line = f"{line} [{orphan.rstrip(':：')}](/about/terminology){orphan[-1]}"
            else:
                new_line = f"{line} [{orphan}](/about/terminology)"

            lines[i] = new_line
            lines[i + 1] = ''
            lines[i + 2] = ''
            fixed = True
            break

        if fixed:
            result = '\n'.join(lines)
            result = re.sub(r'\n{3,}', '\n\n', result)
            f.write_text(result, 'utf-8')
            print(f"  {locale}/connecting-device: restored access key link")
            total += 1

    return total


def fix_delete_server():
    """Fix stripped [set up a new server](/manager/server-setup/setup-server) link."""
    total = 0
    doc = "manager/server-management/delete-server"
    url = "/manager/server-setup/setup-server"

    for locale in LOCALES:
        f = get_file(locale, doc)
        if not f.exists():
            continue

        text = f.read_text('utf-8')
        if url in text:
            continue

        # Same orphaned text pattern
        lines = text.split('\n')
        fixed = False

        for i in range(len(lines) - 2):
            line = lines[i].rstrip()
            if not line or line[-1] in '.!?:;,)>]"\'。！？：；，）》」':
                continue
            if lines[i + 1].strip() != '':
                continue
            orphan = lines[i + 2].strip()
            if not orphan or len(orphan) > 100:
                continue

            new_line = f"{line} [{orphan}]({url})"
            lines[i] = new_line
            lines[i + 1] = ''
            lines[i + 2] = ''
            fixed = True
            break

        if fixed:
            result = '\n'.join(lines)
            result = re.sub(r'\n{3,}', '\n\n', result)
            f.write_text(result, 'utf-8')
            print(f"  {locale}/delete-server: restored setup-server link")
            total += 1

    return total


def fix_windows_install():
    """Fix stripped [contact support](/about/feedback) link at end of file."""
    total = 0
    doc = "client/troubleshooting/windows-install"
    url = "/about/feedback"

    for locale in LOCALES:
        f = get_file(locale, doc)
        if not f.exists():
            continue

        text = f.read_text('utf-8')
        # English has 3 links to /about/feedback, check if translation has fewer
        feedback_count = len(re.findall(r'\]\(/about/feedback\)', text))
        if feedback_count >= 2:
            # Has both feedback links, skip
            continue

        # The missing link is typically at the end of the file
        lines = text.split('\n')
        fixed = False

        for i in range(len(lines) - 2):
            line = lines[i].rstrip()
            if not line or line[-1] in '.!?:;,)>]"\'。！？：；，）》」':
                continue
            if lines[i + 1].strip() != '':
                continue
            orphan = lines[i + 2].strip()
            if not orphan:
                continue
            # The orphan should be short and near end of file
            if len(orphan) > 50 and i < len(lines) - 10:
                continue

            new_line = f"{line} [{orphan.rstrip('.')}]({url})."
            if orphan and orphan[-1] in '.。':
                new_line = f"{line} [{orphan.rstrip('.。')}]({url}){orphan[-1]}"
            else:
                new_line = f"{line} [{orphan}]({url})"

            lines[i] = new_line
            lines[i + 1] = ''
            lines[i + 2] = ''
            fixed = True
            break

        if fixed:
            result = '\n'.join(lines)
            result = re.sub(r'\n{3,}', '\n\n', result)
            f.write_text(result, 'utf-8')
            print(f"  {locale}/windows-install: restored contact support link")
            total += 1

    return total


def fix_feedback():
    """Fix stripped GitHub and Reddit links in feedback page."""
    total = 0
    doc = "about/feedback"

    for locale in LOCALES:
        f = get_file(locale, doc)
        if not f.exists():
            continue

        text = f.read_text('utf-8')
        fixed = False

        # Check for GitHub mention without link
        if 'GitHub' in text and '[GitHub]' not in text and 'github.com' not in text:
            # Find "GitHub" in the developer bullet and wrap it
            text = re.sub(
                r'(?<!\[)(GitHub)(?!\])',
                r'[\1](https://github.com/jigsaw-Code/?q=outline)',
                text,
                count=1  # Only first occurrence
            )
            fixed = True

        # Check for Reddit mention without link
        if 'Reddit' in text and '[Reddit]' not in text and 'reddit.com' not in text:
            text = re.sub(
                r'(?<!\[)(Reddit)(?!\])',
                r'[\1](https://www.reddit.com/r/outlinevpn/)',
                text,
                count=1
            )
            fixed = True

        if fixed:
            f.write_text(text, 'utf-8')
            print(f"  {locale}/feedback: restored GitHub/Reddit links")
            total += 1

    return total


def fix_how_outline_works():
    """Fix stripped links in how-outline-works.

    This page has many stripped links. We fix the ones that can be
    reliably detected: orphaned text patterns and known URL references.
    """
    total = 0
    doc = "about/how-outline-works"

    link_map = {
        'Watchtower': 'https://github.com/v2tec/watchtower',
        'GitHub': 'https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline',
        'Radically Open Security': 'https://radicallyopensecurity.com/',
        'Cure53': 'https://cure53.de/',
    }

    for locale in LOCALES:
        f = get_file(locale, doc)
        if not f.exists():
            continue

        text = f.read_text('utf-8')
        fixed = False

        # Fix known proper nouns that should be links
        for name, url in link_map.items():
            if name in text and f'[{name}]' not in text and url not in text:
                text = re.sub(
                    r'(?<!\[)(' + re.escape(name) + r')(?!\])',
                    rf'[\1]({url})',
                    text,
                    count=1
                )
                fixed = True

        # Fix orphaned text patterns (blank line splits)
        text_new, was_fixed = rejoin_orphaned_line(
            text,
            r'(?:hosted|gehostet|hébergé|hospedado|alojado|host|gehost).*$',
            r'^.{0,10}$',  # very short orphan
            'https://en.wikipedia.org/wiki/Self-signed_certificate',
        )
        if was_fixed:
            text = text_new
            fixed = True

        # Fix /about/security-and-privacy link if missing
        if '/about/security-and-privacy' not in text:
            # Look for orphaned "here" text
            for here_word in ['here', 'hier', 'ici', 'aquí', 'aqui', 'qui', 'здесь',
                              'こちら', '여기', '此处', '這裡']:
                if here_word in text:
                    text_new = text.replace(
                        f' {here_word}.',
                        f' [{here_word}](/about/security-and-privacy).',
                        1
                    )
                    if text_new != text:
                        text = text_new
                        fixed = True
                        break

        if fixed:
            f.write_text(text, 'utf-8')
            print(f"  {locale}/how-outline-works: restored links")
            total += 1

    return total


def main():
    total = 0
    print("Fixing connecting-device...")
    total += fix_connecting_device()
    print("\nFixing delete-server...")
    total += fix_delete_server()
    print("\nFixing windows-install...")
    total += fix_windows_install()
    print("\nFixing feedback...")
    total += fix_feedback()
    print("\nFixing how-outline-works...")
    total += fix_how_outline_works()
    print(f"\nDone: {total} total fixes")


if __name__ == "__main__":
    main()

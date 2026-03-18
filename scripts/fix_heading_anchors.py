#!/usr/bin/env python3
"""Add English heading anchor IDs to all translated docs.

For each English doc that has custom heading anchors ({#id}), finds the
corresponding translated docs and adds the same anchor IDs to their headings
at matching positions (by heading index, not by text match).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
I18N = ROOT / "i18n"

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*?)(?:\s*\{#[^}]+\})?\s*$', re.MULTILINE)
ANCHOR_RE = re.compile(r'\{#([^}]+)\}')


def extract_headings_with_anchors(text):
    """Extract all headings with their anchor IDs. Returns [(level, text, anchor_id)]."""
    results = []
    for m in HEADING_RE.finditer(text):
        level = len(m.group(1))
        heading_text = m.group(2).strip()
        # Check if there's an anchor
        anchor_match = ANCHOR_RE.search(m.group(0))
        anchor_id = anchor_match.group(1) if anchor_match else None
        results.append((level, heading_text, anchor_id))
    return results


def add_anchors_to_translation(en_text, tr_text):
    """Add English anchor IDs to translated headings at matching positions.

    Returns (modified_text, count_added) or (None, 0) if no changes needed.
    """
    en_headings = extract_headings_with_anchors(en_text)
    tr_headings = extract_headings_with_anchors(tr_text)

    # Collect English anchors by (level, position_index_at_that_level)
    # We match by overall heading index since heading text differs across languages
    en_anchors = {}  # heading_index -> anchor_id
    for i, (level, text, anchor_id) in enumerate(en_headings):
        if anchor_id:
            en_anchors[i] = anchor_id

    if not en_anchors:
        return None, 0

    # Find all heading positions in the translation text
    tr_heading_matches = list(HEADING_RE.finditer(tr_text))

    if len(tr_heading_matches) != len(en_headings):
        # Heading count mismatch — try matching by level sequence instead
        # Build a mapping: for each English heading with an anchor, find the
        # translation heading at the same level-order position
        en_level_seq = [(i, h[0], h[2]) for i, h in enumerate(en_headings) if h[2]]
        tr_by_idx = {i: m for i, m in enumerate(tr_heading_matches)}

        # If counts differ too much, skip
        if abs(len(tr_heading_matches) - len(en_headings)) > len(en_headings) * 0.5:
            return None, 0

        # Fall back: match anchored English headings to translation headings
        # by finding translation headings at the same level
        anchor_assignments = {}  # tr_match_index -> anchor_id
        tr_idx = 0
        en_idx = 0
        while en_idx < len(en_headings) and tr_idx < len(tr_heading_matches):
            en_level = en_headings[en_idx][0]
            tr_match = tr_heading_matches[tr_idx]
            tr_level = len(tr_match.group(1))

            if en_level == tr_level:
                if en_headings[en_idx][2]:  # Has anchor
                    anchor_assignments[tr_idx] = en_headings[en_idx][2]
                en_idx += 1
                tr_idx += 1
            elif tr_level > en_level:
                # Translation has extra heading, skip it
                tr_idx += 1
            else:
                # English has extra heading, skip it
                en_idx += 1

        if not anchor_assignments:
            return None, 0

        # Apply anchors
        changes = 0
        result = tr_text
        for tr_match_idx in sorted(anchor_assignments.keys(), reverse=True):
            anchor_id = anchor_assignments[tr_match_idx]
            m = tr_heading_matches[tr_match_idx]
            existing_anchor = ANCHOR_RE.search(m.group(0))
            if existing_anchor:
                continue  # Already has an anchor

            # Insert anchor before end of line
            old_line = m.group(0)
            heading_prefix = m.group(1)
            heading_text = m.group(2).strip()
            new_line = f"{heading_prefix} {heading_text} {{#{anchor_id}}}"
            result = result[:m.start()] + new_line + result[m.end():]
            changes += 1

        return (result, changes) if changes > 0 else (None, 0)

    # Same heading count — straightforward positional matching
    changes = 0
    result = tr_text
    for idx in sorted(en_anchors.keys(), reverse=True):
        anchor_id = en_anchors[idx]

        if idx >= len(tr_heading_matches):
            continue

        m = tr_heading_matches[idx]
        existing_anchor = ANCHOR_RE.search(m.group(0))
        if existing_anchor:
            continue  # Already has an anchor

        old_line = m.group(0)
        heading_prefix = m.group(1)
        heading_text = m.group(2).strip()
        new_line = f"{heading_prefix} {heading_text} {{#{anchor_id}}}"
        result = result[:m.start()] + new_line + result[m.end():]
        changes += 1

    return (result, changes) if changes > 0 else (None, 0)


def get_locale_dirs():
    """Get all locale directories in i18n/."""
    dirs = []
    for d in sorted(I18N.iterdir()):
        if d.is_dir() and d.name != "partial-translations":
            docs_dir = d / "docusaurus-plugin-content-docs" / "current"
            if docs_dir.exists():
                dirs.append((d.name, docs_dir))
    return dirs


def main():
    # Find all English docs with custom anchors
    en_docs_with_anchors = {}
    for en_file in DOCS.rglob("*.md"):
        text = en_file.read_text(encoding="utf-8")
        headings = extract_headings_with_anchors(text)
        has_anchors = any(h[2] for h in headings)
        if has_anchors:
            doc_path = str(en_file.relative_to(DOCS).with_suffix(""))
            en_docs_with_anchors[doc_path] = text

    print(f"English docs with custom anchors: {len(en_docs_with_anchors)}")
    for dp in sorted(en_docs_with_anchors):
        anchors = [h[2] for h in extract_headings_with_anchors(en_docs_with_anchors[dp]) if h[2]]
        print(f"  {dp}: {anchors}")
    print()

    total_files = 0
    total_anchors = 0

    for locale, locale_dir in get_locale_dirs():
        for doc_path, en_text in en_docs_with_anchors.items():
            tr_file = locale_dir / f"{doc_path}.md"
            if not tr_file.exists():
                continue

            tr_text = tr_file.read_text(encoding="utf-8")
            result, count = add_anchors_to_translation(en_text, tr_text)

            if result:
                tr_file.write_text(result, encoding="utf-8")
                print(f"  {locale}/{doc_path}: added {count} anchor(s)")
                total_files += 1
                total_anchors += count

    print(f"\nDone: added {total_anchors} anchors in {total_files} files")


if __name__ == "__main__":
    main()

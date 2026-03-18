#!/usr/bin/env python3
"""Convert GKMS HTML exports to Markdown for Docusaurus."""

import os
import re
import textwrap
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parent.parent
OLD_SITE = ROOT / "old-site"
DOCS = ROOT / "docs"

HELP_CENTER_WEBS = OLD_SITE / "Help Center" / "WEBS_14917423,14919822,15330317,15330818,plus_31_more_en.HTML"
IMAGE_SNIPPETS = OLD_SITE / "FAQ Snippets" / "IMAGE_SNIPPETS_15474360,15787036,15787037,15787423,plus_191_more_en.HTML"

# WEB ID → (doc_path relative to docs/, sidebar_label from existing frontmatter)
WEB_ID_TO_DOC = {
    "14917423": "about/how-outline-works",
    "14919822": "about/security-and-privacy",
    "15330317": "client/troubleshooting/internet-access",
    "15330818": "client/getting-started/system-requirements",
    "15330824": "manager/server-management/update-software",
    "15330825": "manager/troubleshooting/manager-download",
    "15330920": "about/terminology",
    "15331121": "about/getoutline-me-telegram",
    "15331122": "client/getting-started/available-languages",
    "15331125": "client/troubleshooting/windows-install",
    "15331126": "client/troubleshooting/connection-issues",
    "15331127": "client/troubleshooting/download-link",
    "15331222": "about/data-collection",
    "15331223": "client/troubleshooting/access-key-issues",
    "15331322": "manager/server-setup/cost",
    "15331326": "manager/server-management/data-limits",
    "15331327": "manager/server-management/reset-server-id",
    "15331328": "manager/server-management/change-location",
    "15331423": "about/feedback",
    "15331424": "manager/server-management/manage-access-keys",
    "15331524": "about/access-resources-blocked",
    "15331527": "client/getting-started/install-linux",
    "15331528": "client/getting-started/access-key-reuse",
    "15331529": "client/getting-started/connecting-device",
    "15331530": "manager/server-setup/setup-server",
    "15331625": "about/brand-usage",
    "15331628": "client/getting-started/get-access-key",
    "15331630": "manager/server-management/delete-server",
    "15331631": "manager/server-setup/multiple-servers",
    "15331632": "manager/troubleshooting/windows-install",
    "15331727": "manager/server-setup/google-cloud",
    "15331728": "manager/server-setup/setup-faqs",
    "15331758": "developers/sdk-support",
    "15448041": "manager/server-setup/available-languages",
    "15528599": "client/troubleshooting/firewall-errors",
    # Legacy FAQ WEB IDs that redirect to Help Center articles
    "15548974": "manager/server-management/reset-server-id",
}

# Build URL path map for link remapping
WEB_ID_TO_URL = {wid: f"/{path}" for wid, path in WEB_ID_TO_DOC.items()}


def parse_image_snippets():
    """Parse IMAGE_SNIPPETS file to build snippet_id → {alt, blob, mime} map."""
    snippets = {}
    with open(IMAGE_SNIPPETS, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    current_id = None
    for div in soup.find_all("div", class_="gkms"):
        classes = div.get("class", [])
        text = div.get_text(strip=True)

        if "id" in classes and "notranslate" in classes:
            m = re.match(r"IMAGE_SNIPPET:(\d+)", text)
            if m:
                current_id = m.group(1)
                snippets[current_id] = {"alt": "", "blob": "", "mime": "image/png", "url": ""}
        elif current_id:
            if "alt" in classes and "text" in classes:
                snippets[current_id]["alt"] = text
            elif "blob" in classes and "name" in classes:
                snippets[current_id]["blob"] = text
            elif "mime" in classes and "type" in classes:
                snippets[current_id]["mime"] = text
            elif "url" in classes and "shoebox" not in classes and "notranslate" in classes:
                if text.startswith("//"):
                    snippets[current_id]["url"] = "https:" + text
                else:
                    snippets[current_id]["url"] = text

    return snippets


def remap_link(href):
    """Convert old internal links to new doc paths."""
    if not href:
        return href

    # Match /outline-faq/answer/WEB_ID or /outline/answer/WEB_ID with optional #anchor
    m = re.match(r"/outline(?:-faq)?/answer/(\d+)(#\w+)?", href)
    if m:
        web_id = m.group(1)
        anchor = m.group(2) or ""
        if web_id in WEB_ID_TO_URL:
            return WEB_ID_TO_URL[web_id] + anchor
        return href

    return href


def is_header_paragraph(element):
    """Check if a <p> contains only a <strong>/<b> child (used as section header).

    Also detects: <p><a id="X"><strong>Title</strong></a></p> (anchor + header)
    """
    if element.name != "p":
        return False
    children = [c for c in element.children if not (isinstance(c, NavigableString) and c.strip() == "")]
    if not children:
        return False

    target = children[0]

    # Unwrap anchor wrapper: <a id="X"><strong>Title</strong></a>
    if len(children) == 1 and isinstance(target, Tag) and target.name == "a" and (target.get("id") or target.get("name")):
        inner_children = [c for c in target.children if not (isinstance(c, NavigableString) and c.strip() == "")]
        if len(inner_children) == 1 and isinstance(inner_children[0], Tag) and inner_children[0].name in ("strong", "b"):
            target = inner_children[0]
        else:
            return False

    if len(children) == 1 and isinstance(target, Tag) and target.name in ("strong", "b"):
        inner_children = [c for c in target.children if not (isinstance(c, NavigableString) and c.strip() == "")]
        if all(isinstance(c, NavigableString) for c in inner_children):
            return True
        # Also handle <b><strong>text</strong></b> nesting
        if len(inner_children) == 1 and isinstance(inner_children[0], Tag) and inner_children[0].name in ("strong", "b"):
            return True
    return False


def get_header_text(element):
    """Extract text from a header-style paragraph."""
    return element.get_text(strip=True)


def convert_inline(element):
    """Convert inline HTML to Markdown text."""
    if isinstance(element, NavigableString):
        text = str(element)
        text = text.replace("\xa0", " ")  # &nbsp;
        return text

    if not isinstance(element, Tag):
        return ""

    tag = element.name

    if tag in ("strong", "b"):
        inner = "".join(convert_inline(c) for c in element.children).strip()
        if not inner:
            return ""
        return f"**{inner}**"

    if tag == "em" or tag == "i":
        inner = "".join(convert_inline(c) for c in element.children).strip()
        if not inner:
            return ""
        return f"*{inner}*"

    if tag == "u":
        # No underline in Markdown, just pass through
        return "".join(convert_inline(c) for c in element.children)

    if tag == "a":
        href = element.get("href", "")
        anchor_id = element.get("id") or element.get("name")

        # Anchor target with no href (or empty href) - just render the text content
        if (not href or href == "") and anchor_id:
            text = "".join(convert_inline(c) for c in element.children).strip()
            return text
        # Empty anchor with no id either - just render children
        if not href:
            return "".join(convert_inline(c) for c in element.children)

        href = remap_link(href)
        text = "".join(convert_inline(c) for c in element.children).strip()
        if not text:
            text = href
        return f"[{text}]({href})"

    if tag == "br":
        return "\n"

    if tag == "code":
        return f"`{''.join(convert_inline(c) for c in element.children)}`"

    if tag == "sup":
        return "".join(convert_inline(c) for c in element.children)

    if tag == "img":
        # Skip 1x1 tracking/broken images
        width = element.get("width", "")
        height = element.get("height", "")
        if width == "1" or height == "1":
            return ""
        alt = element.get("alt", "")
        src = element.get("src", "")
        return f"![{alt}]({src})"

    # For any other inline tag, just recurse
    return "".join(convert_inline(c) for c in element.children)


def convert_list(element, indent=0):
    """Convert <ul> or <ol> to Markdown list."""
    lines = []
    ordered = element.name == "ol"
    counter = 1

    for child in element.children:
        if isinstance(child, NavigableString):
            continue
        if child.name != "li":
            continue

        prefix = f"{counter}. " if ordered else "- "
        indent_str = "   " * indent

        # Collect inline content and sub-elements
        inline_parts = []
        sub_blocks = []

        for item in child.children:
            if isinstance(item, Tag) and item.name in ("ul", "ol"):
                sub_blocks.append(("list", item))
            elif isinstance(item, Tag) and item.name == "div" and "code" in item.get("class", []):
                sub_blocks.append(("code", item))
            elif isinstance(item, Tag) and item.name == "p":
                text = "".join(convert_inline(c) for c in item.children).strip()
                if text:
                    inline_parts.append(text)
            else:
                inline_parts.append(convert_inline(item))

        text = "".join(inline_parts).strip()
        # Clean up multiple spaces
        text = re.sub(r" {2,}", " ", text)
        lines.append(f"{indent_str}{prefix}{text}")

        for block_type, block_el in sub_blocks:
            if block_type == "list":
                lines.append(convert_list(block_el, indent + 1))
            elif block_type == "code":
                code_text = extract_code_text(block_el)
                # Indent code block to be inside list item
                code_indent = "   " * (indent + 1)
                lines.append(f"{code_indent}```")
                for code_line in code_text.split("\n"):
                    lines.append(f"{code_indent}{code_line}")
                lines.append(f"{code_indent}```")

        counter += 1

    return "\n".join(lines)


def extract_code_text(div):
    """Extract text from <div class="code"><div class="no-margin">...</div></div>."""
    no_margin = div.find("div", class_="no-margin")
    if no_margin:
        # Might contain <p> tags or direct text
        parts = []
        for child in no_margin.children:
            if isinstance(child, NavigableString):
                text = child.strip()
                if text:
                    parts.append(text)
            elif isinstance(child, Tag) and child.name == "p":
                parts.append(child.get_text(strip=True))
            else:
                parts.append(child.get_text(strip=True))
        return "\n".join(parts)
    return div.get_text(strip=True)


def convert_table(table):
    """Convert HTML table to Markdown table."""
    rows = table.find_all("tr")
    if not rows:
        return ""

    md_rows = []
    for row in rows:
        cells = row.find_all(["td", "th"])
        md_cells = []
        for cell in cells:
            text = "".join(convert_inline(c) for c in cell.children).strip()
            text = text.replace("|", "\\|")
            text = re.sub(r"\s+", " ", text)
            md_cells.append(text)
        md_rows.append("| " + " | ".join(md_cells) + " |")

    if len(md_rows) >= 1:
        # Add separator after first row (header)
        num_cols = md_rows[0].count("|") - 1
        separator = "| " + " | ".join(["---"] * num_cols) + " |"
        md_rows.insert(1, separator)

    return "\n".join(md_rows)


def is_inline_element(element):
    """Check if an element is inline (not a block element)."""
    if isinstance(element, NavigableString):
        return True
    if isinstance(element, Tag):
        return element.name in ("a", "strong", "b", "em", "i", "u", "code", "span", "sup", "sub", "br", "img")
    return False


def convert_body(web_div, image_snippets):
    """Convert the content of a <div class="gkms web"> to Markdown."""
    blocks = []

    # Check if the div has mixed inline content (text + <a> without wrapping <p>)
    children = list(web_div.children)
    has_block_children = any(
        isinstance(c, Tag) and c.name in ("p", "ul", "ol", "table", "div", "h1", "h2", "h3", "h4", "h5", "h6", "pre", "hr")
        for c in children
    )

    if not has_block_children:
        # All content is inline - collect it as a single paragraph
        text = "".join(convert_inline(c) for c in children).strip()
        text = text.replace("\xa0", " ")
        text = re.sub(r" {2,}", " ", text)
        if text:
            blocks.append(text)
        return "\n\n".join(blocks)

    for child in children:
        if isinstance(child, NavigableString):
            text = child.strip()
            if text:
                blocks.append(text)
            continue

        if not isinstance(child, Tag):
            continue

        # Skip empty elements
        if not child.get_text(strip=True) and child.name not in ("hr", "br", "img"):
            # Check for gkms:snippet
            snippet = child.find("gkms:snippet")
            if not snippet:
                continue

        # Handle gkms:snippet (image references)
        if child.name == "gkms:snippet":
            sid = child.get("id", "")
            if sid in image_snippets:
                alt = image_snippets[sid]["alt"] or f"Screenshot {sid}"
                blocks.append(f"![{alt}](/images/snippet-{sid}.png)")
            continue

        # Paragraph containing only a snippet
        if child.name == "p":
            snippet = child.find("gkms:snippet")
            if snippet:
                sid = snippet.get("id", "")
                if sid in image_snippets:
                    alt = image_snippets[sid]["alt"] or f"Screenshot {sid}"
                    blocks.append(f"![{alt}](/images/snippet-{sid}.png)")
                continue

        # Header-style paragraph: <p><strong>Title</strong></p>
        if is_header_paragraph(child):
            header_text = get_header_text(child)
            if header_text:
                blocks.append(f"## {header_text}")
            continue

        # Actual headers
        if child.name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(child.name[1])
            text = "".join(convert_inline(c) for c in child.children).strip()
            # Strip bold from headers (redundant)
            text = re.sub(r"^\*\*(.+)\*\*$", r"\1", text)
            if text:
                blocks.append(f"{'#' * level} {text}")
            continue

        # Paragraphs
        if child.name == "p":
            text = "".join(convert_inline(c) for c in child.children).strip()
            # Clean up
            text = text.replace("\xa0", " ")
            text = re.sub(r" {2,}", " ", text)
            # Remove leading/trailing newlines from br conversions
            text = text.strip("\n").strip()
            if text:
                blocks.append(text)
            continue

        # Lists
        if child.name in ("ul", "ol"):
            blocks.append(convert_list(child))
            continue

        # Tables
        if child.name == "table":
            blocks.append(convert_table(child))
            continue

        # Code blocks
        if child.name == "div" and "code" in child.get("class", []):
            code_text = extract_code_text(child)
            blocks.append(f"```\n{code_text}\n```")
            continue

        # Pre blocks
        if child.name == "pre":
            text = child.get_text()
            blocks.append(f"```\n{text.strip()}\n```")
            continue

        # Horizontal rules
        if child.name == "hr":
            blocks.append("---")
            continue

        # Images
        if child.name == "img":
            alt = child.get("alt", "")
            src = child.get("src", "")
            blocks.append(f"![{alt}]({src})")
            continue

        # Divs that aren't code blocks - recurse
        if child.name == "div":
            text = "".join(convert_inline(c) for c in child.children).strip()
            if text:
                blocks.append(text)
            continue

    # Join blocks with double newlines
    md = "\n\n".join(blocks)

    # Clean up excessive whitespace
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = md.strip()

    return md


def extract_articles(html_path):
    """Parse GKMS HTML and return list of (web_id, title, body_html) tuples."""
    with open(html_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    articles = []
    # Find all WEB ID markers
    id_divs = soup.find_all("div", class_="gkms")

    i = 0
    while i < len(id_divs):
        div = id_divs[i]
        classes = div.get("class", [])
        text = div.get_text(strip=True)

        if "id" in classes and "notranslate" in classes:
            m = re.match(r"WEB:(\d+)", text)
            if m:
                web_id = m.group(1)

                # Find title - next sibling with class "gkms article title"
                title = ""
                web_content = None

                # Walk siblings after this div
                sibling = div.next_sibling
                while sibling:
                    if isinstance(sibling, Tag):
                        sib_classes = sibling.get("class", [])
                        if "gkms" in sib_classes:
                            if "article" in sib_classes and "title" in sib_classes:
                                title = sibling.get_text(strip=True)
                            elif "web" in sib_classes:
                                web_content = sibling
                                break
                            elif "id" in sib_classes and "notranslate" in sib_classes:
                                # Next article started, this one has no body
                                break
                    sibling = sibling.next_sibling

                if web_content is not None:
                    articles.append((web_id, title, web_content))

        i += 1

    return articles


def read_existing_frontmatter(doc_path):
    """Read existing frontmatter from a doc file."""
    full_path = DOCS / f"{doc_path}.md"
    if not full_path.exists():
        return {}

    with open(full_path, encoding="utf-8") as f:
        content = f.read()

    fm = {}
    if content.startswith("---"):
        end = content.find("---", 3)
        if end > 0:
            fm_text = content[3:end].strip()
            for line in fm_text.split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    val = val.strip()
                    # Remove quotes
                    if val.startswith('"') and val.endswith('"'):
                        val = val[1:-1]
                    elif val.startswith("'") and val.endswith("'"):
                        val = val[1:-1]
                    fm[key.strip()] = val
    return fm


def needs_yaml_quoting(s):
    """Check if a YAML value needs quoting."""
    # Quote if it contains special chars or starts with special chars
    if any(c in s for c in [':', '"', "'", "#", "{", "}", "[", "]", ",", "&", "*", "?", "|", "-", "<", ">", "=", "!", "%", "@", "`"]):
        return True
    if s.startswith((" ", "\t")):
        return True
    return False


def yaml_quote(s):
    """Quote a string for YAML frontmatter."""
    if needs_yaml_quoting(s):
        # Use double quotes, escape internal double quotes
        escaped = s.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return s


def write_doc(doc_path, title, sidebar_label, body_md):
    """Write a Markdown doc file with frontmatter."""
    full_path = DOCS / f"{doc_path}.md"
    full_path.parent.mkdir(parents=True, exist_ok=True)

    fm_lines = [
        "---",
        f"title: {yaml_quote(title)}",
        f"sidebar_label: {yaml_quote(sidebar_label)}",
        "---",
    ]

    content = "\n".join(fm_lines) + "\n\n" + body_md + "\n"

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  Wrote {full_path.relative_to(ROOT)}")


def main():
    print("Parsing image snippets...")
    image_snippets = parse_image_snippets()
    print(f"  Found {len(image_snippets)} image snippets")

    print(f"\nParsing articles from {HELP_CENTER_WEBS.name}...")
    articles = extract_articles(HELP_CENTER_WEBS)
    print(f"  Found {len(articles)} articles")

    converted = 0
    skipped = 0

    for web_id, title, web_content in articles:
        if web_id not in WEB_ID_TO_DOC:
            print(f"  WARNING: No doc mapping for WEB:{web_id} '{title}'")
            skipped += 1
            continue

        doc_path = WEB_ID_TO_DOC[web_id]

        # Read existing frontmatter to preserve sidebar_label
        existing_fm = read_existing_frontmatter(doc_path)
        sidebar_label = existing_fm.get("sidebar_label", title)

        # Convert body
        body_md = convert_body(web_content, image_snippets)

        # Write output
        write_doc(doc_path, title, sidebar_label, body_md)
        converted += 1

    print(f"\nDone: {converted} articles converted, {skipped} skipped")


if __name__ == "__main__":
    main()

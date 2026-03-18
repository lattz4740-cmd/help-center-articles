#!/usr/bin/env python3
"""Create minimal placeholder PNG images for GKMS snippets."""

import os
import struct
import zlib

SNIPPETS = {
    "15787036": ("Data limits setting in Outline Manager", 850, 203),
    "15787037": ("Outline Manager's Access Key page", 939, 652),
    "15787423": ("Selecting the data limit setting icon", 942, 652),
    "15788414": ("Removing the data limit on an individual access key", 943, 651),
    "15788959": ("Setting a data limit for an individual access key", 946, 652),
}

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "static", "images")


def create_png(width, height):
    """Create a minimal valid 1x1 light gray PNG scaled to given dimensions in metadata."""

    def chunk(chunk_type, data):
        c = chunk_type + data
        crc = struct.pack(">I", zlib.crc32(c) & 0xFFFFFFFF)
        return struct.pack(">I", len(data)) + c + crc

    signature = b"\x89PNG\r\n\x1a\n"
    ihdr = chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))

    # Create a light gray image (RGB 220,220,220)
    raw_data = b""
    for _ in range(height):
        raw_data += b"\x00" + b"\xdc\xdc\xdc" * width

    compressed = zlib.compress(raw_data)
    idat = chunk(b"IDAT", compressed)
    iend = chunk(b"IEND", b"")

    return signature + ihdr + idat + iend


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Use small dimensions for placeholder (not full size, to keep files tiny)
    for snippet_id, (alt, w, h) in SNIPPETS.items():
        filename = f"snippet-{snippet_id}.png"
        dest = os.path.join(OUTPUT_DIR, filename)
        # Scale down to small placeholder
        pw, ph = min(w, 200), min(h, 100)
        png_data = create_png(pw, ph)
        with open(dest, "wb") as f:
            f.write(png_data)
        print(f"  Created {filename} ({pw}x{ph}, {len(png_data)} bytes)")


if __name__ == "__main__":
    main()

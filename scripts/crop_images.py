#!/usr/bin/env python3
"""Crop whitespace from landing page PNG images."""

from PIL import Image
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "static" / "images"

for name in ["landing-guides.png", "landing-reference.png"]:
    img = Image.open(IMAGES / name)
    # Get bounding box of non-white content
    bg = Image.new(img.mode, img.size, (255, 255, 255))
    diff = Image.new(img.mode, img.size)
    for x in range(img.width):
        for y in range(img.height):
            p = img.getpixel((x, y))
            b = bg.getpixel((x, y))
            if isinstance(p, int):
                diff.putpixel((x, y), abs(p - b))
            else:
                diff.putpixel((x, y), tuple(abs(a - c) for a, c in zip(p, b)))

    bbox = diff.getbbox()
    if bbox:
        # Add small padding
        pad = 10
        bbox = (max(0, bbox[0] - pad), max(0, bbox[1] - pad),
                min(img.width, bbox[2] + pad), min(img.height, bbox[3] + pad))
        cropped = img.crop(bbox)
        cropped.save(IMAGES / name)
        print(f"  {name}: {img.size} -> {cropped.size}")
    else:
        print(f"  {name}: no crop needed")

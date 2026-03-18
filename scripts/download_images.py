#!/usr/bin/env python3
"""Download GKMS image snippets from Google Cloud Storage."""

import os
import subprocess

IMAGES = {
    "15787036": "pTG43YJIlkO0SnYCaWF6eaCmL305E0WjTddh",
    "15787037": "FxZII6l9JarUVtFbkqJA962CPkA3PlCOHwOo",
    "15787423": "xkSqdIov2SIZomMP9wqDXCs6b3x7Lhh25EXO",
    "15788414": "0NEzskHJPCkVwyyYsz9GDwNAO1wkYS5KriLs",
    "15788959": "KTYMAKRiG6EvZUskKayNzs3KpnMOoUW8JQlH",
}

BASE_URL = "https://storage.cloud.google.com/support-kms-prod/"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "static", "images")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for snippet_id, blob in IMAGES.items():
        filename = f"snippet-{snippet_id}.png"
        url = BASE_URL + blob
        dest = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(dest):
            print(f"  Already exists: {dest}")
            continue
        print(f"  Downloading snippet {snippet_id} -> {filename}")
        result = subprocess.run(
            ["curl", "-sL", "-o", dest, "-w", "%{http_code}", url],
            capture_output=True, text=True,
        )
        status = result.stdout.strip()
        if status == "200" and os.path.exists(dest):
            size = os.path.getsize(dest)
            print(f"  OK ({size} bytes)")
        else:
            print(f"  FAILED: HTTP {status}")
            if os.path.exists(dest):
                os.remove(dest)


if __name__ == "__main__":
    main()

#!/bin/bash
# Rename downloaded blob images to snippet-ID filenames expected by the docs.

DIR="$(dirname "$0")/../static/images"

mv "$DIR/pTG43YJIlkO0SnYCaWF6eaCmL305E0WjTddh.png" "$DIR/snippet-15787036.png"
mv "$DIR/FxZII6l9JarUVtFbkqJA962CPkA3PlCOHwOo.png" "$DIR/snippet-15787037.png"
mv "$DIR/xkSqdIov2SIZomMP9wqDXCs6b3x7Lhh25EXO.png" "$DIR/snippet-15787423.png"
mv "$DIR/0NEzskHJPCkVwyyYsz9GDwNAO1wkYS5KriLs.png" "$DIR/snippet-15788414.png"
mv "$DIR/KTYMAKRiG6EvZUskKayNzs3KpnMOoUW8JQlH.png" "$DIR/snippet-15788959.png"

echo "Done. Renamed 5 images."

#!/bin/bash
# Move partial translation locales from i18n/ to i18n/partial-translations/
# These are locales not listed on support.google.com/outline AND with < 35 docs.

set -euo pipefail

PARTIAL_DIR="i18n/partial-translations"
mkdir -p "$PARTIAL_DIR"

LOCALES=(
  ar-EG as be cy de-CH en-AU en-CA en-IN en-SG eu
  fr-CA ga gl gu ha kn ky lt ml or
  pa te uz yo zu
)

for locale in "${LOCALES[@]}"; do
  if [ -d "i18n/$locale" ]; then
    echo "Moving i18n/$locale -> $PARTIAL_DIR/$locale"
    mv "i18n/$locale" "$PARTIAL_DIR/$locale"
  else
    echo "SKIP i18n/$locale (not found)"
  fi
done

echo ""
echo "Done. Moved ${#LOCALES[@]} locales to $PARTIAL_DIR/"

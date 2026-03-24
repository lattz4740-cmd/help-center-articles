#!/bin/bash
# Updates old S3/Google links to new getoutline.org URLs across the help-center-articles repo.
# Usage: ./scripts/update-links.sh

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Updating links in $PROJECT_DIR..."

find "$PROJECT_DIR" \( -name "*.ts" -o -name "*.tsx" -o -name "*.md" -o -name "*.mdx" -o -name "*.json" \) \
  -not -path "*/node_modules/*" \
  -not -path "*/.docusaurus/*" \
  -not -path "*/build/*" \
  -not -path "*/old-site/*" \
  -exec sed -i '' \
    -e 's|https://s3.amazonaws.com/outline-vpn/static_downloads/Outline-Terms-of-Service.html|https://getoutline.org/policies/terms-of-service|g' \
    -e 's|https://s3.amazonaws.com/outline-vpn/static_downloads/Outline-Privacy-Policy.html|https://getoutline.org/policies/privacy|g' \
    -e 's|https://s3.amazonaws.com/outline-vpn/static_downloads/Outline-Data-Collection-Policy.html|https://getoutline.org/policies/data-collection|g' \
    -e 's|https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf|https://getoutline.org/reports/ros-report.pdf|g' \
    -e 's|https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf|https://getoutline.org/reports/cure53-report.pdf|g' \
    -e 's|https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf|https://getoutline.org/reports/ros-report-2022.pdf|g' \
    -e 's|https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf|https://getoutline.org/reports/cure53-report-SDK-2024.pdf|g' \
    {} +

echo "Done."

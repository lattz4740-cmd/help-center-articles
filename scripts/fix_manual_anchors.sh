#!/bin/bash
# Re-apply manual anchor fixes that get lost when converter is re-run.
set -euo pipefail
I18N="i18n"

# German: plain text section titles → ## headings
sed -i '' 's/^Probleme mit der Firewall oder dem Antivirenprogramm:$/## Probleme mit der Firewall oder dem Antivirenprogramm: {#SoftwareIssues}/' "$I18N/de/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/^Geräteeinstellungen:$/## Geräteeinstellungen: {#DeviceSettings}/' "$I18N/de/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/^Probleme mit dem Server:$/## Probleme mit dem Server: {#ServerIssues}/' "$I18N/de/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
# Remove misplaced {#SoftwareIssues} from Server section's test heading
sed -i '' 's/## So können Sie testen, ob hier die Ursache liegt: {#SoftwareIssues}/## So können Sie testen, ob hier die Ursache liegt:/' "$I18N/de/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"

# Italian (same content as German due to GKMS error)
sed -i '' 's/^Probleme mit der Firewall oder dem Antivirenprogramm:$/## Probleme mit der Firewall oder dem Antivirenprogramm: {#SoftwareIssues}/' "$I18N/it/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/^Geräteeinstellungen:$/## Geräteeinstellungen: {#DeviceSettings}/' "$I18N/it/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/^Probleme mit dem Server:$/## Probleme mit dem Server: {#ServerIssues}/' "$I18N/it/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/## So können Sie testen, ob hier die Ursache liegt: {#SoftwareIssues}/## So können Sie testen, ob hier die Ursache liegt:/' "$I18N/it/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"

# Japanese
sed -i '' 's/^ファイアウォールやウイルス対策ソフトウェアに関する問題:$/## ファイアウォールやウイルス対策ソフトウェアに関する問題: {#SoftwareIssues}/' "$I18N/ja/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/^デバイス設定:$/## デバイス設定: {#DeviceSettings}/' "$I18N/ja/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/^サーバーに関する問題:$/## サーバーに関する問題: {#ServerIssues}/' "$I18N/ja/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/## テスト方法: {#SoftwareIssues}/## テスト方法:/' "$I18N/ja/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"

# zh-Hant
sed -i '' 's/^網路防火牆問題：$/## 網路防火牆問題： {#FirewallIssues}/' "$I18N/zh-Hant/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/^防火牆或防毒軟體問題：$/## 防火牆或防毒軟體問題： {#SoftwareIssues}/' "$I18N/zh-Hant/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/^伺服器問題：$/## 伺服器問題： {#ServerIssues}/' "$I18N/zh-Hant/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/{#devicesettings}/{#DeviceSettings}/' "$I18N/zh-Hant/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/## 測試方法： {#SoftwareIssues}/## 測試方法：/' "$I18N/zh-Hant/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"

# French: ServerIssues section
sed -i '' 's/^Problèmes liés au serveur :$/## Problèmes liés au serveur : {#ServerIssues}/' "$I18N/fr/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/#serverissues)/#ServerIssues)/g' "$I18N/fr/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"

# Arabic: all 5 section anchors + typos
sed -i '' 's/^#### مشاكل الاتصال بالإنترنت:$/#### مشاكل الاتصال بالإنترنت: {#Internetissues}/' "$I18N/ar/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/^#### مشاكل جدار حماية الشبكة:$/#### مشاكل جدار حماية الشبكة: {#FirewallIssues}/' "$I18N/ar/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/^#### مشاكل جدار الحماية أو برامج مكافحة الفيروسات:$/#### مشاكل جدار الحماية أو برامج مكافحة الفيروسات: {#SoftwareIssues}/' "$I18N/ar/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/^#### إعدادات الجهاز:$/#### إعدادات الجهاز: {#DeviceSettings}/' "$I18N/ar/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/^#### مشاكل الخادم:$/#### مشاكل الخادم: {#ServerIssues}/' "$I18N/ar/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/#Internetissues1)/#Internetissues)/g' "$I18N/ar/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/#softwareissuesss)/#SoftwareIssues)/g' "$I18N/ar/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"
sed -i '' 's/{#serivcemanager}/{#servicemanager}/' "$I18N/ar/docusaurus-plugin-content-docs/current/about/terminology.md"
sed -i '' 's/#serivcemanager)/#servicemanager)/g' "$I18N/ar/docusaurus-plugin-content-docs/current/about/terminology.md"

# Urdu: RTL marks in anchor refs
python3 -c "
p = '$I18N/ur/docusaurus-plugin-content-docs/current/about/terminology.md'
t = open(p, encoding='utf-8').read()
t = t.replace('#servicemanager\u202b)', '#servicemanager)')
t = t.replace('#accesskey\u202b)', '#accesskey)')
open(p, 'w', encoding='utf-8').write(t)
"

# Farsi: lowercase anchor
sed -i '' 's/{#serverissues}/{#ServerIssues}/' "$I18N/fa/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"

# zh-Hans: lowercase anchor
sed -i '' 's/{#internetissues}/{#Internetissues}/' "$I18N/zh-Hans/docusaurus-plugin-content-docs/current/client/troubleshooting/connection-issues.md"

echo "Done: manual anchor fixes applied"

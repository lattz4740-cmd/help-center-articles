---
title: 為何我無法在 Windows 裝置上安裝 Outline Manager？
sidebar_label: 為何我無法在 Windows 裝置上安裝 Outline Manager？
---

你可能看到以下錯誤訊息：「很抱歉，系統無法正確安裝 Outline，請再安裝一次。如果仍無法解決問題，請[提交意見](https://support.getoutline.org/s/contactsupport?)。」

透過 Windows 裝置使用 Outline 時，有時可能會遇到未預期的錯誤。在大多數情況下，你需要刪除 Outline TAP 介面卡 (驅動程式)，並重新安裝 Outline。

解決問題的具體步驟可能會因你的 Windows 作業系統版本而異，以下提供解除安裝 TAP 介面卡和 Outline Manager，再重新安裝 Outline Manager 的一般步驟。

1. 解除安裝 Outline Manager 的 TAP 介面卡
   1. 前往「裝置管理工具」和「網絡介面卡」
   2. 找出 TAP-Windows Adapter V9 檔案，或與 Outline 相關聯的 TAP 介面卡
   3. 解除安裝或刪除此介面卡。請注意，此操作可能會影響你已安裝的其他 VPN 應用程式。
2. 解除安裝 Outline Manager
   1. 前往「程式和功能」和「解除安裝程式」
   2. 找出 Outline Manager 應用程式，然後解除安裝 Outline Manager
   3. [下載最新版 Outline Manager](https://getoutline.org/get-started/#step-1)，然後在 Windows 裝置上重新安裝此應用程式。重新安裝 Outline 時，亦會自動安裝新的 TAP 介面卡。

如果你仍然遇到問題，請[聯絡支援團隊](https://support.getoutline.org/s/contactsupport?)。

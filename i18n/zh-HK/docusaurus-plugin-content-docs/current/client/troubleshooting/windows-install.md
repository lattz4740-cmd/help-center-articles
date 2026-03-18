---
title: 為什麼我無法在 Windows 裝置上安裝 Outline 用戶端？
sidebar_label: 為什麼我無法在 Windows 裝置上安裝 Outline 用戶端？
---

你可能看到以下錯誤訊息：「很抱歉，系統無法正確安裝 Outline，請再安裝一次。如果仍無法解決問題，請[提交意見](/about/feedback)。」

透過 Windows 裝置使用 Outline 時，有時可能會遇到預料之外的錯誤。在大多數情況下，你需要刪除 Outline TAP 介面卡 (驅動程式)，並重新安裝 Outline。

解決問題的具體步驟可能會因你的 Windows 作業系統版本而異，以下提供解除安裝 TAP 介面卡和 Outline，再重新安裝 Outline 的一般步驟。

1. 解除安裝 Outline 用戶端的 TAP 介面卡
   - 前往「裝置管理工具」和「網絡介面卡」
   - 找出 **TAP-Windows Adapter V9** 檔案，或與 Outline 相關聯的 TAP 介面卡
   - 解除安裝或刪除此介面卡。請注意，此操作可能會影響你已安裝的其他 VPN 應用程式。
2. 解除安裝 Outline 用戶端
   - 前往「程式和功能」和「解除安裝程式」
   - 找出 Outline 用戶端應用程式，然後解除安裝 Outline 用戶端
   - [下載最新版本 Outline 用戶端](https://getoutline.org/get-started/#step-3)，然後在 Windows 裝置上重新安裝此應用程式。重新安裝 Outline 時，亦會自動安裝新的 TAP 介面卡。

如果你仍然遇到問題，請[聯絡支援團隊](/about/feedback)。

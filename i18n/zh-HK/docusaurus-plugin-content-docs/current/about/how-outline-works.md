---
title: Outline 的運作原理
sidebar_label: Outline 的運作原理
---

**伺服器安裝**

 雖然 Outline 的安裝程序看起來很簡單，但其實背後需要很多複雜的步驟，才能順利安裝伺服器。安裝 Outline 後，安裝指令碼將會執行以下步驟：

- 使用 Docker 擷取及匯入 Shadowbox 圖像穩定版本。圖像由 [Quay.io](https://quay.io/) 寄存於 [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags)。此圖像包含 Outline 伺服器和 Management API。Outline Server Management 應用程式稍後會使用此 API 建立及移除存取金鑰、選擇報告/不報告匿名數據等。
- 安裝及設定 [Watchtower](https://github.com/v2tec/watchtower)，以便每小時檢查圖像更新，並確認每個 Outline 伺服器隨時具備最新的功能和安全改善措施。
- 在私密隨機路徑的隨機通訊埠上執行用於存取 Management API 的網絡伺服器。
- 建立[自簽 SSL 憑證](https://zh.wikipedia.org/zh-hk/Self-signed_certificate)，即使沒有網域名稱，亦能使用 TLS 為 Outline 伺服器加密。系統亦會產生此憑證的專屬指紋，並儲存在 Outline Manager 應用程式中，以用於防範中間人 (MITM) 攻擊。

Outline 安裝完成後不需要再進行任何設定。

**伺服器安全性**

 Outline 是開放原始碼軟件，因此所有人都可查看其程式碼，並在發現安全漏洞時作出改良。我們將程式碼寄存在 [GitHub](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline)。

 此外，所有已安裝的 Outline 伺服器都會在新版本發佈時自動更新，確保所有 Outline 伺服器不會執行舊版本軟件。

 為管理伺服器上的存取金鑰，Outline Manager 應用程式會和 Outline 伺服器上的 Management Service 互動。Management Service 會在隨機通訊埠和私密專屬路徑上執行。由於 Management Service 只會在已指定適當私密路徑的情況下回應查詢，因此可防止探測。最後，系統會使用[自簽 SSL 憑證](https://zh.wikipedia.org/zh-hk/Self-signed_certificate)為所有 Management Service 通訊加密。

 Outline 伺服器不會儲存任何記錄，所以即使被入侵，亦無需擔心使用者資料外洩。按[這裡](https://support.getoutline.org/s/article/Security-and-privacy)瞭解詳情。2018 年，Outline 通過 [Radically Open Security](https://radicallyopensecurity.com/) 和 [Cure53](https://cure53.de/) 的審核。按[這裡](https://support.getoutline.org/s/article/Security-and-privacy)查看報告。

**處理 UDP 流量**

 Outline 可作為全系統 VPN 運作，因此所有 UDP 流量都能透過 Outline 伺服器傳輸。

**DNS 流量**

Outline 會透過 Outline 伺服器執行所有 DNS 查詢，並使用保護其他網絡活動的加密方式來保護這些查詢。你的 DNS 查詢會透過 Outline 伺服器傳輸至 Dyn Internet Guide、OpenDNS、Cloudflare DNS 或 Quad9 DNS。Outline 絕不會記錄你的 DNS 查詢。

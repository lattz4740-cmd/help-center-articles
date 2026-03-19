---
title: Outline 的運作原理
sidebar_label: Outline 的運作原理
---

### 伺服器安裝

雖然 Outline 的安裝程序看起來很簡單，但其實背後需要很多複雜的步驟，才能順利安裝伺服器。

安裝 Outline 之後，安裝指令碼將會執行以下步驟：

- 使用 Docker 擷取及匯入 Shadowbox 映像檔穩定版，這個映像檔將由 Quay.io 代管於 https://quay.io/repository/outline/shadowbox?tab=tags。此映像檔包含 Outline 伺服器和 Management API；Outline Server Management 應用程式稍後會使用這個 API 來建立及移除存取金鑰、選擇回報/不回報匿名指標等。
- 安裝及設定 Watchtower，以便每小時檢查映像檔更新，並確認每台 Outline 伺服器隨時具備最新的功能和安全性改良設定。
- 用於存取 Management API 的網路伺服器開始在私密隨機路徑的隨機通訊埠上執行。
- 建立自行簽署安全資料傳輸層 (SSL) 憑證，這樣一來，即使沒有網域名稱，也能使用傳輸層安全標準 (TLS) 為 Outline 伺服器加密。系統也會產生這個憑證的專屬指紋，並儲存在 Outline Manager 應用程式中，以用於防範中間人 (MITM) 攻擊。

Outline 安裝完成後不需要再進行任何設定。

### 伺服器安全性

Outline 是開放原始碼軟體，代表任何人都可以查看程式碼，並在發現任何漏洞時予以改善。我們將程式碼交由

代管。

此外，只要有新版發布，所有已安裝的 Outline 伺服器都會自動更新，這樣就不會有任何 Outline 伺服器執行舊版軟體。

為管理伺服器上的存取金鑰，Outline Manager 應用程式會與 Outline 伺服器上的 Management Service 互動；Management Service 會在隨機通訊埠和私密專屬路徑上執行。另外，由於 Management Service 只會在已指定適當私密路徑的情況下回應查詢，因此可以防止探測。最後，系統會使用

為所有 Management Service 通訊加密。

Outline 伺服器不會儲存任何記錄，所以即使遭到入侵，也不必擔心使用者資料洩漏。

。

Outline 已於 2018 年接受

和

的稽核。請按

參閱報告。

### 處理 UDP 流量

Outline 可做為全系統 VPN 運作，因此所有 UDP 流量都能透過 Outline 伺服器傳輸。

### DNS 流量

Outline 會透過 Outline 伺服器執行所有 DNS 查詢作業，並使用保護其他網路活動的加密方式來保護這些查詢作業。您的 DNS 查詢會透過 Outline 伺服器傳輸至 Dyn Internet Guide 或 OpenDNS。

Outline 絕對不會記錄您的 DNS 查詢作業。

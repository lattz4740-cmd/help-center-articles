---
title: 為什麼我無法連接 Outline 服務？
sidebar_label: 為什麼我無法連接 Outline 服務？
---

以下是幾種可能無法連接 Outline 服務的原因：

- **裝置**/client/troubleshooting/connection-issues#One [**未連接互聯網**](#Internetissues)[#Internetissues](#Internetissues)**。**有時裝置會遇到網絡連線中斷問題，需要一些時間才能更新網絡圖示。裝置亦有可能已連接到區域網絡，惟區域網絡的互聯網停止運作。
- **你的**/client/troubleshooting/connection-issues#Two [**網絡防火牆禁止存取**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[#FirewallIssues](#FirewallIssues) Outline 伺服器。**在使用公共網絡 (例如學校、公司或免費的無線網絡) 的時候很常發生這種情況。
- **裝置上的**/client/troubleshooting/connection-issues#Three [**防火牆或防毒軟件**](#SoftwareIssues)[#SoftwareIssues](#SoftwareIssues)**封鎖了 Outline 伺服器。**
- **你的**[**手機裝置設定**](#DeviceSettings)**可能需要調整。**
- **服務管理員可能已**[**刪除伺服器，或 ISP 可能已封鎖你的要求**](#ServerIssues)。

## 互聯網連線問題： {#Internetissues}

### 測試方法：

關閉 Outline，然後查看互聯網連線是否恢復。

- 如果已恢復連線，請進一步查看以下解決疑難做法。
- 如果連線並未恢復，請先稍等幾分鐘，再查看連線設定是否自行更新。

### 修正事項：

讓裝置恢復連線：

1. 檢查其他裝置是否能連接同一個網絡。如果其他裝置亦無法連線，表示此網絡可能已停止運作。你需要等待網絡恢復運作，或主動解決相關問題。
2. 如果其他裝置可連接同一個網絡，你可嘗試按照以下做法讓有問題的裝置恢復連線：
   1. 將裝置切換至飛行模式 (適用於流動裝置)
   2. 重新啟動裝置
   3. 關閉裝置，等待 2 分鐘後再重新開啟裝置

## 網絡防火牆問題： {#FirewallIssues}

### 測試方法：

1. 與目前的 Wi-Fi 或有線網絡解除連線。
2. 連線至其他網絡，例如流動網絡
3. 嘗試重新連線至 Outline 伺服器

如果你可透過其他網絡成功連線，代表此問題需要由你解決。

### 修正事項：

聯絡服務管理員，要求對方讓你存取 Outline 伺服器；你亦可改為繼續使用連線正常的網絡。

## 防火牆或防毒軟件問題： {#SoftwareIssues}
### 測試方法：
 嘗試透過其他裝置連線至 Outline。

注意：提提你，你需要有存取金鑰和 Outline 應用程式才能在其他裝置上使用 Outline。

### 修正事項：
檢查防火牆或防毒軟件設定，確保這些設定允許 VPN 和 Outline 的流量通過。

## 裝置設定： {#DeviceSettings}

## 檢查事項： {#ServerIssues}
Android 裝置：

1. 開啟「設定」應用程式。
2. 尋找裝置上的 **VPN 設定** (VPN 設定中會顯示手機上目前擁有存取權的所有 VPN 應用程式。)
3. 如果你在 VPN 設定中沒有看到 Outline，請解除安裝 Outline 並重新安裝。安裝完成後，裝置應會自動向 Outline 授予存取權。

請確保你沒有在 Android 裝置上安裝任何重疊式畫面應用程式，因為此類應用程式可能會將 Outline 權限視窗傳送至背景導致其沒有在前景顯示。

 在 Android 裝置上前往「設定」> [應用程式] > [特殊應用程式存取權]，然後輕按 [在其他應用程式上面顯示]。如有應用程式可執行此操作，你可移除其權限。

 iOS 裝置：閱讀[此說明中心文章](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web)。

### 伺服器問題：

### 測試方法：
如果你可存取多個伺服器，請嘗試連線至其他伺服器。

### 修正事項：

聯絡服務管理員，瞭解該伺服器是否已刪除。如果是，請向服務管理員索取其他伺服器的[存取金鑰](/about/terminology)。

如果你設定伺服器，請嘗試透過 Outline Manager 或其他方式 (例如 [SSH](https://zh.wikipedia.org/zh-hk/Secure_Shell)) 連線至該伺服器。如果問題仍未解決，你可嘗試檢查雲端服務供應商控制台 (如有)，看看伺服器是否仍然連線。

---
title: 為何我無法連上 Outline 服務？
sidebar_label: 為何我無法連上 Outline 服務？
---

以下是無法連上 Outline 服務的幾種可能原因：

- **裝置**[**未連上網際網路**](https://docs.google.com/document/d/1YDlrtMErHZ2aoPehRlglSsSnbGjTfUWZ/edit?resourcekey=0-1uh7Y6iU_CCPDj22n3NGTQ#heading=h.2et92p0)**。**有時裝置會遇到網路連線中斷的問題，需要一些時間才能更新網路圖示。此外，裝置也可能連上已停止運作的區域網路。
- [**網路防火牆已封鎖**](https://docs.google.com/document/d/1YDlrtMErHZ2aoPehRlglSsSnbGjTfUWZ/edit?resourcekey=0-1uh7Y6iU_CCPDj22n3NGTQ#heading=h.4d34og8)**Outline 伺服器。**這很常發生在使用公用網路 (比如學校、公司或免費的無線網路) 的時候。
- **裝置上的**[**防火牆或防毒軟體**](https://docs.google.com/document/d/1YDlrtMErHZ2aoPehRlglSsSnbGjTfUWZ/edit?resourcekey=0-1uh7Y6iU_CCPDj22n3NGTQ#heading=h.26in1rg)**封鎖了 Outline 伺服器。**
- [**手機裝置的設定**](https://docs.google.com/document/d/1YDlrtMErHZ2aoPehRlglSsSnbGjTfUWZ/edit?resourcekey=0-1uh7Y6iU_CCPDj22n3NGTQ#bookmark=id.1ksv4uv)**可能需要調整。**

**服務管理員可能已**[**刪除伺服器，或是網際網路服務供應商 (ISP) 可能已封鎖你的要求**](https://docs.google.com/document/d/1YDlrtMErHZ2aoPehRlglSsSnbGjTfUWZ/edit?resourcekey=0-1uh7Y6iU_CCPDj22n3NGTQ#bookmark=id.z337ya)**。**

網際網路連線問題：

## 測試方法： {#Internetissues}
關閉 Outline，然後查看網際網路連線是否恢復。

- 如果連線已經恢復，請進一步查看下列疑難排解做法。
- 如果連線並未恢復，請先稍等幾分鐘，再查看連線設定是否自行更新。

#### 修正事項：

## 讓裝置恢復連線：

1. 檢查其他裝置是否能連上同一個網路。如果其他裝置也無法連線，表示這個網路可能已停止運作，你必須等待網路恢復連線，或主動排解相關問題。
2. 如果其他裝置可連上同一個網路，你可以嘗試按照下列做法讓有問題的裝置恢復連線：
   1. 將裝置切換到飛航模式 (適用於行動裝置)
   2. 重新啟動裝置
   3. 關閉裝置，等待 2 分鐘後再重新開啟裝置

網路防火牆問題：

## 測試方法：

1. 中斷目前的 Wi-Fi 或有線網路。
2. 連線至其他網路，例如行動數據網路。
3. 嘗試重新連線至 Outline 伺服器。

如果使用其他網路可以成功連線，表示問題出在你這裡

修正事項：

與服務管理員聯絡，請對方讓你存取 Outline 伺服器；或者你也可以改為繼續使用連線正常的網路。

防火牆或防毒軟體問題：

## 測試方法： {#FirewallIssues}
嘗試透過其他裝置連線至 Outline。

注意：提醒你，你需要有存取金鑰和 Outline 應用程式才能在其他裝置上使用 Outline。

## 修正事項：

檢查防火牆或防毒軟體設定，確保這些設定允許 VPN 和 Outline 的流量通過。

**裝置設定：**

## 檢查事項： {#devicesettings}

Android 裝置：

1. 開啟「設定」應用程式。
2. 找出裝置上的 **VPN 設定**，其中會顯示手機上目前已獲得存取權的所有 VPN 應用程式。
3. 如果 VPN 設定中未顯示 Outline，請先解除安裝 Outline 再重新安裝。安裝完成後，裝置會自動將存取權授予 Outline。

請確認你的 Android 裝置上未安裝任何會重疊顯示的應用程式，因為這可能會導致 Outline 權限視窗移至背景，無法顯示在前景。

在 Android 裝置上依序前往「設定」>「應用程式」>「特殊應用程式存取權」，然後輕觸「顯示在其他應用程式上層」。你可以針對能執行這項操作的應用程式移除權限。

iOS 裝置：閱讀[這篇支援文章](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web)。

伺服器問題：

## 測試方法： {#SoftwareIssues}
如果你可以存取多部伺服器，請嘗試連線至其他伺服器。

## 修正事項：

與服務管理員聯絡，瞭解該伺服器是否已刪除。如果是的話，請向服務管理員索取其他伺服器的[存取金鑰](https://docs.google.com/document/d/1Mp-hH49D0bn02LO-MkgVVh95O7FrG-6XXCjX49WA3nE/edit#heading=h.2dn8xnck0993)。

如果你是自行設定伺服器，請嘗試透過 Outline Manager 或其他方式 (例如 [SSH](https://en.wikipedia.org/wiki/Secure_Shell)) 連線至該伺服器。如果問題仍未解決，你可以試著檢查雲端服務供應商主控台 (如果有的話)，看看伺服器是否仍在線上。

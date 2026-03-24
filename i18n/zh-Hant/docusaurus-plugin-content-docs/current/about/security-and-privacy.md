---
title: 在使用 Outline 時確保安全與隱私
sidebar_label: 在使用 Outline 時確保安全與隱私
---

在使用 Outline 時確保安全與隱私

## Outline 如何保護你的線上通訊安全

網路流量在區域或國內網路中傳輸時，最容易受到監控。

Outline 會確保網路流量從國內網路傳送到 Outline 伺服器時全程加密，保護您的通訊隱私。Outline 加密流量後，網路窺探者就無法檢視你造訪的網站或正在傳輸的資訊。

此外，Outline 能協助你使用在當地原本無法存取的安全端對端通訊工具。

## 加密標準

Outline 採用 AEAD 256 位元的 Chacha2020 IETF Poly 1305 編碼器，加密裝置與 Outline 伺服器之間的通訊。AEAD 編碼器在現代硬體上的效能一流，能確保資料的機密性、完整性和真實性。

## 安全性稽核

Outline 於 2018 年接受 Radically Open Security 與 Cure53 稽核，這兩家獨立數位安全機構皆依據最新安全性標準審查軟體。Radically Open Security 於 2022 年再次進行稽核，Cure53 則在 2024 年完成對 Outline SDK 的稽核。歡迎參閱下列報告：

- [Radically Open Security 滲透測試報告 (2018 年 3 月)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53 的 Jigsaw Outline 滲透測試與稽核報告 (2018 年 12 月)](https://getoutline.org/reports/cure53-report.pdf)
- [Radically Open Security 滲透測試報告 (2022 年 12 月)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Cure53 的 Jigsaw Outline VPN SDK 滲透測試報告 (2024 年 1 月)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## 匿名指標和記錄

Outline 會追蹤每組存取金鑰使用的頻寬，並記錄為「已傳輸的位元組數」。伺服器管理員可以根據這些資訊，視需要向雲端伺服器供應商調整頻寬租用量，但他們無法看到實際透過 Outline 伺服器傳送的資訊內容。

進一步瞭解 Outline 採取的[資料和資訊收集做法](/about/data-collection)。

---

## 安全性和隱私權常見問題

## Outline 能讓我匿名上網嗎？

不行。Outline 不是匿名工具，但會防止潛在網路窺探者侵犯你的隱私。

Outline 不會讓您在造訪的網站上完全匿名，這些網站還是能在您登入時，或透過瀏覽器指紋等技術來識別您的身分。針對行動應用程式，現代智慧型手機多半都有 API，這些 API 能讓已安裝的應用程式透過內嵌的 GPS 擷取您的所在位置，而不須使用您的 Proxy。

通常 VPN 都有保護功能，而且特別能防止網際網路監視，不過在網路上進行任何活動還是有其風險。即便使用 VPN，如果網際網路服務供應商 (ISP) 已經知道你的身分，並能觀察你的網路流量，他們或許還是能判斷出 Outline 伺服器的 IP 位址。這些資訊可用來封鎖對 Outline 伺服器的存取，或瞭解你的使用模式，例如你通常上線的時間，甚至可能推測你的大致位置。

## 別人能看出我在使用 Outline 嗎？

有可能。你存取的平台和服務很可能辨識出連線來自雲端伺服器，有時可以推測出在使用 VPN，但無法看到實際的網路流量內容。

## Outline 能完全防範所有潛在網路威脅嗎？

不能，沒有任何單一工具可以做到。Outline 提供開放網際網路的存取管道，並藉由加密流量增強隱私防護，但我們仍建議採取其他預防措施，防範惡意軟體、網路釣魚等其他類型的攻擊。

為了強化網路防禦，請考慮與貴機構的網路安全專家合作，或尋求 [Security Planner](https://securityplanner.org/) 網站頂尖安全專家的個人化指導。該網站會提供清晰說明，協助你根據需求選擇合適的網路安全工具。

你也可以參考 [Jigsaw](https://jigsaw.google.com/) 的其他網路安全產品，例如 [Intra](https://getintra.org/)、[Project Shield](https://g.co/shield) 和 [密碼防護警示](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?)。

## 使用 VPN 是否合法？

在運行 Outline 或使用該應用程式之前，請查閱所在地的法律及法規，以及所選雲端服務供應商的服務條款。

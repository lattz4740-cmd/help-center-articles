---
title: 使用 Outline 時的安全和私隱
sidebar_label: 使用 Outline 時的安全和私隱
---

使用 Outline 時的安全和私隱

## Outline 如何保護你的網上通訊安全

互聯網流量透過區域或全國網絡傳送時，最容易出現與監控相關的安全漏洞。

Outline 能在互聯網流量透過你的全國網絡傳送時全程加密，直到流量抵達 Outline 伺服器，讓你的通訊私隱安全有保障。利用 Outline 加密流量，網絡窺探者就無法查看你瀏覽過的網站或傳送的資料。

此外，Outline 亦可協助你重新存取原本可能無法從你國家/地區使用的安全端對端通訊工具。

## 加密標準

Outline 採用 AEAD 256 位元的 Chacha2020 IETF Poly 1305 編碼器來為你的裝置和 Outline 伺服器之間的通訊加密。AEAD 編碼器在現代硬件上的效能一流，可確保資料的機密性、完整性和真確性。

## 安全審核

2018 年，Outline 通過 Radically Open Security 和 Cure53 的審核，這兩間獨立數碼安全機構根據最新安全標準對軟件進行嚴格審核。此外，Radically Open Security 亦在 2022 年完成額外審核，而 Cure53 則在 2024 年完成對 Outline SDK 的審核。你可參閱以下報告：

- [Radically Open Security 滲透測試報告 (2018 年 3 月)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53 的 Jigsaw Outline 滲透測試與審核報告 (2018 年 12 月)](https://getoutline.org/reports/cure53-report.pdf)
- [Radically Open Security 滲透測試報告 (2022 年 12 月)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Cure53 Jigsaw Outline VPN SDK 滲透測試報告 (2024 年 1 月)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## 匿名數據和記錄

針對每組存取金鑰，Outline 會追蹤使用的頻寬，並將其視為「已傳輸的字節」。此資料允許伺服器管理員按需要向雲端伺服器供應商調整頻寬租用量，但伺服器管理員無法看到實際上透過 Outline 伺服器傳送的資料。

進一步瞭解 Outline 的[資料和資訊收集方式](https://getoutline.org/policies/data-collection)。

---

## 安全和私隱常見問題

## Outline 能讓我在網上匿名嗎？

Outline 不是匿名工具，因此無法讓你匿名。但請放心，Outline 會保護你的私隱安全，令潛在網絡窺探者無法看到你的資料。

Outline 不會讓你在瀏覽的網站上完全匿名，這些網站仍可在你登入時，或透過瀏覽器指紋等技術來識別你的身分。針對流動應用程式，現代智能手機大多數都有 API，這些 API 可讓已安裝的應用程式透過內嵌的 GPS 擷取你的位置，無需使用 Proxy。

VPN 通常都有保護功能，且特別可防止互聯網監控，不過在網絡上進行任何活動還是有風險。即使使用 VPN 連線，只要 ISP 已識別你的身分，且可觀察網絡流量，就有辦法推斷出你 Outline 伺服器的 IP 位址。此資料可用來封鎖對 Outline 伺服器的存取，或掌握使用者的使用模式 (例如你通常什麼時候上網、你的概略位置等)。

## 別人會知道我正在使用 Outline 嗎？

有可能。其他人非常有可能從你存取的平台和服務中得知你的連線是來自雲端伺服器。有時候，這些人還有可能推斷你正在使用 VPN，但無法查看你互聯網流量的實際內容。

## Outline 可保護我不受所有潛在的網絡威脅嗎？

不能。沒有任何工具可保證你不受所有潛在的網絡威脅。Outline 的功用是提供開放互聯網的存取渠道，並透過加密流量加強保障你的私隱；建議你採取額外的安全防護措施，避免惡意軟件和仿冒詐騙等其他類型攻擊。

請考慮與機構的網絡安全專家合作，進一步提升網上防禦能力。或者，你可前往 [Security Planner](https://securityplanner.org/) 取得相關協助；此網站會就你的考慮提供清晰指示以助你尋找合適的網絡安全工具，還有頂尖的安全專家為你提供個人化指引。

此外，你亦可參考 [Jigsaw](https://jigsaw.google.com/) 的其他網絡安全產品 (例如 [Intra](https://getintra.org/)、[Project Shield](https://g.co/shield) 和「[密碼防護警示](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?)」)。

## 使用 VPN 是否合法？

開始運作 Outline 或使用應用程式前，請先詳閱你當地的法律和條例，以及你預計採用的雲端服務供應商服務條款。

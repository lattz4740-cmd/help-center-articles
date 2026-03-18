---
title: 防火牆錯誤
sidebar_label: 防火牆錯誤
---

您可能會遇到以下三種類型的防火牆問題：

## 遭到網路防火牆封鎖。

連線到已開啟防火牆的網路時 (例如學校或辦公地點的網路)，請勿嘗試安裝 Outline，建議等連線至其他網路後，再行安裝。

 如果這個方式行不通，請聯絡您的網路管理員，要求對方允許已開啟防火牆的網路與您的 Outline 伺服器連線。您必須備妥 Outline 伺服器的 IP 位址和執行 Outline 的連接埠資料；安裝指令碼的最後部分提供相關資訊，歡迎參閱。

**遭到裝置防火牆封鎖**。

如果您裝置上的軟體會封鎖非標準連接埠/無法辨識軟體 (例如 CheckPoint 的 ZoneAlarm) 的連出連線，請參閱您的裝置或軟體說明文件，瞭解如何為 Outline 建立例外狀況。

## 遭到伺服器防火牆封鎖。

您選用的雲端服務供應商可能會要求您手動建立伺服器防火牆例外狀況，以開啟要執行 Outline 的連接埠。執行安裝指令碼後，系統應會提供兩個隨機選取的連接埠，讓您在伺服器中執行 Outline。開啟這兩個連接埠應已可滿足使用需求。

 如要為伺服器防火牆建立例外狀況，建議您參閱「ufw」和「iptables」的說明文件。

- UFW：[https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables：[https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

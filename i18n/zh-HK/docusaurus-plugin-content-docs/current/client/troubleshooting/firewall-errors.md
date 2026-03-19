---
title: 防火牆錯誤
sidebar_label: 防火牆錯誤
---

你可能會遇到以下三種類型的防火牆問題：

## 被網絡防火牆封鎖。

如果你正使用連線到已開啟防火牆的網路 (例如學校或辦公地點的網路) 安裝 Outline，建議你轉用其他網絡後再安裝。

如果此方式無效，請聯絡網絡管理員，要求對方允許已開啟防火牆的網絡與你的 Outline 伺服器連線。你將需要知道 Outline 伺服器的 IP 位址和執行 Outline 的連接埠 (在安裝指令碼的最後部分顯示)。

## 被裝置防火牆封鎖

。

如果你裝置上的軟件會封鎖非標準連接埠/無法辨識軟件的對外連線 (例如 CheckPoint 的 ZoneAlarm)，請參閱你的裝置或軟件說明文件，瞭解如何為 Outline 建立例外情況。

## 被伺服器防火牆封鎖。

你選用的雲端服務供應商可能會要求你手動建立伺服器防火牆例外情況，以開啟要執行 Outline 的連接埠。執行安裝指令碼後，系統應會提供兩個隨機選取的連接埠，讓你在伺服器中執行 Outline。開啟這兩個連接埠應已能滿足使用需求。

 如要為伺服器防火牆建立例外情況，建議你參閱「ufw」和「iptables」的說明文件。

- UFW：[https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables：[https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

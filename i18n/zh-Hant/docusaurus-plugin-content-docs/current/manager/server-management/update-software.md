---
title: 如何更新 Outline 伺服器軟體？
sidebar_label: 如何更新 Outline 伺服器軟體？
---

Outline 伺服器會自動更新以採用最新的安全改進措施，確保你使用的是最先進的 Outline 技術。自動更新程序採用了 [Watchtower](https://github.com/containrrr/watchtower) 開放原始碼程式庫。這個程式庫會定期檢查並更新含有 Outline 軟體的 Docker 映像檔。

此外，當你使用 Outline Manager 安裝 Outline，系統就會設定 Cron 工作，藉此自動使用 Ubuntu 的 [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) 升級伺服器上的軟體，並在必要時重新啟動。請注意，由於系統假設主機除了執行 Outline 外，也會用於其他用途，因此為保留現有設定，在進階模式中不會執行自動更新。

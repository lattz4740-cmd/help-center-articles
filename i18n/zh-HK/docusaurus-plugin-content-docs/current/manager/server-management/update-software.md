---
title: 如何更新 Outline 伺服器軟件？
sidebar_label: 如何更新 Outline 伺服器軟件？
---

Outline 伺服器會自動更新以採用最新的安全改善措施，確保你使用的是最先進的 Outline 技術。自動更新程序採用了 [Watchtower](https://github.com/containrrr/watchtower) 開放原始碼程式庫。這個程式庫會定期檢查並更新包含 Outline 軟件的 Docker 映像。

此外，當你使用 Outline Manager 安裝 Outline，系統就會設定 Cron 工作，藉此自動使用 Ubuntu 的 [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) 升級伺服器上的軟件，並在必要時重新啟動。請注意，由於系統假設主機除了執行 Outline 外，亦會用於其他用途，因此為保留現有設定，在「進階模式」中不會執行自動更新。

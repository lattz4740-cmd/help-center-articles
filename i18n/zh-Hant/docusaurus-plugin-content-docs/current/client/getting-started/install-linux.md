---
title: 在 Linux 上安裝 Outline 用戶端
sidebar_label: 在 Linux 上安裝 Outline 用戶端
---

自 Outline 用戶端 1.15 版起，適用於 Linux 作業系統的所有後續版本都會以 Debian 套件形式發布。如要進一步瞭解我們支援的作業系統，請參閱[最低系統需求](/client/getting-started/system-requirements)。

## 為 Debian 型 Linux 發行版安裝 Outline 用戶端 (建議)

請執行下列指令：

1. 安裝 Outline 的存放區金鑰並新增存放區。
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. 更新 APT 套件清單，並安裝最新版 Outline 用戶端。
   ```
   sudo apt update
   sudo apt install outline-client
   ```

如要檢查或安裝後續更新，請再次執行步驟 2 的指令。請注意，自 1.15 版起，Linux 版 Outline 用戶端已停用應用程式內自動更新功能。

如要解除安裝 Outline 用戶端，請執行以下指令：

```
sudo apt purge outline-client
```

## 替代方案

1. 前往 [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)，下載最新版 Outline 用戶端 Debian 套件
2. 在指令列執行以下指令，即可安裝套件
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. 自 1.15 版起，Linux 版 Outline 用戶端已停用應用程式內自動更新功能，因此請手動檢查更新。
4. 如要解除安裝 Outline 用戶端，請在指令列執行以下指令：
   ```
   sudo apt purge outline-client
   ```

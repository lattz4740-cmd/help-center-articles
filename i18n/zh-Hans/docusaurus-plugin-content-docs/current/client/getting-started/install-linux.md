---
title: 在 Linux 上安装 Outline 客户端
sidebar_label: 在 Linux 上安装 Outline 客户端
---

从 Outline 客户端 1.15 版开始，所有适用于 Linux 操作系统的后续版本都将以 Debian 软件包的形式发布。如需详细了解我们支持哪些操作系统，请参阅我们的[最低系统要求](/client/getting-started/system-requirements)。

## 为基于 Debian 的 Linux 发行版安装 Outline 客户端（推荐）

运行以下命令：

1. 安装 Outline 的仓库密钥并添加仓库。
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. 更新 apt 软件包列表并安装最新版 Outline 客户端。

```
sudo apt update
sudo apt install outline-client
```

如需检查或安装后续更新，请再次运行第 2 步中的命令。请注意，从 1.15 版开始，Linux 上的 Outline 客户端已停用应用内自动更新。

如需卸载 Outline 客户端，请运行以下命令：

```
sudo apt purge outline-client
```

## 备用方法

1. 前往 [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) 下载最新版 Outline 客户端 Debian 软件包
2. 在命令行中运行以下命令，以安装软件包

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. 从 1.15 版开始，Linux 上的 Outline 客户端已停用应用内自动更新，因此请手动检查更新。

4. 在命令行中运行以下命令，以卸载 Outline 客户端：

```
sudo apt purge outline-client
```

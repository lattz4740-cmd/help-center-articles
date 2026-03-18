---
title: Outline 的运作原理
sidebar_label: Outline 的运作原理
---

### 服务器安装

安装 Outline 看似简单，但实际上，在服务器的安装过程中，屏幕背后隐藏着许多复杂的步骤。

每次安装 Outline 时都会运行一个安装脚本，并执行以下步骤：

- 使用 Docker 检索和导入稳定版 Shadowbox 映像。该映像托管在 [Quay.io](https://support.getoutline.org/s/article/how-outline-works?language=zh_CN)，网址为 [https://quay.io/repository/outline/shadowbox?tab=tags](https://support.getoutline.org/s/article/how-outline-works?language=zh_CN)。该映像包含 Outline 服务器和管理 API。Outline 服务器管理应用稍后会使用此 API 创建和移除访问密钥，选择/取消报告匿名指标等。
- 安装并配置 [Watchtower](https://support.getoutline.org/s/article/how-outline-works?language=zh_CN) 以每隔一小时检查映像更新，从而帮助确保每个 Outline 服务器均始终使用最新的功能和安全改进设置。
- 通过非公开的随机路径，使用随机端口启动一个网络服务器，用于访问管理 API。
- 创建[自签名 SSL 证书](https://support.getoutline.org/s/article/how-outline-works?language=zh_CN)，以便在没有域名的情况下通过 TLS 加密 Outline 服务器的管理。系统还会生成一个唯一的证书指纹，并将其存储在 Outline 管理器应用中，帮助防止 MITM 攻击。

Outline 安装完成后，无需进行任何配置。

### 服务器安全

Outline 是一款开放源代码软件。也就是说，任何人都可以查看代码，并可在发现漏洞后改进代码。我们的代码托管在

。

此外，软件一有新版本发布，所有已安装的 Outline 服务器都会自动更新，以确保所有 Outline 服务器均使用最新版本的软件。

为了管理服务器上的访问密钥，Outline 管理器应用会与 Outline 服务器上的特定管理服务进行交互。该管理服务在随机端口上运行，并使用非公开的唯一路径。除非指定了恰当的非公开路径，否则该服务不会响应任何查询，因此无法探测。最后，指向该管理服务的所有通讯均经过

加密。

此外，Outline 服务器不存储任何日志，因此即使被破解，也不会泄漏用户数据。您可以在

了解详情。

Outline 在 2018 年通过了

和

的审核。请在

查看相应报告。

### 处理 UDP 流量

Outline 可以作为整个系统的 VPN 运行。也就是说，所有 UDP 流量均会流向 Outline 服务器。

### DNS 流量

Outline 会通过 Outline 服务器执行所有 DNS 查询，并采用与其他所有互联网活动相同的加密方式保护相应数据。DNS 查询将经过 Outline 服务器到达 Dyn Internet Guide 或 OpenDNS。

Outline 不会记录您的 DNS 查询。

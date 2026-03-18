---
title: 术语
sidebar_label: 术语
---

## 什么是 VPN？

虚拟专用网 (VPN) 是在您的设备和主机服务器之间的专用连接。使用 VPN 时，您的流量将对互联网服务提供商隐藏。

您在以下场景中可能会需要使用 VPN：

- 在使用公共 Wi-Fi 网络的情况下保护您的数据
- 不想让互联网服务提供商和政府机构看到您的浏览数据
- 访问全球各种来源的未经审查的内容

## Outline 和传统 VPN 之间有何区别?

互联网服务提供商可通过识别常见安全协议和/或流量模式，轻松检测并封锁传统 VPN。Outline 比传统 VPN 更加可靠稳定，因为它是采用一种特殊的协议开发的，这种协议难以被检测到，因此更难被封锁。Outline 能够防范各种复杂形式的审查，包括基于网络的封锁和 IP 封锁。

## 什么是 Outline 服务器？

Outline 服务器会运行 VPN，供获得许可的用户连接。

如果您要创建新的网络，则可以将自己的安全服务器（如有）用作 Outline 服务器，或者使用云端服务提供商，例如：

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

请在 Outline 管理器中设置服务器。

## 什么是服务管理员？ {#servicemanager}

服务管理员负责设置 Outline 服务器并与用户分享访问密钥，且通常还负责服务器的使用费用。

## 什么是访问密钥？ {#accesskey}

访问密钥用于访问现有 Outline 服务器及连接到 VPN。[服务管理员](#servicemanager)会向您提供访问密钥，您也可以自行[设置 Outline 服务器](/manager/server-setup/setup-server)。

访问密钥大致如下例所示（本示例仅供参考，没有实际作用）：

ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## 什么是 Outline 管理器？

Outline 管理器是一款桌面应用，可让服务管理员设置 Outline 服务器、生成[访问密钥](#accesskey)并设置每个密钥的数据用量上限。您可以点击[此处](https://getoutline.org/get-started/#step-1)或[此处](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/)，下载最新版 Outline 管理器。

## 什么是 Outline 客户端？

Outline 客户端是一款应用，提供桌面版和移动版，可让您连接到 Outline 服务器并使用访问密钥访问 VPN。您可以点击[此处](https://getoutline.org/get-started/#step-3)或[此处](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/)，下载最新版 Outline 客户端。

## 什么是数据上限？

通过 Outline 管理器，服务管理员可针对访问密钥设置 30 天的浮动数据上限，以防止过度使用并帮助将费用控制在可预测的范围内。服务管理员可以设置适用于每个密钥的默认上限，也可以为任何密钥设置不同的上限来覆盖默认上限。上限一经设置，便会立即生效，并且会每小时强制执行一次。

如果服务管理员选择与 Jigsaw 分享指标，则应参阅

，详细了解数据上限功能使用情况的报告方式。

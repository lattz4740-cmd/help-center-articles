---
title: 防火墙错误
sidebar_label: 防火墙错误
---

您可能遇到的防火墙问题可分为三类：

## 您可能遭到网络防火墙的屏蔽。

如果您是在安装了防火墙的网络（例如学校或公司网络）中安装 Outline，请尝试换个网络进行安装。

 如果这无法解决问题，请联系您的网络管理员，让其允许在安装了防火墙的网络和您的 Outline 服务器之间建立连接。您需要知道 Outline 服务器的 IP 地址和 Outline 使用的端口（显示在安装脚本的末尾）。

## 您可能遭到设备防火墙的屏蔽。

如果您的设备上有软件禁止通过非标准端口或不明软件建立出站连接（例如 CheckPoint 的 ZoneAlarm），请查看设备或软件文档以了解如何为 Outline 创建例外。

## 您可能遭到服务器防火墙的屏蔽。

您选择的云服务提供商可能会要求您手动为服务器防火墙创建例外，以打开 Outline 所需使用的端口。运行安装脚本后，您应该会看到两个随机选择的端口，用于在您的服务器上运行 Outline。打开这两个端口应该就足以解决问题。

 为了给您的服务器防火墙创建例外，我们建议您查看“ufw”和“iptables”的相关文档：

- UFW：[https://help.ubuntu.com/community/UFW](/client/troubleshooting/firewall-errors)
- Iptables：[https://help.ubuntu.com/community/IptablesHowTo](/client/troubleshooting/firewall-errors)

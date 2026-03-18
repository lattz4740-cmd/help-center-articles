---
title: 为什么无法在 Windows 上安装 Outline 管理器？
sidebar_label: 为什么无法在 Windows 上安装 Outline 管理器？
---

您可能会看到以下错误消息：“抱歉，Outline 似乎未能正确安装。请尝试重新安装。如果还是无法解决问题，请[提交反馈](/about/feedback)。”

在 Windows 设备上使用 Outline 时，您有时可能会遇到意外错误。在多数情况下，您需要删除 Outline TAP 适配器（驱动程序）并应重新安装 Outline。

解决此问题的具体步骤可能会因您的 Windows 操作系统版本而有所不同，不过，以下提供了卸载 TAP 适配器以及卸载后重新安装 Outline 管理器的常规步骤。

1. 卸载 Outline 管理器的 TAP 适配器
   1. 进入**设备管理器**，然后在**网络适配器**下方
   2. 查找 **TAP-Windows Adapter V9** 文件或与 Outline 关联的 TAP 适配器
   3. 卸载或删除此适配器。请注意，这可能会影响您已安装的其他 VPN 应用。
2. 卸载 Outline 管理器
   1. 进入**程序和功能**，然后进入**卸载程序**
   2. 找到并卸载 Outline 管理器应用
   3. [下载最新版本的 Outline 管理器](https://getoutline.org/get-started/#step-3)，然后在 Windows 设备上重新安装 Outline 管理器。在重新安装时，系统应会自动安装新的 TAP 适配器。

如果问题仍然存在，请[与支持团队联系](/about/feedback)。

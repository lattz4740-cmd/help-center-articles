---
title: 如何更新 Outline 服务器软件？
sidebar_label: 如何更新 Outline 服务器软件？
---

Outline 服务器会及时自动获取最新的安全改进更新，确保您始终使用最新的 Outline 技术。自动更新流程由 [Watchtower](https://github.com/containrrr/watchtower) 支持。Watchtower 是一个开放源代码库，会定期检查和更新包含 Outline 软件的 Docker 映像。

此外，当您通过 Outline 管理器安装 Outline 时，我们会设置一个 Cron 作业，以自动使用适用于 Ubuntu 的[无人值守升级工具](https://wiki.debian.org/UnattendedUpgrades)升级服务器上的软件，并在需要的时候重新启动。请注意，由于系统假定主机除了运行 Outline，可能还在用于其他用途，因此为了保留现有配置，此功能不适用于高级模式。

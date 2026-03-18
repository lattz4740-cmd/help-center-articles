---
title: Google Cloud 自动设置 概述
sidebar_label: Google Cloud 自动设置 概述
---

## 概述

Outline 管理器包含一项功能，可让您在运行于 Google Cloud 的服务器上自动配置 Outline 服务器。如果您选择使用此功能，Outline 管理器会要求您使用 Google 帐号登录，此操作会授予您在本地安装的 Outline 管理器某些 [OAuth](https://developers.google.com/identity/protocols/oauth2) 权限，以便配置您的 Google Cloud 帐号。

如果您不想提供这些权限，可以按照 Outline 管理器中的高级设置说明操作，在 Google Cloud Platform 上运行 Outline。

## 授予的权限

为了提供自动设置功能，Outline 管理器需要获得您 Google 帐号的以下权限。

## Google Cloud Platform

- 查看和管理您的 Google Compute Engine 资源
- 查看您在各项 Google Cloud 服务中的数据以及您 Google 帐号的电子邮件地址

## 基本帐号信息

- 查看您的主要 Google 帐号电子邮件地址
- 将您与您在 Google 上的个人信息关联起来

## 其他访问权限

- 管理您的 Cloud Platform 项目
- 查看和管理您的 Google Cloud Platform 结算帐号
- 管理您的 Google API 服务配置

## 这些权限让我们能支持用于管理 Outline 服务器的高级功能，包括：

- 允许您选择正确的结算帐号
- 创建新项目来整理 Outline 服务器
- 列出可用的数据中心
- 创建新的虚拟机以运行 Outline
- 使用 Outline 配置新虚拟机

## 撤消权限

您可以访问[我的帐号](https://myaccount.google.com/permissions)，撤消 Outline 管理器对 Google Cloud Platform 的访问权限。如果您撤消访问权限，您使用自动设置创建的所有服务器都会继续运行，但不会再显示在 Outline 管理器中。要恢复访问权限，只需启动自动设置流程，以重新连接到 Google Cloud Platform。

## Outline 项目整理

Google Cloud 自动设置使用单一 [Google Cloud 项目](https://cloud.google.com/resource-manager/docs/creating-managing-projects)来整理您的 Outline 服务器。该项目会在您首次使用自动设置时创建，系统将提供建议项目 ID，ID 以“Outline-”开头，后跟一串随机字符。您可以在创建时选择其他偏好的项目 ID。该项目将命名为“Outline 服务器”。

## 结算帐号

Google Cloud 项目需要一个确定了付款信息的关联“结算帐号”。首次使用 Google Cloud 自动设置时，系统会要求您提供结算帐号以与您的 Outline 服务器关联。有时，服务器会因结算帐号存在问题而停止运行。在这种情况下，您应该登录 [Google Cloud Console](https://console.cloud.google.com/getting-started)，找到与 Outline 关联的 Google Cloud 项目（名为“Outline 服务器”），然后更新结算设置。

## 销毁服务器

如果您想销毁使用自动设置创建的服务器，最简单的方法是使用 Outline 管理器。但是，如果您想自行销毁服务器，则可以登录 [Google Cloud Console](https://console.cloud.google.com/getting-started)，找到初始设置期间创建的项目（名为“Outline 服务器”），然后删除其中的资源或关闭项目。

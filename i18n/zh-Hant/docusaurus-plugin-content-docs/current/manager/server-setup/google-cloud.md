---
title: Google Cloud 自動化設定
sidebar_label: Google Cloud 自動化設定
---

## 總覽

Outline Manager 有項功能可以在執行 Google Cloud 的伺服器上自動設定 Outline 伺服器。如果你選擇使用這項功能，Outline Manager 就會要求你使用 Google 帳戶登入，而這項操作會將特定 [OAuth](https://developers.google.com/identity/protocols/oauth2) 權限授予本機安裝的 Outline Manager，以供設定 Google Cloud 帳戶使用。

如果你不想提供這些權限，可以依照 Outline Manager 中的進階設定操作說明，在 Google Cloud Platform 上執行 Outline。

## 授予的權限

為了提供自動設定功能，Outline Manager 需要從你的 Google 帳戶取得下列權限。

## Google Cloud Platform

- 查看及管理 Google Compute Engine 資源
- 查看你在各項 Google Cloud 服務中的資料，以及你的 Google 帳戶電子郵件地址

## 基本帳戶資訊

- 查看 Google 帳戶的主要電子郵件地址
- 將你與你在 Google 上的個人資訊建立關聯

## 其他存取權

- 管理 Cloud Platform 專案
- 查看及管理 Google Cloud Platform 帳單帳戶
- 管理 Google API 服務設定

## 有了這些權限，Outline Manager 即可針對 Outline 伺服器提供下列進階管理功能：

- 讓你選取正確的帳單帳戶
- 建立用於管理 Outline 伺服器的新專案
- 列出可用的資料中心
- 建立新的 Outline 虛擬執行機器
- 使用 Outline 設定新的虛擬機器

## 撤銷權限

你可以前往[我的帳戶](https://myaccount.google.com/permissions)撤銷 Outline Manager 的 Google Cloud Platform 存取權。撤銷存取權後，原先透過自動化設定建立的伺服器仍會繼續運作，但是 Outline Manager 就不會再顯示這些伺服器。如要重新授權，請啟動自動化設定流程，重新連線至 Google Cloud Platform。

## Outline 專案機構

Google Cloud 自動化設定會使用單一 [Google Cloud 專案](https://cloud.google.com/resource-manager/docs/creating-managing-projects)來管理 Outline 伺服器。這個專案是在你首次使用自動化設定時建立的，建議的專案 ID 是「Outline-」加上一串隨機字元，你也可以在建立專案時選擇其他偏好的專案 ID。該專案將命名為「Outline 伺服器」。

## 帳單帳戶

Google Cloud 專案需要連結至定義付款資訊的「帳單帳戶」。首次使用 Google Cloud 自動化設定時，你必須提供要與 Outline 伺服器建立關聯的帳單帳戶。帳單帳戶的問題有時會導致伺服器停止運作。發生這種情況時，請登入 [Google Cloud Console](https://console.cloud.google.com/)，找出與 Outline 相關聯的 Google Cloud 專案 (名為「Outline 伺服器」)，然後更新帳單設定。

## 刪除伺服器

如果想刪除透過自動化設定建立的伺服器，最簡單的方法是從 Outline Manager 執行刪除作業。不過，如果你想自行刪除伺服器，可以登入 [Google Cloud Console](https://console.cloud.google.com/)，找出首次設定時建立的專案 (名為「Outline 伺服器」)，然後刪除其中的資源或關閉整個專案。

---
title: Google Cloud 自動化設定
sidebar_label: Google Cloud 自動化設定
---

## 概覽

Outline Manager 有一項功能，讓你可在執行 Google Cloud 的伺服器上自動設定 Outline 伺服器。如果你選擇使用此功能，Outline Manager 會要求你使用 Google 帳戶登入，這會向本機安裝的 Outline Manager 授予特定 [OAuth](https://developers.google.com/identity/protocols/oauth2) 權限，以供設定 Google Cloud 帳戶使用。

 如果你不想提供這些權限，可按照 Outline Manager 中的進階設定指示，在 Google Cloud Platform 上執行 Outline。

## 授予的權限

為提供自動化設定功能，Outline Manager 需要從你的 Google 帳戶取得以下權限。

## Google Cloud Platform

- 查看及管理「Google 運算引擎」資源
- 查看你在各項 Google Cloud 服務中的資料，以及你的 Google 帳戶電郵地址

## 基本帳戶資料

- 查看 Google 帳戶的主要電郵地址
- 將你與你在 Google 上的個人資料建立關聯

## 額外存取權

- 管理 Cloud Platform 項目
- 查看及管理 Google Cloud Platform 付款帳戶
- 管理 Google API 服務設定

這些權限允許我們在管理 Outline 伺服器時提供以下進階管理功能：

- 讓你選取正確的付款帳戶
- 建立用於管理 Outline 伺服器的新項目
- 列出可用的數據中心
- 建立新的虛擬機器以執行 Outline
- 使用 Outline 設定新的虛擬機器

## 撤銷權限

您可以瀏覽「[我的帳戶](https://myaccount.google.com/permissions)」，撤銷 Outline Manager 的 Google Cloud Platform 存取權。撤銷存取權後，原先透過自動化設定建立的伺服器仍會繼續運作，但 Outline Manager 將不再顯示這些伺服器。如要重新授權，請啟動自動化設定流程，重新連線至 Google Cloud Platform。

## Outline 項目整理

Google Cloud 自動化設定會使用單一[Google Cloud 項目](https://cloud.google.com/resource-manager/docs/creating-managing-projects)以整理您的 Outline 伺服器。該項目會在首次使用自動化設定時建立，建議項目 ID 以「Outline-」開頭，然後是一串隨機字元。你亦可在建立項目時選擇其他偏好的項目 ID。項目名稱將命名為「Outline 伺服器」。

## 付款帳戶

Google Cloud 項目需要使用定義付款資料的「付款帳戶」連結。在您首次使用 Google Cloud 自動化設定時，系統會要求您提供關聯至 Outline 伺服器的付款帳戶。付款帳戶的問題有時會導致伺服器停止運作。發生這種情況時，請登入 [Google Cloud Console](https://console.cloud.google.com/getting-started)，找出與 Outline 相關聯的 Google Cloud 項目 (名為「Outline 伺服器」)，然後更新帳單設定。

## 刪除伺服器

如果想刪除透過自動化設定建立的伺服器，最簡單的方法是從 Outline Manager 中刪除。不過，如果你想自行刪除伺服器，可以登入 [Google Cloud Console](https://console.cloud.google.com/getting-started)，找出首次設定時建立的項目 (名為「Outline 伺服器」)，然後刪除其中的資源或關閉整個項目。

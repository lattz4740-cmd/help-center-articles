---
title: 概要
sidebar_label: 概要
---

Outline マネージャーには、Google Cloud で実行しているサーバー上に Outline サーバーを自動でセットアップする機能があります。この機能を使用する場合は、Google アカウントを使用してログインするよう Outline マネージャーから要求されます。Google アカウントでログインすると、ローカルの Outline マネージャーに特定の [OAuth](https://developers.google.com/identity/protocols/oauth2) 権限が付与され、お客様の Google Cloud アカウントを設定できるようになります。

OAuth 権限を付与しない場合は、Outline マネージャーの詳細なセットアップの手順に沿って Google Cloud Platform で Outline を実行してください。

## 権限の付与

自動でセットアップするには、Outline マネージャーで Google アカウントの次の権限が要求されます。

## Google Cloud Platform

- Google Compute Engine リソースの参照と管理
- Google Cloud サービス全体のデータの参照と、Google アカウントのメールアドレスの参照

## 基本的なアカウント情報

- Google アカウントのメインのメールアドレスの参照
- Google でのお客様とその個人情報の関連付け

## その他の権限

- Cloud Platform プロジェクトの管理
- Google Cloud Platform の請求先アカウントの表示と管理
- Google API サービスの設定の管理

これらの権限を付与することで、Outline サーバーの次のような詳細な管理機能を利用できるようになります。

- 正しい請求先アカウントの選択
- 複数の Outline サーバーを編成するための新しいプロジェクトの作成
- 利用可能なデータセンターの一覧表示
- Outline を実行するための新しい仮想マシンの作成
- Outline を使用した新しい仮想マシンの設定

## 権限の取り消し

[[Google アカウント](https://myaccount.google.com/permissions)] にアクセスして、Outline マネージャーから Google Cloud Platform の権限を取り消すことができます。権限を取り消すと、自動セットアップで作成したサーバーは引き続き実行されますが、Outline マネージャーには表示されなくなります。権限を復元するには、自動セットアップのフローを開始して Google Cloud Platform に再接続するだけです。

## Outline プロジェクトの編成

Google Cloud の自動セットアップでは、1 つの [Google Cloud プロジェクト](https://cloud.google.com/resource-manager/docs/creating-managing-projects)で複数の Outline サーバーを編成します。このプロジェクトは自動セットアップを初めて使用するときに作成され、「Outline-」の後にランダムな文字列が追加されたプロジェクト ID が提案されます。必要に応じて、作成時に別のプロジェクト ID を選択することもできます。プロジェクト名は「Outline servers」になります。

## 請求先アカウント

Google Cloud プロジェクトには、お支払い情報を指定した「請求先アカウント」を関連付ける必要があります。Google Cloud の自動セットアップを初めて使用するときに、Outline サーバーに関連付ける請求先アカウントを指定するよう求められます。請求先アカウントに問題がある場合、サーバーが停止することがあります。サーバーが停止した場合は、[Google Cloud Console](https://console.cloud.google.com/getting-started) にログインし、Outline に関連付けられた Google Cloud プロジェクト（「Outline servers」）を見つけて、請求先の設定を更新してください。

## サーバーの破棄

自動セットアップで作成したサーバーを破棄する場合は、Outline マネージャーを使用する方法が最も簡単です。ただし、サーバーを自分で破棄する場合は、[Google Cloud Console](https://console.cloud.google.com/getting-started) にログインし、最初のセットアップ時に作成したプロジェクト（「Outline servers」）を見つけて、そこでリソースを削除するか、プロジェクトをシャットダウンしてください。

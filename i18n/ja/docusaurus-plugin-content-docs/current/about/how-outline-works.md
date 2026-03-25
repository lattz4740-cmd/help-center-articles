---
title: Outline の仕組み
sidebar_label: Outline の仕組み
---

## サーバーのインストール

Outline サーバーのインストールは一見単純に思われるかもしれませんが、実際にはインストールが完了するまでにバックグラウンドで複雑な一連の手順が実行されています。

Outline サーバーのインストール時には必ず、インストール スクリプトによって以下の手順が実行されます。

- Docker を使用して、安定バージョンの Shadowbox イメージが取得され、読み込まれます。イメージは [Quay.io](https://quay.io/) の [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags) でホストされています。このイメージには、Outline サーバーと Management API が含まれています。後に、Outline サーバー管理アプリケーションがこの API を使用して、アクセスキーの作成と削除、匿名化された指標の報告のオプトイン、オプトアウトなどを行います。
- [Watchtower](https://github.com/v2tec/watchtower) がインストールされ、1 時間ごとにイメージの更新をチェックするよう設定されます。この設定により、すべての Outline サーバーが常に最新の機能とセキュリティ修正が適用された状態になります。
- Management API にアクセスするために使用するウェブサーバーが、ランダムなポート上で秘密のランダムなパスを使用して起動されます。
- [自己署名 SSL 証明書](https://en.wikipedia.org/wiki/Self-signed_certificate)が作成されます。この証明書は、Outline サーバーの管理を、ドメイン名を使用せずに TLS を使用して暗号化できるようにするためのものです。この証明書に固有のフィンガープリントも生成されて、Outline マネージャー アプリケーションに保管されます。このフィンガープリントは、MITM 攻撃の防止に役立ちます。

Outline サーバーのインストール後に必要な設定はありません。

## サーバーのセキュリティ

Outline ソフトウェアはオープンソースです。つまり、誰でもコードを確認して、脆弱性が見つかった場合には修正できます。Outline のコードは [GitHub](https://github.com/search?q=org%3AOutline-Foundation+outline&unscoped_q=outline) でホストされています。

さらに、インストールした Outline サーバーはすべて、新しいバージョンがリリースされると自動的に更新されます。したがって、Outline サーバーで古いバージョンのソフトウェアが実行されたままになることはありません。

サーバー上のアクセスキーを管理するために、Outline マネージャー アプリケーションは Outline サーバー上の管理サービスとやり取りします。管理サービスはランダムなポート上で秘密の固有パスを使用して実行されます。管理サービスは該当する秘密のパスが指定されない限りクエリに応答しないことから、サービス自体にプローブへの耐性が備わっています。さらに、管理サービスへの通信はすべて、 [自己署名 SSL 証明書](https://en.wikipedia.org/wiki/Self-signed_certificate) を使用して暗号化されます。

また、Outline サーバーはログを一切保管しないため、セキュリティが侵害されたとしても、ユーザーのデータが開示されることはありません。詳しくは[こちら](/about/security-and-privacy)をご覧ください。

Outline は 2018 年、 [Radically Open Security](https://radicallyopensecurity.com/) 社と [Cure53](https://cure53.de/) 社による監査を受けました。2 社によるレポートは[こちら](/about/security-and-privacy)からご覧になれます。

## UDP トラフィックの処理

Outline はシステム全体の VPN として動作可能です。つまり、すべての UDP トラフィックは Outline サーバー経由でトンネリングされます。

## DNS トラフィック

Outline は常に Outline サーバーを介して DNS ルックアップを行い、他のすべてのネットワーク アクティビティに使用されるのと同じ暗号化を使用して DNS トラフィックを保護します。DNS クエリは Outline サーバーから Dyn Internet Guide または OpenDNS に送信されます。

Outline によって DNS ルックアップのログが記録されることはありません。

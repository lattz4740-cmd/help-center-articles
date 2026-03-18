---
title: Linux に Outline クライアントをインストールする
sidebar_label: Linux に Outline クライアントをインストールする
---

Outline クライアント バージョン 1.15 以降のすべてのバージョンは、Linux オペレーティング システム用の Debian パッケージとしてリリースされます。サポートされているオペレーティング システムについて詳しくは、[最小システム要件](/client/getting-started/system-requirements)をご覧ください。

## Debian ベースの Linux ディストリビューションに Outline クライアントをインストールする（推奨）

次のコマンドを実行します。

1. Outline のリポジトリキーをインストールして、リポジトリを追加します。
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. apt パッケージ リストを更新し、最新バージョンの Outline クライアントをインストールします。
   ```
   sudo apt update
   sudo apt install outline-client
   ```

今後のアップデートを確認またはインストールするには、手順 2 のコマンドを再度実行します。バージョン 1.15 以降、Linux 上の Outline クライアントではアプリ内自動更新が無効になっています。

Outline クライアントをアンインストールするには、次のコマンドを実行します。

```
sudo apt purge outline-client
```

## 代替オプション

1. 最新の Outline クライアント Debian パッケージを [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) からダウンロードします。
2. コマンドラインで次のコマンドを実行してパッケージをインストールします。
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. バージョン 1.15 以降、Linux 上の Outline クライアントではアプリ内自動更新が無効になっているため、手動で更新を確認してください。
4. Outline クライアントをアンインストールするには、コマンドラインで次のコマンドを実行します。
   ```
   sudo apt purge outline-client
   ```

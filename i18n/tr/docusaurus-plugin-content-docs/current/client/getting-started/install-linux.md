---
title: "Outline istemcisini Linux'a yükleme"
sidebar_label: "Outline istemcisini Linux'a yükleme"
---

Outline istemcisinin 1.15 sürümü itibarıyla gelecekteki tüm sürümler, Linux işletim sistemlerinde Debian paketleri olarak yayınlanacak. Desteklediğimiz işletim sistemleri hakkında daha fazla bilgi için [minimum sistem gereksinimlerimizi](/client/getting-started/system-requirements) inceleyin.

## Debian tabanlı Linux dağıtımları için Outline istemcisini yükleme (Önerilir)

Aşağıdaki komutları çalıştırın:

1. Outline'ın depo anahtarını yükleyip depoyu ekleyin.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. "apt" paket listesini güncelleyin ve Outline istemcisinin en yeni sürümünü yükleyin.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Gelecekteki güncellemeleri kontrol etmek veya yüklemek için 2. adımdaki komutları tekrar çalıştırın. Linux'taki Outline istemcisinde 1.15 sürümü itibarıyla uygulama içi otomatik güncellemenin devre dışı bırakıldığını unutmayın.

Outline istemcisini kaldırmak için aşağıdaki komutu çalıştırın:

```
sudo apt purge outline-client
```

## Alternatif seçenek

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) adresinden en yeni Outline istemcisi Debian paketini indirin.
2. Paketi yüklemek için komut satırında aşağıdaki komutları çalıştırın
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Linux'taki Outline istemcisinde 1.15 sürümü itibarıyla uygulama içi otomatik güncelleme devre dışı bırakıldığından güncellemeleri manuel olarak kontrol edin.
4. Outline istemcisini kaldırmak için komut satırında aşağıdaki komutu çalıştırın:
   ```
   sudo apt purge outline-client
   ```

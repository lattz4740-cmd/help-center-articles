---
title: Memasang Outline Client pada Linux
sidebar_label: Memasang Outline Client pada Linux
---

Bermula dengan Outline Client versi 1.15, semua versi akan datang akan dikeluarkan sebagai pakej Debian untuk sistem pengendalian Linux. Semak [keperluan minimum sistem](/client/getting-started/system-requirements) kami untuk mendapatkan maklumat lanjut tentang sistem pengendalian yang disokong.

## Pasang Outline Client untuk pengagihan Linux berasaskan Debian (Disyorkan)

Jalankan perintah yang berikut:

1. Pasang kunci repositori Outline dan tambahkan repositori.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Kemas kinikan senarai pakej apt dan pasang versi terkini Outline Client.

```
kemas kinikan sudo apt
pemasangan sudo apt outline-client
```

Untuk menyemak atau memasang kemaskinian pada masa hadapan, jalankan arahan dalam Langkah 2 sekali lagi. Harap maklum bahawa kemaskinian automatik dalam apl dilumpuhkan untuk Outline Client pada Linux, bermula dengan versi 1.15.

Untuk menyahpasang Outline Client, jalankan perintah yang berikut:

```
sudo apt purge outline-client
```

## Pilihan Alternatif

1. Muat turun pakej Debian Outline Client terkini daripada [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Jalankan perintah yang berikut dalam baris arahan untuk memasang pakej

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
pemasangan sudo apt ./outline-client.deb
```

3. Semak kemaskinian secara manual kerana kemaskinian automatik dalam apl dilumpuhkan untuk Outline Client pada Linux, bermula dengan versi 1.15.

4. Untuk menyahpasang Outline Client, jalankan perintah yang berikut dalam baris perintah:

```
sudo apt singkir outline-client
```

---
title: Menginstal Klien Outline di Linux
sidebar_label: Menginstal Klien Outline di Linux
---

Mulai Aplikasi Outline versi 1.15, semua versi mendatang akan dirilis sebagai paket Debian untuk sistem operasi Linux. Tinjau [persyaratan sistem minimum](/client/getting-started/system-requirements) kami untuk mengetahui informasi selengkapnya tentang sistem operasi yang kami dukung.

## Menginstal Aplikasi Outline untuk distribusi Linux berbasis Debian (Direkomendasikan)

Jalankan perintah berikut:

1. Instal kunci repositori Outline dan tambahkan repositori.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Perbarui daftar paket apt dan instal Aplikasi Outline versi terbaru.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Untuk memeriksa atau menginstal update mendatang, jalankan kembali perintah di Langkah 2. Perhatikan bahwa update otomatis dalam aplikasi dinonaktifkan untuk Aplikasi Outline di Linux, mulai versi 1.15.

Untuk meng-uninstal Aplikasi Outline, jalankan perintah berikut:

```
sudo apt purge outline-client
```

## Opsi Alternatif

1. Download paket Debian Aplikasi Outline terbaru di [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Jalankan perintah berikut di command line untuk menginstal paket
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Periksa update secara manual, karena update otomatis dalam aplikasi dinonaktifkan untuk Aplikasi Outline di Linux, mulai versi 1.15.
4. Untuk meng-uninstal Aplikasi Outline, jalankan perintah berikut di command line:
   ```
   sudo apt purge outline-client
   ```

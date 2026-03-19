---
title: Error pada firewall
sidebar_label: Error pada firewall
---

Ada tiga jenis masalah firewall yang mungkin Anda temui:

## Anda mungkin diblokir oleh firewall jaringan.

Jika Anda mencoba menginstal Outline saat terhubung ke jaringan firewall, seperti di sekolah atau di tempat kerja, cobalah menginstal saat berada di jaringan yang berbeda.

Jika tindakan ini tidak berhasil, hubungi administrator jaringan untuk mengizinkan koneksi antara jaringan firewall ke server Outline Anda. Anda perlu mengetahui alamat IP server Outline Anda dan port tempat Outline berjalan yang ditunjukkan di akhir skrip penginstalan.

## Anda mungkin diblokir oleh firewall perangkat.

Jika Anda memiliki software di perangkat yang memblokir koneksi keluar pada port non-standar, atau software tidak dikenal, (ZoneAlarm CheckPoint), baca dokumentasi perangkat atau software untuk mempelajari cara membuat pengecualian untuk Outline.

## Anda mungkin diblokir oleh firewall server.

Penyedia cloud yang telah Anda pilih mungkin mengharuskan Anda membuat pengecualian untuk firewall server secara manual agar dapat membuka port tempat Outline berjalan. Setelah menjalankan skrip penginstalan, Anda akan diberi dua port tempat Outline berjalan di server Anda yang dipilih secara acak. Membuka kedua port ini saja sudah cukup.

 Untuk membuat pengecualian pada firewall Server, sebaiknya baca dokumentasi 'ufw' dan 'iptables':

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

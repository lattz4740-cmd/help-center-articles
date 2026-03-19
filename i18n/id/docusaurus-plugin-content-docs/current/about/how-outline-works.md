---
title: Cara Kerja Outline
sidebar_label: Cara Kerja Outline
---

## Penginstalan server
 Meskipun penginstalan Outline mungkin tampak sederhana, ada serangkaian langkah rumit yang perlu dilakukan untuk menginstal server Anda. Setiap kali Outline diinstal, skrip penginstalan akan berjalan melalui langkah-langkah berikut:

- Image Shadowbox versi stabil diambil dan diimpor menggunakan Docker. Image dihosting di [Quay.io](https://quay.io/), di [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Image ini berisi server Outline dan Management API yang nantinya digunakan oleh aplikasi Outline Server Management untuk membuat dan menghapus kunci akses, melaporkan/tidak melaporkan metrik anonim, dan sebagainya.
- [Watchtower](https://github.com/v2tec/watchtower) diinstal dan dikonfigurasi untuk memeriksa update image setiap jam, yang membantu memastikan bahwa setiap server Outline selalu diupdate dengan peningkatan fitur dan keamanan terbaru.
- Server web, yang digunakan untuk mengakses Management API, akan dimulai di port acak pada jalur rahasia yang diacak.
- [Sertifikat SSL yang ditandatangani sendiri](https://en.wikipedia.org/wiki/Self-signed_certificate) dibuat agar pengelolaan server Outline dapat dienkripsi menggunakan TLS meskipun tidak memiliki nama domain. Sidik jari unik untuk sertifikat ini juga akan dibuat dan disimpan di aplikasi Outline Manager sehingga serangan MITM dapat dicegah.

Setelah diinstal, Outline tidak memerlukan konfigurasi lain.

## Keamanan server
 Software Outline adalah open source, yang berarti siapa saja dapat melihat kodenya dan meningkatkannya jika ada kerentanan yang ditemukan. Kode kami dihosting di [GitHub](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline).

 Selain itu, semua server Outline yang terinstal akan otomatis diupdate ketika versi baru telah dirilis untuk memastikan tidak ada server Outline yang menjalankan software versi lama.

 Untuk mengelola kunci akses di server, aplikasi Outline Manager berinteraksi dengan Layanan Pengelolaan di server Outline. Layanan Pengelolaan ini beroperasi pada port acak serta jalur rahasia yang unik. Layanan Pengelolaan sendiri tahan terhadap serangan karena tidak merespons kueri kecuali diberikan jalur rahasia yang sesuai. Terakhir, semua komunikasi ke Layanan Pengelolaan dienkripsi dengan [sertifikat SSL yang ditandatangani sendiri](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Perlu diketahui bahwa server Outline tidak menyimpan log apa pun sehingga tidak akan ada data pengguna yang terungkap meskipun disusupi. Pelajari lebih lanjut [di sini](/about/security-and-privacy). Outline diaudit oleh [Radically Open Security](https://radicallyopensecurity.com/) dan [Cure53](https://cure53.de/) pada tahun 2018. Lihat laporannya [di sini](/about/security-and-privacy).

## Menangani traffic UDP
 Outline dapat beroperasi sebagai VPN untuk seluruh sistem, yang berarti bahwa semua traffic UDP ditransfer melalui server Outline.

## Traffic DNS
Outline melakukan semua pencarian DNS melalui server Outline dan melindunginya menggunakan enkripsi yang sama dengan yang digunakan untuk semua aktivitas jaringan. Kueri DNS Anda akan melewati server Outline ke Dyn Internet Guide, OpenDNS, Cloudflare DNS, atau Quad9 DNS. Outline tidak pernah menyimpan log pencarian DNS Anda.

---
title: Keamanan dan privasi saat menggunakan Outline
sidebar_label: Keamanan dan privasi saat menggunakan Outline
---

Keamanan dan privasi saat menggunakan Outline

## Cara Outline melindungi komunikasi online Anda

Traffic internet paling rentan untuk diawasi saat melintasi jaringan lokal atau nasional Anda.

Outline membantu menjaga privasi komunikasi Anda dengan mengenkripsi traffic internet saat melintasi jaringan nasional Anda dan menjaganya tetap terenkripsi hingga mencapai server Outline. Jika traffic dienkripsi dengan Outline, pemantau jaringan tidak dapat memeriksa situs yang Anda kunjungi atau informasi yang Anda transfer.

Outline juga dapat membantu Anda memulihkan akses ke fitur komunikasi menyeluruh aman yang mungkin tidak dapat diakses di negara Anda.

## Standar enkripsi

Outline mengenkripsi komunikasi antara perangkat Anda dan server Outline menggunakan cipher AEAD 256-bit Chacha2020 IETF Poly 1305. Cipher AEAD menawarkan kerahasiaan, integritas, dan autentisitas, serta performa yang unggul pada hardware modern.

## Audit keamanan

Pada tahun 2018, Outline diaudit oleh Radically Open Security dan Cure53, dua organisasi keamanan digital independen yang meninjau software terhadap standar keamanan terbaru. Radically Open Security melakukan audit tambahan pada tahun 2022 dan Cure53 melakukan audit terhadap Outline SDK pada tahun 2024. Anda dapat membaca laporannya di sini:

- [Laporan Hasil Uji Penetrasi oleh Radically Open Security (Maret 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Laporan Uji Penetrasi & Audit Jigsaw Outline oleh Cure53 (Desember 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Laporan Hasil Uji Penetrasi oleh Radically Open Security (Desember 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Laporan Hasil Uji Penetrasi oleh Cure53 Jigsaw Outline VPN SDK (Januari 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Metrik dan log anonim

Outline melacak bandwidth yang digunakan, sebagai "byte yang ditransfer" untuk setiap kunci akses. Dengan informasi ini, administrator server dapat menyesuaikan langganan bandwidth-nya dengan penyedia server cloud sesuai kebutuhan, tetapi tidak memungkinkan administrator server melihat informasi aktual yang melewati server Outline.

Pelajari lebih lanjut [pengumpulan data dan informasi](/about/data-collection) oleh Outline.

---

## FAQ keamanan dan privasi

## Dapatkah Outline menyembunyikan identitas saya saat online?

Tidak, Outline bukanlah fitur untuk menyembunyikan identitas. Outline melindungi privasi Anda dari kemungkinan adanya pemantau jaringan.

Outline tidak menawarkan penyembunyian identitas Anda secara penuh pada situs yang Anda kunjungi karena situs masih dapat mengidentifikasi Anda ketika Anda login dan terkadang melalui teknik, seperti sidik jari browser. Untuk aplikasi seluler, sebagian besar smartphone modern memiliki API yang memungkinkan aplikasi terinstal mendapatkan lokasi Anda secara independen melalui proxy karena mengandalkan GPS yang disematkan.

VPN secara umum menawarkan perlindungan penting, terutama dari pengawasan internet, tetapi selalu ada risiko saat online. Meskipun dengan VPN, jika ISP sudah mengetahui identitas Anda dan dapat mengamati traffic jaringan, ISP mungkin dapat menentukan alamat IP server Outline Anda. Informasi ini dapat digunakan untuk memblokir akses ke server Outline atau mempelajari pola penggunaan seperti kapan Anda biasanya online, dan perkiraan lokasi Anda.

## Apakah orang lain dapat mengetahui jika saya menggunakan Outline?

Mungkin. Platform dan layanan yang Anda akses kemungkinan besar dapat memberi tahu bahwa koneksi Anda berasal dari server cloud. Terkadang, mereka dapat menyimpulkan bahwa Anda menggunakan VPN, tetapi tidak akan dapat melihat konten traffic internet Anda.

## Apakah Outline melindungi saya dari semua potensi ancaman cyber?

Tidak, tidak ada fitur yang akan melindungi Anda dari semua potensi ancaman cyber. Outline memberi Anda akses ke internet terbuka dan meningkatkan privasi Anda dengan mengenkripsi traffic, tetapi Anda disarankan mengambil tindakan pencegahan tambahan untuk melindungi diri dari serangan cyber jenis lain, seperti malware dan phishing.

Untuk memperkuat pertahanan online, pertimbangkan untuk bekerja sama dengan ahli keamanan cyber di organisasi Anda. Atau, Anda dapat memperoleh panduan yang dipersonalisasi dari ahli keamanan terkemuka di [Security Planner](https://securityplanner.org/), situs web yang dibuat untuk memberi Anda instruksi yang jelas dalam memilih alat keamanan siber yang tepat bagi masalah Anda.

Anda juga dapat melihat produk keamanan cyber lainnya dari [Jigsaw](https://jigsaw.google.com/), seperti [Intra](https://getintra.org/), [Project Shield](https://g.co/shield), dan [Notifikasi Sandi](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Apakah menggunakan VPN merupakan tindakan yang legal?

Sebelum menjalankan Outline atau menggunakan aplikasi, harap periksa hukum dan regulasi setempat, serta Persyaratan Layanan untuk penyedia cloud yang ingin Anda gunakan.

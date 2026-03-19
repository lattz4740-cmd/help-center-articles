---
title: Pengumpulan Data dan Informasi
sidebar_label: Pengumpulan Data dan Informasi
---

Outline tidak mengumpulkan informasi pribadi kecuali jika Anda memilih untuk memberikannya. Outline juga tidak mengumpulkan informasi tentang situs yang Anda kunjungi atau dengan siapa atau apa yang Anda komunikasikan.

 Jika Anda membuat atau login ke akun dengan penyedia cloud pihak ketiga melalui Outline Manager, kami tidak memperoleh informasi apa pun yang Anda berikan kepada penyedia cloud pihak ketiga, seperti alamat email, nama, informasi penagihan, dan detail pembayaran.

## Informasi yang kami peroleh secara otomatis
 Kami mengumpulkan dua jenis informasi secara otomatis.

 1. IP Server

 IP server Outline dikumpulkan oleh [Quay.io](https://quay.io/), dan dapat diakses oleh kami jika server diupdate secara otomatis menggunakan penyempurnaan keamanan dan fitur terbaru. IP Server dapat mengidentifikasi penyedia server cloud dan kota tempat server Outline disiapkan, tetapi hal ini tidak akan memberikan informasi tentang siapa yang menjalankan atau mengakses server.

 2. Informasi teknis non-pribadi yang dapat diidentifikasi

 Jika Outline mengalami error atau terjadi pengecualian fatal, atau jika Anda mengirim masukan secara manual melalui aplikasi Outline, informasi yang tercantum di bawah ini akan dilaporkan. Informasi ini hanya akan digunakan untuk membantu proses identifikasi dan memperbaiki masalah performa atau stabilitas.

- Negara
- Lokal
- Tanggal dan waktu terjadinya error/pengecualian dan maksimum 100 peristiwa sebelumnya, seperti saat pengguna membuka bagian ‘Tentang’
- Pesan pengecualian yang dikumpulkan secara statis
- Nama dan versi OS
- Model ponsel (jika ada)
- Waktu mulai aplikasi
- Browser
- Arsitektur
- Versi dan nomor versi Outline

Informasi ini ditransfer menggunakan HTTPS ke Sentry ([sentry.io](https://sentry.io/)), penyedia layanan pelacakan error pihak ketiga yang bersifat open source. Sentry menggunakan berbagai teknologi dan layanan standar industri untuk melindungi data Anda dari akses, pengungkapan, dan penggunaan yang tidak sah, atau kehilangan. Jika Anda memiliki pertanyaan terkait kebijakan Sentry, harap buka [https://sentry.io/security/](https://sentry.io/security/) dan [https://sentry.io/privacy/](https://sentry.io/privacy/), atau hubungi [security@sentry.io](mailto:security@sentry.io). Semua data Outline yang disimpan oleh Sentry dibatasi sehingga hanya anggota tim Outline yang dapat mengaksesnya.

## Kami memperoleh informasi hanya dengan izin pengguna
 Outline melaporkan informasi berikut ke tim Outline jika pengguna memilih untuk membagikannya.

 1. Metrik penggunaan

 Setiap server Outline secara otomatis mengumpulkan (selama satu jam terakhir dan dengan basis per kunci akses) jumlah byte yang ditransfer, jumlah waktu pengguna tersambung ke server, negara, dan sistem otonom asal kredensial yang digunakan, dan apakah ada fitur yang diaktifkan atau dinonaktifkan. Isi komunikasi atau metadata pribadi yang dapat diidentifikasi apa pun (seperti info login, email, ID perangkat, dll.) tidak akan disimpan dalam log. Semua metrik terkait dengan ID server. Petunjuk untuk mengubah ID server dapat ditemukan [/manager/server-management/reset-server-id](/manager/server-management/reset-server-id)di sini.

 Secara default, server Outline tidak membagikan metrik ini dengan tim Outline. Jika administrator Server secara eksplisit memilih untuk membagikan metrik penggunaan, informasi ini akan dikirimkan dengan aman kepada tim Outline setiap jam. Setelah 60 hari, metrik penggunaan akan digabungkan ke tingkat negara. Administrator Server dapat mengubah preferensi berbagi metrik penggunaan kapan saja dengan membuka menu ‘Setelan’ di Outline Manager.

 Kami menghargai kepercayaan Anda untuk membagikan metrik anonim tentang penggunaan server, karena data ini akan kami gunakan untuk mengukur tren penggunaan dan menyempurnakan kualitas produk.

 Misalnya, jika administrator Server memilih untuk membagikan metrik penggunaan, kami dapat memperoleh informasi yang menunjukkan bahwa Server dengan ID 12345 kemarin digunakan selama 3 jam, dengan total transfer data sebesar 500 megabyte, dari tiga kunci yang masing-masing digunakan di Amerika Serikat dan Kanada, dengan fitur batas data yang diaktifkan.

 2. Komentar dan email Anda ketika mengirimkan masukan

 Aplikasi Outline Manager dan Outline memungkinkan Anda mengirim masukan kepada tim. Sebaiknya jangan menyertakan informasi identitas pribadi, tetapi kami menyediakan kolom email opsional jika Anda ingin memperoleh balasan dari tim. Kami juga mengumpulkan beberapa informasi dasar secara otomatis sehingga kami dapat memahami masukan yang Anda berikan. Untuk mengetahui data apa saja yang kami kumpulkan, Anda dapat membaca butir 2 di atas di bagian "Informasi yang kami peroleh secara otomatis". Pelajari lebih lanjut praktik keamanan dan privasi Outline [di sini](/about/security-and-privacy).

 Jika Anda menggunakan aplikasi Outline versi beta di Android, kami dapat menggunakan layanan [Firebase](https://firebase.google.com/) milik Google untuk mengumpulkan informasi proses debug yang dapat membantu kami mendeteksi masalah dan menyempurnakan Outline. Anda dapat mempelajari kebijakan privasi dan keamanan Firebase lebih lanjut dari website: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Jika Anda tidak ingin Outline mengirimkan informasi ini melalui Firebase, gunakan versi produksi aplikasi.

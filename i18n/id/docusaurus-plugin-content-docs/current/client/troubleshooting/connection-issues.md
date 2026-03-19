---
title: "Mengapa saya tidak dapat terhubung ke layanan Outline?"
sidebar_label: "Mengapa saya tidak dapat terhubung ke layanan Outline?"
---

Ada beberapa kemungkinan alasan Anda tidak dapat terhubung ke layanan Outline:

- **Perangkat Anda**[**terputus dari internet**](#Internetissues)**.**Terkadang perangkat akan mengalami gangguan pada koneksi jaringan dan mungkin perlu beberapa saat untuk memperbarui ikon jaringan. Mungkin juga bahwa perangkat Anda terhubung ke jaringan lokal, tetapi internet sedang tidak aktif.
- **Firewall**[**jaringan Anda memblokir akses**](#FirewallIssues)**ke server Outline.**Hal ini umum terjadi jika Anda menggunakan jaringan publik, seperti jaringan nirkabel gratis, kantor, atau sekolah.
- **Perangkat Anda memiliki**[**software antivirus atau firewall**](#SoftwareIssues)**yang memblokir akses ke server Outline Anda.**
- **Your**[**Setelan perangkat ponsel**](#DeviceSettings) Anda**mungkin perlu diubah.**
- **Pengelola layanan mungkin telah**[**menghapus server atau ISP Anda mungkin memblokir permintaan Anda**](#ServerIssues) .

## Masalah koneksi internet: {#Internetissues}

### Cara mengujinya:

Nonaktifkan Outline dan lihat apakah koneksi internet telah pulih.

- Jika ya, lihat opsi pemecahan masalah lainnya di bawah.
- Jika tidak, tunggu beberapa saat untuk melihat apakah setelan koneksi Anda diperbarui secara otomatis.

### Cara memperbaikinya:

Hubungkan kembali perangkat Anda ke internet:

1. Periksa perangkat lain untuk melihat apakah perangkat dapat tersambung ke jaringan yang sama. Jika perangkat lain tidak dapat terhubung ke internet, jaringan mungkin sedang tidak aktif dan Anda harus menunggu hingga aktif kembali atau pecahkan masalahnya.
2. Jika perangkat lain dapat terhubung ke jaringan yang sama, Anda dapat mencoba satu atau beberapa tindakan berikut untuk menghubungkan kembali ke internet:
   1. Aktifkan mode pesawat (seluler) pada perangkat
   2. Mulai ulang perangkat
   3. Matikan perangkat, lalu tunggu selama 2 menit dan nyalakan kembali perangkat

## Masalah firewall jaringan: {#FirewallIssues}

### Cara mengujinya:

1. Putuskan koneksi dari jaringan kabel atau Wi-Fi saat ini.
2. Hubungkan ke jaringan lain, seperti jaringan seluler
3. Coba hubungkan kembali ke server Outline

Jika Anda dapat terhubung saat menggunakan jaringan lain, berarti masalahnya ada pada jaringan Anda.

### Cara memperbaikinya:

Hubungi pengelola layanan dan minta mereka untuk mengizinkan akses ke server Outline, atau tetap gunakan jaringan lain.

## Masalah software antivirus atau firewall: {#SoftwareIssues}
### Cara mengujinya:
 Coba hubungkan ke Outline dari perangkat lain.

Catatan: Perlu diingat bahwa Anda memerlukan kunci akses dan aplikasi Outline untuk menggunakan Outline di perangkat lain.

### Cara memperbaikinya:
Periksa setelan software antivirus atau firewall Anda untuk memastikan keduanya disetel untuk mengizinkan traffic VPN dan Outline.

## Setelan perangkat: {#DeviceSettings}

## Cara memeriksanya: {#ServerIssues}
Untuk Android:

1. Buka Aplikasi Setelan.
2. Cari **setelan VPN** di perangkat Anda. (Setelan VPN akan menampilkan semua aplikasi VPN yang saat ini memiliki akses di ponsel Anda).
3. Jika Anda tidak melihat Outline di setelan VPN, uninstal dan instal ulang Outline. Setelah diinstal, Outline akan otomatis diberi akses oleh perangkat.

Pastikan Anda tidak memiliki aplikasi overlay layar yang diinstal di perangkat Android. Hal ini karena aplikasi tersebut mungkin mengalihkan jendela izin Outline ke latar belakang sehingga tidak terlihat di latar depan.

 Di perangkat Android, buka Setelan > Aplikasi > Akses aplikasi khusus. Kemudian ketuk ‘Tampilkan di aplikasi lain’. Anda dapat menghapus akses ke semua aplikasi yang mengizinkan perilaku ini.

 Untuk iOS: Baca [artikel dukungan ini](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

### Masalah server:

### Cara mengujinya:
Jika Anda memiliki akses ke lebih dari satu server, coba hubungkan ke server lainnya.

### Cara memperbaikinya:

Hubungi pengelola layanan untuk mengetahui apakah server telah dihapus. Jika ya, minta mereka untuk memberikan [kunci akses](/about/terminology) ke server lain.

Jika Anda menyiapkan server, coba hubungkan ke server tersebut melalui Outline Manager atau metode lain seperti [SSH](https://en.wikipedia.org/wiki/Secure_Shell). Jika tidak berhasil, coba periksa konsol penyedia cloud (jika ada) untuk mengetahui apakah server masih terhubung ke internet.

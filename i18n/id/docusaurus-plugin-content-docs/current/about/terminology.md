---
title: Terminologi
sidebar_label: Terminologi
---

**Apa itu VPN?**

 Virtual private network (VPN) adalah koneksi pribadi antara perangkat Anda dengan server host. Saat menggunakan VPN, traffic Anda akan disembunyikan dari penyedia internet. Anda mungkin perlu menggunakan VPN dalam skenario berikut:

- Melindungi data Anda saat menggunakan jaringan Wi-Fi publik
- Menjaga kerahasiaan data penjelajahan Anda dari penyedia internet dan lembaga pemerintah
- Mengakses konten yang tidak disensor dari berbagai sumber di seluruh dunia

**Apa perbedaan Outline dengan VPN tradisional?**

 Penyedia internet dapat dengan mudah mendeteksi dan memblokir VPN tradisional dengan mengenali protokol keamanan umum dan/atau pola volume traffic. Outline lebih tangguh daripada VPN tradisional karena dibuat menggunakan satu protokol yang dirancang agar sulit dideteksi, yang membuatnya lebih sulit diblokir. Outline tahan terhadap berbagai penyensoran yang canggih, termasuk pemblokiran berbasis jaringan dan pemblokiran IP.

**Apa itu server Outline?**

 Server Outline menjalankan VPN yang akan dihubungkan ke pengguna yang diizinkan. Jika membuat jaringan baru, Anda dapat menggunakan server aman Anda sendiri sebagai server Outline, jika ada. Atau, Anda dapat menggunakan penyedia layanan cloud seperti:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Anda dapat menyiapkan server Anda di Outline Manager.

**Apa itu pengelola layanan?**

 Pengelola layanan adalah orang yang bertanggung jawab untuk menyiapkan server Outline dan membagikan kunci akses kepada pengguna. Pengelola layanan umumnya bertanggung jawab atas biaya penggunaan server. 

**Apa itu kunci akses?**

 Kunci akses digunakan untuk mengakses server Outline yang ada dan menghubungkan ke VPN. Seorang [pengelola layanan](#servicemanager) akan memberi Anda kunci akses, atau Anda dapat [menyiapkan server Outline](/manager/server-setup/setup-server) sendiri. Berikut adalah contoh tampilan kunci akses (hanya contoh; tidak akan berfungsi): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

**Apa itu Outline Manager?**

 Outline Manager adalah aplikasi desktop yang memungkinkan pengelola layanan menyiapkan server Outline, menghasilkan [kunci akses](#accesskey), dan menetapkan batas penggunaan data per kunci. Anda dapat mendownload Outline Manager versi terbaru [di sini](https://getoutline.org/get-started/#step-3) atau [di sini](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Apa itu Aplikasi Outline?**

 Aplikasi Outline adalah aplikasi yang tersedia untuk desktop dan seluler, yang memungkinkan Anda untuk terhubung ke server Outline dan mengakses VPN menggunakan kunci akses. Anda dapat mendownload Aplikasi Outline versi terbaru [di sini](https://getoutline.org/get-started/#step-3) atau [di sini](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Apa itu batas data?**

 Outline Manager memungkinkan pengelola layanan menetapkan pemantauan batas data 30 hari pada kunci akses untuk mencegah penggunaan yang berlebihan dan membantu menjaga agar biaya tetap dapat diprediksi. Pengelola layanan dapat menetapkan batas default yang berlaku untuk setiap kunci, dan juga menetapkan batas yang berbeda pada setiap kunci untuk menggantikan batas default. Setelah ditetapkan, batas tersebut langsung berlaku dan diterapkan setiap jam.

Jika pengelola layanan memilih untuk membagikan metrik kepada Jigsaw, mereka harus membaca [kebijakan pengumpulan data](/about/data-collection) untuk mengetahui detail tentang bagaimana penggunaan batas data akan dilaporkan.

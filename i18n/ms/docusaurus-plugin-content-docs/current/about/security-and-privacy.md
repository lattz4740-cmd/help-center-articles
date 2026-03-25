---
title: Keselamatan dan privasi semasa menggunakan Outline
sidebar_label: Keselamatan dan privasi semasa menggunakan Outline
---

Keselamatan dan privasi semasa menggunakan Outline

## Cara Outline melindungi komunikasi dalam talian anda

Trafik Internet paling rentan kepada perisikan semasa bergerak menerusi rangkaian setempat atau nasional anda.

Outline memastikan komunikasi anda peribadi dengan menyulitkan trafik Internet anda semasa bergerak dalam rangkaian nasional anda dan memastikan trafik itu disulitkan sehingga tiba kepada pelayan Outline. Apabila trafik disulitkan dengan Outline, pemerhati rangkaian tidak dapat memeriksa laman web yang anda lawati atau maklumat yang sedang anda pindahkan.

Outline juga boleh membantu anda memulihkan akses untuk melindungi alatan komunikasi menyeluruh yang mungkin tidak boleh diakses di negara anda.

## Standard penyulitan

Outline menyulitkan komunikasi antara peranti anda dengan Pelayan Outline menggunakan sifer AEAD 256-bit Chacha2020 IETF Poly 1305. Sifer AEAD menawarkan kerahsiaan, integriti dan ketulenan dan mempamerkan prestasi yang cemerlang pada perkakasan moden.

## Audit keselamatan

Pada tahun 2018, Outline telah diaudit oleh Radically Open Security dan Cure53, dua organisasi keselamatan digital bebas yang menyemak perisian berbanding dengan standard keselamatan yang terkini. Radically Open Security menjalankan audit tambahan pada tahun 2022 dan Cure53 menjalankan audit Outline SDK pada tahun 2024. Anda boleh membaca laporan di sini:

- [Laporan Ujian Penyusupan Radically Open Security (Mac 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53 Pentest & Laporan Audit Jigsaw Outline (Disember 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Laporan Ujian Penyusupan Radically Open Security (Disember 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [SDK VPN Outline Jigsaw Laporan Ujian Penembusan Cure53 (Januari 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Metrik dan log awanama

Outline menjejaki lebar jalur yang digunakan, sebagai "bait yang dipindahkan" bagi setiap kunci akses. Maklumat ini membolehkan pentadbir pelayan untuk melaraskan langganan lebar jalur mereka dengan penyedia pelayan mereka mengikut keperluan tetapi tidak membolehkan mereka melihat maklumat sebenar yang melalui pelayan Outline tersebut.

Ketahui [pengumpulan data dan maklumat Outline](https://getoutline.org/policies/data-collection) dengan lebih lanjut.

---

## Soalan Lazim keselamatan dan privasi

## Bolehkah Outline membuatkan saya awanama dalam talian?

Tidak, Outline bukan alat untuk memberikan keawanamaan. Outline melindungi privasi anda daripada penonton rangkaian potensi.

Outline tidak menawarkan keawanamaan penuh pada laman web yang anda lawati, disebabkan oleh laman tersebut masih boleh mengenal pasti anda apabila anda log masuk dan kadangkala menerusi teknik, seperti pengambilan cap jari penyemak imbas. Untuk apl mudah alih, kebanyakan telefon pintar moden memiliki API yang membolehkan apl yang dipasang untuk mendapatkan kembali lokasi anda bebas daripada proksi anda disebabkan oleh API ini boleh bergantung kepada GPS yang dibenamkan.

Secara umumnya, VPN menawarkan perlindungan penting, khususnya daripada perisikan Internet tetapi sentiasa terdapat risiko untuk beroperasi dalam talian. Meskipun dengan VPN, jika ISP sudah mengetahui identiti anda dan dapat memerhatikan trafik rangkaian anda, ISP ini mungkin boleh menentukan alamat IP pelayan Outline anda. Maklumat ini boleh digunakan untuk menyekat akses kepada pelayan Outline atau mempelajari pola penggunaan, seperti masa anda lazimnya dalam talian dan kemungkinan lokasi kasar anda.

## Bolehkah seseorang mengetahui sama ada saya menggunakan Outline atau tidak?

Berkemungkinan boleh. Platform dan perkhidmatan yang anda akses berkemungkinan besar dapat mengetahui bahawa sambungan anda datang daripada pelayan awan. Kadangkala, mereka boleh menyimpulkan bahawa anda menggunakan VPN tetapi mereka tidak dapat melihat kandungan trafik Internet anda.

## Adakah Outline melindungi saya daripada semua kemungkinan serangan siber?

Tidak. Tiada alat tunggal yang akan melindungi anda daripada kesemua kemungkinan ancaman siber. Outline memberi anda akses kepada Internet terbuka dan meningkatkan privasi anda dengan menyulitkan trafik anda tetapi kami mengesyorkan agar anda mengambil langkah berjaga-jaga tambahan bagi melindungi diri anda daripada serangan, seperti perisian hasad dan pancingan data.

Untuk mengukuhkan pertahanan dalam talian anda, sila pertimbangkan untuk bekerjasama dengan pakar keselamatan siber organisasi anda. Secara alternatif, anda boleh memperoleh panduan yang diperibadikan daripada pakar keselamatan terkemuka pada [https://securityplanner.org/](https://securityplanner.org/)Security Planner, sebuah laman web yang dibina untuk menyediakan arahan yang jelas untuk anda tentang pemilihan alatan keselamatan siber yang betul bagi menangani kebimbangan anda.

Anda juga boleh melihat produk keselamatan siber lain daripada [Jigsaw](https://jigsaw.google.com/), seperti [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) dan [Amaran Kata Laluan](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Adakah penggunaan VPN sah di sisi undang-undang?

Sila semak undang-undang, peraturan dan Syarat Perkhidmatan setempat untuk penyedia awan yang mahu anda gunakan sebelum mengendalikan Outline atau menggunakan apl ini.

---
title: "Bagaimana cara menetapkan batas data di kunci akses?"
sidebar_label: "Bagaimana cara menetapkan batas data di kunci akses?"
---

Anda dapat menetapkan batas data yang akan berlaku ke semua kunci akses. Untuk menetapkan batas, buka Outline Manager, lalu pilih Setelan. Dari sana, Anda akan melihat tombol Batas data yang dapat digunakan untuk menetapkan batas jika diaktifkan.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Setelah menetapkan batas, Anda dapat melihat seberapa dekat pengguna mencapai batas di halaman kunci akses, yang menampilkan grafik batang penggunaan data dalam 30 hari terakhir.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Selain menetapkan batas untuk semua kunci akses, Anda dapat memberi setiap kunci batas datanya masing-masing. Setelan ini akan mengganti batas data default apa pun yang pernah Anda tetapkan. Namun, jika belum menetapkan batas data default, Anda masih bisa menetapkan batas data untuk kunci mana pun. 

 Untuk menetapkan batas transfer data kunci, buka Outline Manager, lalu pilih tab Koneksi berisi kunci yang ingin Anda tetapkan, lalu klik menu di sebelah kanan baris kunci. Dari sana, klik Batas Data. Untuk mengubah batas data di "Kunci akses saya", klik ikon Batas Data ![Ikon batas data](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Pilih Tetapkan batas data kustom. Setelah Anda memilih kotak centang ini, kolom akan muncul tempat Anda dapat menetapkan batas data kustom untuk kunci tersebut. Klik tombol SIMPAN jika Anda sudah selesai untuk menyimpan batas data.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Setelah Anda menyimpan batas transfer data untuk kunci yang dipilih, batas ini akan ditampilkan di layar utama, beserta penggunaan data (selama 30 hari terakhir) untuk setiap kunci.

Untuk menghapus batas data dari kunci akses, buka dialog Batas Data kunci seperti sebelumnya, hapus centang pada kotak berlabel Tetapkan batas data kustom, lalu klik tombol SIMPAN.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

## **FAQ Batas Data**
## **Apa yang dimaksud dengan pemantauan batas data 30 hari?**
 Pemantauan batas data 30 hari akan menghitung jumlah penggunaan data setiap kunci selama 30 hari terakhir dan menjaga agar penggunaan setiap kunci dalam periode tersebut tidak melampaui batas. Dengan demikian, kunci tidak dapat melampaui batas dalam rentang waktu 30 hari, termasuk pada bulan yang memiliki 30 hari atau kurang. Intinya, setiap data pengguna yang tersedia akan meningkat setiap hari berdasarkan jumlah data yang mereka gunakan 31 hari yang lalu.

## Mengapa Outline menggunakan pemantauan batas data?
 Pemantauan batas data memberikan jaminan untuk setiap periode 30 hari. Artinya, pemantauan batas data akan lebih mudah dikonfigurasi daripada batas berulang (misalnya hari yang dapat disesuaikan dalam setiap bulan) dengan memberikan jaminan yang serupa. Batas ini juga cocok dengan tampilan penggunaan data Outline yang ada, serta alat umum, seperti layanan analisis dan statistik server.

## Data apa yang dihitung dalam batas data?
 Setiap traffic kunci akses yang keluar dari server akan disertakan dalam penghitungan. Dengan kata lain, ini berarti data yang dikirim atas nama kunci ke luar server, serta data yang dikirimkan kembali kepada klien. Data ini semestinya sesuai dengan traffic yang dikirim dari kunci ke server dan yang dikirimkan kembali. Kami harap penghitungan ini akan sesuai dengan penghitungan pengguna Anda. Kami memilih traffic keluar karena traffic tersebut adalah apa yang dibayarkan oleh penyedia cloud yang kami survei.

## Apakah pengguna akan mendapatkan notifikasi jika telah melampaui batas data mereka?
 Tidak pada saat ini. Banyak penyedia cloud menyertakan batas seperti 1 TB untuk satu bulan penuh. Jumlah ini dapat mendukung 10 pengguna dengan 100 GB atau 100 pengguna dengan 10 GB. Jumlah ini cukup besar dan kami tidak mengantisipasi banyak pengguna akan mencapai batas tersebut. Kami berharap pengguna akan menghubungi pengelola server saat mereka telah mencapai batas. Namun, kami menghargai masukan Anda tentang bagaimana notifikasi dapat membantu dalam kasus penggunaan Anda, dan Anda dapat menghubungi kami[/about/feedback](/about/feedback)di sini.

## Apakah pengguna akan mendapatkan notifikasi jika mendekati batas data mereka?
 Jumlah data baru yang diterima oleh pengguna yang mendekati batas akan berbeda dari hari ke hari karena didasarkan pada penggunaannya 30 hari yang lalu. Menurut kami, hal ini dapat membingungkan pengguna akhir, bukan membantu mereka. Kami menghargai masukan Anda tentang perilaku ini [di sini](/about/feedback).

## Dapatkah saya mereset penggunaan data pengguna?
 Tidak, batas pengguna selalu menyertakan penggunaan data selama 30 hari terakhir. Namun, Anda dapat meningkatkan batas data kunci mereka atau membuat kunci baru untuk mereka.

## Mengapa beberapa pengguna saya kehilangan akses setelah saya mengaktifkan batas data?
 Batas data dihitung berdasarkan transfer data pengguna 30 hari sebelumnya, yang dicatat terlepas dari aktif tidaknya batas data. Terdapat kemungkinan bahwa pengguna yang dimaksud telah melampaui batas sebelum batas tersebut diberlakukan. Selain itu, perhatikan bahwa semua batas data selalu diterapkan, bahkan saat mengubah batas data di satu kunci.

## Dapatkah saya menetapkan batas di seluruh server, seperti “1 TB per 30 hari”?
 Tidak untuk saat ini. Kami ingin mendengar lebih lanjut tentang kasus penggunaan Anda [di sini](/about/feedback).

## Jika terdapat batas data default dan batas data di kunci tertentu, manakah yang akan diterapkan?
 Batas data tertentu akan mengganti batas data default apa pun (jika ada) yang telah Anda tetapkan.

## Dapatkah saya menetapkan batas data untuk kunci tertentu tanpa perlu menetapkan batas data default?
 Ya. Anda tidak perlu memiliki batas default untuk menetapkan batas data di satu kunci. Misalnya, Anda dapat menetapkan batas di satu kunci yang menurut Anda mungkin bisa diterapkan secara luas untuk melindungi diri Anda dari transfer data berlebih melalui kunci tersebut.

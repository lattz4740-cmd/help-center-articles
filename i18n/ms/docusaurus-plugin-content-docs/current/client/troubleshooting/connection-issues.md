---
title: "Mengapakah saya tidak dapat menyambung kepada perkhidmatan Outline?"
sidebar_label: "Mengapakah saya tidak dapat menyambung kepada perkhidmatan Outline?"
---

Terdapat beberapa sebab anda mungkin tidak dapat menyambung kepada perkhidmatan Outline:

- **Peranti anda**/client/troubleshooting/connection-issues#One[**terputus sambungan daripada Internet**](#Internetissues)[#MasalahInternet](#Internetissues)**.**Kadangkala peranti anda akan terputus sambungan rangkaian dan mungkin mengambil sedikit masa untuk peranti anda mengemaskinikan ikon rangkaian tersebut. Terdapat juga kemungkinan peranti anda disambungkan kepada rangkaian setempat tetapi Internet tergendala.
- [**Tembok api rangkaian anda menyekat akses**](#FirewallIssues)[#MasalahTembokApi](#FirewallIssues)**[kepada](#FirewallIssues) pelayan Outline anda.**Perkara ini biasa terjadi jika anda menggunakan rangkaian awam, seperti sekolah, kerja atau rangkaian wayarles percuma.
- **Peranti anda memiliki**/client/troubleshooting/connection-issues#Three[**tembok api atau perisian antivirus**](#SoftwareIssues)[#MasalahPerisian](#SoftwareIssues)**yang menyekat akses kepada pelayan Outline anda.**
- **Your**[**Tetapan peranti telefon anda**](#DeviceSettings)**mungkin perlu ditukar.**
- **Pengurus perkhidmatan anda mungkin telah**[**memusnahkan pelayan atau ISP anda mungkin menyekat permintaan anda**](#ServerIssues) .

## Masalah sambungan Internet: {#Internetissues}

## Cara menguji:

Matikan Outline dan lihat sama ada sambungan kepada Internet dipulihkan.

- Jika ya, lihat lebih banyak pilihan penyelesaian masalah di bawah.
- Jika tidak, tunggu sebentar untuk melihat sama ada tetapan sambungan anda dikemaskinikan dengan sendiri.

## Perkara yang perlu dibetulkan:

Dapatkan sambungan Internet untuk peranti anda:

1. Semak peranti lain untuk melihat sama ada peranti tersebut boleh bersambung kepada rangkaian yang sama. Jika peranti lain tidak dapat menyambung kepada Internet, rangkaian mungkin tergendala dan anda perlu menunggu sehingga rangkaian tersebut kembali pulih atau menyelesaikan masalah tersebut.
2. Jika peranti lain dapat menyambung kepada rangkaian yang sama, anda boleh mencuba beberapa langkah yang berikut untuk kembali menyambung kepada Internet:
   1. Letakkan peranti dalam mod pesawat (peranti mudah alih)
   2. Mulakan semula peranti
   3. Matikan peranti, tunggu 2 minit, hidupkan kembali peranti

## Masalah tembok api rangkaian: {#FirewallIssues}

## Cara menguji:

1. Putuskan sambungan daripada Wi-Fi atau rangkaian berwayar semasa anda.
2. Buat sambungan kepada rangkaian yang berbeza, seperti rangkaian selular
3. Cuba sambungkan semula kepada pelayan Outline

Jika anda dapat membuat sambungan semasa berada pada rangkaian lain, maka akses anda bermasalah.

## Perkara yang perlu dibetulkan:

Hubungi pentadbir perkhidmatan dan minta mereka membenarkan akses kepada pelayan Outline anda atau terus gunakan rangkaian yang lain itu.

## Masalah tembok api atau perisian antivirus:
## Cara menguji:
 Cuba menyambung kepada Outline daripada peranti yang lain.

Nota: Ingat bahawa anda memerlukan kunci akses dan apl Outline untuk menggunakan Outline pada peranti yang lain.

## Perkara yang perlu dibetulkan: {#SoftwareIssues}
Semak tetapan tembok api atau perisian antivirus untuk memastikan tembok api dan antivirus ditetapkan supaya membenarkan laluan trafik VPN dan Outline.

## Tetapan peranti: {#DeviceSettings}

## Perkara yang perlu disemak: {#DeviceSettings}
Untuk Android:

1. Buka Apl Tetapan.
2. Cari **tetapan VPN** pada peranti anda. (Tetapan VPN akan menunjukkan kepada anda semua apl VPN yang memiliki akses kepada telefon anda pada masa ini.)
3. Jika anda tidak melihat Outline pada tetapan VPN tersebut, nyahpasang Outline dan pasang semula. Outline mestilah diberi akses secara automatik oleh peranti sebaik sahaja dipasang.

Pastikan anda tiada apa-apa aplikasi tindanan skrin yang dipasang pada peranti Android anda kerana hal ini mungkin menghantar tetingkap kebenaran Outline kepada latar yang tidak dapat dilihat dalam latar depan.

 Pada peranti Android anda, akses Tetapan > Apl > Akses apl khas. Kemudian ketik ‘Paparkan di atas apl yang lain’. Anda boleh mengalih keluar akses kepada mana-mana apl yang membenarkan gelagat ini.

 Untuk iOS: Baca[artikel sokongan ini](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

## Masalah pelayan: {#ServerIssues}

## Cara menguji: {#ServerIssues}
Jika anda mempunyai akses kepada lebih daripada satu pelayan, cuba menyambung kepada pelayan yang lain.

## Perkara yang perlu dibetulkan:

Hubungi pentadbir perkhidmatan anda untuk melihat sama ada pelayan telah dimusnahkan atau tidak. Jika demikian, minta[kunci akses](/about/terminology) kepada pelayan yang lain daripada mereka.

Jika anda menyediakan pelayan, cuba menyambung kepada pelayan ini melalui Outline Manager atau gunakan kaedah lain seperti[SSH](https://en.wikipedia.org/wiki/Secure_Shell). Jika langkah tersebut tidak berfungsi, anda boleh cuba memeriksa konsol penyedia awan, jika ada, untuk melihat sama ada pelayan itu masih dalam talian.

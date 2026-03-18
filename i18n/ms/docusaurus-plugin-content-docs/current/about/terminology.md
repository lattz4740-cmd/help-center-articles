---
title: Istilah
sidebar_label: Istilah
---

**Apakah itu VPN?**

 Rangkaian peribadi maya (VPN) ialah sambungan persendirian antara peranti anda dengan pelayan hos. Apabila anda menggunakan VPN, trafik anda tersembunyi daripada penyedia Internet. Anda mungkin perlu menggunakan VPN dalam senario yang berikut:

- Melindungi data anda apabila menggunakan rangkaian Wi-Fi awam
- Memastikan data semakan imbas anda dirahsiakan daripada penyedia Internet dan agensi kerajaan
- Mengakses kandungan yang tidak ditapis daripada pelbagai sumber di seluruh dunia

**Apakah perbezaan Outline berbanding dengan VPN tradisional?**

 Penyedia Internet boleh mengesan dan menyekat VPN tradisional dengan mudah melalui pengecaman protokol keselamatan biasa dan/atau corak jumlah trafik. Outline lebih bingkas berbanding dengan VPN tradisional kerana perisian ini dibina menggunakan protokol yang direka bentuk agar sukar untuk dikesan dan dengan itu, lebih sukar untuk disekat. Outline mampu mengatasi bentuk penapisan yang canggih termasuk sekatan berasaskan rangkaian dan sekatan IP.

**Apakah itu pelayan Outline?**

 Pelayan Outline menjalankan VPN yang akan disambungkan kepada pengguna yang dibenarkan. Jika anda membuat rangkaian baharu, anda boleh menggunakan pelayan selamat anda sebagai pelayan Outline jika anda mempunyai pelayan tersebut atau anda boleh menggunakan penyedia perkhidmatan awan seperti:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Anda akan menyediakan pelayan anda dalam Outline Manager.

## Apakah itu pengurus perkhidmatan? {#servicemanager}
 Pengurus perkhidmatan ialah orang yang bertanggungjawab untuk menyediakan pelayan Outline dan berkongsi kunci akses dengan pengguna. Pengurus perkhidmatan biasanya bertanggungjawab terhadap kos penggunaan pelayan. 

## Apakah itu kunci akses? {#accesskey}
 Kunci akses digunakan untuk mengakses pelayan Outline yang sedia ada dan membuat sambungan kepada VPN. [Pengurus perkhidmatan](#servicemanager) akan memberi anda kunci akses atau anda boleh[menyediakan pelayan Outline](/manager/server-setup/setup-server) sendiri. Yang berikut ialah contoh rupa kunci akses (sampel sahaja; kunci ini tidak akan berfungsi): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

**Apakah itu Outline Manager?**

 Outline Manager ialah aplikasi desktop yang membolehkan pengurus perkhidmatan menyediakan pelayan Outline, menjana [kunci akses](#accesskey) dan menetapkan had data untuk penggunaan setiap kunci. Anda boleh memuat turun versi terkini Outline Manager[di sini](https://getoutline.org/get-started/#step-3) atau[di sini](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Apakah itu Outline Client?**

 Outline Client ialah aplikasi yang tersedia untuk desktop dan mudah alih, yang membolehkan anda membuat sambungan kepada pelayan Outline dan mengakses VPN menggunakan kunci akses. Anda boleh memuat turun versi terkini Outline Client[di sini](https://getoutline.org/get-started/#step-3) atau[di sini](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Apakah itu had data?**

 Outline Manager membolehkan pengurus perkhidmatan menetapkan had data belakang 30 hari pada kunci akses untuk mengelakkan penggunaan berlebihan dan memastikan kos boleh diramalkan. Pengurus pelayan boleh menetapkan had lalai yang digunakan pada setiap kunci dan juga menetapkan had berlainan pada sebarang kunci untuk menggantikan had lalai. Setelah had ditetapkan, had tersebut akan berkuat kuasa dengan serta-merta dan dikuatkuasakan setiap jam.

Jika pengurus perkhidmatan ikut serta untuk berkongsi metrik dengan Jigsaw, mereka perlu melihat[dasar pengumpulan data](/about/data-collection) untuk mendapatkan butiran tentang cara penggunaan had data akan dilaporkan.

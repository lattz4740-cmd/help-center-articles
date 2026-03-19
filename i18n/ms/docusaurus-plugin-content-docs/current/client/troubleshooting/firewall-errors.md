---
title: Ralat tembok api
sidebar_label: Ralat tembok api
---

Terdapat tiga jenis masalah tembok api yang mungkin anda temukan:

## Anda mungkin disekat oleh tembok api rangkaian.

Jika anda sedang cuba memasang Outline semasa disambungkan kepada rangkaian bertembok api, seperti di sekolah atau di tempat kerja anda, cuba buat pemasangan semasa berada pada rangkaian yang berbeza.

Jika langkah ini tidak berjaya, sila hubungi pentadbir rangkaian anda untuk membolehkan sambungan antara rangkaian bertembok api tersebut dengan pelayan Outline anda. Anda perlu mengetahui alamat IP pelayan Outline anda dan port tempat Outline dijalankan, yang ditunjukkan pada penghujung skrip pemasangan.

## Anda mungkin disekat oleh tembok api peranti.

Jika anda mempunyai perisian pada peranti anda yang menyekat sambungan keluar pada port tidak standard atau perisian yang tidak dikenali, (ZoneAlarm CheckPoint), sila rujuk dokumentasi peranti atau perisian anda untuk mengetahui cara membuat pengecualian bagi Outline.

## Anda mungkin disekat oleh tembok api pelayan.

Penyedia awan pilihan anda mungkin menghendaki anda membuat pengecualian secara manual kepada tembok api pelayan anda untuk membuka port yang digunakan untuk menjalankan Outline. Setelah anda menjalankan skrip pemasangan, anda hendaklah telah ditunjukkan dua port yang dipilih secara rawak tempat Outline berjalan pada pelayan anda. Pembukaan kedua-dua port ini sepatutnya memadai.

 Untuk membuat pengecualian kepada tembok api Pelayan anda, kami mengesyorkan supaya anda melihat pada dokumentasi untuk 'ufw' dan 'iptables':

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

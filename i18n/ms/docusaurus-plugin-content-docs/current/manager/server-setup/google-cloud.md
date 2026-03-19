---
title: Persediaan Automatik Google Cloud
sidebar_label: Persediaan Automatik Google Cloud
---

## Ikhtisar

Outline Manager menyertakan ciri yang membolehkan anda mengkonfigurasikan Pelayan Outline secara automatik pada pelayan yang dijalankan pada Google Cloud. Jika anda memilih untuk menggunakan ciri ini, Outline Manager akan meminta anda log masuk dengan Google Account anda, yang akan memberikan kebenaran [OAuth](https://developers.google.com/identity/protocols/oauth2) tertentu kepada pemasangan setempat Outline Manager anda bagi tujuan mengkonfigurasikan Akaun Google Cloud anda.
Jika anda tidak mahu memberikan kebenaran ini, anda boleh mengikut arahan persediaan lanjutan dalam Outline Manager untuk menjalankan Outline pada Google Cloud Platform.

## Kebenaran Diberikan

Untuk menyediakan persediaan automatik, Outline Manager memerlukan kebenaran yang berikut daripada Google Account anda.

## Google Cloud Platform

- Melihat dan mengurus sumber Enjin Kiraan Google anda
- Melihat data anda merentas perkhidmatan Google Cloud dan melihat alamat e-mel Google Account anda

## Maklumat akaun asas

- Melihat alamat e-mel Google Account utama anda
- Mengaitkan diri anda dengan maklumat peribadi anda pada Google

## Akses tambahan

- Mengurus projek Platform Cloud anda
- Melihat dan mengurus akaun pengebilan Google Cloud Platform anda
- Mengurus konfigurasi perkhidmatan Google API anda

Kebenaran ini membolehkan kami menyokong kefungsian lanjutan untuk mengurus pelayan Outline anda termasuk:

- Membolehkan anda memilih akaun pengebilan yang betul
- Membuat projek yang baharu untuk mengatur pelayan Outline anda
- Menyenaraikan pusat data yang tersedia
- Membuat mesin maya baharu untuk menjalankan Outline
- Mengkonfigurasikan mesin maya baharu dengan Outline

## Membatalkan Kebenaran

Anda boleh membatalkan akses kepada Google Cloud Platform bagi Outline Manager dengan melawati [Akaun saya](https://myaccount.google.com/permissions). Jika anda membatalkan akses, mana-mana pelayan yang telah anda buat dengan langkah automatik ini akan kekal berjalan tetapi tidak akan dipaparkan lagi dalam Outline Manager. Untuk memulihkan akses kepada pelayan ini, sambungkan semula kepada Google Cloud Platform dengan memulakan aliran persediaan automatik.

## Organisasi Projek Outline

Persediaan automatik Google Cloud menggunakan satu [projek Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects) untuk mengatur pelayan Outline anda. Projek ini dibuat semasa penggunaan persediaan automatik pertama, dengan ID projek yang dicadangkan yang bermula dengan “Outline-” diikuti dengan rentetan aksara rawak. Anda boleh memilih ID projek yang lain semasa pembuatan jika anda mahu. Projek ini akan dinamakan sebagai “Pelayan Outline”.

## Akaun Pengebilan

Projek Google Cloud memerlukan “akaun pengebilan” yang dipautkan yang mentakrifkan maklumat pembayaran. Pertama kali anda menggunakan persediaan automatik Google Cloud anda akan diminta untuk menyediakan akaun pengebilan untuk dikaitkan dengan pelayan Outline anda. Kadangkala sesebuah pelayan akan berhenti berjalan disebabkan terdapat masalah dengan akaun pengebilan. Dalam keadaan ini, anda hendaklah log masuk ke [Konsol Google Cloud](https://console.cloud.google.com/getting-started), mencari projek Google Cloud yang dikaitkan dengan Outline (dinamakan sebagai “Pelayan Outline”) dan mengemaskinikan tetapan pengebilan.

## Memusnahkan Pelayan

Jika anda mahu memusnahkan pelayan yang anda buat menggunakan persediaan automatik, cara termudah berbuat demikian adalah daripada dalam Outline Manager. Walau bagaimanapun, jika anda mahu memusnahkan pelayan itu sendiri, anda boleh log masuk ke [Konsol Google Cloud](https://console.cloud.google.com/getting-started), mencari projek yang dibuat semasa persediaan awal (dinamakan sebagai “Pelayan Outline”) dan sama ada memadamkan sumber di sana atau mematikan projek tersebut.

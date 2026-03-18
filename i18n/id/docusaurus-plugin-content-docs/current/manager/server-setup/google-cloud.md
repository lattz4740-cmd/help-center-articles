---
title: Penyiapan Otomatis Google Cloud
sidebar_label: Penyiapan Otomatis Google Cloud
---

## Ringkasan

Outline Manager menyertakan fitur yang memungkinkan Anda mengonfigurasi Server Outline secara otomatis di server yang berjalan pada Google Cloud. Jika memilih untuk menggunakan fitur ini, Outline Manager akan meminta Anda login dengan Akun Google, yang akan memberikan izin [OAuth](https://developers.google.com/identity/protocols/oauth2) tertentu ke penginstalan lokal Outline Manager untuk mengonfigurasi Akun Google Cloud Anda.

 Jika tidak ingin memberikan izin ini, Anda dapat mengikuti petunjuk penyiapan lanjutan di Outline Manager untuk menjalankan Outline di Google Cloud Platform.

## Izin yang Diberikan

Untuk menyediakan penyiapan otomatis, Outline Manager memerlukan izin berikut dari Akun Google Anda.

## Google Cloud Platform

- Melihat dan mengelola resource Google Compute Engine Anda
- Melihat data Anda di semua layanan Google Cloud dan melihat alamat email Akun Google Anda

## Info akun dasar

- Melihat alamat email Akun Google utama Anda
- Mengaitkan Anda dengan info pribadi Anda di Google

## Akses tambahan

- Mengelola project Cloud Platform
- Melihat dan mengelola akun penagihan Google Cloud Platform Anda
- Mengelola konfigurasi layanan Google API Anda

Izin ini memungkinkan kami mendukung fungsi lanjutan untuk mengelola server Outline Anda, termasuk:

- Memungkinkan Anda memilih akun penagihan yang benar
- Membuat project baru untuk mengelola server Outline Anda
- Membuat daftar pusat data yang tersedia
- Membuat mesin virtual baru untuk menjalankan Outline
- Mengonfigurasi mesin virtual baru dengan Outline

## Mencabut Izin

Anda dapat mencabut akses ke Google Cloud Platform untuk Outline Manager dengan membuka [Akun Saya](https://myaccount.google.com/permissions). Jika Anda mencabut akses, server apa pun yang dibuat dengan penyiapan otomatis akan tetap berjalan, tetapi tidak akan muncul lagi di Outline Manager. Untuk memulihkan aksesnya, cukup hubungkan kembali ke Google Cloud Platform dengan memulai alur penyiapan otomatis.

## Pengelolaan Project Outline

Penyiapan otomatis Google Cloud menggunakan [project Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects) tunggal untuk mengelola server Outline Anda. Project dibuat selama penggunaan pertama penyiapan otomatis, dengan project ID yang disarankan yang diawali dengan “Outline-” dan diikuti string karakter acak. Anda dapat memilih project ID yang berbeda saat membuat project. Project akan diberi nama “Outline servers”.

## Akun Penagihan

Project Google Cloud memerlukan "akun penagihan" tertaut yang menjelaskan informasi pembayaran. Saat pertama kali menggunakan penyiapan otomatis Google Cloud, Anda akan diminta untuk memberikan akun penagihan yang akan dikaitkan dengan server Outline Anda. Terkadang server akan berhenti berjalan karena ada masalah dengan akun penagihan. Dalam hal ini, Anda harus login ke [Google Cloud Console](https://console.cloud.google.com/getting-started), lalu temukan project Google Cloud yang terkait dengan Outline (bernama “Outline servers”), dan perbarui setelan penagihan.

## Menghancurkan Server

Jika Anda ingin menghancurkan server yang dibuat menggunakan penyiapan otomatis, cara termudah untuk melakukannya adalah dari dalam Outline Manager. Namun, jika ingin menghancurkan server sendiri, Anda dapat login ke [Google Cloud Console](https://console.cloud.google.com/getting-started), lalu temukan project yang dibuat selama penyiapan awal (bernama “Outline servers”), dan hapus resource atau matikan project tersebut.

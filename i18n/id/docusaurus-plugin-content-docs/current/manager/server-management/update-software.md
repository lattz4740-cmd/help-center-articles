---
title: "Bagaimana cara mengupdate software server Outline?"
sidebar_label: "Bagaimana cara mengupdate software server Outline?"
---

Server Outline akan otomatis diupdate dengan peningkatan keamanan terbaru guna menghadirkan teknologi Outline terkini untuk Anda. Proses update otomatis ini diaktifkan oleh [Watchtower](https://github.com/containrrr/watchtower), yaitu library open source yang secara rutin memeriksa dan mengupdate image docker yang berisi software Outline.

Selain itu, jika Anda menginstal Outline menggunakan Outline Manager, kami akan menyiapkan cron job untuk otomatis mengupgrade software di server menggunakan [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) dan memulai ulang sistem jika diperlukan. Perhatikan bahwa proses ini tidak terjadi dalam Mode Lanjutan agar konfigurasi yang ada tidak berubah, dengan asumsi bahwa host digunakan untuk keperluan lain selain menjalankan Outline.

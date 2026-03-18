---
title: "Cum actualizez software-ul de server Outline?"
sidebar_label: "Cum actualizez software-ul de server Outline?"
---

Serverele Outline se actualizează automat incluzând cele mai recente măsuri de securitate îmbunătățite, astfel încât să rulați mereu cea mai recentă tehnologie Outline. Procesul automatizat de actualizare este activat de [Watchtower](https://github.com/v2tec/watchtower), o bibliotecă open-source care verifică regulat și actualizează imaginea Docker care conține software-ul Outline.

În plus, când instalați Outline folosind Outline Manager, vom configura o sarcină cron pentru a face upgrade automat la software pe server folosind [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) și pentru a reporni când este necesar. Rețineți că acest lucru nu se întâmplă în Modul avansat pentru a conserva configurația existentă, presupunând că gazda este folosită pentru alte scopuri pe lângă rularea Outline.

---
title: "Kako ažurirati softver Outline servera?"
sidebar_label: "Kako ažurirati softver Outline servera?"
---

Outline serveri se automatski ažuriraju najnovijim sigurnosnim poboljšanjima tako da će uvijek imati najnoviju tehnologiju Outlinea. Postupak automatskog ažuriranja se omogućava putem [Watchtowera](https://github.com/v2tec/watchtower), biblioteke otvorenog koda koja redovno provjerava i ažurira Docker sliku koja sadržava softver Outlinea.

Dodatno, kada instalirate Outline pomoću Outline Managera, postavit ćemo hronološki zadatak za automatsku nadogradnju softvera na serveru pomoću [Nadogradnji bez nadzora](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) i ponovno pokretanje po potrebi. Napominjemo da se ovo ne provodi u Naprednom načinu rada radi zadržavanja postojeće konfiguracije pod pretpostavkom da se host računar koristi u druge svrhe pored rada Outlinea.

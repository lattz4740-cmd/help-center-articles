---
title: "Kako mogu ažurirati svoj Outline poslužiteljski softver?"
sidebar_label: "Kako mogu ažurirati svoj Outline poslužiteljski softver?"
---

Outline poslužitelji automatski se ažuriraju pomoću najnovijih sigurnosnih poboljšanja tako da ćete uvijek imati najnoviju tehnologiju aplikacije Outline. Automatizirano ažuriranje omogućuje [Watchtower](https://github.com/containrrr/watchtower), biblioteka otvorenog izvornog koda koja redovito provjerava i ažurira Docker sliku koja sadrži softver Outlinea.

Nadalje, kada instalirate Outline pomoću Upravitelja Outlinea, postavljamo kronološki zadatak za automatsko ažuriranje softvera na poslužitelju pomoću značajke [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) i njegovo ponovno pokretanje kad je to potrebno. Do toga ne dolazi u naprednom načinu kako bi se sačuvala postojeća konfiguracija, uz pretpostavku da host osim za Outline služi i za druge namjene.

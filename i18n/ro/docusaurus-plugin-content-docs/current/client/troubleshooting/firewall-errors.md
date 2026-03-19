---
title: Erori de firewall
sidebar_label: Erori de firewall
---

Vă puteți confrunta cu trei tipuri de erori legate de firewall.

## Puteți fi blocat(ă) de un firewall al rețelei.

Dacă încercați să instalați Outline în timp ce sunteți conectat(ă) la o rețea cu firewall, de exemplu, la școală sau la locul de muncă, încercați să instalați când sunteți în altă rețea.

Dacă nu funcționează, contactați administratorul de rețea, solicitându-i să permită conexiunile între rețeaua cu firewall și serverul dvs. Outline. Trebuie să cunoașteți adresa IP a serverului dvs. Outline și porturile pe care rulează Outline, indicate la finalul scriptului de instalare.

## Puteți fi blocat(ă) de un firewall al dispozitivului.

Dacă aveți pe dispozitiv un software care blochează conexiunile de ieșire pe porturi care nu sunt standard sau un software nerecunoscut (ZoneAlarm de la CheckPoint), consultați documentația dispozitivului sau a software-ului pentru a afla cum puteți crea o excepție pentru Outline.

## Puteți fi blocat(ă) de un firewall al serverului.

Furnizorul serviciilor cloud pe care l-ați ales poate impune crearea manuală a excepțiilor pentru firewallul serverului pentru a deschide porturile pe care rulează Outline. După ce ați rulat scriptul de instalare, ar trebui să vi se fi prezentat cele două porturi selectate aleatoriu prin care Outline rulează pe server. Ar trebui să fie suficientă deschiderea acestor două porturi.

 Pentru a crea excepții în firewallul serverului, vă recomandăm să consultați documentația pentru „ufw” și „iptables”:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

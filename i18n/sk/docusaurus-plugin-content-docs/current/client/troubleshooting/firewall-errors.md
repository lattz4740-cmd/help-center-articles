---
title: Chyby súvisiace s firewallom
sidebar_label: Chyby súvisiace s firewallom
---

Môžete sa stretnúť s tromi typmi problémov s firewallom:

## Možno vás blokuje sieťový firewall

Ak sa snažíte inštalovať Outline pri pripojení k sieti chránenej firewallom, napríklad v škole alebo v práci, skúste počas inštalácie použiť inú sieť.

Ak to nepomôže, požiadajte správcu siete, aby povolil pripojenia medzi sieťou chránenou firewallom a vaším serverom Outline. Budete potrebovať adresu IP servera Outline a porty, na ktorých je služba Outline spustená. Tie nájdete na konci inštalačného skriptu.

## Možno vás blokuje firewall zariadenia

Ak máte v zariadení softvér, ktorý blokuje odchádzajúce pripojenia na neštandardných portoch alebo nerozpoznaný softvér (napríklad ZoneAlarm od firmy CheckPoint), pozrite si v dokumentácii k zariadeniu alebo softvéru, ako pre Outline vytvoriť výnimku.

## Možno vás blokuje firewall servera

Vami zvolený poskytovateľ cloudu niekedy môže vyžadovať, aby ste manuálne vytvorili výnimky pre firewall servera na otvorenie portov, na ktorých je služba Outline spustená. Po spustení inštalačného skriptu by ste mali mať k dispozícii dva náhodne vybraté porty, na ktorých je služba Outline spustená vo vašom serveri. Otvorenie týchto dvoch portov by malo stačiť.

 Ak chcete vytvoriť výnimky pre firewall svojho servera, informácie odporúčame vyhľadať v dokumentácii pre nástroje ufw a iptables:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

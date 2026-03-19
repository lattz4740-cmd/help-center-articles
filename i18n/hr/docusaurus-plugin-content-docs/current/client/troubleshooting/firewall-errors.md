---
title: Pogreške vatrozida
sidebar_label: Pogreške vatrozida
---

Postoje tri vrste problema s vatrozidom na koje možete naići:

## Možda vas blokira mrežni vatrozid.

Ako pokušavate instalirati Outline dok ste povezani s mrežom koja ima vatrozidnu zaštitu, na primjer u školi ili na radnom mjestu, instalirajte ga na drugoj mreži.

Ako time ne riješite problem, obratite se administratoru mreže i zatražite da omogući povezivanje mreže s vatrozidnom zaštitom i vašeg Outline poslužitelja. Morate znati IP adresu Outline poslužitelja i priključke na kojima se Outline pokreće. Navedeni su na kraju instalacijske skripte.

## Možda vas blokira vatrozid na uređaju.

Ako vaš uređaj sadrži softver koji blokira odlazna povezivanja na nestandardnim priključcima ili nepoznatom softveru (kao što je CheckPointov ZoneAlarm), u dokumentaciji uređaja ili softvera potražite upute za izradu iznimke za Outline.

## Možda vas blokira vatrozid na poslužitelju.

Davatelj usluga oblaka kojeg ste odabrali može od vas zatražiti da ručno stvorite iznimke za vatrozid poslužitelja kako bi se priključci na kojima se Outline pokreće otvorili. Nakon što ste pokrenuli instalacijsku skriptu, trebali ste vidjeti dva slučajno odabrana priključka na kojima se Outline pokreće na vašem poslužitelju. Otvaranje ta dva priključka trebalo bi biti dovoljno.

 Da biste stvorili iznimke za vatrozid na poslužitelju, preporučujemo da potražite ufw i iptables u dokumentaciji.

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

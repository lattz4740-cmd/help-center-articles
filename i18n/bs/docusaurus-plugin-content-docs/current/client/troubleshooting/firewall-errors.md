---
title: Greške u vezi sa zaštitnim zidom
sidebar_label: Greške u vezi sa zaštitnim zidom
---

Postoje tri vrste problema sa zaštitnim zidom na koje možete naići:

## Možda će vas blokirati zaštitni zid mreže.

Ako pokušavate instalirati Outline dok ste povezani s mrežom sa zaštitnim zidom, kao što su mreže u školi ili na radnom mjestu, pokušajte ga instalirati dok ste na drugoj mreži.

Ako to ne riješi problem, kontaktirajte administratora mreže da dozvoli veze između mreže sa zaštitnim zidom i vašeg Outline servera. Morate znati IP adresu Outline servera i priključke na kojima je pokrenut Outline, koji su navedeni na kraju instalacijskih skripata.

## Možda će vas blokirati zaštitni zid uređaja.

Ako na uređaju imate softver koji blokira odlazne veze na nestandardnim priključcima ili neprepoznatljiv softver (npr. CheckPointov ZoneAlarm), pogledajte dokumentaciju uređaja ili softvera da saznate kako kreirati izuzetak za Outline.

## Možda će vas blokirati zaštitni zid servera.

Pružalac usluge oblaka može zahtijevati da ručno kreirate izuzetke za zaštitni zid servera da se otvore priključci na kojima se pokreće Outline. Nakon pokretanja instalacijskih skripata, trebala su biti prikazana dva nasumično odabrana priključka na kojima se pokreće Outline na vašem serveru. Dovoljno je otvoriti ta dva priključka.

 Da kreirate izuzetke na zaštitnom zidu servera preporučujemo da pogledate dokumentaciju za "UFW" i "iptables":

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

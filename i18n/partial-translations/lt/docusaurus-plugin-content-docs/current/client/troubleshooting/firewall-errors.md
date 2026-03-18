---
title: Užkardos klaidos
sidebar_label: Užkardos klaidos
---

Yra trijų tipų užkardos problemos, su kuriomis galite susidurti.

## Galite būti užblokuoti tinklo užkardos.

Jei bandote įdiegti „Outline“ prisijungę prie tinklo, kuriam taikoma užkarda, pvz., mokykloje ar darbo vietoje, pabandykite įdiegti prisijungę prie kito tinklo.

Jei nepavyksta, susisiekite su tinklo administratoriumi, kad leistų užmegzti užkarda saugomo tinklo ir „Outline“ serverio ryšį. Reikės „Outline“ serverio IP adreso ir prievadų, kur vykdoma „Outline“, kurie nurodyti diegimo scenarijaus pabaigoje.

**Galite būti užblokuoti įrenginio užkardos**.

Jei įrenginyje yra programinė įranga, blokuojanti siunčiamuosius ryšius nestandartiniuose prievaduose, arba neatpažįstama programinė įranga („CheckPoint's ZoneAlarm“), žr. įrenginio arba programinės įrangos dokumentus, kad sužinotumėte, kaip sukurti „Outline“ išimtį.

## Galite būti užblokuoti serverio užkardos.

Pasirinktas debesies paslaugų teikėjas gali reikalauti patiems sukurti serverio užkardos išimtis, kad būtų galima atidaryti prievadus, kuriuos naudojant vykdoma „Outline“. Paleidus diegimo scenarijų turėtų būti pateikti du atsitiktinai parinkti prievadai, kuriuos naudojant vykdoma „Outline“ jūsų serveryje. Turėtų pakakti atidaryti šiuos du prievadus.

 Kad sukurtumėte serverio užkardos išimčių, rekomenduojame peržiūrėti „ufw“ ir „iptables“ dokumentus.

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- „Iptables“: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

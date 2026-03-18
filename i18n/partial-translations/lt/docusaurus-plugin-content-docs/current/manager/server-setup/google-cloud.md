---
title: „Google Cloud“ automatinė sąranka
sidebar_label: „Google Cloud“ automatinė sąranka
---

## Apžvalga

„Outline Manager“ yra funkcija, kurią naudojant galima automatiškai konfigūruoti „Outline“ serverį „Google Cloud“ veikiančiame serveryje. Jei pasirinksite naudoti šią funkciją, „Outline Manager“ paprašys prisijungti naudojant „Google“ paskyrą, kuri suteiks tam tikrus[„OAuth“](https://developers.google.com/identity/protocols/oauth2) leidimus vietiniu mastu įdiegtai „Outline Manager“, kad būtų galima konfigūruoti „Google Cloud“ paskyrą.

 Jei nenorite suteikti šių leidimų, galite vadovautis „Outline Manager“ išplėstinėmis sąrankos instrukcijomis ir paleisti „Outline“ sistemoje „Google Cloud Platform“.

## Suteikti leidimai

Kad galėtų teikti automatinę sąranką, „Outline Manager“ reikia toliau nurodytų leidimų iš jūsų „Google“ paskyros.

## Google Cloud Platform

- Peržiūrėti ir tvarkyti „Google“ įvertinimo variklio išteklius
- Peržiūrėti jūsų duomenis visose „Google Cloud“ paslaugose ir jūsų „Google“ paskyros el. pašto adresą

## Pagrindinė paskyros informacija

- Peržiūrėti pirminį „Google“ paskyros el. pašto adresą
- Susieti jus su asmens informacija sistemoje „Google“

## Papildoma prieiga

- Tvarkyti „Cloud Platform“ projektus
- Peržiūrėti ir tvarkyti „Google Cloud Platform“ atsiskaitomąsias paskyras
- Tvarkyti „Google“ API paslaugos konfigūraciją

Naudodami šiuos leidimus galime palaikyti išplėstines „Outline“ serverių tvarkymo funkcijas, įskaitant toliau nurodytas.

- Leidimas pasirinkti tinkamą atsiskaitomąją paskyrą
- Naujo projekto, skirto „Outline“ serveriams tvarkyti, kūrimas
- Pasiekiamų duomenų centrų sąrašas
- Naujų virtualiųjų mašinų kūrimas norint paleisti „Outline“
- Naujos virtualiosios mašinos konfigūravimas naudojant „Outline“

## Leidimų anuliavimas

Galite anuliuoti „Outline Manager“ prieigą prie „Google Cloud Platform“ apsilankę skiltyje[„Mano paskyra“](https://myaccount.google.com/permissions). Jei anuliuosite prieigą, visi serveriai, kuriuos sukūrėte naudodami automatinę sąranką, toliau veiks, bet nebebus rodomi „Outline Manager“. Kad atkurtumėte prieigą prie jų, tiesiog iš naujo prisijunkite prie „Google Cloud Platform“ pradėdami automatinę sąranką.

## „Outline“ projekto organizacija

„Google Cloud“ automatinė sąranka naudoja vieną[„Google“ debesies projektą](https://cloud.google.com/resource-manager/docs/creating-managing-projects) „Outline“ serveriams tvarkyti. Projektas sukuriamas pirmą kartą vykdant automatinę sąranką. Tada pasiūlomas projekto ID, kuris sudarytas iš „Outline-“ ir atsitiktinių simbolių eilutės. Jei norite, kurdami galite pasirinkti kitą projekto ID. Projekto pavadinimas bus „Outline“ serveriai“.

## Atsiskaitomoji paskyra

„Google“ debesies projektams reikia nurodyti susietą atsiskaitomąją paskyrą ir mokėjimo informaciją. Kai pirmą kartą naudosite „Google Cloud“ automatinę sąranką, jūsų bus paprašyta pateikti atsiskaitomąją paskyrą, kuri bus susieta su „Outline“ serveriais. Serveris gali nustoti veikti, jei iškils su atsiskaitomąja paskyra susijusi problema. Tokiu atveju turėtumėte prisijungti prie[„Google Cloud Console“](https://console.cloud.google.com/getting-started), rasti „Google“ debesies projektą, susietą su „Outline“ (pavad. „Outline“ serveriai“), ir atnaujinti atsiskaitymo nustatymus.

## Serverių naikinimas

Jei norite panaikinti serverius, sukurtus naudojant automatinę sąranką, lengviausias būdas tai padaryti yra pasinaudoti „Outline Manager“. Tačiau, jei norite patys panaikinti serverius, galite prisijungti prie[„Google Cloud Console“](https://console.cloud.google.com/getting-started), surasti projektą, kuris buvo sukurtas atliekant pradinę sąranką (pavad. „Outline“ serveriai“), ir ištrinti ten esančius išteklius arba išjungti projektą.

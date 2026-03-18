---
title: Sauga ir privatumas naudojant „Outline“
sidebar_label: Sauga ir privatumas naudojant „Outline“
---

Sauga ir privatumas naudojant „Outline“

## Kaip „Outline“ saugo internetinius pranešimus

Srautą internete lengviausia sekti, kai jis perduodamas vietiniu arba šalies tinklu.

„Outline“ padeda užtikrinti pranešimų privatumą šifruodama interneto srautą, jį perduodant šalies tinkle, ir išlaikydama jį šifruotą, kol pasiekiamas „Outline“ serveris. Kai srautas šifruojamas naudojant „Outline“, tinklo stebėtojai negali tikrinti svetainių, kuriose lankotės, ar perduodamos informacijos.

Be to, „Outline“ gali padėti atgauti prieigą prie saugių tiesioginių pranešimų įrankių, kurie kitais būdais gali būti nepasiekiami jūsų šalyje.

## Šifravimo standartai

„Outline“ šifruoja iš jūsų įrenginio į „Outline“ serverį ir atvirkščiai perduodamus pranešimus naudodama AEAD 256 bitų „Chacha2020 IETF Poly 1305“ šifrą. AEAD šifrai užtikrina konfidencialumą, vientisumą ir autentiškumą bei puikų našumą naudojant modernią aparatinę įrangą.

## Saugos patikra

2018 m. „Outline“ tikrino dvi nepriklausomos skaitmeninės saugos organizacijos: „Radically Open Security“ ir „Cure53“, kurios peržiūrėjo programinę įrangą pagal naujausius saugos standartus. „Radically Open Security“ atliko papildomą patikrinimą 2022 m., o „Cure53“ atliko „Outline SDK“ patikrinimą 2024 m. Ataskaitas galite perskaityti čia:

- [„Radically Open Security Penetration Test Report“ (2018 m. kovo mėn.)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [„Cure53 Pentest & Audit Report Jigsaw Outline“ (2018 m. gruodžio mėn.)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [„Radically Open Security Penetration Test Report“ (2022 m. gruodžio mėn.)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [„Cure53 Pentest Report Jigsaw Outline VPN SDK“ (2024 m. sausio mėn.)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Anoniminė metrika ir žurnalai

„Outline“ stebi naudojamą pralaidumą, pvz., kiekvieno prieigos rakto perduotų baitų skaičių. Pagal šią informaciją serverių administratoriai gali atitinkamai derinti pralaidumo prenumeratas su debesies serverio teikėjais, bet negali peržiūrėti faktinės informacijos, kuri buvo perduota per „Outline“ serverį.

Sužinokite daugiau apie „Outline“ [duomenų ir informacijos rinkimą](/about/data-collection).

---

## DUK apie saugą ir privatumą

## Ar „Outline“ gali užtikrinti mano anonimiškumą prisijungus?

Ne, „Outline“ nėra anonimiškumo užtikrinimo įrankis. „Outline“ saugo jūsų privatumą nuo potencialių tinklo stebėtojų.

„Outline“ neužtikrina visiško anonimiškumo svetainėse, kuriose lankotės, nes tokios svetainės vis tiek gali jus identifikuoti, kai prisijungiate ir kartais naudodamos tokius metodus kaip naršyklės kontrolinio kodo nustatymas. Naudojant programas mobiliesiems daugelyje modernių išmaniųjų telefonų yra API, leidžiančios įdiegtoms programoms gauti jūsų vietos informaciją, neatsižvelgiant į tarpinį serverį, nes galima naudoti įterptą GPS.

Paprastai VPN teikia svarbią apsaugą, ypač nuo sekimo internetu, bet dirbant internetu visada yra pavojus. Net naudojant VPN, jei IPT jau žino jūsų tapatybę ir gali stebėti jūsų tinklo srautą, jis gali nustatyti jūsų „Outline“ serverio IP adresą. Šią informaciją galima naudoti norint užblokuoti prieigą prie „Outline“ serverio arba sužinoti naudojimo šablonus, pvz., kada paprastai esate prisijungę ir galbūt jūsų apytikslę vietą.

## Ar kas nors žino, kad naudoju „Outline“?

Galbūt. Pasiekiamos platformos ir paslaugos tikriausiai galės nustatyti, kad jūsų ryšys gaunamas iš debesies serverio. Retkarčiais jie gali nustatyti, kad naudojate VPN, bet negalės matyti jūsų srauto internete turinio.

## Ar „Outline“ apsaugo nuo visų galimų kibernetinių grėsmių?

Ne. Joks įrankis neapsaugos nuo visų galimų kibernetinių grėsmių. „Outline“ suteikia prieigą prie atviro interneto ir užtikrina jūsų privatumą šifruodama srautą, bet rekomenduojame imtis papildomų saugos priemonių, kad apsisaugotumėte nuo kitų tipų išpuolių, pvz., kenkėjiškų programų ir sukčiavimo.

Kad sustiprintumėte apsaugą prisijungus, apsvarstykite galimybę bendradarbiauti su organizacijos saugos kibernetinėje erdvėje užtikrinimo ekspertu. Arba galite gauti suasmenintų nurodymų iš pagrindinių saugos ekspertų, apsilankę [„Security Planner“](https://securityplanner.org/) – svetainėje, kuri sukurta siekiant teikti aiškias instrukcijas, kaip pasirinkti tinkamus saugos kibernetinėje erdvėje užtikrinimo įrankius pagal savo poreikius.

Be to, galite peržiūrėti kitus [„Jigsaw“](https://jigsaw.google.com/) teikiamus saugos kibernetinėje erdvėje užtikrinimo produktus, pvz., [„Intra“](https://getintra.org/), [„Project Shield“](https://g.co/shield) ir [Slaptažodžio apsaugą](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Ar teisėta naudoti VPN?

Prieš naudodami „Outline“ ar programą, žr. vietinius įstatymus, nuostatus ir debesies paslaugų teikėjo, kurio paslaugomis ketinate naudotis, paslaugų teikimo sąlygas.

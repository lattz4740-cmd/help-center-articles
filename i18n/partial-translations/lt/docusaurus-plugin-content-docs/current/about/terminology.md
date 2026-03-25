---
title: Terminologija
sidebar_label: Terminologija
---

## Kas yra VPN?

Virtualusis privatusis tinklas (VPN) yra privatus ryšys tarp jūsų įrenginio (-ių) ir prieglobos serverio. Kai naudojate VPN, jūsų srautas yra paslėptas nuo interneto tiekėjo.

VPN rekomenduojame naudoti toliau nurodytais atvejais.

- Jei reikia apsaugoti savo duomenis naudojant viešąjį „Wi-Fi“ tinklą
- Jei norite išsaugoti naršymo duomenų privatumą neatskleidžiant jų interneto tiekėjui ir vyriausybinėms įstaigoms
- Jei norite pasiekti necenzūruotą turinį iš įvairių šaltinių visame pasaulyje

## Kuo „Outline“ skiriasi nuo įprastų VPN?

Interneto tiekėjai lengvai aptinka ir gali blokuoti įprastus VPN pagal įprastus saugumo protokolus ir (arba) srauto tendencijas. „Outline“ yra atsparesnė už įprastus VPN, nes sukurta naudojant protokolą, kurį sudėtinga aptikti ir todėl sunkiau užblokuoti. „Outline“ yra atspari įmantrių tipų cenzūrai, pvz., blokavimui tinklo pagrindu ar IP blokavimui.

## Kas yra „Outline“ serveris?

„Outline“ serveris paleidžia VPN, prie kurio jungiasi atitinkamą teisę turintys naudotojai.

Jei kuriate naują tinklą, kaip „Outline“ serverį galite naudoti savo saugų serverį, jei jį turite, arba galite kreiptis į toliau nurodytus debesies paslaugų teikėjus.

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Savo serverį nustatysite naudodami „Outline Manager“.

## Kas yra paslaugos valdytojas? {#servicemanager}

Paslaugos valdytojas yra asmuo, atsakingas už „Outline“ serverio nustatymą ir prieigos raktų bendrinimą su naudotojais. Paprastai paslaugos valdytojas turi padengti serverio naudojimo kaštus.

## Kas yra prieigos raktas? {#accesskey}

Prieigos raktas naudojamas norint pasiekti esamą „Outline“ serverį ir prisijungti prie VPN. [Paslaugos valdytojas](#servicemanager) suteiks jums prieigos raktą arba galite patys [nustatyti „Outline“ serverį](/manager/server-setup/setup-server).

Pavyzdys, kaip atrodo prieigos raktas (tik pavyzdys; neveikia):

ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Kas yra „Outline Manager“?

„Outline Manager“ – tai darbalaukio programa, kurią naudodamas paslaugos valdytojas nustato „Outline“ serverį, generuoja [prieigos raktus](#accesskey) ir nustato naudojamų duomenų apribojimus vienam raktui. Naujausią „Outline Manager“ versiją galite atsisiųsti [čia](https://getoutline.org/get-started/#step-1) arba [čia](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Kas yra „Outline“ klientų programa?

Pasiekiamos darbalaukiui ir mobiliesiems įrenginiams skirtos „Outline“ klientų programos versijos, ši programa suteikia galimybę prisijungti prie „Outline“ serverio ir pasiekti VPN naudojant prieigos raktą. Naujausią „Outline“ klientų programos versiją galite atsisiųsti [čia](https://getoutline.org/get-started/#step-3) arba [čia](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Kas yra duomenų apribojimai?

Naudodami „Outline Manager“ paslaugos valdytojai prieigos raktams gali nustatyti pastarųjų 30 dienų duomenų apribojimą, kad išvengtų per didelio naudojimo ir lengviau numatytų mokesčius. Paslaugos valdytojai gali nustatyti numatytąjį apribojimą, taikomą kiekvienam raktui, arba bet kokiam raktui nustatyti kitokį apribojimą, pakeičiantį numatytąjį. Nustatytas apribojimas įsigalioja iš karto, jis vykdomas kas valandą.

Paslaugos valdytojai, kurie pasirenka bendrinti metriką su „Jigsaw“, turėtų peržiūrėti [duomenų rinkimo politiką](https://getoutline.org/policies/data-collection), kad daugiau sužinotų apie tai, kaip pranešama apie duomenų apribojimų naudojimą.

---
title: Varnost in zasebnost pri uporabi storitve Outline
sidebar_label: Varnost in zasebnost pri uporabi storitve Outline
---

Varnost in zasebnost pri uporabi storitve Outline

## Kako Outline zaščiti spletno komunikacijo

Največje tveganje za nadzor internetnega prometa obstaja, ko potuje prek lokalnega ali državnega omrežja.

Outline pomaga zagotavljati zasebnost komunikacije tako, da šifrira internetni promet, medtem ko poteka v državnem omrežju, pri čemer promet ostane šifriran, dokler ne prispe do strežnika Outline. Pri šifriranju prometa s storitvijo Outline si opazovalci omrežja ne morejo ogledati spletnih mest, ki jih obiskujete, ali podatkov, ki jih prenašate.

Prek storitve Outline lahko morda tudi pridobite dostop do varnih komunikacijskih orodij s celovitim šifriranjem, ki sicer morda niso dostopna v vaši državi.

## Standardi šifriranja

Outline šifrira komunikacijo med napravo in strežnikom Outline z 256-bitno šifro AEAD Chacha2020 IETF Poly 1305. Šifre AEAD zagotavljajo zaupnost, celovitost in pristnost ter odlično delujejo v sodobni strojni opremi.

## Varnostni pregledi

Leta 2018 sta Outline pregledali Radically Open Security in Cure53, neodvisni organizaciji za digitalno varnost, ki pregledujeta skladnost programske opreme z najnovejšimi varnostnimi standardi. Organizacija Radically Open Security je leta 2022 opravila dodatno revizijo in Cure53 je leta 2024 izvedel revizijo kompleta Outline SDK. Poročila lahko preberete tukaj:

- [Radically Open Security Penetration Test Report (marec 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [Cure53 Pentest & Audit Report Jigsaw Outline (december 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [Radically Open Security Penetration Test Report (december 2022)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [Cure53 Pentest Report Jigsaw Outline VPN SDK (januar 2024)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Anonimne meritve in dnevniki

Outline beleži porabo pasovne širine v obliki števila prenesenih bajtov za posamezen ključ za dostop. Na podlagi teh podatkov lahko skrbniki strežnikov v skladu s potrebami prilagodijo naročnino za pasovno širino pri ponudnikih strežnikov v oblaku, ne morejo pa si ogledati dejanskih podatkov, ki so se prenesli prek strežnika Outline.

Preberite več o tem, kako Outline [zbira podatke](/about/data-collection).

---

## Pogosta vprašanja o varnosti in zasebnosti

## Ali Outline zagotavlja spletno anonimnost?

Ne, Outline ni orodje za anonimnost. Outline varuje vašo zasebnost pred morebitnimi opazovalci omrežja.

Outline vam ne zagotavlja popolne anonimnosti na spletnih mestih, ki jih obiščete, saj lahko taka spletna mesta ugotovijo vašo identiteto, ko se prijavite nanje z vnosom poverilnic in v nekaterih primerih prek postopkov, kot je prstni odtis brskalnika. Kar zadeva aplikacije za mobilne telefone, ima večina sodobnih pametnih telefonov API-je, ki nameščenim aplikacijam omogočajo pridobivanje vaše lokacije neodvisno od vašega strežnika proxy, ker pri tem uporabijo podatke vdelane tehnologije GPS.

Omrežja VPN na splošno zagotavljajo pomembno zaščito, zlasti pred internetnim nadzorom, vendar pri uporabi spleta vedno obstajajo tveganja. Če ponudnik internetnih storitev že pozna vašo identiteto in lahko spremlja vaš omrežni promet, bo morda lahko ugotovil naslov IP vašega strežnika Outline, čeprav uporabljate VPN. Na podlagi teh podatkov je mogoče blokirati dostop do strežnika Outline ali ugotoviti vzorce uporabe, na primer kdaj ste običajno v spletu, in morda tudi vašo okvirno lokacijo.

## Ali lahko drugi ugotovijo, da uporabljam Outline?

Morda. Platforme in storitve, do katerih dostopate, bodo najverjetneje lahko ugotovile, da je vaša povezava vzpostavljena prek strežnika v oblaku. V nekaterih primerih lahko ugotovijo, da uporabljate VPN, vendar si ne bodo mogle ogledati vsebine vašega internetnega prometa.

## Ali me Outline varuje pred vsemi možnimi kibernetskimi grožnjami?

Ne. Z nobenim orodjem se ni mogoče zaščititi pred vsemi možnimi kibernetskimi grožnjami. Outline zagotavlja dostop do odprtega interneta in poveča zasebnost prek šifriranja prometa, vendar priporočamo, da se dodatno zaščitite pred drugimi vrstami napadov, kot sta zlonamerna programska oprema in lažno predstavljanje.

Če želite okrepiti svojo zaščito pred grožnjami v spletu, se posvetujte s strokovnjakom za kibernetsko varnost v svoji organizaciji. Druga možnost je, da za osebno prilagojene nasvete prosite vodilne strokovnjake za varnost na spletnem mestu [Security Planner](https://securityplanner.org/), zasnovanem za zagotavljanje jasnih navodil pri izbiri ustreznih orodij za kibernetsko varnost.

Prav tako si lahko ogledate druge izdelke za kibernetsko varnost inkubatorja [Jigsaw](https://jigsaw.google.com/), kot so [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) in [Zaščita gesla](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Ali je zakonsko dovoljeno uporabljati VPN?

Pred uporabo storitve Outline ali aplikacije preverite lokalno zakonodajo in predpise ter pogoje storitve pri ponudniku storitev v oblaku, ki ga nameravate uporabiti.

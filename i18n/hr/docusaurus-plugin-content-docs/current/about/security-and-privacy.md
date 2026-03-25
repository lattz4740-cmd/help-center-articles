---
title: Sigurnost i privatnost tijekom upotrebe Outlinea
sidebar_label: Sigurnost i privatnost tijekom upotrebe Outlinea
---

Sigurnost i privatnost tijekom upotrebe Outlinea

## Kako Outline štiti online komunikaciju

Internetski promet obično je najizloženiji dok podaci putuju lokalnom ili nacionalnom mrežom.

Outline će zadržati privatnost komunikacija kriptiranjem internetskog prometa dok putuje nacionalnom mrežom. Promet ostaje kriptiran dok ne stigne do Outline poslužitelja. Ako je promet šifriran pomoću Outlinea, promatrači na mreži ne mogu vidjeti koje web-lokacije posjećujete ili podatke koje prenosite.

Outline vam može pomoći i da vratite pristup alatima za komunikaciju između krajnjih točaka kojima se inače možda ne može pristupiti u vašoj državi.

## Standardi šifriranja

Outline šifrira komunikaciju između vašeg uređaja i Outline poslužitelja pomoću 256-bitne šifre AEAD Chacha2020 IETF Poly 1305. AEAD šifre pružaju povjerljivost, integritet i autentičnost te imaju odlične rezultate na modernom hardveru.

## Sigurnosna ispitivanja

Dvije neovisne sigurnosne organizacije, Radically Open Security i Cure53, koje ocjenjuju softver na temelju najnovijih sigurnosnih standarda izvršile su reviziju Outlinea 2018. Radically Open Security proveo je dodatno ispitivanje 2022., a Cure53 je proveo ispitivanje Outline SDK-a 2024. Izvješća možete pročitati ovdje:

- [Izvješće organizacije Radically Open Security o testu prodiranja (ožujak 2018.)](https://getoutline.org/reports/ros-report.pdf)
- [Izvješće organizacije Cure53 o reviziji i testu prodiranja za Outline tvrtke Jigsaw (prosinac 2018.)](https://getoutline.org/reports/cure53-report.pdf)
- [Izvješće organizacije Radically Open Security o testu prodiranja (prosinac 2022.)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Izvješće organizacije Cure53 o testu prodiranja za Outline VPN SDK tvrtke Jigsaw (siječanj 2024.)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Anonimni mjerni podaci i zapisnici

Outline prati upotrijebljenu propusnost kao "prenesene bajtove" za svaki pristupni ključ. Te informacije omogućuju administratorima poslužitelja da prema potrebi prilagode pretplate na propusnost kod davatelja usluga oblaka, no ne omogućuju im da vide stvarne podatke koji su prošli kroz Outline poslužitelj.

Saznajte više o tome kako Outline [prikuplja podatke i informacije](https://getoutline.org/policies/data-collection).

---

## Česta pitanja o sigurnosti i privatnosti

## Može li mi Outline omogućiti anonimnost online?

Ne, Outline nije alat za anonimnost. Outline štiti vašu privatnost od mogućih mrežnih promatrača.

Outline vam ne nudi potpunu anonimnost na web-lokacijama koje posjećujete jer vas i dalje mogu identificirati kada se prijavite. Ponekad upotrebljavaju i razne tehnike za identifikaciju, na primjer otisak preglednika. Što se tiče mobilnih aplikacija, većina modernih pametnih telefona ima API-je koji instaliranim aplikacijama omogućuju da dohvate vašu lokaciju neovisno o proxyju jer to čine pomoću ugrađenog GPS-a.

VPN-ovi općenito omogućuju važnu zaštitu, posebno od internetskog nadzora, no uvijek postoje rizici pri radu online. Čak i ako imate VPN, ako ISP već zna vaš identitet i promatra vaš mrežni promet, može saznati IP adresu vašeg Outline poslužitelja. Te se informacije mogu upotrijebiti za blokiranje pristupa Outline poslužitelju ili određivanje uzoraka upotrebe, na primjer kada ste obično online i koja je vaša približna lokacija.

## Može li netko saznati da upotrebljavam Outline?

Moguće je. Platforme i usluge kojima pristupate najvjerojatnije će znati da ste se povezali putem poslužitelja u oblaku. Ponekad će moći zaključiti da upotrebljavate VPN, ali neće moći vidjeti sadržaj vašeg internetskog prometa.

## Štiti li me Outline od mogućih cyber prijetnji?

Ne. Nijedan vas alat ne može zaštititi od mogućih cyber prijetnji. Outline omogućuje da pristupate otvorenom internetu i štiti vašu privatnost šifriranjem prometa, ali preporučujemo da primijenite dodatne mjere opreza kako biste se zaštitili od drugih vrsta napada, na primjer zlonamjernog softvera i krađe identiteta.

Kako biste poboljšali online zaštitu, razmislite o suradnji sa stručnjakom za cyber sigurnost u svojoj organizaciji. Osim toga, možete dobiti personalizirane savjete od vodećih stručnjaka za sigurnost na web-lokaciji [Security Planner](https://securityplanner.org/) koja je osmišljena da vam pruži jasne upute o odabiru alata za cyber sigurnost koji vam najviše odgovaraju.

Pogledajte i druge proizvode za cyber sigurnost tvrtke [Jigsaw](https://jigsaw.google.com/), kao što su [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) i [Password Alert](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Je li upotreba VPN-a legalna?

Prije pokretanja Outlinea ili upotrebe aplikacije pročitajte lokalne zakone, uredbe, kao i uvjete pružanja usluge odabranog davatelja usluga u oblaku.

---
title: Kako Outline funkcionira
sidebar_label: Kako Outline funkcionira
---

## Instalacija servera
 ​Iako se instalacija Outlinea čini jednostavnom, zapravo postoji složen skup koraka koji se izvršavaju u pozadini i omogućavaju instalaciju servera. Prilikom svake instalacije Outlinea instalacijska skripta izvršava sljedeće korake:

- Stabilna verzija slike Shadowboxa se preuzima i uvozi pomoću Dockera. Slika se hostira na [Quay.io](https://quay.io/), na [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Ta slika sadržava Outline server i Management API koje će kasnije koristiti aplikacija Outline Server Management za kreiranje i uklanjanje pristupnih ključeva, uključivanje/isključivanje izvještavanja o anonimnim pokazateljima itd.
- [Watchtower](https://github.com/v2tec/watchtower) se instalira i konfigurira. On svaki sat provjerava postoje li ažuriranja slika, čime se osigurava da svaki Outline server bude uvijek ažuran i ima najnovija poboljšanja funkcija i sigurnosti.
- Web server koji se koristi za pristupanje Management API-ju se pokreće na nasumično odabranom priključku, na tajnoj i nasumično odabranoj putanji.
- Kreira se [samostalno potpisani SSL certifikat](https://en.wikipedia.org/wiki/Self-signed_certificate) da se upravljanje Outline serverom može šifrirati pomoću TLS-a, iako ne postoji naziv domene. Generira se i jedinstveni digitalni otisak ovog certifikata i pohranjuje u aplikaciji Outline Manager, što pomaže u sprečavanju MITM napada.

Prilikom instalacije Outlinea nije potrebna nikakva konfiguracija nakon instalacije.

## Sigurnost servera
 Outline je softver otvorenog koda, što znači da svako može vidjeti kôd i poboljšati ga ako uoči neke propuste. Naš kôd se hostira na [GitHubu](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline).

 Osim toga, svi instalirani Outline serveri se automatski ažuriraju kad god se objavi nova verzija, čime se osigurava da nijedan Outline server ne ostane sa starim verzijama softvera.

 Radi upravljanja pristupnim ključevima na serveru, aplikacija Outline Manager stupa u interakciju s Management Serviceom na Outline serveru. Management Service se pokreće na nasumično odabranom priključku i tajnoj, jedinstvenoj putanji. Management Service je i sam otporan na sondiranje, pošto ne reagira na upite ukoliko se ne navede tajna putanja. Konačno, sva komunikacija s Management Serviceom se šifrira pomoću [samostalno potpisanog SSL certifikata](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Osim toga, Outline server ne pohranjuje nikakve zapisnike, tako da se podaci korisnika neće otkriti ni u slučaju da bude ugrožen. Saznajte više [ovdje](/about/security-and-privacy). Reviziju Outlinea su izvršili [Radically Open Security](https://radicallyopensecurity.com/) i [Cure53](https://cure53.de/) 2018. godine. Pogledajte izvještaje [ovdje](/about/security-and-privacy).

## Rukovanje UDP saobraćajem
 Outline može raditi kao VPN na čitavom sistemu, što znači da se sav UDP saobraćaj tunelira putem Outline servera.

## DNS saobraćaj
Outline izvršava sva DNS pretraživanja putem Outline servera i štiti ih korištenjem istog šifriranja koje se koristi za svu drugu aktivnost na mreži. Vaši DNS upiti će prolaziti putem Outline servera do Dyn Internet Guidea, OpenDNS-a, Cloudflare DNS-a ili Quad9 DNS-a. Outline nikada ne zapisuje vaša DNS pretraživanja.

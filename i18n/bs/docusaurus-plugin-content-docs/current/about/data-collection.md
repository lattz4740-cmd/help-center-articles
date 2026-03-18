---
title: Prikupljanje podataka i informacija
sidebar_label: Prikupljanje podataka i informacija
---

Outline ne prikuplja lične informacije, osim ako pristanete da ih pružite. Outline ne prikuplja ni informacije o web lokacijama koje posjećujete niti s kim ili o čemu komunicirate.

 Ako kreirate ili se prijavljujete na račun pomoću pružaoca usluge oblaka treće strane putem Outline Managera, nećemo dobiti nijednu informaciju koju date pružaocu usluge oblaka treće strane, kao što su adresa e-pošte, ime, podaci o naplati i podaci o plaćanju.

****Informacije koje automatski dobijamo****

 Automatski prikupljamo dvije vrste informacija.

 1. IP servera

 IP Outline servera prikuplja [Quay.io](https://quay.io/) i omogućava da mu pristupimo kada se na serveru izvrše automatska ažuriranja s najnovijim poboljšanjima sigurnosti i funkcija. Pomoću IP-a servera može se identificirati pružalac usluge oblaka i grad u kojem je postavljen Outline server, ali on ne pruža informacije o tome ko upravlja serverom niti ko mu pristupa.

 2. Tehničke informacije kojima se ne otkriva identitet osobe

 Ako Outline padne ili dođe do fatalnog izuzetka ili ako ručno pošaljete povratne informacije u aplikaciji Outline, prijavit će informacije navedene u nastavku. Te informacije će se koristiti samo kao pomoć u identificiranju ili ispravljanju problema sa stabilnošću ili performansama.

- Zemlja
- Jezik/zemlja
- Datum i vrijeme pada aplikacije / izuzetka i do 100 prethodnih događaja, kao što je otvaranje odjeljka "O aplikaciji"
- Statistički sastavljene poruke o izuzecima
- Naziv i verzija OS-a
- Model telefona (ako je primjenjivo)
- Vrijeme pokretanja aplikacije
- Preglednik
- Arhitektura
- Broj verzije i podverzije Outlinea

Ove informacije se prenose pomoću HTTPS-a Sentryju ([sentry.io](https://sentry.io/)), pružaocu usluge praćenja grešaka treće strane otvorenog koda. Sentry koristi različite tehnologije i usluge, standardne u industriji, da zaštiti vaše podatke od neovlaštenog pristupa, otkrivanja, korištenja i gubitka. Ako imate pitanja o pravilima koja koristi Sentry, posjetite [https://sentry.io/security/](https://sentry.io/security/) i [https://sentry.io/privacy/](https://sentry.io/privacy/) ili pišite na [security@sentry.io](mailto:security@sentry.io). Pristup svim podacima Outlinea koje Sentry pohranjuje je ograničen tako da im mogu pristupati samo članovi tima Outlinea.

****Informacije koje prikupljamo samo ako prihvatite prikupljanje****

 Outline prenosi sljedeće informacije timu Outlinea ako to prihvatite.

 1. Pokazatelji korištenja

 Svaki Outline server automatski prikuplja broj prenesenih bajtova, vrijeme tokom kojeg je korisnik bio povezan sa serverom, zemlje i autonomne sisteme porijekla upotrijebljenih akreditiva i jesu li funkcije bile omogućene ili onemogućene. Ove informacije se prikupljaju tokom posljednjeg sata i po pristupnom ključu. Ne zapisuje se ni sadržaj komunikacije niti bilo kakvi metapodaci kojima se otkriva identitet (npr. prijave, e-poruke, ID-ovi uređaja itd.). Svi pokazatelji se povezuju s ID-om servera. Uputstva za promjenu ID-a servera možete pronaći [ovdje](/manager/server-management/reset-server-id).

 Prema zadanim postavkama, Outline serveri ne dijele ove pokazatelje s timom Outlinea. Ako administrator servera eksplicitno prihvati dijeljenje pokazatelja korištenja, ove informacije će se na siguran način slati timu Outlinea svaki sat. Nakon 60 dana pokazatelji korištenja će se agregirati na nivou zemlje. Administratori servera mogu uvijek promijeniti postavku dijeljenja pokazatelja korištenja odlaskom u meni "Postavke" u Outline Manageru.

 Cijenimo što dijelite s nama anonimne pokazatelje o korištenju servera, koje koristimo za mjerenje trendova korištenja i poboljšanje proizvoda.

 Naprimjer, ako administrator servera prihvati dijeljenje pokazatelja korištenja s nama, možemo dobiti informacije koje pokazuju da je server s ID-om 12345 bio korišten 3 sata jučer, da je preneseno ukupno 500 megabajta podataka s tri ključa, da je svaki korišten u Sjedinjenim Američkim Državama i Kanadi uz omogućenu funkciju ograničenja prenosa podataka.

 2. Vaši komentari i adresa e-pošte ako pošaljete povratne informacije

 U aplikacijama Outline Manager i Outline možete poslati povratne informacije timu. Preporučujemo da ne navodite podatke koji otkrivaju identitet, a polje za adresu e-pošte je neobavezno i dostupno ako želite odgovor od tima. Automatski prikupljamo i neke osnovne informacije kako bismo mogli razumjeti vaše povratne informacije. Pogledajte 2. stavku u odjeljku "Informacije koje automatski dobijamo" iznad da vidite koje podatke prikupljamo. Saznajte više o praksama zaštite privatnosti i sigurnosti Outlinea [ovdje](/about/security-and-privacy).

 Ako koristite beta verziju aplikacije Outline na Androidu, možemo koristiti Googleovu uslugu [Firebase](https://firebase.google.com/) za prikupljanje informacija o otklanjanju grešaka koje nam pomažu da otkrijemo probleme i poboljšamo Outline. Više o pravilima privatnosti i sigurnosti Firebasea možete saznati na njihovoj web lokaciji: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Ako ne želite da Outline šalje ove informacije putem Firebasea, koristite proizvodnu verziju aplikacije.

---
title: Sigurnost i privatnost prilikom korištenja Outlinea
sidebar_label: Sigurnost i privatnost prilikom korištenja Outlinea
---

Sigurnost i privatnost prilikom korištenja Outlinea

## Kako Outline štiti vaše online komunikacije

Internetski saobraćaj je najpodložniji prismotri dok putuje kroz lokalnu ili nacionalnu mrežu.

Outline pomaže u održavanju privatnosti komunikacija šifriranjem internetskog saobraćaja dok putuje unutar nacionalne mreže i zadržava to šifriranje dok ne stigne do Outline servera. Kada je saobraćaj šifriran pomoću Outlinea, posmatrači mreže ne mogu provjeravati web lokacije koje posjećujete niti informacije koje prenosite.

Outline vam može pomoći i da oporavite pristup alatima za sigurnu komunikaciju između krajnjih korisnika, koji možda na drugi način nisu dostupni u vašoj zemlji.

## Standardi šifriranja

Outline šifrira komunikacije između uređaja i Outline servera pomoću AEAD 256-bitne šifre Chacha2020 IETF Poly 1305. AEAD šifre pružaju pouzdanost, integritet i autentičnost te pokazuju izuzetne performanse na modernom hardveru.

## Revizije sigurnosti

Reviziju Outlinea su 2018. godine izvršili Radically Open Security i Cure53, dvije neovisne organizacije iz oblasti digitalne sigurnosti, koje su provjeravale najnovije sigurnosne standarde u softveru. Radically Open Security je izvršio dodatnu reviziju 2022, a Cure53 je izvršio reviziju Outline SDK-a 2024. Izvještaje možete pročitati ovdje:

- [Radically Open Security Penetration Test Report (mart 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53 Pentest & Audit Report Jigsaw Outline (decembar 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Radically Open Security Penetration Test Report (decembar 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Cure53 Pentest Report Jigsaw Outline VPN SDK (januar 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Anonimni pokazatelji i zapisnici

Outline prati iskorištenu propusnost i to u obliku "prenesenih bajtova" za svaki pristupni ključ. Pomoću tih informacija administratori servera mogu po potrebi podesiti svoje pretplate na propusnost kod pružalaca usluge oblaka, ali ne mogu vidjeti stvarne informacije koje prolaze kroz Outline server.

Saznajte više o [prikupljanju podataka i informacija u Outlineu](https://getoutline.org/policies/data-collection).

---

## Česta pitanja o sigurnosti i privatnosti

## Može li me Outline učiniti anonimnim online?

Ne, Outline nije alat za anonimnost. Outline štiti vašu privatnost od potencijalnih posmatrača mreže.

Outline vam ne pruža potpunu anonimnost na web lokacijama koje posjećujete, jer vas one i dalje mogu identificirati kada se prijavite, a ponekad i pomoću drugih tehnika, kao što je praćenje digitalnih otisaka preglednika. Kada su u pitanju mobilne aplikacije, najmoderniji pametni telefoni imaju API-je koji omogućavaju instaliranim aplikacijama da preuzmu vašu lokaciju neovisno o proksi serveru, jer se mogu oslanjati na ugrađeni GPS.

VPN-ovi uglavnom pružaju važne zaštite, prije svega od prismotre na internetu, ali uvijek postoje rizici kada radite online. Čak i kod VPN-a, ako ISP već zna vaš identitet i može posmatrati vaš mrežni saobraćaj, on će možda moći utvrditi IP adresu vašeg Outline servera. Ta informacija se može iskoristiti za blokiranje pristupa Outline serveru ili otkrivanje obrazaca korištenja, npr. vrijeme kada ste obično online, a možda i vašu približnu lokaciju.

## Mogu li drugi prepoznati da koristim Outline?

Možda. Platforme i usluge kojima pristupate će najvjerovatnije moći prepoznati da vaša veza dolazi sa servera u oblaku. Ponekad će moći zaključiti da koristite VPN, ali neće moći vidjeti sadržaj vašeg internetskog saobraćaja.

## Može li me Outline zaštiti od svih mogućih cyber prijetnji?

Ne, nijedan alat vas ne može zaštiti od svih mogućih cyber prijetnji. Outline vam pruža pristup otvorenom internetu i povećava privatnost šifriranjem saobraćaja, ali vam preporučujemo da poduzimate dodatne mjere opreza da se zaštitite od drugih vrsta napada, poput zlonamjernog softvera i krađe identiteta.

Da ojačate svoju online odbranu, razmislite o saradnji sa stručnjakom za sigurnost na internetu u vašoj organizaciji. Možete dobiti i personalizirane smjernice od stručnjaka za sigurnost na web lokaciji [Security Planner](https://securityplanner.org/) koja je izrađena kako bi pružala jasna uputstva za odabir pravih alata za sigurnost na internetu, ovisno o vašim bojaznima.

Možete pogledati i druge proizvode iz oblasti sigurnosti na internetu koje pruža [Jigsaw](https://jigsaw.google.com/), kao što su [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) i [Zaštita lozinke](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Je li zakonito koristiti VPN?

Provjerite lokalne zakone, propise i Uslove korištenja usluge pružaoca usluge oblaka kojeg planirate koristiti prije aktiviranja Outlinea ili korištenja aplikacije.

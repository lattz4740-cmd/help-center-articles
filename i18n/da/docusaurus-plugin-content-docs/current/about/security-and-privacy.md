---
title: Sikkerhed og privatliv ved brug af Outline
sidebar_label: Sikkerhed og privatliv ved brug af Outline
---

Sikkerhed og privatliv ved brug af Outline

## Sådan beskytter Outline din kommunikation på nettet

Internettrafik er mest sårbar over for overvågning, når den bevæger sig gennem dit lokale eller nationale netværk.

Outline hjælper med at holde din kommunikation privat ved at kryptere din internettrafik, mens den bevæger sig inden for dit nationale netværk, og holder den krypteret, indtil den når Outline-serveren. Når trafikken er krypteret med Outline, kan iagttagere på netværket ikke inspicere de websites, du besøger, eller de oplysninger, du overfører.

Outline kan også hjælpe dig med at gendanne adgang til sikre end to end-kommunikationsværktøjer, der måske ellers ikke er tilgængelige i dit land.

## Krypteringsstandarder

Outline krypterer kommunikation mellem din enhed og Outline-serveren ved hjælp af krypteringsalgoritmen AEAD 256-bit Chacha2020 IETF Poly 1305. AEAD-krypteringsalgoritmerne sikrer fortrolighed, integritet samt autenticitet og udviser fremragende ydeevne på moderne hardware.

## Sikkerhedsauditering

Outline blev auditeret i 2018 af Radically Open Security og Cure53, to uafhængige organisationer for digital sikkerhed, der gennemgår software i forhold til de nyeste standarder for sikkerhed. Radically Open Security udførte en yderligere audit i 2022, og Cure53 udførte en audit af Outline SDK i 2024. Du kan læse rapporterne her:

- [Radically Open Security Penetration Test Report (marts 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53 Pentest & Audit Report Jigsaw Outline (december 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Radically Open Security Penetration Test Report (december 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Cure53 Pentest Report Jigsaw Outline VPN SDK (januar 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Anonyme metrics og logs

Outline sporer den anvendte båndbredde som "overførte bytes" for hver adgangsnøgle. Disse oplysninger gør det muligt for serveradministratorer at tilpasse deres abonnementer på båndbredde til deres cloudserverudbydere efter behov, men det giver dem ikke mulighed for at se de faktiske oplysninger, der går gennem Outline-serveren.

Få flere oplysninger om Outlines [indsamling af data og oplysninger](/about/data-collection).

---

## Ofte stillede spørgsmål om sikkerhed og privatlivsbeskyttelse

## Kan Outline gøre mig anonym online?

Nej, Outline er ikke et anonymitetsværktøj. Outline beskytter dit privatliv mod potentielle iagttagere på netværket.

Outline giver dig ikke fuld anonymitet på de websites, du besøger, fordi de stadig kan identificere dig, når du logger ind, og af og til ved hjælp af teknikker som f.eks. browserregistrering. Når det gælder mobilapps, har de fleste moderne smartphones API'er, der gør det muligt for installerede apps at hente din placering uafhængigt af din proxy, da de kan benytte den indbyggede GPS.

VPN'er giver generelt vigtige former for beskyttelse, især mod internetovervågning, men der er altid risici forbundet ved at bruge nettet. Selv med et VPN kan en netværksudbyder have mulighed for at bestemme IP-adressen på din Outline-server, hvis udbyderen allerede kender din identitet og kan observere din netværkstrafik. Disse oplysninger kan bruges til at blokere for adgangen til Outline-serveren eller til at opsnappe brugsmønstre, som f.eks. hvornår du typisk er online, og muligvis din omtrentlige lokation.

## Kan andre se, at jeg bruger Outline?

Muligvis. De platforme og tjenester, du bruger, vil højst sandsynligt kunne se, at din forbindelse kommer fra en cloudserver. De kan lejlighedsvist udlede, at du bruger et VPN, men de kan ikke se indholdet af din internettrafik.

## Beskytter Outline mig mod alle mulige cybertrusler?

Nej. Intet værktøj kan beskytte dig mod alle mulige cybertrusler. Outline giver dig adgang til det åbne internet og øger privatlivsbeskyttelsen ved at kryptere din trafik, men vi anbefaler, at du træffer yderligere forholdsregler for at beskytte dig mod andre typer angreb som f.eks. malware og phishing.

Hvis du vil styrke dit onlineforsvar, bør du overveje at samarbejde med din organisations ekspert i cybersikkerhed. Ellers kan du få personlig vejledning fra førende sikkerhedseksperter på websitet [Security Planner](https://securityplanner.org/), der er udviklet til at give dig klar vejledning i, hvordan du vælger de rette værktøjer til cybersikkerhed efter dine behov.

Du kan også tjekke de andre produkter til cybersikkerhed fra [Jigsaw](https://jigsaw.google.com/), f.eks. [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) og [Password Alert](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Er det lovligt at bruge et VPN?

Tjek dine lokale love og regler samt servicevilkårene for den cloududbyder, du har planer om at bruge, inden du anvender Outline eller bruger appen.</p>

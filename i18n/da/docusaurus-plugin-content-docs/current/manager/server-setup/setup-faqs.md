---
title: "Ofte stillede spørgsmål om konfiguration af Outline-servere"
sidebar_label: "Ofte stillede spørgsmål om konfiguration af Outline-servere"
---

**Kan jeg bruge Outline uden en server?**

 Nej, desværre. Outline-softwaren kræver adgang til en server, uanset om den administreres af dig, din organisation eller en godkendt tredjepart.

## Hvor lang tid tager det at konfigurere en Outline-server?

I de fleste tilfælde tager det under fem minutter. Du kan installere Outline på en hvilken som helst cloudserver, men vi har samarbejdet med DigitalOcean for at tilbyde en mere brugervenlig, guidet installationsoplevelse, hvor du kan konfigurere din server med et par klik uden scripts.

Hvis du har valgt AWS, GCP eller en avanceret konfiguration, har vi forenklet serverinstallationen til et enkelt script, som håndterer de fleste miljøer.

## Hvor kan jeg oprette en Outline-server?

Du kan oprette en Outline-server hos de fleste cloududbydere, uanset hvor de driver forretning.

Den enkleste valgmulighed er at oprette den hos DigitalOcean, som har servere flere steder, bl.a. i Amsterdam, Toronto, San Francisco og Singapore. Hvis du foretrækker at installere hos en anden cloududbyder eller på din egen infrastruktur, kan du vælge avanceret tilstand i programmet Outline Manager og følge installationsvejledningen ved hjælp af et konfigurationsscript.

## Hvor bør jeg oprette min Outline-server?

1. Der er et par ting, du bør overveje, når du vælger placering til din Outline-server:
2. Placeringen af Outline-serveren har indflydelse på, hvordan brugerne oplever internettet. Hvis serveren f.eks. er placeret i Amsterdam, oplever brugere af denne server internettet, som om de fysisk befandt sig i Holland. Nogle websites kan endda blive vist på hollandsk. Du kan typisk tilsidesætte det lokale sprog ved hjælp af en sprogvælger på websitet.
3. Afstanden mellem dine brugere og Outline-serveren kan påvirke hastigheden. Generelt kan den fysiske afstand mellem Outline-brugere og serveren påvirke brugernes internethastighed. I de fleste tilfælde kan du vælge den serverlokation, der er tættest på det sted, dine forventede brugere er, men du kan tjekke [kortet over undersøiske kabler](https://www.submarinecablemap.com/) for at se, hvilke internetkabler der er forbundet med dit land eller din region.
4. Placeringen af din VPN-server kan have indflydelse på de juridiske rammer. Vær opmærksom på, at Outline-software ikke logfører din trafik. Få flere oplysninger om [sikkerhed og privatliv ved brug af Outline](/about/security-and-privacy).

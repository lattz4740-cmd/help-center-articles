---
title: "Hvordan oppdaterer jeg Outline-tjenerprogramvaren?"
sidebar_label: "Hvordan oppdaterer jeg Outline-tjenerprogramvaren?"
---

Outline-tjenerne oppdateres automatisk med de nyeste sikkerhetsforbedringene, slik at du alltid kjører den nyeste Outline-teknologien. Den automatiske oppdateringsprosessen aktiveres av [Watchtower](https://github.com/v2tec/watchtower), et bibliotek med åpen kildekode, som regelmessig sjekker og oppdaterer Docker-bildet som inneholder Outline-programvaren.

Når du installerer Outline ved hjelp av Outline-administrator, oppretter vi dessuten en cron-jobb for automatisk oppgradering av programvaren på tjeneren ved hjelp av [Ubetjente oppgraderinger](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) og omstart ved behov. Merk at dette ikke skjer i Avansert modus, slik at den gjeldende konfigurasjonen bevares, under forutsetning av at verten brukes til andre formål i tillegg til å kjøre Outline.

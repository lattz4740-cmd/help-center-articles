---
title: "Hvordan opdaterer jeg min Outline-serversoftware?"
sidebar_label: "Hvordan opdaterer jeg min Outline-serversoftware?"
---

Outline-servere opdateres automatisk med de nyeste sikkerhedsforbedringer, så du altid bruger den nyeste Outline-teknologi. Den automatiske opdateringsprocedure aktiveres ved hjælp af open source-biblioteket [Watchtower](https://github.com/v2tec/watchtower), der jævnligt tjekker og opdaterer det docker-systembillede, der indeholder Outline-softwaren.

Når du installerer Outline ved hjælp af Outline Manager, opretter vi desuden et cron-job, som autoamtisk opgraderer softwaren på serveren ved hjælp af [Ikke-overvågede opgraderinger](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) og genstarter, når det er nødvendigt. Bemærk, at dette ikke sker i Avanceret tilstand for at bevare den eksisterende konfiguration med den formodning, at hosten bruges til andre formål end at køre Outline.

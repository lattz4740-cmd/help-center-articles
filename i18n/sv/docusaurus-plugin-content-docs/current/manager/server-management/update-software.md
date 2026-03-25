---
title: "Hur uppdaterar jag programvaran för min Outline-server?"
sidebar_label: "Hur uppdaterar jag programvaran för min Outline-server?"
---

Outline-servrar uppdateras automatiskt med de senaste säkerhetsförbättringarna, vilket innebär att du alltid använder den senaste Outline-tekniken. Den automatiserade uppdateringsprocessen drivs av [Watchtower](https://github.com/containrrr/watchtower), ett bibliotek med öppen källkod som regelbundet kontrollerar och uppdaterar dockerbilden som innehåller Outline-programvaran.

När du installerar Outline med Outline Manager konfigurerar vi även ett cron-jobb som automatiskt uppgraderar programvaran på servern med [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) och startar om efter behov. Observera att det här inte händer i avancerat läge, för att den befintliga konfigurationen ska bevaras. Detta beror på att vi antar att värden används i andra syften utöver att köra Outline.

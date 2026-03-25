---
title: "Jak mám aktualizovat serverový software Outline?"
sidebar_label: "Jak mám aktualizovat serverový software Outline?"
---

Servery Outline se automaticky aktualizují, aby využívaly nejnovější bezpečnostní vylepšení. Vždycky tak máte nejnovější technologii Outline. Automatické aktualizace zajišťuje opensourcová knihovna [Watchtower](https://github.com/containrrr/watchtower). Ta pravidelně kontroluje a aktualizuje obraz dockeru, kde je uložen software Outline.

Pokud si navíc aplikaci Outline nainstalujete pomocí Správce Outline, nastavíme vám plánovanou úlohu, která automaticky aktualizuje software na serveru pomocí [bezobslužných upgradů](https://wiki.debian.org/UnattendedUpgrades) (funkce Unattended Upgrades v Ubuntu) a podle potřeby server restartuje. Tato funkce se neuplatňuje v rozšířeném režimu, aby se zachovala stávající konfigurace. Předpokládáme totiž, že hostitelský systém se v tomto případě využívá i k jiným účelům, nejen ke spouštění Outline.

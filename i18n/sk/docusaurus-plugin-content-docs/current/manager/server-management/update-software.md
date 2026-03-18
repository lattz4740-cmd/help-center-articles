---
title: "Ako aktualizujem softvér na serveri Outline?"
sidebar_label: "Ako aktualizujem softvér na serveri Outline?"
---

Servery Outline sa automaticky aktualizujú využitím najnovších zlepšení zabezpečenia, vďaka čomu vždy používate najnovšiu technológiu služby Outline. Tento automatický aktualizačný proces aktivuje knižnica open source s názvom [Watchtower](https://github.com/v2tec/watchtower), ktorá pravidelne kontroluje a aktualizuje obraz Docker obsahujúci softvér Outline.

Keď si nainštalujete Outline pomocou Správcu Outline, nastavíme aj úlohu softvéru Cron, ktorá automaticky inovuje softvér na serveri pomocou funkcie [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) a v prípade potreby ho reštartuje. Upozorňujeme, že k tomu nedochádza v rozšírenom režime, aby sa zachovala existujúca konfigurácia, keďže sa predpokladá, že hostiteľ sa používa aj na iné účely, než iba spúšťanie služby Outline.

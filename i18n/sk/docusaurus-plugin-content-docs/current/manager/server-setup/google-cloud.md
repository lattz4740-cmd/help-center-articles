---
title: Automatické nastavenie služby Google Cloud
sidebar_label: Automatické nastavenie služby Google Cloud
---

## Prehľad

Správca Outline zahŕňa funkciu, ktorá vám umožňuje automaticky konfigurovať server služby Outline na serveri spustenom v službe Google Cloud. Ak sa túto funkciu rozhodnete používať, Správca Outline vás požiada o prihlásenie pomocou účtu Google, ktorý vašej lokálnej inštalácii Správcu Outline udelí určité[povolenia OAuth](https://developers.google.com/identity/protocols/oauth2), aby vám bolo možné konfigurovať účet Google Cloud.

 Ak tieto povolenia nechcete poskytnúť, môžete v Správcovi Outline postupovať podľa pokynov na rozšírené nastavenie, ktoré umožní spustiť Outline v službe Google Cloud Platform.

## Povolenia udelené

Na zaistenie automatického nastavenia Správca Outline od vášho účtu vyžaduje nasledujúce povolenia.

## Google Cloud Platform

- Zobrazovanie a správa vašich zdrojov Google Compute Engine
- Čítanie vašich údajov v službách Google Cloud a zobrazenie e‑mailovej adresy vášho účtu Google

## Základné informácie o účte

- Čítanie primárnej e‑mailovej adresy vášho účtu Google
- Možnosť spojiť vás s vašimi osobnými údajmi na Googli

## Ďalší prístup

- Správa vašich projektov Cloud Platform
- Zobrazovanie a správa vašich fakturačných účtov v službe Google Cloud Platform
- Správa vašej konfigurácie služby s rozhraním Google API

Vďaka týmto povoleniam môžeme poskytovať rozšírené funkcie na správu vašich serverov služby Outline vrátane týchto:

- Možnosť vybrať si správny fakturačný účet
- Vytvorenie nového projektu na usporiadanie serverov služby Outline
- Uvedenie dostupných dátových centier
- Vytváranie nových virtuálnych počítačov na spúšťanie služby Outline
- Konfigurácia nového virtuálneho počítača pomocou služby Outline

## Zrušenie povolení

Prístup k službe Google Cloud Platform, ktorý ste udelili Správcovi Outline, môžete zrušiť na stránke [Môj účet](https://myaccount.google.com/permissions). Ak zrušíte prístup, všetky servery, ktoré ste vytvorili pomocou automatického nastavenia, zostanú spustené, no už sa nebudú zobrazovať v Správcovi Outline. Ak prístup k nim budete chcieť obnoviť, jednoducho sa znova pripojte k službe Google Cloud Platform spustením procesu automatického nastavenia.

## Usporiadanie projektov Outline

Automatické nastavenie služby Google Cloud používa na usporiadanie serverov služby Outline jeden [projekt Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects). Projekt sa vytvorí pri prvom použití automatického nastavenia. Bude označený navrhovaným identifikátorom projektu začínajúcim sa reťazcom Outline-, za ktorým nasleduje reťazec náhodných znakov. Ak chcete, pri vytváraní môžete vybrať iný identifikátor projektu. Projekt bude mať názov Outline servers (Servery služby Outline).

## Fakturačný účet

Projekty Google Cloud si vyžadujú pripojený fakturačný účet, ktorý definuje platobné údaje. Pri prvom použití automatického nastavenia služby Google Cloud sa vám zobrazí výzva na zadanie fakturačného účtu, ktorý sa má spojiť s vašimi servermi služby Outline. Niekedy sa server zastaví pre problém s fakturačným účtom. V tom prípade by ste sa mali prihlásiť do služby [Google Cloud Console](https://console.cloud.google.com/getting-started), vyhľadať projekt Google Cloud spojený so službou Outline (s názvom Outline servers (Servery služby Outline)) a aktualizovať nastavenia fakturácie.

## Zničenie serverov

Ak chcete zničiť servery vytvorené pomocou automatického nastavenia, najjednoduchšie je použiť Správcu Outline. Ak však chcete servery zničiť svojpomocne, môžete sa prihlásiť do služby [Google Cloud Console](https://console.cloud.google.com/getting-started), vyhľadať projekt vytvorený pri úvodnom nastavení (s názvom Outline servers (Servery služby Outline)) a buď odstrániť zdroje v rámci neho, alebo ho celý zastaviť.

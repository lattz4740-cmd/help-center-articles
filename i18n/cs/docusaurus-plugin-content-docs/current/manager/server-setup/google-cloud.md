---
title: Automatické nastavení ve službě Google Cloud
sidebar_label: Automatické nastavení ve službě Google Cloud
---

## Přehled

Správce Outline zahrnuje funkci, která umožňuje na serveru spuštěném ve službě Google Cloud automaticky nakonfigurovat server Outline. Pokud se rozhodnete tuto funkci využít, Správce Outline vás vyzve k přihlášení pomocí účtu Google. Tím místní instalaci Správce Outline udělíte určitá [oprávnění protokolu OAuth](https://developers.google.com/identity/protocols/oauth2) pro účely konfigurace účtu Google Cloud.

 Jestli tato oprávnění udělit nechcete, můžete podle pokynů k pokročilému nastavení ve Správci Outline spustit server Outline ve službě Google Cloud Platform.

## Potřebná oprávnění

K zajištění automatického nastavení potřebuje Správce Outline od vašeho účtu Google následující oprávnění.

## Google Cloud Platform

- Zobrazení a správa zdrojů modulu Google Compute Engine
- Zobrazení dat ve službách Google Cloud a zobrazení e‑mailové adresy účtu Google

## Základní informace o účtu

- Zobrazení primární e‑mailové adresy účtu Google
- Spojení vašich osobních údajů na Googlu s vaší osobou

## Další přístup

- Správa projektů Cloud Platform
- Zobrazení a správa fakturačních účtů služby Google Cloud Platform
- Správa vašeho nastavení služby Google API

Tato oprávnění nám umožňují podporu pokročilých funkcí pro správu serverů Outline, mimo jiné:

- výběr správného fakturačního účtu,
- vytvoření nového projektu k uspořádání serverů Outline,
- vypsání dostupných datových center,
- vytváření nových virtuálních počítačů, kde se bude spouštět Outline,
- konfigurace softwaru Outline na novém virtuálním počítači.

## Zrušení oprávnění

Oprávnění Správce Outline ke službě Google Cloud Platform můžete zrušit na stránce [Můj účet](https://myaccount.google.com/permissions). Pokud oprávnění zrušíte, všechny servery, které jste vytvořili pomocí automatického nastavení, poběží dál, ale už se nebudou zobrazovat ve Správci Outline. Abyste k nim opět získali přístup, jednoduše se znovu připojte ke službě Google Cloud Platform tak, že zahájíte automatické nastavení.

## Uspořádání projektu Outline

Automatické nastavení služby Google Cloud dovoluje uspořádat vaše servery Outline v jednom [projektu Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects). Projekt se vytváří při prvním použití automatického nastavení. Navržené ID projektu začíná řetězcem „Outline-“, po kterém následuje řetězec náhodných znaků. Pokud chcete, můžete při vytváření určit jiné ID projektu. Projekt bude mít název „Servery Outline“.

## Fakturační účet

S projekty Google Cloud je nutné propojit tzv. fakturační účet, který určuje platební údaje. Při prvním použití automatického nastavení Google Cloud budete vyzváni k zadání fakturačního účtu, který se přiřadí k vašim serverům Outline. Někdy se server zastaví, protože dochází k potížím s fakturačním účtem. Pokud se to stane, přihlaste se do služby [Google Cloud Console](https://console.cloud.google.com/getting-started), vyhledejte projekt Google Cloud spojený s aplikací Outline (má název „Servery Outline“) a aktualizujte nastavení fakturace.

## Zničení serverů

Pokud chcete servery vytvořené pomocí automatického nastavení zničit, uděláte to nejsnáz ve Správci Outline. Jestliže však servery chcete zničit sami, můžete se přihlásit do služby [Google Cloud Console](https://console.cloud.google.com/getting-started), vyhledat projekt vytvořený během úvodního nastavení (s názvem „Servery Outline“) a smazat v něm zdroje nebo projekt vypnout.

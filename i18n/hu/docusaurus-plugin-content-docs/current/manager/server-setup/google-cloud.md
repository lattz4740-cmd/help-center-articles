---
title: A Google Cloud automatikus beállítása
sidebar_label: A Google Cloud automatikus beállítása
---

## Áttekintés

Az Outline Manager tartalmaz egy funkciót, amely automatikusan konfigurálja az Outline szervert egy, a Google Cloudon futó szerveren. Ha úgy dönt, hogy használja ezt a funkciót, az Outline Manager arra kéri, hogy jelentkezzen be a Google-fiókjával. Ezzel Ön megad bizonyos [OAuth](https://developers.google.com/identity/protocols/oauth2)-engedélyeket az Outline Manager helyi telepítésének, hogy az konfigurálni tudja a Google Cloud-fiókját.

 Ha nem szeretné megadni ezeket az engedélyeket, az Outline Manager speciális beállítási útmutatásának megfelelően konfigurálhatja az Outline-t a Google Cloud Platformon történő futtatásra.

## Engedélyek megadva

Ahhoz, hogy az Outline Manager automatikusan elvégezhesse a beállítást, a következő engedélyekre van szüksége az Ön Google-fiókjától.

## Google Cloud Platform

- Google Compute Engine-erőforrások megtekintése és kezelése
- A Google Cloud-szolgáltatásban szereplő adatok, illetve a Google-fiókjához tartozó e-mail-cím megtekintése

## Alapvető fiókadatok

- Az Ön elsődleges Google-fiókjához tartozó e-mail-cím megtekintése
- Az Ön összekapcsolása a Google rendszerében lévő személyes adataival

## További hozzáférés

- Az Ön Cloud Platform-projektjeinek kezelése
- Az Ön Google Cloud Platform-számlázási fiókjainak megtekintése és kezelése
- A Google API-szolgáltatáskonfiguráció kezelése

Ezek az engedélyek lehetővé teszik, hogy speciális funkciókat biztosítsunk az Outline-szerverek kezelésére, például:

- A helyes számlázási fiók kiválasztása
- Új projekt létrehozása az Outline szerverek csoportosítására
- A rendelkezésre álló adatközpontok listázása
- Új virtuális gépek létrehozása az Outline futtatására
- Az Outline konfigurálása az új virtuális gépen

## Az engedélyek visszavonása

A [Saját fiók](https://myaccount.google.com/permissions) oldalon visszavonhatja az Outline Managertől a Google Cloud Platformhoz való hozzáférést. Ha visszavonja a hozzáférést, az automatikus beállítással létrehozott szerverek továbbra is futni fognak, de többé nem jelennek meg az Outline Managerben. Ha vissza szeretné állítani a hozzáférést, egyszerűen csatlakozzon újra a Google Cloud Platformhoz az automatikus beállítási folyamat elvégzésével.

## Az Outline szervereket egybefogó projekt

A Google Cloud automatizált beállítása egyetlen [Google Cloud-projektbe](https://cloud.google.com/resource-manager/docs/creating-managing-projects) csoportosítja az Outline szervereket. A projekt az automatikus beállítás első használata során jön létre. A javasolt projektazonosító az „Outline-” karakterlánccal kezdődik, ezt pedig egy véletlenszerű karaktersorozat követi. A létrehozás alkalmával más projektazonosítót is megadhat. A projekt neve „Outline servers” lesz.

## Számlázási fiók

A Google Cloud-projektekhez szükséges egy összekapcsolt „számlázási fiók”, amely meghatározza a fizetési információkat. Amikor először használja az automatikus Google Cloud-telepítést, meg kell adnia az Outline-szervereihez társítandó számlázási fiókot. Egyes esetekben a szerver leáll, mert probléma van a számlázási fiókkal. Ebben az esetben jelentkezzen be a [Google Cloud Console-ra](https://console.cloud.google.com/getting-started), keresse meg az Outline-hoz társított Google Cloud-projektet („Outline servers” a neve), és frissítse a számlázási beállításokat.

## A szerverek megsemmisítése

Ha meg szeretné semmisíteni az automatizált beállítással létrehozott szervereit, ezt az Outline Managerben teheti meg a legegyszerűbben. Ha azonban maga szeretné megsemmisíteni a szervereket, bejelentkezhet a [Google Cloud Console-ra](https://console.cloud.google.com/getting-started), megkeresheti az első beállítás során létrehozott projektet („Outline servers” a neve), és törölheti az ott található erőforrásokat, vagy leállíthatja a projektet.

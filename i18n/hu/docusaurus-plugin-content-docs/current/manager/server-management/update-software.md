---
title: "Hogyan frissíthetem az Outline-szerverem szoftverét?"
sidebar_label: "Hogyan frissíthetem az Outline-szerverem szoftverét?"
---

A rendszer automatikusan a legújabb biztonsági fejlesztésekkel frissíti az Outline-szervereket, hogy mindig a legkorszerűbb Outline-technológiát vehesse igénybe. Az automatizált frissítési folyamatot a [Watchtower](https://github.com/containrrr/watchtower) nevű nyílt forráskódú könyvtár teszi lehetővé, amely rendszeresen ellenőrzi és frissíti az Outline szoftverét tartalmazó dockerképet.

Ha pedig az Outline Manager segítségével telepíti az Outline szolgáltatást, a rendszer egy cron-feladatot is beállít, amely automatikusan frissíti a szerveren futó szoftvert az Ubuntu [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) (Felügyelet nélküli frissítések) funkciójával, és szükség esetén újraindítja a szoftvert. Ne feledje, hogy ezt Advanced Mode (Speciális mód) üzemmódban a rendszer a meglévő konfiguráció megőrzése érdekében nem hajtja végre, azt feltételezve, hogy a gazdagépet az Outline futtatásán kívül más célokra is használják.

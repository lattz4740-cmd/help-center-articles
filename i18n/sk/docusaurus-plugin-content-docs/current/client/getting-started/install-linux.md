---
title: Inštalácia aplikácie Outline Client v systéme Linux
sidebar_label: Inštalácia aplikácie Outline Client v systéme Linux
---

Od verzie aplikácie Outline Client 1.15 budú všetky budúce verzie vydávané ako balíky Debian pre operačné systémy Linux. Viac o tom, ktoré operačné systémy podporujeme, sa dozviete v [minimálnych systémových požiadavkách](/client/getting-started/system-requirements).

## Inštalácia aplikácie Outline Client pre distribúcie systému Linux založené na systéme Debian (odporúčané)

Spustite nasledujúce príkazy:

1. Nainštalujte kľúč odkladacieho priestoru služby Outline a pridajte odkladací priestor.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Aktualizujte zoznam balíčkov apt a nainštalujte najnovšiu verziu aplikácie Outline Client.

```
sudo apt update
sudo apt install outline-client
```

Ak chcete skontrolovať alebo nainštalovať budúce aktualizácie, znova spustite príkazy v druhom kroku. Upozorňujeme, že automatická aktualizácia v aplikácii je v prípade aplikácie Outline Client v systéme Linux zakázaná od verzie 1.15.

Ak chcete aplikáciu Outline Client odinštalovať, spustite nasledujúci príkaz:

```
sudo apt purge outline-client
```

## Alternatívna možnosť

1. Stiahnite si najnovší balík Debian aplikácie Outline Client z webu [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb).
2. Ak chcete nainštalovať balík, spustite v príkazovom riadku nasledujúce príkazy.

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Aktualizácie kontrolujte manuálne, pretože automatické aktualizácie v aplikácii sú v prípade aplikácie Outline Client v systéme Linux zakázané od verzie 1.15.

4. Ak chcete aplikáciu Outline Client odinštalovať, spustite v príkazovom riadku tento príkaz:

```
sudo apt purge outline-client
```

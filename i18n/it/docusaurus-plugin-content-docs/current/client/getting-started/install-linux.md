---
title: Installa client Outline su Linux
sidebar_label: Installa client Outline su Linux
---

A partire dalla versione 1.15 di client Outline, tutte le versioni future verranno rilasciate come pacchetti Debian per i sistemi operativi Linux. Consulta i nostri [requisiti di sistema minimi](/client/getting-started/system-requirements) per saperne di più sui sistemi operativi supportati.

## Installa client Outline per le distribuzioni Linux basate su Debian (consigliato)

Esegui questi comandi:

1. Installa la chiave del repository di Outline e aggiungi il repository.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Aggiorna l'elenco dei pacchetti apt e installa l'ultima versione del client Outline.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Per controllare la disponibilità di aggiornamenti futuri o installarli, esegui di nuovo i comandi del Passaggio 2. Tieni presente che l'aggiornamento automatico in-app è disabilitato per client Outline su Linux a partire dalla versione 1.15.

Per disinstallare client Outline, esegui il seguente comando:

```
sudo apt purge outline-client
```

## Alternativa

1. Scarica l'ultimo pacchetto Debian di client Outline da [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Nella riga di comando, esegui i seguenti comandi per installare il pacchetto
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Controlla manualmente la disponibilità degli aggiornamenti, poiché l'aggiornamento automatico in-app è disattivato per client Outline su Linux a partire dalla versione 1.15.
4. Per disinstallare client Outline, esegui il seguente comando nella riga di comando:
   ```
   sudo apt purge outline-client
   ```

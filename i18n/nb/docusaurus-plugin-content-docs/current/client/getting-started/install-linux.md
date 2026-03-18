---
title: "Slik installerer du Outline-klienten på Linux"
sidebar_label: "Slik installerer du Outline-klienten på Linux"
---

Fra og med Outline-klientversjon 1.15 lanseres alle fremtidige versjoner som Debian-pakker på Linux-operativsystemer. Gå gjennom [minimumskravene til systemet](/client/getting-started/system-requirements) for å finne ut mer om hvilke operativsystemer vi støtter.

## Installer Outline-klienten på Debian-baserte Linux-distribusjoner (anbefales)

Kjør følgende kommandoer:

1. Installer nøkkelen til Outline-repositoriet, og legg til repositoriet.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Oppdater apt-pakkelisten, og installer den nyeste versjonen av Outline-klienten.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

For å se etter eller installere fremtidige oppdateringer kjører du kommandoene i trinn 2 på nytt. Merk at automatiske oppdateringer i appen er deaktivert for Outline-klienten på Linux fra og med versjon 1.15.

For å avinstallere Outline-klienten kjører du følgende kommando:

```
sudo apt purge outline-client
```

## Alternativ fremgangsmåte

1. Last ned den nyeste Debian-pakken for Outline-klienten fra [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Kjør følgende kommandoer i kommandolinjen for å installere pakken.
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Se etter oppdateringer manuelt, siden automatiske oppdateringer i appen er deaktivert for Outline-klienten på Linux fra og med versjon 1.15.
4. For å avinstallere Outline-klienten kjører du følgende kommando i kommandolinjen:
   ```
   sudo apt purge outline-client
   ```

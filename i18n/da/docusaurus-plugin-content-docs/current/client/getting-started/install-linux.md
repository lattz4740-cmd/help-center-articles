---
title: "Installation af Outline-klienten på Linux"
sidebar_label: "Installation af Outline-klienten på Linux"
---

Fra og med Outline Client-version 1.15 udgives alle fremtidige versioner som Debian-pakker til Linux-operativsystemer. Gennemgå vores [minimumskrav til systemet](/client/getting-started/system-requirements) for at få flere oplysninger om, hvilke operativsystemer vi understøtter.

## Installer Outline Client til Debian-baserede Linux-distributioner (anbefales)

Kør følgende kommandoer:

1. Installer Outlines lagernøgle, og tilføj lageret.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Opdater apt-pakkelisten, og installer den nyeste version af Outline Client.

```
sudo apt update
sudo apt install outline-client
```

Hvis du vil tjekke efter eller installere fremtidige opdateringer, skal du køre kommandoerne under trin 2 igen. Vær opmærksom på, at automatisk opdatering i appen er deaktiveret for Outline-klienten på Linux fra og med version 1.15.

Du kan afinstallere Outline Client ved at køre følgende kommando:

```
sudo apt purge outline-client
```

## Alternativ mulighed

1. Download den nyeste Debian-pakke til Outline Client fra [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Kør følgende kommandoer på kommandolinjen for at installere pakken

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Søg efter opdateringer manuelt, da automatisk opdatering i appen er deaktiveret for Outline Client i Linux fra og med version 1.15.

4. Hvis du vil afinstallere Outline Client, skal du køre følgende kommando i kommandolinjen:

```
sudo apt purge outline-client
```

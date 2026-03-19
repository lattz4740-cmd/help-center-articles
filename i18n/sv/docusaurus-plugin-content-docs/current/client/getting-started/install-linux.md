---
title: "Installera Outline-klienten på Linux"
sidebar_label: "Installera Outline-klienten på Linux"
---

Från och med Outline Client-version 1.15 släpps alla framtida versioner som Debian-paket för Linux-operativsystem. Sätt dig in i [minimisystemkraven](/client/getting-started/system-requirements) om du vill veta mer om vilka operativsystem vi har stöd för.

## Installera Outline-klienten för Debian-baserade Linux-distributioner (rekommenderas)

Kör följande kommandon:

1. Installera Outlines lagringsnyckel och lägg till lagringsplatsen.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Uppdatera apt-paketlistan och installera den senaste versionen av Outline-klienten.

```
sudo apt update
sudo apt install outline-client
```

Om du vill söka efter eller installera framtida uppdateringar kör du kommandona i steg 2 igen. Tänk på att automatisk uppdatering i appen har inaktiverats för Outline-klienten på Linux från och med version 1.15.

Kör följande kommando om du vill avinstallera Outline-klienten:

```
sudo apt purge outline-client
```

## Alternativ

1. Ladda ned det senaste Debian-paketet för Outline-klienten från [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Kör följande kommandon på kommandoraden för att installera paketet

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Sök efter uppdateringar manuellt eftersom automatisk uppdatering i appen har inaktiverats för Outline-klienten på Linux från och med version 1.15.

4. Om du vill avinstallera Outline-klienten kör du följande kommando på kommandoraden:

```
sudo apt purge outline-client
```

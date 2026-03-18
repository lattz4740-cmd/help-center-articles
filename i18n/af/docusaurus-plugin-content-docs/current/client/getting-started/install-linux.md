---
title: "Installering van Outline-kliënt op Linux"
sidebar_label: "Installering van Outline-kliënt op Linux"
---

Vanaf Outline Client-weergawe 1.15 sal alle toekomstige weergawes vir Linux-bedryfstelsels as Debian-pakkette vrygestel word. Gaan ons [minimum stelselvereistes](/client/getting-started/system-requirements) na vir meer inligting oor watter bedryfstelsels ons steun.

## Installeer Outline Client vir Debian-gegronde Linux-verspreidings (aanbeveel)

Voer die volgende opdragte uit:

1. Installeer Outline se bewaarpleksleutel en voeg die bewaarplek by.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Dateer die apt-pakketlys op en installeer die jongste weergawe van Outline Client.

```
sudo apt update
sudo apt install outline-client
```

Voer die opdragte in stap 2 weer uit om vir toekomstige opdaterings te kyk of dit te installeer. Let daarop dat outo-opdatering in die app vanaf weergawe 1.15 vir Outline Client op Linux gedeaktiveer is.

Voer die volgende opdrag uit om Outline Client te deïnstalleer:

```
sudo apt purge outline-client
```

## Alternatiewe opsie

1. Laai die jongste Debian-pakket vir Outline Client af by [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Voer die volgende opdragte in die opdragreël uit om die pakket te installeer

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Kyk self vir opdaterings aangesien outo-opdatering in die app vanaf weergawe 1.15 vir Outline Client op Linux gedeaktiveer is.

4. Voer die volgende opdrag in die opdragreël uit om Outline Client te deïnstalleer:

```
sudo apt purge outline-client
```

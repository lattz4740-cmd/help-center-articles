---
title: "De Outline-client installeren op Linux"
sidebar_label: "De Outline-client installeren op Linux"
---

Vanaf versie 1.15 van de Outline-client worden alle toekomstige versies uitgebracht als Debian-pakketten voor Linux-besturingssystemen. Neem onze [minimale systeemvereisten](/client/getting-started/system-requirements) door voor meer informatie over de besturingssystemen die we ondersteunen.

## De Outline-client installeren voor op Debian gebaseerde Linux-distributies (aanbevolen)

Voer de volgende opdrachten uit:

1. Installeer de repositorysleutel van Outline en voeg de repository toe.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Update de apt-pakketlijst en installeer de nieuwste versie van de Outline-client.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Als je wilt controleren of er toekomstige updates zijn of deze wilt installeren, voer je de opdrachten bij stap 2 opnieuw uit. Automatisch updaten in de app staat vanaf versie 1.15 uit voor de Outline-client op Linux.

Voer de volgende opdracht uit om de Outline-client te verwijderen:

```
sudo apt purge outline-client
```

## Alternatieve optie

1. Download het nieuwste Debian-pakket voor de Outline-client via [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb).
2. Voer de volgende opdrachten uit via de opdrachtregel om het pakket te installeren:
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Controleer handmatig op updates, omdat automatische updates in de app vanaf versie 1.15 zijn uitgezet voor de Outline-client op Linux.
4. Als je de Outline-client wilt verwijderen, voer je de volgende opdracht uit via de opdrachtregel:
   ```
   sudo apt purge outline-client
   ```

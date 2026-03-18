---
title: "Outline-Client unter Linux installieren"
sidebar_label: "Outline-Client unter Linux installieren"
---

Ab der Version 1.15 des Outline-Clients werden alle zukünftigen Versionen als Debian-Pakete für Linux-Betriebssysteme veröffentlicht. Weitere Informationen zu den von uns unterstützten Betriebssystemen finden Sie in den [Mindestanforderungen](/client/getting-started/system-requirements).

## Outline-Client für Debian-basierte Linux-Distributionen installieren (empfohlen)

Führen Sie folgende Befehle aus:

1. Installieren Sie den Repository-Schlüssel von Outline und fügen Sie das Repository hinzu.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Aktualisieren Sie die apt-Paketliste und installieren Sie die aktuelle Version des Outline-Clients.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Wenn Sie nach weiteren Updates suchen oder diese installieren möchten, führen Sie die Befehle in Schritt 2 noch einmal aus. Hinweis: Die automatische App-Aktualisierung ist für den Outline-Client unter Linux ab Version 1.15 deaktiviert.

Führen Sie den folgenden Befehl aus, um den Outline Client zu deinstallieren:

```
sudo apt purge outline-client
```

## Alternative Option

1. Laden Sie das aktuelle Debian-Paket des Outline-Clients unter [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) herunter.
2. Um das Paket zu installieren, führen Sie die folgenden Befehle in der Befehlszeile aus.
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Prüfen Sie manuell nach Updates, da die automatische App-Aktualisierung für den Outline-Client unter Linux ab Version 1.15 deaktiviert ist.
4. Um den Outline-Client zu deinstallieren, führen Sie in der Befehlszeile den folgenden Befehl aus:
   ```
   sudo apt purge outline-client
   ```

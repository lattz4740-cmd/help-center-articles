---
title: Outline’i kliendi installimine Linuxis
sidebar_label: Outline’i kliendi installimine Linuxis
---

Alates Outline’i kliendi versioonist 1.15 antakse kõik tulevased Linuxi operatsioonisüsteemi versioonid välja Debiani pakettidena. Meie toetatavate operatsioonisüsteemide kohta leiate lisateavet meie [minimaalsetest süsteeminõuetest](/client/getting-started/system-requirements).

## Outline’i kliendi installimine Debianil põhinevate Linuxi levituspakettide jaoks (soovitatud)

Käivitage järgmised käsud.

1. Installige Outline’i andmehoidla võti ja lisage andmehoidla.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Värskendage APT paketiloendit ja installige Outline’i kliendi uusim versioon.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Tulevaste värskenduste otsimiseks või installimiseks käivitage uuesti 2. punktis esitatud käsud. Pidage meeles, et alates versioonist 1.15 on Linuxis Outline’i kliendi rakendusesisene automaatne värskendamine keelatud.

Outline’i kliendi desinstallimiseks käivitage järgmine käsk.

```
sudo apt purge outline-client
```

## Teine võimalus

1. Laadige veebilehelt [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) alla uusim Outline’i kliendi Debiani pakett.
2. Paketi installimiseks käivitage käsureal järgmised käsud.
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Otsige värskendusi käsitsi, sest alates versioonist 1.15 on Linuxis Outline’i kliendi rakendusesisene automaatne värskendamine keelatud.
4. Outline’i kliendi desinstallimiseks käivitage käsureal järgmine käsk.
   ```
   sudo apt purge outline-client
   ```

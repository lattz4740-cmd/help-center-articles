---
title: "Pag-install ng Outline Client sa Linux"
sidebar_label: "Pag-install ng Outline Client sa Linux"
---

Simula sa bersyon 1.15 ng Outline Client, ire-release ang lahat ng bersyon sa hinaharap bilang mga Debian package para sa mga Linux operating system. Suriin ang aming [mga minimum na requirement sa system](/client/getting-started/system-requirements) para sa higit pang impormasyon tungkol sa kung aling mga operating system ang sinusuportahan namin.

## I-install ang Outline Client para sa mga Debian-based na distribution ng Linux (Inirerekomenda)

Patakbuhin ang mga sumusunod na command:

1. I-install ang key ng repository ng Outline at idagdag ang repository.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. I-update ang listahan ng apt package at i-install ang pinakabagong bersyon ng Outline Client.

```
sudo apt update
sudo apt install outline-client
```

Para tingnan kung may mga update o i-install ang mga update sa hinaharap, patakbuhin ulit ang mga command sa Hakbang 2. Tandaan na naka-disable ang awtomatikong pag-update sa app para sa Outline Client sa Linux, simula sa bersyon 1.15.

Para i-uninstall ang Outline Client, patakbuhin ang sumusunod na command:

```
sudo apt purge outline-client
```

## Alternatibong Opsyon

1. I-download ang pinakabagong Debian package ng Outline Client mula sa [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Patakbuhin ang mga sumusunod na command sa linya ng command para i-install ang package

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Manual na tingnan kung may mga update, dahil naka-disable ang awtomatikong pag-update sa app para sa Outline Client sa Linux, simula sa bersyon 1.15.

4. Para i-uninstall ang Outline Client, patakbuhin ang sumusunod na command sa linya ng command:

```
sudo apt purge outline-client
```

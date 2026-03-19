---
title: "Outline-asiakassovelluksen asentaminen Linuxille"
sidebar_label: "Outline-asiakassovelluksen asentaminen Linuxille"
---

Outline-asiakassovelluksen versiosta 1.15 alkaen kaikki tulevat versiot julkaistaan Debian-paketteina Linux-käyttöjärjestelmille. Katso [järjestelmän vähimmäisvaatimuksista](/client/getting-started/system-requirements), mitä käyttöjärjestelmiä tuetaan.

## Outline-asiakassovelluksen asentaminen Debian-pohjaisille Linux-laitteille (suositus)

Suorita seuraavat komennot:

1. Asenna Outlinen datasäilön avain ja lisää datasäilö.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Päivitä apt-pakettilista ja asenna Outline-asiakassovelluksen uusin versio.

```
sudo apt update
sudo apt install outline-client
```

Jos haluat tarkistaa tai asentaa tulevia päivityksiä, suorita vaiheen 2 komennot uudelleen. Huom. Sovelluksen sisäinen automaattinen päivitys on poistettu käytöstä Outline-asiakassovelluksessa Linuxilla versiosta 1.15 alkaen.

Voit poistaa Outline-asiakassovelluksen suorittamalla seuraavan komennon:

```
sudo apt purge outline-client
```

## Vaihtoehto

1. Lataa uusin Outline-asiakassovelluksen Debian-paketti osoitteesta [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Asenna paketti suorittamalla seuraavat komennot komentorivillä:

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Tarkista päivitykset manuaalisesti, koska sovelluksen sisäinen automaattinen päivitys on poistettu käytöstä Outline-asiakassovelluksessa Linuxilla versiosta 1.15 alkaen.

4. Poista Outline-asiakassovelluksen asennus suorittamalla komentorivillä seuraava komento:

```
sudo apt purge outline-client
```

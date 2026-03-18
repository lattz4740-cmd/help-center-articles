---
title: Instaliranje Outline Clienta na Linuxu
sidebar_label: Instaliranje Outline Clienta na Linuxu
---

Od verzije Outline Clienta 1.15 sve buduće verzije izdavat će se kao Debian paketi za operativne sustave Linux. Više informacija o tome koje operativne sustave podržavamo potražite u našim [minimalnim preduvjetima sustava](/client/getting-started/system-requirements).

## Instaliranje Outline Clienta za Debian distribucije Linuxa (preporučeno)

Pokrenite sljedeće naredbe:

1. Instalirajte ključ spremišta za Outline i dodajte spremište.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Ažurirajte popis apt paketa i instalirajte najnoviju verziju Outline Clienta.

```
sudo apt update
sudo apt install outline-client
```

Da biste provjerili jesu li dostupna buduća ažuriranja ili ih instalirali, ponovo pokrenite naredbe u 2. koraku. Automatsko ažuriranje u aplikaciji onemogućeno je za Outline Client na Linuxu od verzije 1.15.

Da biste deinstalirali Outline Client, pokrenite sljedeću naredbu:

```
sudo apt purge outline-client
```

## Alternativna opcija

1. Preuzmite najnoviji Debian paket Outline Clienta s web-lokacije [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Pokrenite sljedeće naredbe u naredbenom retku da biste instalirali paket

```
wget-O./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Ručno potražite ažuriranja jer je automatsko ažuriranje u aplikaciji onemogućeno za Outline Client na Linuxu od verzije 1.15.

4. Da biste deinstalirali Outline Client, u naredbenom retku pokrenite sljedeću naredbu:

```
sudo apt purge outline-client
```

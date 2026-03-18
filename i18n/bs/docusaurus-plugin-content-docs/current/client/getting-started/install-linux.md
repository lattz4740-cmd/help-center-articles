---
title: Instaliranje klijenta za Outline na Linuxu
sidebar_label: Instaliranje klijenta za Outline na Linuxu
---

Od verzije 1.15 klijenta za Outline sve buduće verzije će se izdavati kao paketi Debian za operativne sisteme Linux. Pregledajte naše [minimalne zahtjeve sistema](/client/getting-started/system-requirements) za više informacija o operativnim sistemima koje podržavamo.

## Instalirajte klijent za Outline za distribucije Linuxa zasnovane na Debianu (preporučeno)

Izvršite sljedeće komande:

1. Instalirajte Outlineov ključ repozitorija i dodajte repozitorij.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Ažurirajte listu paketa APT i instalirajte najnoviju verziju klijenta za Outline.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Da provjerite ili instalirate buduća ažuriranja, ponovo izvršite komande iz 2. koraka. Napominjemo da je automatsko ažuriranje u aplikaciji onemogućeno za klijent za Outline u Linuxu, počevši od verzije 1.15.

Da deinstalirate klijent za Outline, izvršite sljedeću komandu:

```
sudo apt purge outline-client
```

## Alternativna opcija

1. Preuzmite najnoviji paket Debian za klijent za Outline s [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Da instalirate paket, izvršite sljedeće komade u komandnoj liniji
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Ručno provjerite ažuriranja, jer je automatsko ažuriranje u aplikaciji onemogućeno za klijent za Outline u Linuxu, počevši od verzije 1.15.
4. Da deinstalirate klijent za Outline, izvršite sljedeću komandu u komandnoj liniji:
   ```
   sudo apt purge outline-client
   ```

---
title: Instalarea clientului Outline pe Linux
sidebar_label: Instalarea clientului Outline pe Linux
---

Începând cu versiunea 1.15 a clientului Outline, toate versiunile viitoare vor fi lansate ca pachete Debian pentru sistemele de operare Linux. Consultați [cerințele minime de sistem](/client/getting-started/system-requirements) pentru mai multe informații despre sistemele de operare pe care le acceptăm.

## Instalați clientul Outline pentru distribuțiile Linux bazate pe Debian (recomandat)

Rulați următoarele comenzi:

1. instalați cheia directorul Outline și adăugați directorul;
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. actualizați lista de pachete apt și instalați cea mai recentă versiune a clientului Outline.

```
sudo apt update
sudo apt install outline-client
```

Pentru a verifica sau a instala actualizări viitoare, rulați din nou comenzile din Pasul 2. Rețineți că actualizarea automată în aplicație este dezactivată pentru clientul Outline pe Linux, începând cu versiunea 1.15.

Pentru a dezinstala clientul Outline, rulați comanda de mai jos

```
sudo apt purge outline-client
```

## Opțiune alternativă

1. Descărcați cel mai recent pachet al clientului Outline pentru Debian de la [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Executați următoarele comenzi în linia de comandă pentru a instala pachetul

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Verificați manual dacă există actualizări, deoarece actualizarea automată în aplicație este dezactivată pentru clientul Outline pe Linux, începând cu versiunea 1.15.

4. Pentru a dezinstala clientul Outline, rulați următoarea comandă în linia de comandă:

```
sudo apt purge outline-client
```

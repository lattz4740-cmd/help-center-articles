---
title: Instalace Klienta Outline v systému Linux
sidebar_label: Instalace Klienta Outline v systému Linux
---

Od verze 1.15 Klienta Outline budou všechny budoucí verze pro operační systémy Linux vydávány jako balíčky Debian. Další informace o tom, které operační systémy podporujeme, najdete v [minimálních systémových požadavcích](/client/getting-started/system-requirements).

## Instalace Klienta Outline v distribucích Linuxu založených na Debianu (doporučeno)

Spusťte následující příkazy:

1. Nainstalujte klíč repozitáře od Outline a repozitář přidejte.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Aktualizujte seznam balíčků APT a nainstalujte nejnovější verzi Klienta Outline.

```
sudo apt update
sudo apt install outline-client
```

Až budete v budoucnu chtít ověřit, zda jsou k dispozici aktualizace, nebo je nainstalovat, spusťte příkazy uvedené v kroku 2 znovu. Upozorňujeme, že automatické aktualizace v aplikaci jsou u Klienta Outline pro Linux od verze 1.15 vypnuté.

Pokud chcete Klienta Outline odinstalovat, spusťte následující příkaz:

```
sudo apt purge outline-client
```

## Alternativní možnost

1. Stáhněte si nejnovější balíček Klienta Outline pro Debian z adresy [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb).
2. Balíček nainstalujete spuštěním následujících příkazů z příkazového řádku:

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Aktualizace kontrolujte ručně, protože automatické aktualizace v aplikaci jsou u Klienta Outline pro Linux od verze 1.15 vypnuté.

4. Pokud chcete Klienta Outline odinstalovat, spusťte z příkazového řádku následující příkaz:

```
sudo apt purge outline-client
```

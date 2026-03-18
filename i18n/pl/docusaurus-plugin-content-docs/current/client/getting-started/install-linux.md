---
title: Instalowanie klienta Outline w Linuksie
sidebar_label: Instalowanie klienta Outline w Linuksie
---

Od wersji 1.15 klienta Outline wszystkie przyszłe wersje będą wydawane jako pakiety Debiana na systemy operacyjne Linux. Aby dowiedzieć się, które systemy operacyjne obsługujemy, zapoznaj się z [minimalnymi wymaganiami systemowymi](/client/getting-started/system-requirements).

## Instalowanie klienta Outline w dystrybucjach Linuksa opartych na Debianie (zalecane)

Uruchom te polecenia:

1. Zainstaluj klucz repozytorium Outline i dodaj je.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Zaktualizuj listę pakietów APT i zainstaluj najnowszą wersję klienta Outline.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Aby sprawdzić, czy są dostępne nowe aktualizacje, lub je zainstalować, ponownie uruchom polecenia z kroku 2. Pamiętaj, że od wersji 1.15 klienta Outline w Linuksie automatyczne aktualizowanie w aplikacji jest wyłączone.

Aby odinstalować klienta Outline, uruchom to polecenie:

```
sudo apt purge outline-client
```

## Opcja alternatywna

1. Pobierz najnowszy pakiet Debiana klienta Outline z adresu [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb).
2. Aby zainstalować pakiet, w wierszu poleceń uruchom te polecenia:
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Sprawdzaj aktualizacje ręcznie, ponieważ od wersji 1.15 klienta Outline w Linuksie automatyczne aktualizowanie w aplikacji jest wyłączone.
4. Aby odinstalować klienta Outline, w wierszu poleceń uruchom to polecenie:
   ```
   sudo apt purge outline-client
   ```

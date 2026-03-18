---
title: Błędy zapory sieciowej
sidebar_label: Błędy zapory sieciowej
---

Możesz napotkać trzy rodzaje problemów z zaporą:

## Zablokowanie przez zaporę sieciową

Jeśli próbujesz zainstalować Outline, korzystając z połączenia z siecią chronioną przez zaporę, na przykład w szkole lub w pracy, na czas instalacji połącz się z inną siecią.

 Jeśli to nie pomoże, skontaktuj się z administratorem sieci i poproś, by zezwolił na połączenie między siecią chronioną przez zaporę a serwerem Outline. Do nawiązania połączenia będzie potrzebny adres IP serwera Outline i numery portów, na których działa usługa (znajdziesz je na końcu skryptu instalacji).

## Zablokowanie przez zaporę urządzenia

Jeśli masz na swoim urządzeniu oprogramowanie, które blokuje połączenia wychodzące z niestandardowymi portami lub nierozpoznane programy (np. ZoneAlarm firmy CheckPoint), sprawdź w dokumentacji urządzenia lub oprogramowania, jak utworzyć wyjątek dla Outline.

## Zablokowanie przez zaporę serwera

Wybrany przez Ciebie dostawca usług chmurowych może wymagać ręcznego utworzenia wyjątków w zaporze sieciowej serwera, by otworzyć porty, na których działa Outline. Po uruchomieniu skryptu instalacji powinny pojawić się dwa losowo wybrane porty, na których na Twoim serwerze działa Outline. Otworzenie tych portów powinno rozwiązać problem.

 Aby utworzyć wyjątki dla zapory sieciowej serwera, poszukaj w dokumentacji informacji o „ufw” i „iptables”:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

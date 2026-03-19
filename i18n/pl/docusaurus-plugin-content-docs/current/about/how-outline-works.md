---
title: Jak działa Outline
sidebar_label: Jak działa Outline
---

### Instalacja serwera

Instalacja serwera Outline może wydawać się prosta, ale w rzeczywistości jest to seria złożonych procesów.

Podczas każdej instalacji Outline jej skrypt uruchamia te procesy:

- Pobranie stabilnej wersji obrazu Shadowbox i zaimportowanie jej za pomocą narzędzia Docker. Obraz jest hostowany w serwisie Quay.io, na stronie [https://quay.io/](https://quay.io/)repository/outline/shadowbox?tab=tags, i obejmuje serwer Outline oraz interfejs Management API, za pomocą którego aplikacja Outline Server Management tworzy i usuwa klucze dostępu, włącza i wyłącza przesyłanie anonimowych danych oraz wykonuje inne działania.
- Zainstalowanie i skonfigurowanie aplikacji Watchtower, która co godzinę będzie sprawdzać, czy nie nastąpiła aktualizacja obrazu. Dzięki temu będziesz mieć pewność, że serwer Outline jest zawsze aktualny oraz korzysta z najnowszych funkcji i zabezpieczeń.
- Uruchomienie serwera WWW służącego do uzyskiwania dostępu do interfejsu Management API na losowym porcie oraz tajnej i losowej ścieżce.
- Utworzenie podpisanego samodzielnie certyfikatu SSL, który pozwala szyfrować działania związane z zarządzaniem serwerem Outline za pomocą protokołu TLS mimo braku nazwy domeny. Niepowtarzalny odcisk cyfrowy tego certyfikatu jest też tworzony i zapisywany w aplikacji Menedżer Outline. Pomaga to zapobiegać atakom typu man in the middle.

Po zainstalowaniu Outline nie jest wymagana żadna konfiguracja.

### Bezpieczeństwo serwera

Outline to oprogramowanie typu open source. Oznacza to, że każdy może zobaczyć jego kod i go ulepszyć, jeśli wykryje luki w zabezpieczeniach. Kod jest hostowany w serwisie

.

Wszystkie zainstalowane serwery Outline aktualizują się automatycznie, gdy jest dostępna nowa wersja oprogramowania. Dzięki temu mamy pewność, że żaden z nich nie używa starszej wersji Outline.

Aby zarządzać kluczami dostępu na serwerze, aplikacja Menedżer Outline współpracuje z usługą zarządzania na serwerze Outline. Usługa ta korzysta z losowego portu oraz tajnej i niepowtarzalnej ścieżki. Usługi zarządzania nie można weryfikować, ponieważ nie odpowiada ona na zapytania, chyba że odwołują się one do tajnej ścieżki, z której korzysta. Komunikacja z usługą zarządzania jest szyfrowana za pomocą

.

Warto też pamiętać, że serwer Outline nie zapisuje logów, więc nawet jeśli zostanie przejęty, nie dojdzie do ujawnienia żadnych danych użytkowników. Więcej informacji znajdziesz

.

W 2018 roku firmy

i

przeprowadziły audyt Outline. Ich raporty są dostępne

### Obsługa ruchu UDP

Outline może działać jako sieć VPN obejmująca cały system. W takim przypadku cały ruch UDP jest przekazywany przez serwer Outline.

### Ruch DNS

Outline przeprowadza wszystkie wyszukiwania DNS przez serwer Outline, a do ich zabezpieczenia używa tej samej metody szyfrowania co w przypadku pozostałej aktywności sieciowej. Serwer Outline będzie przesyłać Twoje zapytania DNS do usługi Dyn Internet Guide lub OpenDNS.

Outline nigdy nie zapisuje Twoich wyszukiwań DNS.

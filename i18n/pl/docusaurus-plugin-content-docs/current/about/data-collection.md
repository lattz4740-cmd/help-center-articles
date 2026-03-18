---
title: Zbieranie danych i informacji
sidebar_label: Zbieranie danych i informacji
---

Outline nie zbiera danych osobowych, chyba że włączysz opcję ich przesyłania. Nie gromadzi też informacji o witrynach, które odwiedzasz, i osobach, z którymi się kontaktujesz, ani informacji o przesyłanych treściach.

 Gdy tworzysz konto na platformie zewnętrznego dostawcy chmury lub logujesz się na nie przy użyciu Menedżera Outline, nie uzyskujemy żadnych informacji, które przekazujesz (takich jak adres e-mail, imię i nazwisko, informacje rozliczeniowe i dane do płatności).

****Informacje zbierane automatycznie****

 Automatycznie zbieramy 2 rodzaje informacji.

 1. Adres IP serwera

Usługa [Quay.io](https://quay.io/) zbiera informacje o adresie IP serwera Outline i udostępnia je nam, gdy serwer automatycznie się aktualizuje, by wprowadzić najnowsze funkcje i ulepszenia zabezpieczeń. Na podstawie adresu IP można zidentyfikować dostawcę usług chmurowych i miejscowość, w której skonfigurowano serwer Outline, ale nie można określić tożsamości osób, które nim zarządzają lub uzyskują do niego dostęp.

 2. Dane techniczne, które nie umożliwiają identyfikacji konkretnej osoby

Jeśli w oprogramowaniu Outline wystąpi poważny błąd lub krytyczny wyjątek albo jeśli ręcznie prześlesz opinię w aplikacji Outline, otrzymamy informacje wymienione poniżej. Wykorzystujemy je tylko do wykrycia i naprawienia problemów ze stabilnością lub działaniem aplikacji.

- Kraj
- Lokalizacja
- Data i godzina wystąpienia błędu lub wyjątku oraz do 100 wcześniejszych zdarzeń, takich jak otwarcie sekcji „Informacje”
- Statystyczne zestawienie komunikatów o wyjątkach
- Nazwa systemu operacyjnego i jego wersja
- Model telefonu (w odpowiednich przypadkach)
- Godzina uruchomienia aplikacji
- Przeglądarka
- Architektura
- Wersja aplikacji Outline i numer kompilacji

Te informacje są przesyłane przy użyciu protokołu HTTPS do Sentry ([sentry.io](https://sentry.io/)), zewnętrznego dostawcy oprogramowania open source do śledzenia błędów. Sentry wykorzystuje różne technologie i usługi zgodne ze standardami branżowymi, by chronić Twoje dane przed nieuprawnionym dostępem, ujawnieniem i wykorzystaniem oraz by nie dopuścić do ich utraty. Jeśli masz pytania dotyczące zasad Sentry, wejdź na [https://sentry.io/security/](https://sentry.io/security/) i [https://sentry.io/privacy/](https://sentry.io/privacy/) lub napisz na adres [security@sentry.io](mailto:security@sentry.io). Dostęp do wszystkich danych dotyczących Outline przechowywanych przez Sentry mają tylko członkowie zespołu Outline.

****Informacje uzyskiwane po wyrażeniu zgody na przekazywanie danych****

 Jeśli wyrazisz zgodę na przekazywanie danych, zespół Outline będzie otrzymywać te informacje:

 1. Dane o użyciu

Każdy serwer Outline automatycznie zbiera informacje – z ostatniej godziny i na podstawie klucza dostępu – o liczbie przesłanych bajtów, czasie, przez jaki użytkownik miał połączenie z serwerem, krajach i systemach, z których pochodziły wykorzystane dane logowania oraz o tym, czy jakieś funkcje zostały włączone lub wyłączone. Nie są zapisywane przesyłane treści ani żadne metadane umożliwiające identyfikację konkretnej osoby (np. loginy, adresy e-mail czy identyfikatory urządzeń). Wszystkie dane są powiązane z identyfikatorem serwera. Instrukcje zmiany identyfikatora serwera znajdziesz [tutaj](/manager/server-management/reset-server-id).

Domyślnie serwery Outline nie udostępniają tych danych zespołowi Outline. Jeśli administrator serwera wyraźnie zgodzi się na udostępnianie danych o użyciu, będą one bezpiecznie przesyłane zespołowi Outline co godzinę. Po 60 dniach dane zostaną zagregowane na poziomie kraju. Administratorzy serwera mogą w każdej chwili zmienić ustawienia udostępniania danych o użyciu w menu „Ustawienia” w aplikacji Menedżer Outline.

Zależy nam na anonimowych danych o użyciu serwera, ponieważ wykorzystujemy je do śledzenia trendów i ulepszania usługi.

Jeśli na przykład administrator serwera zgodzi się na udostępnianie nam danych o użyciu, możemy uzyskać informację, że z serwera o identyfikatorze 12345 korzystano wczoraj przez 3 godziny, w ciągu których przesłano 500 MB danych z trzech kluczy użytych w Stanach Zjednoczonych i Kanadzie przy włączonej funkcji limitu danych.

 2. Twoje uwagi i adres e-mail (jeśli prześlesz opinię)

 W aplikacjach Outline i Menedżer Outline możesz przesyłać opinie do naszego zespołu. Odradzamy podawanie w nich danych umożliwiających identyfikację, jednak jeśli chcesz otrzymać od nas odpowiedź, wypełnij pole adresu e-mail. Automatycznie zbieramy też pewne podstawowe dane, które pozwalają nam uzyskać odpowiedni kontekst. Informacje o tym, jakie dane zbieramy, znajdziesz powyżej w drugim punkcie sekcji „Informacje uzyskiwane automatycznie”.Więcej informacji o procedurach bezpieczeństwa i ochrony prywatności w Outline znajdziesz [tutaj](/about/security-and-privacy).

Jeśli używasz wersji beta aplikacji Outline na urządzeniu z Androidem, możemy korzystać z usługi Google [Firebase](https://firebase.google.com/), by zbierać informacje na potrzeby debugowania. Mogą one być przydatne podczas wykrywania problemów i ulepszania Outline. Więcej informacji na temat zasad ochrony prywatności i bezpieczeństwa w Firebase znajdziesz na stronie: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Jeśli nie chcesz zezwolić Outline na przesyłanie takich informacji przez Firebase, używaj wersji produkcyjnej tej aplikacji.

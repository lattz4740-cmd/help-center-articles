---
title: "Dlaczego nie mogę połączyć się z usługą Outline?"
sidebar_label: "Dlaczego nie mogę połączyć się z usługą Outline?"
---

Istnieje kilka powodów, dla których możesz nie być w stanie połączyć się z usługą Outline:

- **Urządzenie jest**[**odłączone od internetu**](#Internetissues)**.**Czasem urządzenie może zostać chwilowo odłączone od sieci, a aktualizacja ikon informujących o stanie połączenia może trochę potrwać. Urządzenie może też być połączone z siecią lokalną, ale nie mieć połączenia z internetem.
- [**Zapora sieciowa blokuje dostęp**](#FirewallIssues)**do Twojego serwera Outline.**Zdarza się to często, jeśli korzystasz z sieci publicznej, na przykład w szkole lub pracy, albo z darmowej sieci bezprzewodowej.
- **Urządzenie ma**[**zaporę sieciową lub oprogramowanie antywirusowe**](#SoftwareIssues)**, które blokują dostęp do serwera Outline.**
- **Konieczna może być zmiana**[**ustawień telefonu**](#DeviceSettings)**.**
- **Menedżer usługi**[**zlikwidował serwer lub dostawca internetu blokuje żądania**](#ServerIssues)**.**

## Problemy z połączeniem z internetem: {#Internetissues}

### Jak przeprowadzić test:
Wyłącz Outline i sprawdź, czy połączenie z internetem zostało przywrócone.

- Jeśli tak, sprawdź inne sposoby rozwiązania tego problemu (opisane poniżej).
- Jeśli nie, odczekaj chwilę, aby sprawdzić, czy ustawienia połączenia same się zaktualizują.

### Do naprawienia:

Przywróć połączenie urządzenia z internetem:

1. Sprawdź, czy inne urządzenia mogą połączyć się z tą samą siecią. Jeśli inne urządzenia nie są w stanie połączyć się z internetem, może to oznaczać, że sieć nie działa. W takiej sytuacji musisz zaczekać, aż połączenie zostanie przywrócone, lub spróbować rozwiązać ten problem.
2. Jeśli inne urządzenia mogą połączyć się z tą samą siecią, spróbuj wykonać co najmniej jedną z tych czynności, aby przywrócić połączenie z internetem na swoim urządzeniu:
   1. Włącz na urządzeniu tryb samolotowy (dotyczy urządzeń mobilnych).
   2. Uruchom ponownie urządzenie.
   3. Wyłącz urządzenie, odczekaj 2 minuty i włącz je ponownie.

Problemy z zaporą sieciową:

### Jak przeprowadzić test:

1. Odłącz się od bieżącej sieci Wi-Fi lub przewodowej.
2. Połącz się z inną siecią, np. komórkową.
3. Spróbuj ponownie połączyć się z serwerem Outline.

Jeśli możesz nawiązać połączenie w innej sieci, oznacza to, że problem jest po Twojej stronie.

### Do naprawienia:
Skontaktuj się z menedżerem usługi i poproś o zezwolenie na dostęp do serwera Outline lub skorzystaj z innej sieci.

Problemy z zaporą sieciową lub oprogramowaniem antywirusowym:

### Jak przeprowadzić test:

Spróbuj połączyć się z Outline na innym urządzeniu.

Uwaga: pamiętaj, że do korzystania z Outline na innym urządzeniu jest potrzebna aplikacja Outline i klucz dostępu.

### Do naprawienia:

Sprawdź, czy ustawienia zapory sieciowej i oprogramowania antywirusowego zezwalają na ruch przez sieć VPN i Outline.

## Ustawienia urządzenia: {#FirewallIssues}

## Do sprawdzenia: {#SoftwareIssues}
Na urządzeniu z Androidem:

1. Otwórz aplikację Ustawienia.
2. Poszukaj na urządzeniu **ustawień VPN** (zobaczysz tam wszystkie aplikacje VPN, które aktualnie mają dostęp na Twoim telefonie).
3. Jeśli nie widzisz Outline w ustawieniach VPN, odinstaluj aplikację Outline i zainstaluj ją ponownie. Po zainstalowaniu aplikacja Outline powinna automatycznie otrzymać dostęp na urządzeniu.

Upewnij się, że na urządzeniu z Androidem nie masz zainstalowanej żadnej nakładki ekranu, ponieważ może to powodować, że okno uprawnień Outline będzie wyświetlane w tle, przez co nie będzie widoczne na ekranie.

Na urządzeniu z Androidem otwórz Ustawienia > Aplikacje > Specjalny dostęp do aplikacji. Następnie kliknij „Wyświetl nad innymi aplikacjami”. Możesz usunąć dostęp do wszystkich aplikacji, które umożliwiają takie zachowanie.

iOS: przeczytaj [ten artykuł pomocy](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

## Problemy z serwerem: {#DeviceSettings}

### Jak przeprowadzić test:

## Jeśli masz dostęp do większej liczby serwerów, spróbuj połączyć się z innym serwerem. {#ServerIssues}

### Do naprawienia:
Skontaktuj się z menedżerem usługi, aby dowiedzieć się, czy serwer został usunięty. Jeśli tak, poproś o [klucz dostępu](/about/terminology) do innego serwera.

Jeśli serwer był konfigurowany przez Ciebie, spróbuj połączyć się z nim przez Menedżera Outline lub w inny sposób, np. przez [SSH](https://en.wikipedia.org/wiki/Secure_Shell). Jeśli to nie pomoże, możesz sprawdzić w konsoli usług w chmurze, czy serwer jest nadal online.

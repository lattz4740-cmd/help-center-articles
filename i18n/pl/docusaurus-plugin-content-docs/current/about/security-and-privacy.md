---
title: Bezpieczeństwo i prywatność podczas korzystania z Outline
sidebar_label: Bezpieczeństwo i prywatność podczas korzystania z Outline
---

Bezpieczeństwo i prywatność podczas korzystania z Outline

## Jak Outline chroni informacje przesyłane online

Ruch internetowy jest najbardziej narażony na inwigilację podczas przesyłania danych w sieci lokalnej lub krajowej.

Outline dba o poufność połączenia, szyfrując przesyłane w sieci krajowej informacje, dopóki nie dotrą na serwer Outline. Gdy ruch jest szyfrowany przez Outline, osoby obserwujące sieć nie mogą zobaczyć, jakie strony odwiedzasz ani jakie informacje przesyłasz.

Dzięki Outline możesz też korzystać z bezpiecznych narzędzi komunikacji z pełnym szyfrowaniem, które mogą być niedostępne w Twoim kraju.

## Standardy szyfrowania

Outline szyfruje komunikację między Twoim urządzeniem a serwerem Outline za pomocą mechanizmu AEAD i 256-bitowych standardów IETF Chacha2020 i Poly 1305. Algorytmy AEAD zapewniają poufność, spójność i autentyczność szyfrowanych informacji. Doskonale sprawdzają się na nowoczesnym sprzęcie.

## Audyty bezpieczeństwa

W 2018 r. Radically Open Security i Cure53 – dwie niezależne organizacje ds. bezpieczeństwa cyfrowego, które sprawdzają oprogramowanie pod kątem najnowszych standardów bezpieczeństwa – przeprowadziły audyt Outline. W 2022 r. organizacja Radically Open Security przeprowadziła dodatkową kontrolę, a w 2024 r. organizacja Cure53 przeprowadziła kontrolę Outline SDK. Ze sprawozdaniami można zapoznać się tutaj:

- [Raport z testu penetracyjnego przeprowadzonego przez Radically Open Security (marzec 2018 r.)](https://getoutline.org/reports/ros-report.pdf)
- [Raport z testu penetracyjnego i audytu Jigsaw Outline przeprowadzonego przez Cure53 (grudzień 2018 r.)](https://getoutline.org/reports/cure53-report.pdf)
- [Raport z testu penetracyjnego przeprowadzonego przez Radically Open Security (grudzień 2022 r.)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Raport z przeprowadzonego przez Cure53 testu penetracyjnego pakietu SDK usługi Jigsaw Outline VPN (styczeń 2024 r.)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Anonimowe dane i dzienniki

Outline śledzi wykorzystaną przepustowość, czyli bajty przesłane za pomocą poszczególnych kluczy dostępu. Dzięki temu administratorzy serwerów mogą dostosować przepustowość objętą subskrypcją u dostawców usług chmurowych do własnych potrzeb. Nie widzą oni jednak samych informacji, które przechodzą przez serwer Outline.

Dowiedz się więcej o [zbieraniu danych i informacji](https://getoutline.org/policies/data-collection) przez Outline.

---

## Najczęstsze pytania dotyczące bezpieczeństwa i prywatności

## Czy Outline może zapewnić mi anonimowość w internecie?

Nie, Outline nie jest narzędziem zapewniającym anonimowość. Służy do ochrony prywatności przed osobami, które mogą monitorować sieć.

Outline nie zapewnia pełnej anonimowości na odwiedzanych stronach – mogą Cię one zidentyfikować, gdy się na nich zalogujesz, a czasem także dzięki rozwiązaniom takim jak sygnatura przeglądarki. W przypadku aplikacji mobilnych większość nowoczesnych smartfonów ma interfejsy API, które za pomocą wbudowanych modułów GPS zapewniają zainstalowanym aplikacjom dostęp do danych o lokalizacji niezależnie od ustawień serwera proxy.

Zwykle sieci VPN mają rozbudowane zabezpieczenia, zwłaszcza przed monitorowaniem działań użytkowników w internecie, ale aktywność online zawsze wiąże się z ryzykiem. Jeśli dostawca internetu zna Twoją tożsamość i może śledzić Twój ruch w sieci, będzie w stanie ustalić adres IP serwera Outline, nawet wtedy, gdy korzystasz z sieci VPN. Dostawca internetu może wykorzystać te informacje, by zablokować dostęp do serwera Outline lub poznać wzorce Twojego korzystania z sieci, np. typowe godziny Twojej aktywności online, a także Twoją przybliżoną lokalizację.

## Czy ktoś może wykryć, że używam Outline?

To możliwe. Platformy i usługi, z których korzystasz za pomocą Outline, prawdopodobnie będą w stanie stwierdzić, że połączenie pochodzi z serwera w chmurze. Czasem mogą one wywnioskować, że korzystasz z połączenia VPN, ale nie widzą treści, które przesyłasz.

## Czy Outline chroni mnie przed wszystkimi możliwymi zagrożeniami sieciowymi?

Nie. Żadne narzędzie nie chroni przed wszystkimi zagrożeniami w sieci. Outline zapewnia dostęp do otwartego internetu i zwiększa prywatność połączenia, szyfrując ruch, jednak zalecamy podjęcie dodatkowych środków ostrożności, które zapewnią ochronę przed innymi typami ataków, np. przed złośliwym oprogramowaniem czy phishingiem.

Aby wzmocnić zabezpieczenia sieciowe, możesz nawiązać współpracę ze specjalistą ds. zabezpieczeń w Twojej organizacji. Możesz też uzyskać spersonalizowane wskazówki od najlepszych specjalistów ds. zabezpieczeń z [Security Planner](https://securityplanner.org/) – serwisu, którego celem jest przekazywanie jasnych instrukcji dotyczących wyboru odpowiednich narzędzi zapewniających bezpieczeństwo w sieci.

Warto też zapoznać się z innymi usługami [Jigsaw](https://jigsaw.google.com/) związanymi z bezpieczeństwem w sieci, takimi jak [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) i [Ochrona hasła](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Czy używanie sieci VPN jest legalne?

Zanim skonfigurujesz serwer i zaczniesz używać aplikacji Outline, sprawdź przepisy i regulacje obowiązujące w danym kraju oraz warunki dostawcy usług chmurowych, z którego oferty chcesz korzystać.

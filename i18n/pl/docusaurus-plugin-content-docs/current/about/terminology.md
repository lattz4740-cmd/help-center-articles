---
title: Terminologia
sidebar_label: Terminologia
---

## Co to jest VPN?

VPN, czyli wirtualna sieć prywatna (ang. virtual private network), to prywatne połączenie pomiędzy Twoimi urządzeniami a serwerem. Kiedy korzystasz z sieci VPN, Twój ruch jest ukryty przed dostawcą internetu.

Możesz zdecydować się na użycie sieci VPN w tych sytuacjach:

- Gdy chcesz chronić swoje dane podczas korzystania z publicznej sieci Wi-Fi.
- Gdy chcesz zachować prywatność danych przeglądania, tak aby były niedostępne dla dostawcy internetu i instytucji państwowych.
- Gdy chcesz uzyskać dostęp do nieocenzurowanych treści z różnych źródeł z całego świata.

## Czym Outline różni się od tradycyjnych sieci VPN?

Dostawcy internetu mogą łatwo wykrywać i blokować tradycyjne sieci VPN, rozpoznając często występujące w nich protokoły zabezpieczeń i wzory natężenia ruchu. Oprogramowanie Outline ma większą odporność od tradycyjnych sieci VPN, ponieważ zostało stworzone z wykorzystaniem protokołu zaprojektowanego tak, aby było go trudno wykryć, a więc i zablokować. Jest odporne na zaawansowane formy cenzury, w tym na blokowanie według sieci czy adresu IP.

## Czym jest serwer Outline?

Na serwerze Outline działa sieć VPN, z którą mogą łączyć się uprawnieni użytkownicy.

Jeżeli tworzysz nową sieć, możesz jako serwer Outline wykorzystać własny bezpieczny serwer, jeśli taki posiadasz. Możesz też skorzystać z usług jednego z dostawców chmury, takiego jak:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Serwer skonfigurujesz w Menedżerze Outline.

## Kim jest menedżer usługi? {#servicemanager}

Menedżer usługi to osoba odpowiedzialna za konfigurowanie serwera Outline i udostępnianie użytkownikom kluczy dostępu. Odpowiada też za opłaty związane z korzystaniem z serwera.

## Czym jest klucz dostępu? {#accesskey}

Klucza dostępu używa się, aby uzyskać dostęp do serwera Outline i połączyć się z siecią VPN. Dostaniesz go od [menedżera usługi](#servicemanager). Możesz też samodzielnie [skonfigurować serwer Outline](/manager/server-setup/setup-server).

Klucz dostępu wygląda tak (to tylko przykład – w rzeczywistości nie zadziała):

ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Czym jest Menedżer Outline?

Menedżer Outline to aplikacja na komputer, dzięki której menedżer usługi może skonfigurować serwer Outline, wygenerować [klucze dostępu](#accesskey) oraz ustalić limity wykorzystania danych przez poszczególne klucze. Najnowszą wersję Menedżera Outline możesz pobrać [stąd](https://getoutline.org/get-started/#step-1) lub [stąd](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Czym jest klient Outline?

Klient Outline to aplikacja na komputery i komórki pozwalająca na połączenie się z serwerem Outline i uzyskanie dostępu do sieci VPN za pomocą klucza dostępu. Najnowszą wersję klienta Outline możesz pobrać [stąd](https://getoutline.org/get-started/#step-1) lub [stąd](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Czym są limity danych?

Menedżer Outline daje menedżerom usługi możliwość ustawienia 30-dniowego limitu okresowego dla kluczy dostępu, co pozwala zapobiec użyciu zbyt dużych ilości danych i pomaga utrzymać koszty w przewidywalnych granicach. Menedżerowie usługi mogą ustawić domyślny limit obowiązujący w przypadku każdego klucza lub ustawić różne limity dla poszczególnych kluczy, zastępujące limit domyślny. Po ustawieniu limitu wchodzi on od razu w życie i jest egzekwowany co godzinę.

Jeżeli menedżerowie usługi chcą udostępniać dane usłudze Jigsaw, powinni zapoznać się z [zasadami gromadzenia danych](/about/data-collection), aby dowiedzieć się, jak raportowane będzie korzystanie z limitów danych.

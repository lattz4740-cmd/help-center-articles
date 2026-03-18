---
title: Informacje ogólne
sidebar_label: Informacje ogólne
---

Menedżer Outline obejmuje funkcję umożliwiającą automatyczne skonfigurowanie serwera Outline na serwerze działającym w Google Cloud. Jeśli zdecydujesz się skorzystać z tej funkcji, Menedżer Outline poprosi Cię o zalogowanie się na konto Google, które przyzna pewne uprawnienia [OAuth](https://developers.google.com/identity/protocols/oauth2) lokalnej instalacji Menedżera Outline na potrzeby skonfigurowania konta Google Cloud.

Jeśli nie chcesz przyznawać tych uprawnień, możesz wykonać zaawansowane instrukcje konfiguracji w Menedżerze Outline, aby uruchomić Outline w Google Cloud Platform.

## Uprawnienia, które zostaną przyznane

Aby umożliwić automatyczną konfigurację, Menedżer Outline wymaga od konta Google poniższych uprawnień.

## Google Cloud Platform

- Wyświetlanie zasobów Google Compute Engine i zarządzanie nimi
- Wyświetlanie danych z usług Google Cloud i sprawdzanie adresu e-mail Twojego konta Google

## Podstawowe informacje o koncie

- Wyświetlanie podstawowego adresu e-mail Twojego konta Google
- Powiązanie informacji na Twój temat z Twoimi danymi osobowymi dostępnymi w Google

## Dodatkowy dostęp

- Zarządzanie projektami Cloud Platform
- Wyświetlanie kont rozliczeniowych Google Cloud Platform i zarządzanie nimi
- Zarządzanie konfiguracją usługi interfejsów Google API

## Dzięki tym uprawnieniom możemy obsługiwać zaawansowane funkcje zarządzania serwerami Outline, takie jak:

- wybór właściwego konta rozliczeniowego,
- tworzenie nowego projektu w celu uporządkowania serwerów Outline,
- wyświetlanie listy dostępnych centrów danych,
- tworzenie nowych maszyn wirtualnych do uruchamiania Outline,
- konfigurowanie nowej maszyny wirtualnej w Outline.

## Unieważnianie uprawnień

Dostęp do Google Cloud Platform dla Menedżera Outline możesz anulować na stronie [Moje konto](https://myaccount.google.com/permissions). Jeśli anulujesz dostęp, wszystkie serwery utworzone przez Ciebie w ramach automatycznej konfiguracji pozostaną aktywne, ale nie będą już widoczne w Menedżerze Outline. Aby odzyskać do nich dostęp, wystarczy ponownie połączyć się z Google Cloud Platform, rozpoczynając proces automatycznej konfiguracji.

## Organizacja projektu Outline

Automatyczna konfiguracja Google Cloud wykorzystuje 1 [projekt Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects) do porządkowania serwerów Outline. Projekt jest tworzony podczas pierwszego użycia automatycznej konfiguracji. Sugerowany identyfikator projektu rozpoczyna się od „Outline-”, po czym następuje ciąg znaków losowych. Jeśli chcesz, podczas tworzenia możesz wybrać inny identyfikator projektu. Projekt będzie nosił nazwę „Serwery Outline”.

## Konto rozliczeniowe

Z projektami Google Cloud należy połączyć „konto rozliczeniowe”, które określa informacje o płatnościach. Po pierwszym uruchomieniu automatycznej konfiguracji Google Cloud zobaczysz prośbę o podanie konta rozliczeniowego, które będzie powiązane z Twoimi serwerami Outline. Czasami serwer przestaje działać, ponieważ wystąpił problem z kontem rozliczeniowym. W takim przypadku zaloguj się w [Google Cloud Console](https://console.cloud.google.com/), znajdź projekt Google Cloud powiązany z Outline (o nazwie „Serwery Outline”) i zaktualizuj ustawienia płatności.

## Niszczenie serwerów

Jeśli chcesz zniszczyć serwery utworzone w ramach automatycznej konfiguracji, najprostszym sposobem jest skorzystanie z Menedżera Outline. Jeśli jednak wolisz samodzielnie zniszczyć serwery, możesz zalogować się w [Google Cloud Console](https://console.cloud.google.com/), znaleźć projekt utworzony podczas początkowej konfiguracji (o nazwie „Serwery Outline”) i usunąć z niego zasoby lub wyłączyć sam projekt.

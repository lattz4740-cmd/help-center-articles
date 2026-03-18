---
title: Jak ustawić limity danych na kluczach dostępu
sidebar_label: Jak ustawić limity danych na kluczach dostępu
---

Możesz ustawić limit danych, który będzie obowiązywał wszystkie klucze dostępu. Aby to zrobić, otwórz Menedżera Outline i przejdź do Ustawień. Zobaczysz przełącznik Limity danych, który po włączeniu umożliwia ustawienie limitu.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Po ustawieniu limitu możesz sprawdzić, na ile zbliżają się do niego poszczególni użytkownicy – umożliwia to strona klucza dostępu, na której wykres słupkowy pokazuje użycie danych w ciągu ostatnich 30 dni.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Oprócz ustawienia jednego limitu dla wszystkich kluczy dostępu możesz przyznać każdemu kluczowi jego własny limit danych. To ustawienie zawsze zastąpi domyślny limit danych, ale jeśli nie określono domyślnego limitu danych, nadal można ustawić limit danych dla każdego klucza. 

 Aby ustawić limit transferu danych dla danego klucza, otwórz Menedżera Outline, przejdź do karty Połączenia, która zawiera ten klucz, i kliknij menu po prawej stronie wiersza klucza. Tam wybierz Limit danych. Aby zmienić limit danych dla „Mój klucz dostępu”, kliknij ikonę Limity danych ![Ten obraz jest niedostępny, ponieważ: nie masz uprawnień do jego wyświetlenia lub został on usunięty z systemu.](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Wybierz opcję Ustaw niestandardowy limit danych. Po zaznaczeniu tego pola wyboru pojawi się miejsce, w którym można ustawić niestandardowy limit danych dla klucza. Kliknij przycisk ZAPISZ, aby zapisać wybrany limit danych.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Po zapisaniu limitu transferu danych dla wybranego klucza limit będzie widoczny na ekranie głównym obok użycia danych (z ostatnich 30 dni) dla każdego klucza.

Aby usunąć limit danych z klucza dostępu, przejdź do okna „Limit danych” dla danego klucza jak poprzednio, odznacz pole „Ustaw niestandardowy limit danych” i kliknij przycisk ZAPISZ.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

****Najczęstsze pytania dotyczące limitów danych****

****Co to jest 30-dniowy limit danych?****

 Funkcja 30-dniowego limitu danych będzie sumować użycie danych przez poszczególne klucze dostępu z ostatnich 30 dni i zagwarantuje nieprzekroczenie limitu w tym okresie. W efekcie klucz nie może przekroczyć limitu w żadnym okresie 30 dni, również w przypadku miesięcy kalendarzowych liczących 30 dni i mniej. Oznacza to, że dostępne dane poszczególnych użytkowników będą zwiększać się każdego dnia o ilość wykorzystaną 31 dni wcześniej.

Dlaczego Outline używa limitów okresowych?

 Limity okresowe dają gwarancje na każde 30 dni, co oznacza, że są łatwiejsze do konfiguracji niż limit cykliczny (np. odnawiany określonego dnia miesiąca) przy jednoczesnym zapewnieniu podobnych gwarancji. Są one również zgodne z obecnym sposobem wyświetlania użycia danych Outline, a także często stosowanymi narzędziami, takimi jak usługi analityczne i statystyki serwera.

**Jakie dane są wliczane do limitu danych?**

 W rejestrze uwzględniony jest ruch wychodzący z serwera każdego klucza dostępu. Dokładniej rzecz biorąc, oznacza to dane wysłane w imieniu klucza zarówno z serwera, jak i z powrotem do klienta. W praktyce powinno to odpowiadać ruchowi wysyłanemu z klucza do serwera i z powrotem. Mamy więc nadzieję, że liczby te będą zgodne z ilością danych przesyłanych przez użytkowników. Wybraliśmy ruch wychodzący, ponieważ takie rozliczenie stosują dostawcy usług w chmurze, którzy wzięli udział w naszej ankiecie.

**Czy użytkownicy będą powiadamiani o przekroczeniu limitu danych?**

 Obecnie nie. Wielu dostawców usług w chmurze określa limit, na przykład 1 TB na cały miesiąc, który może obsłużyć 10 użytkowników przy wykorzystaniu na poziomie 100 GB lub 100 użytkowników przy wykorzystaniu na poziomie 10 GB. Jest to bardzo dużo i nie spodziewamy się, by wielu użytkowników wykorzystało taką ilość danych. Mamy nadzieję, że po osiągnięciu limitu użytkownicy będą kontaktować się z menedżerami serwerów. Będziemy jednak wdzięczni za informacje, na ile powiadomienia mogą być pomocne w Twoim przypadku. Możesz się z nami skontaktować tutaj.

**Czy użytkownicy będą powiadamiani, gdy zbliżą się do swojego limitu danych?**

 Ilość nowych danych otrzymanych przez użytkownika zbliżającego się do limitu będzie się różnić w poszczególnych dniach, ponieważ zależy od użycia danych sprzed 30 dni. Naszym zdaniem takie powiadomienia nie pomagałyby użytkownikom, a wręcz wprowadzałyby ich w błąd. Będziemy wdzięczni za Twoją opinię na ten temat. Możesz ją przekazać [tutaj](/about/feedback).

**Czy mogę zresetować użycie danych użytkownika?**

 Nie, limit użytkownika zawsze obejmuje ostatnie 30 dni użycia danych. Możesz jednak podnieść użytkownikowi limit danych jego klucza lub utworzyć dla niego nowy klucz.

**Dlaczego część moich użytkowników utraciła dostęp po włączeniu przeze mnie limitów danych?**

 Limity danych są oparte na transferze danych użytkowników z poprzednich 30 dni, który jest rejestrowany niezależnie od tego, czy limity danych zostały włączone, czy nie. Możliwe, że użytkownicy, o których mowa, przekroczyli limit jeszcze przed jego wprowadzeniem. Należy również pamiętać, że wszystkie limity danych są egzekwowane nawet podczas zmiany limitu danych pojedynczego klucza.

**Czy mogę ustawić limit obejmujący cały serwer, np. „1 TB na 30 dni”?**

 Obecnie nie. Chętnie dowiemy się więcej o Twoim przypadku użycia danych [tutaj](/about/feedback).

**Jeśli jest ustawiony domyślny limit danych, a także limit danych na konkretnym kluczu, to który z nich będzie egzekwowany?**

 Limit danych określonego klucza zastąpi domyślny limit danych (jeśli taki został ustawiony).

**Czy mogę określić limit danych dla konkretnego klucza, nie mając ustawionego domyślnego limitu danych?**

 Tak. Nie musisz mieć zdefiniowanego domyślnego limitu, aby ustawić limit danych na jednym kluczu. Możesz na przykład ustawić limit na jeden klucz, który Twoim zdaniem może być często udostępniany, aby zabezpieczyć się przed nadmiernym transferem danych przez ten klucz.

---
title: Jak Outline funguje
sidebar_label: Jak Outline funguje
---

**Instalace serveru**

 ​Instalace Outline možná vypadá jednoduše, ale ve skutečnosti při instalaci serveru na pozadí probíhá docela složitý postup. Při instalaci Outline provede instalační skript tyto kroky:

- Získá stabilní verzi obrazu Shadowbox a importuje ji pomocí Dockeru. Obraz je hostován na webu [Quay.io](https://quay.io/) na adrese [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Obsahuje server Outline a rozhraní Management API, které bude aplikace pro správu serveru Outline později používat k vytváření a odstraňování přístupových klíčů, přihlašování a odhlašování z anonymních metrik v přehledech apod.
- Nainstaluje aplikaci [Watchtower](https://github.com/v2tec/watchtower) a nastaví ji tak, aby každou hodinu kontrolovala aktualizace obrazu. Tak je zajištěno, že je každý server Outline stále aktuální a využívá nejnovější funkce a vylepšení zabezpečení.
- Webový server používaný k přístupu k rozhraní Management API je spuštěn na náhodném portu v tajné a náhodné cestě.
- Vytvoří [certifikát SSL podepsaný sám sebou](https://cs.wikipedia.org/wiki/Certifik%C3%A1t_podepsan%C3%BD_s%C3%A1m_sebou), aby bylo možné správu serveru Outline šifrovat pomocí zabezpečení TLS, i když server nemá název domény. Také vygeneruje unikátní otisk tohoto certifikátu a uloží ho v aplikaci Správce Outline, kde brání útokům MITM.

Po instalaci už není Outline potřeba nijak nastavovat.

**Zabezpečení serveru**

 Software Outline je opensourcový, což znamená, že si kdokoli může zobrazit jeho kód a vylepšovat ho, pokud se objeví nějaké slabiny. Náš kód hostujeme na [GitHubu](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline).

 Všechny nainstalované servery Outline se navíc automaticky aktualizují, kdykoli je uvedena nová verze, takže na žádném serveru Outline neběží staré verze softwaru.

 Při správě přístupových klíčů na serveru komunikuje aplikace Správce Outline se spravující službou na serveru Outline. Spravující služba běží na tajném portu a po tajné a unikátní cestě. Samotná spravující služba je odolná vůči vniknutí, protože nereaguje na dotazy, pokud není specifikovaná správná unikátní trasa. Veškerá komunikace se spravující službou je navíc zašifrovaná pomocí [certifikátu SSL podepsaného sebou samým](https://cs.wikipedia.org/wiki/Certifik%C3%A1t_podepsan%C3%BD_s%C3%A1m_sebou).

 Server Outline si taky neukládá žádné protokoly, takže by žádná uživatelská data neunikla ani při jeho napadení. [Další informace](/about/security-and-privacy). V roce 2018 prošla služba Outline audity společností [Radically Open Security](https://radicallyopensecurity.com/) a [Cure53](https://cure53.de/). Jejich zprávy si můžete přečíst [tady](/about/security-and-privacy).

**Zpracování provozu UDP**

 Outline může fungovat jako systémová síť VPN, což znamená, že všechen provoz UDP je směrován přes server Outline.

**Provoz DNS**

Outline provádí všechna vyhledávání DNS přes server Outline a chrání je pomocí stejného šifrování jako všechnu ostatní síťovou aktivitu. Vaše dotazy na DNS jsou směrovány přes server Outline do služby Dyn Internet Guide, OpenDNS, Cloudflare DNS nebo Quad9 DNS. Outline si vaše dotazy na DNS nikdy neukládá.

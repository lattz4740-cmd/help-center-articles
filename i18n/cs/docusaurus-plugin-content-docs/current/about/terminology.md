---
title: Terminologie
sidebar_label: Terminologie
---

**Co je síť VPN?**

 Virtuální privátní síť (VPN) představuje soukromé spojení mezi vaším zařízením nebo zařízeními a hostitelským serverem. Když používáte síť VPN, poskytovatel internetu nevidí váš provoz. Síť VPN se vám může hodit v následujících situacích:

- na ochranu dat, když používáte veřejnou síť Wi‑Fi,
- k zajištění soukromí údajů o prohlížení, aby je nemohl sledovat poskytovatel internetu ani vládní úřady,
- k přístupu k necenzurovanému obsahu z různých světových zdrojů.

**Jak se Outline liší od tradičních sítí VPN?**

 Tradiční sítě VPN můžou poskytovatelé internetu snadno rozpoznat a blokovat. Všimnou si totiž běžných bezpečnostních protokolů nebo vzorů v objemu provozu. Outline je odolnější než tradiční sítě VPN, protože využívá protokol navržený tak, aby bylo těžké ho detekovat. Proto je složitější síť zablokovat. Outline odolá i sofistikovaným formám cenzury, jako je blokování založené na síti nebo IP adrese.

**Co je server Outline?**

 Na serveru Outline běží síť VPN, ke které se můžou přihlásit oprávnění uživatelé. Pokud vytváříte novou síť, můžete jako server Outline nastavit vlastní bezpečný server, případně můžete využít služby poskytovatele cloudu, jako je:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Server nastavíte v aplikaci Správce Outline.

**Kdo je správce služeb?**

 Správce služeb je člověk, který má na starost nastavení serveru Outline a sdílení přístupových klíčů s uživateli. Obvykle odpovídá taky za náklady na používání serveru. 

**Co je přístupový klíč?**

 Přístupový klíč slouží k přístupu k existujícímu serveru Outline a k připojení k síti VPN. Klíč vám poskytne [správce služeb](#servicemanager) nebo si můžete [nastavit server Outline](/manager/server-setup/setup-server) sami. Přístupový klíč vypadá takto (jedná se o ukázku, tento klíč není funkční): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

**Co je Správce Outline?**

 Správce Outline je desktopová aplikace, která správci služeb umožňuje nastavit server Outline, generovat [přístupové klíče](#accesskey) a určit limity pro použití dat s jedním klíčem. Nejnovější verzi Správce Outline si můžete stáhnout [tady](https://getoutline.org/get-started/#step-3) nebo [tady](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Co je Klient Outline?**

 Klient Outline je aplikace dostupná pro desktop i mobilní zařízení, která dovoluje připojit se k serveru Outline a pomocí přístupového klíče získat přístup k síti VPN. Nejnovější verzi Klienta Outline si můžete stáhnout [tady](https://getoutline.org/get-started/#step-3) nebo [tady](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Co jsou datové limity?**

 Správce Outline umožňuje správcům služeb nastavit pro přístupové klíče 30denní klouzavý datový limit, který pomáhá předcházet nadměrnému používání sítě a zajistit tak předvídatelnost nákladů. Správci služeb můžou nastavit výchozí limit platný pro všechny klíče a navíc odlišné limity pro konkrétní klíče, které výchozí limit přepíšou. Jakmile je limit nastavený, začne se okamžitě uplatňovat a vynucuje se každou hodinu.

Pokud se správci služeb rozhodnou sdílet svoje metriky s týmem Jigsaw, měli by se seznámit se [zásadami shromažďování dat](/about/data-collection), kde najdou podrobnosti o tom, jak se využití datových limitů bude vykazovat.

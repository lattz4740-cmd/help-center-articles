---
title: "Proč se nemůžu připojit ke službě Outline?"
sidebar_label: "Proč se nemůžu připojit ke službě Outline?"
---

Když se vám nedaří připojit ke službě Outline, může to mít několik důvodů:

- **Vaše zařízení**/client/troubleshooting/connection-issues#One[**není připojené k internetu**](#Internetissues)[#Internetissues](#Internetissues)**.**Zařízení se někdy může krátkodobě odpojit od sítě a může chvíli trvat, než se síťové ikony aktualizují. Také je možné, že zařízení je připojené k místní síti, ale nefunguje internet.
- **Přístup**/client/troubleshooting/connection-issues#Two[**k serveru Outline blokuje síťový firewall**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[#FirewallIssues](#FirewallIssues).**To je časté, když používáte veřejnou síť (třeba ve škole nebo v práci), případně bezplatnou bezdrátovou síť.
- **Vaše zařízení má**/client/troubleshooting/connection-issues#Three[**firewall nebo antivirový software**](#SoftwareIssues)[#SoftwareIssues](#SoftwareIssues)**, který blokuje přístup k vašemu serveru Outline.**
- **Vaše**[**nastavení telefonu**](#DeviceSettings)**je možná potřeba změnit.**
- **Váš správce služeb mohl**[**server zničit, případně může váš požadavek blokovat poskytovatel internetu**](#ServerIssues).

## Problémy s připojením k internetu: {#Internetissues}

### Jak problém otestujete:

Vypněte Outline a zkontrolujte, jestli se připojení k internetu obnovilo.

- Pokud ano, podívejte se dál, jak je možné problém řešit.
- Pokud ne, pár minut počkejte, jestli se nastavení připojení samo neaktualizuje.

### Co můžete opravit:

Obnovte připojení zařízení k internetu:

1. Zkontrolujte, zda se ke stejné síti může připojit jiné zařízení. Pokud ne, jde pravděpodobně o problém se sítí a budete muset počkat, až začne znovu fungovat, nebo ji opravit.
2. Pokud se ke stejné síti můžou připojit jiná zařízení, vyzkoušejte následující postupy, jak k ní znovu připojit to svoje:
   1. Zapněte na zařízení režim letadla (funguje na mobilních zařízeních).
   2. Restartujte zařízení.
   3. Zařízení vypněte, dvě minuty počkejte a znovu ho zapněte.

## Potíže se síťovým firewallem: {#FirewallIssues}

### Jak problém otestujete:

1. Odpojte se od sítě, k níž jste momentálně připojeni.
2. Připojte se k jiné síti, například k mobilní.
3. Zkuste se znovu připojit k serveru Outline.

Pokud se můžete připojit, když jste na jiné síti, jedná se o tento problém.

### Co můžete opravit:

Obraťte se na správce služeb a požádejte ho, aby vám povolil přístup k serveru Outline. Můžete taky dál používat alternativní síť.

## Potíže s firewallem nebo antivirovým softwarem: {#SoftwareIssues}
### Jak problém otestujete:
 Zkuste se k Outline připojit z jiného zařízení.

Poznámka: Nezapomeňte, že k tomu potřebujete přístupový klíč a aplikaci Outline.

### Co můžete opravit:
Zkontrolujte v nastavení svého firewallu nebo antivirového softwaru, zda umožňují používat VPN a povolují provoz Outline.

## Nastavení zařízení: {#DeviceSettings}

## Co zkontrolovat: {#ServerIssues}
U zařízení s Androidem:

1. Otevřete aplikaci Nastavení.
2. Vyhledejte v zařízení **nastavení sítě VPN**. Najdete tam všechny aplikace VPN, které momentálně k síti mají z vašeho telefonu přístup.
3. Pokud mezi nimi nevidíte aplikaci Outline, odinstalujte ji a znovu nainstalujte. Aplikace Outline by po instalaci měla od zařízení automaticky získat přístup.

Zkontrolujte, že v zařízení s Androidem nemáte nainstalované žádné aplikace využívající překryvnou vrstvu obrazovky. Ty totiž můžou odsouvat okno s oprávněními k serveru Outline na pozadí, takže není viditelné.

 Na zařízení s Androidem přejděte do nabídky Nastavení > Aplikace > Speciální přístup aplikací. Pak klepněte na Zobrazovat přes ostatní aplikace. Aplikacím, které toto chování umožňují, můžete odebrat přístup.

 Na zařízeních s iOS: Přečtěte si [tento článek podpory](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

### Potíže se serverem:

### Jak problém otestujete:
Pokud máte přístup k více serverům, zkuste se připojit k jinému.

### Co můžete opravit:

Zeptejte se správce služeb, jestli server nebyl zničen. Pokud ano, požádejte o [přístupový klíč](/about/terminology) k jinému serveru.

Pokud jste si server nastavili sami, zkuste se k němu připojit přes Správce Outline nebo jiným způsobem, například přes [SSH](https://cs.wikipedia.org/wiki/Secure_Shell). Pokud se to nepovede, zkuste zkontrolovat v konzoli poskytovatele cloudu (jestliže nějakou má), jestli je server ještě online.

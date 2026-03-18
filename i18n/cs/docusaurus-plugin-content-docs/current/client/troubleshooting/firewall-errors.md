---
title: Chyby firewallu
sidebar_label: Chyby firewallu
---

Můžete se setkat se třemi typy potíží s firewallem:

## Můžete být zablokováni síťovým firewallem.

Pokud se aplikaci Outline snažíte nainstalovat, když jste připojeni k síti chráněné firewallem, například ve škole nebo v práci, zkuste instalaci provést v jiné síti.

Pokud to nepomůže, požádejte správce sítě, ať povolí spojení mezi chráněnou sítí a serverem Outline. Budete muset znát IP adresu svého serveru Outline a porty, na nichž Outline běží. Tyto informace najdete na konci instalačního skriptu.

## Můžete být zablokováni firewallem zařízení.

Pokud máte v zařízení software, který blokuje odchozí spojení u nestandardních portů nebo neznámého softwaru (např. ZoneAlarm od CheckPointu), přečtěte si v dokumentaci k zařízení nebo softwaru, jak vytvořit výjimku pro aplikaci Outline.

## Můžete být zablokováni firewallem serveru.

Poskytovatel cloudu, kterého jste si vybrali, může vyžadovat, abyste ručně vytvořili výjimky pro firewall serveru, aby bylo možné otevírat porty, na nichž Outline běží. Po spuštění instalačního skriptu by se vám měly zobrazit dva náhodně vybrané porty, na nichž Outline běží na vašem serveru. Otevření těchto dvou portů by mělo stačit k vyřešení problému.

 Pokud chcete vytvořit výjimky pro firewall vašeho serveru, doporučujeme vám v dokumentaci vyhledat výrazy ufw a iptables:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

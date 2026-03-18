---
title: Zabezpečení a ochrana soukromí při používání Outline
sidebar_label: Zabezpečení a ochrana soukromí při používání Outline
---

Zabezpečení a ochrana soukromí při používání Outline

## Jak Outline chrání vaši komunikaci online

Internetový provoz je nejvíc ohrožený sledováním, když cestuje po místní síti nebo síti v rámci země.

Outline vám pomáhá udržet komunikaci v soukromí tím, že šifruje internetový provoz, když cestuje po síti v rámci vaší země, dokud nedorazí na server Outline. Když je provoz zašifrován pomocí aplikace Outline, entity, které ho můžou sledovat na síti, nemůžou zobrazit, jaké stránky navštěvujete ani jaké informace se přenášejí.

Outline vám také pomůže získat přístup k bezpečným komunikačním nástrojům, které ve vaší zemi jinak nemusí být dostupné.

## Šifrovací standardy

Outline šifruje komunikaci mezi vaším zařízením a serverem Outline pomocí 256bitové šifry Chacha2020 IETF Poly 1305 s AEAD. Šifry s AEAD zajišťují důvěrnost, integritu a ověření a mají skvělý výkon na moderním hardwaru.

## Bezpečnostní audity

V roce 2018 prošla služba Outline audity společností Radically Open Security a Cure53. Tyto nezávislé organizace se zaměřují na digitální bezpečnost a kontrolují, že software splňuje nejnovější bezpečnostní standardy. Společnost Radically Open Security navíc v roce 2022 provedla další audit služby a společnost Cure53 v roce 2024 provedla audit sady Outline SDK. Zprávy z auditů najdete tady:

- [Zpráva z penetračního testu od společnosti Radically Open Security (březen 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [Zpráva společnosti Cure53 o penetračním testu a auditu služby Jigsaw Outline (prosinec 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [Zpráva z penetračního testu od společnosti Radically Open Security (prosinec 2022)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [Zpráva společnosti Cure53 o penetračním testu sady Jigsaw Outline VPN SDK (leden 2024)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Anonymní metriky a protokoly

Outline sleduje využití připojení, a to jako množství přenesených bajtů pro každý přístupový klíč. Tento údaj umožňuje správcům serverů podle potřeby přizpůsobit připojení zakoupené od poskytovatelů cloudových serverů. Nemůžou ale zobrazit informace, které prošly serverem Outline.

Přečtěte si další podrobnosti o [shromažďování dat a informací](/about/data-collection) ve službě Outline.

---

## Časté dotazy týkající se zabezpečení a ochrany soukromí

## Zajišťuje mi Outline anonymitu online?

Ne, Outline není anonymizační nástroj. Outline chrání vaše soukromí před entitami, které vás mohou sledovat na síti.

Outline vám nenabízí plnou anonymitu na stránkách, které navštěvujete, protože tyto stránky vás stále mohou identifikovat, když se přihlásíte, případně za použití technik, jako je rozeznávání otisku prohlížeče. Co se týče mobilních aplikací, většina moderních telefonů používá rozhraní API, která nainstalovaným aplikacím umožňují získat vaši polohu nezávisle na serveru proxy díky zabudovanému systému GPS.

Sítě VPN obecně nabízejí důležitou ochranu, zvlášť před sledováním na internetu, ale pohyb online je vždy rizikový. I v síti VPN platí, že pokud poskytovatel internetu už zná vaši identitu a může sledovat váš síťový provoz, může také určit IP adresu vašeho serveru Outline. Pomocí této informace je možné zablokovat přístup k serveru Outline a zjistit vzory používání (třeba kdy jste obvykle online) a někdy taky vaši přibližnou polohu.

## Pozná někdo, že používám Outline?

Je to možné. Platformy a služby, které používáte, pravděpodobně poznají, že vaše připojení pochází z cloudového serveru. Někdy můžou zjistit, že používáte síť VPN, ale nebudou moct zobrazit obsah vašeho internetového provozu.

## Chrání mě Outline před všemi kybernetickými hrozbami?

Ne. Žádný nástroj vás neochrání před všemi kybernetickými hrozbami. Outline vám dává přístup k volnému internetu a zvyšuje vaše soukromí šifrováním provozu. Doporučujeme nicméně nasadit i další opatření na ochranu před malwarem, phishingem a podobnými útoky.

Na posílení svého zabezpečení na internetu spolupracujte s odborníkem na kybernetickou bezpečnost ve vaší organizaci. Můžete taky získat doporučení na míru od předních odborníků na webu [Security Planner](https://securityplanner.org/), který má za cíl poskytnout lidem jasné pokyny k výběru správných nástrojů kybernetické bezpečnosti pro jejich podmínky.

Můžete zvážit i nasazení dalších služeb od týmu [Jigsaw](https://jigsaw.google.com/), jako je [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) nebo [Ochrana hesla](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Je legální používat síť VPN?

Než začnete používat služby nebo aplikaci Outline, ověřte, jaké zákony a předpisy platí ve vaší zemi. Projděte si taky smluvní podmínky poskytovatele cloudu, kterého se chystáte využívat.

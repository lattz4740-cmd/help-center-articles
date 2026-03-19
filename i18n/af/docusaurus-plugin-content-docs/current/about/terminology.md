---
title: Terminologie
sidebar_label: Terminologie
---

## Wat is ’n VPN?
 ’n Virtuele private netwerk (VPN) is ’n private verbinding tussen jou toestel(le) en ’n gasheerbediener. Jou verkeer word vir die internetverskaffer versteek wanneer jy ’n VPN gebruik. Jy moet dalk ’n VPN in die volgende scenario’s gebruik:

- Om jou data te beskerm wanneer jy ’n publieke wi-fi-netwerk gebruik
- Om jou blaaierdata privaat te hou van jou internetverskaffer en regeringagentskappe
- Om toegang te kry tot ongesensorde inhoud vanaf verskeie bronne oor die wêreld heen

## Hoe verskil Outline van tradisionele VPN’e?
 Internetverskaffers kan tradisionele VPN’e maklik bespeur en blokkeer deur algemene sekuriteitsprotokolle en/of verkeersvolumepatrone te herken. Outline is standvastiger as tradisionele VPN’e omdat dit gebou is met ’n protokol wat ontwerp is om moeilik bespeur te word en dit dus moeiliker is om dit te blokkeer. Outline bied weerstand teen gesofistikeerde vorme van sensuur, insluitende netwerkgegronde blokkering en IP-blokkering.

## Wat is ’n Outline-bediener?
 ’n Outline-bediener laat die VPN loop waaraan toegelate gebruikers sal koppel. As jy ’n nuwe netwerk skep, kan jy jou eie veilige bediener, as jy een het, as jou Outline-bediener gebruik, of jy kan ’n wolkdiensverskaffer gebruik, soos:

- DigitalOcean
- Google Wolkplatform (GCP)
- Amazon Web Services (AWS)

Jy sal jou bediener in Outline Manager opstel.

## Wat is ’n diensbestuurder? {#servicemanager}
 ’n Diensbestuurder is die persoon wat verantwoordelik is om die Outline-bediener op te stel en toegangsleutels met gebruikers te deel. Die diensbestuurder is gewoonlik verantwoordelik vir die koste van die gebruik van die bediener. 

## Wat is ’n toegangsleutel? {#accesskey}
 ’n Toegangsleutel word gebruik om toegang tot ’n bestaande Outline-bediener te kry en aan die VPN te koppel. ’n [Diensbestuurder](#servicemanager) sal vir jou ’n toegangsleutel gee, of jy kan self [’n Outline-bediener opstel](/manager/server-setup/setup-server). Hier is ’n voorbeeld van hoe ’n toegangsleutel lyk (net ’n voorbeeld – dit sal nie werk nie): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Wat is Outline Manager?
 Outline Manager is ’n rekenaarapp wat dit vir ’n diensbestuurder moontlik maak om ’n Outline-bediener op te stel, [toegangsleutels](#accesskey) te genereer, en gebruiksdatalimiete per sleutel te stel. Jy kan die jongste weergawe van Outline Manager [hier](https://getoutline.org/get-started/#step-3) of [hier](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/) aflaai.

## Wat is Outline Client?
 Outline Client is ’n app wat vir rekenaars en mobiele toestelle beskikbaar is, en wat dit vir jou moontlik maak om aan ’n Outline-bediener te koppel en toegang tot die VPN te kry deur ’n toegangsleutel te gebruik. Jy kan die jongste weergawe van Outline Client [hier](https://getoutline.org/get-started/#step-3) of [hier](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/) aflaai.

## Wat is datalimiete?
 Outline Manager maak dit vir diensbestuurders moontlik om ’n aanskuiwende datalimiet vir 30 dae op toegangsleutels te stel om oormatige gebruik te voorkom en te help om koste voorspelbaar te hou. Diensbestuurders kan ’n versteklimiet stel wat vir elke sleutel geld, en ook vir enige sleutel ’n ander limiet stel wat die versteklimiet sal vervang. Sodra ’n limiet gestel is, tree dit onmiddellik in werking en word dit elke uur afgedwing.

As diensbestuurders intekening aanvaar om maatstawwe met Jigsaw te deel, moet hulle die [dataversamelingbeleid](/about/data-collection) lees vir besonderhede oor hoe die gebruik van datalimiete gerapporteer sal word.

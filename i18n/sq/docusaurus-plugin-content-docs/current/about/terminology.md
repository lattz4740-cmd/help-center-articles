---
title: Terminologjia
sidebar_label: Terminologjia
---

## Çfarë është një VPN?
 Një rrjet virtual privat (VPN) është një lidhje private mes pajisjeve të tua dhe një serveri pritës. Kur përdor një VPN, trafiku yt është i fshehur nga ofruesi i internetit. Mund të të duhet të përdorësh një VPN në skenarët e mëposhtëm:

- Për të mbrojtur të dhënat e tua kur përdor një rrjet publik Wi-Fi
- Për të mbajtur private të dhënat e tua të shfletimit nga ofruesi i internetit dhe nga agjencitë qeveritare
- Për të marrë qasje në përmbajtje të pacensuruara nga burime të ndryshme nga e gjithë bota

## Si ndryshon Outline nga VPN-të tradicionale?
 Ofruesit e internetit mund të zbulojnë dhe të bllokojnë me lehtësi VPN-të tradicionale duke njohur protokollet e zakonshme të sigurisë dhe/ose motivet e volumit të trafikut. Outline është më i fortë se VPN-të tradicionale sepse ai është ndërtuar duke përdorur një protokoll që është dizajnuar të jetë i vështirë për t'u zbuluar dhe, për këtë arsye, më i vështirë për t'u bllokuar. Outline është rezistent ndaj formave të sofistikuara të censurës, duke përfshirë bllokimin bazuar te rrjeti dhe bllokimin e adresës IP.

## Çfarë është një server i Outline?
 Një server i Outline ekzekuton rrjetin VPN me të cilin do të lidhen përdoruesit e lejuar. Nëse po krijon një rrjet të ri, mund të përdorësh serverin tënd të sigurt si server të Outline, nëse ke një të tillë, ose mund të përdorësh një ofrues të shërbimeve të resë kompjuterike, si p.sh.:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Do të konfigurosh serverin tënd në Outline Manager.

## Çfarë është një menaxher shërbimi? {#servicemanager}
 Një menaxher shërbimi është personi përgjegjës për konfigurimin e serverit të Outline dhe ndarjen e çelësave të qasjes me përdoruesit. Menaxheri i shërbimit është në përgjithësi përgjegjës për koston e përdorimit të serverit. 

## Çfarë është një çelës qasjeje? {#accesskey}
 Një çelës qasjeje përdoret për të pasur qasje te një server ekzistues i Outline dhe për t'u lidhur me VPN-në. Një [menaxher shërbimi](#servicemanager) do të të japë një çelës qasjeje ose mund [të konfigurosh vetë një server të Outline](/manager/server-setup/setup-server). Këtu është një shembull se si duket një çelës qasjeje (vetëm për shembull; nuk do të funksionojë): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Çfarë është Outline Manager?
 Outline Manager është një aplikacion desktopi që e lejon një menaxher shërbimi që të konfigurojë një server të Outline, të gjenerojë [çelësat e qasjes](#accesskey) dhe të caktojë kufijtë e të dhënave për përdorimin për çelës. Mund të shkarkosh versionin më të fundit të Outline Manager [këtu](https://getoutline.org/get-started/#step-3) ose [këtu](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Çfarë është "Klienti i Outline"?
 "Klienti i Outline" është një aplikacion, i disponueshëm për desktop dhe për celular, i cili të lejon të lidhesh me një server të Outline dhe të qasesh te VPN-ja duke përdorur një çelës qasjeje. Mund të shkarkosh versionin më të fundit të "Klientit të Outline"[këtu](https://getoutline.org/get-started/#step-3) ose [këtu](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Çfarë janë kufijtë e të dhënave?
Outline Manager i lejon menaxherët e shërbimit që të caktojnë një kufi gradual 30-ditor të të dhënave për çelësat e qasjes për të parandaluar përdorimin e tepërt dhe për të ndihmuar në parashikimin e kostove. Menaxherët e shërbimit mund të caktojnë një kufi të parazgjedhur që zbatohet për çdo çelës dhe mund të caktojnë po ashtu një kufi tjetër për secilin çelës për të zëvendësuar kufirin e parazgjedhur. Pasi të caktohet një kufi, ai hyn menjëherë në fuqi dhe zbatohet çdo orë.

Nëse menaxherët e shërbimit zgjedhin që të ndajnë metrikat me Jigsaw, ata duhet të shikojnë[politikën për mbledhjen e të dhënave](/about/data-collection) për detaje se si do të raportohet përdorimi i kufijve të të dhënave.

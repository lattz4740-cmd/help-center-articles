---
title: "Pse nuk mund të lidhem me shërbimin e Outline?"
sidebar_label: "Pse nuk mund të lidhem me shërbimin e Outline?"
---

Ka disa arsye pse mund të mos arrish të lidhesh me shërbimin e Outline:

- **Pajisja jote është**[**shkëputur nga interneti**](#Internetissues)**.**Ndonjëherë pajisja jote do të pësojë shkëputje të lidhjes së rrjetit dhe mund të duhet pak kohë që të përditësojë ikonat e rrjetit. Mund të ndodhë po ashtu që pajisja jote të jetë e lidhur me rrjetin lokal, por interneti nuk funksionon.
- [**Muri mbrojtës i rrjetit po bllokon qasjen**](#FirewallIssues)**në serverin tënd të Outline.**Kjo është diçka e zakonshme nëse po përdor një rrjet publik, si p.sh. rrjetin e shkollës, të punës ose një rrjet falas wireless.
- **Pajisja jote ka një**[**mur mbrojtës ose softuer antivirus**](#SoftwareIssues)**që po bllokon qasjen në serverin tënd të Outline.**
- **Mund të nevojitet që**[**cilësimet e pajisjes sate celulare**](#DeviceSettings)**të ndryshohen.**
- **Menaxheri yt i shërbimit mund të ketë**[**shkatërruar serverin ose ofruesi i shërbimit të internetit mund të ketë bllokuar kërkesën tënde**](#ServerIssues) .

## Problemet me lidhjen e internetit: {#Internetissues}

### Si ta testosh:

Çaktivizo Outline dhe shiko nëse lidhja me internetin është restauruar.

- Nëse po, shiko më shumë opsione të zgjidhjes së problemeve më poshtë.
- Nëse jo, atëherë prit pak për të parë nëse cilësimet e lidhjes përditësohen vetë.

### Gjërat për t'u rregulluar:

Lidhe pajisjen tënde përsëri online:

1. Kontrollo një pajisje tjetër për të parë nëse mund të lidhet me të njëjtin rrjet. Nëse pajisjet e tjera nuk mund të lidhen online, rrjeti mund të mos funksionojë dhe do të duhet të presësh të rikthehet lidhja ose të zgjidhësh problemet e tij.
2. Nëse pajisjet e tjera mund të lidhen në të njëjtin rrjet, mund të provosh një ose disa nga sa më poshtë për ta lidhur përsëri online:
   1. Vendose pajisjen në modalitetin e aeroplanit (celulari)
   2. Rinise pajisjen
   3. Fike pajisjen, prit për 2 minuta dhe ndize përsëri

## Problemet me murin mbrojtës të rrjetit: {#FirewallIssues}

### Si ta testosh:

1. Shkëputu nga rrjeti yt aktual me tel ose Wi-Fi.
2. Lidhu me një rrjet tjetër, si p.sh. një rrjet celular
3. Provo të lidhesh përsëri me serverin e Outline

Nëse mund të lidhesh ndërkohë që je në rrjetin tjetër, atëherë ky është problemi yt.

### Gjërat për t'u rregulluar:

Kontakto me menaxherin e shërbimit dhe kërkoji të lejojë qasjen në serverin tënd të Outline ose vazhdo të përdorësh rrjetin tjetër më mirë.

## Problemet me murin mbrojtës ose softuerin antivirus: {#SoftwareIssues}
### Si ta testosh:
 Provo të lidhesh me Outline nga një pajisje tjetër.

:::note
Mos harro se do të të duhet një çelës qasjeje dhe aplikacioni Outline për ta përdorur Outline në një pajisje tjetër.
:::

### Gjërat për t'u rregulluar:
Kontrollo cilësimet e murit mbrojtës ose të softuerit antivirus për t'u siguruar që janë caktuar të lejojnë kalimin e trafikut të rrjetit VPN dhe të Outline.

## Cilësimet e pajisjes: {#DeviceSettings}

## Gjërat për t'u kontrolluar: {#ServerIssues}
Për Android:

1. Hap aplikacionin "Cilësimet".
2. Kërko për **cilësimin e VPN-së** në pajisjen tënde. (Cilësimi i VPN-së do të të shfaqë të gjitha aplikacionet e VPN-së që kanë aktualisht qasje në telefonin tënd.)
3. Nëse nuk e shikon Outline te cilësimet e VPN-së, çinstalo Outline dhe instaloje atë përsëri. Outline do t'i jepet automatikisht qasje nga pajisja kur të instalohet.

Sigurohu që të mos kesh ndonjë aplikacion të mbivendosjes së ekranit të instaluar në pajisjen tënde Android, pasi kjo mund ta dërgojë në sfond dritaren e lejeve të Outline dhe mund të mos jetë e dukshme në plan të parë.

 Në pajisjen tënde Android, shko te Cilësimet > Aplikacionet > Qasja e aplikacioneve të veçanta. Më pas trokit te "Shfaq mbi aplikacionet e tjera". Mund ta heqësh qasjen për çdo aplikacion që e lejon këtë sjellje.

 Për iOS: Lexo [këtë artikull të mbështetjes](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

### Problemet me serverin:

### Si ta testosh:
Nëse ke qasje në më shumë se një server, provo të lidhesh me serverin tjetër.

### Gjërat për t'u rregulluar:

Kontakto me menaxherin e shërbimit për të parë nëse serveri është shkatërruar. Nëse po, kërkoji një[çelës qasjeje](/about/terminology) për një server tjetër.

Nëse e konfiguron serverin, provo të lidhesh me të nëpërmjet Outline Manager ose një metode tjetër, si p.sh.[SSH](https://en.wikipedia.org/wiki/Secure_Shell). Nëse kjo nuk funksionon, mund të provosh të kontrollosh panelin e ofruesit të shërbimit të resë kompjuterike, nëse ka, për të parë nëse serveri është akoma online.

---
title: Mbledhja e të dhënave dhe informacioneve
sidebar_label: Mbledhja e të dhënave dhe informacioneve
---

Outline nuk mbledh informacione personale përveçse nëse zgjedh t'i japësh ato. Outline nuk mbledh as informacione për uebsajtet që viziton ti apo se me kë apo çfarë komunikon ti.

 Nëse krijon ose identifikohesh në një llogari me një ofrues palë të tretë të shërbimit të resë kompjuterike nëpërmjet Outline Manager, ne nuk i marrim informacionet që ti i jep ofruesit të shërbimit të resë kompjuterike, si p.sh. adresën e email-it, emrin tënd, informacionet e faturimit dhe detajet e pagesës.

## Informacionet që marrim automatikisht
 Ne mbledhim automatikisht dy lloje informacionesh.

 1. Adresën IP të serverit

 Adresa IP e serverit të Outline mblidhet nga [Quay.io](https://quay.io/) dhe bëhet e qasshme për ne kur serveri përditësohet automatikisht me përmirësimet më të fundit të sigurisë dhe të veçorive. Adresa IP e serverit mund të identifikojë ofruesin e shërbimit të resë kompjuterike dhe qytetin ku është konfiguruar serveri i Outline, por kjo gjë nuk jep informacione se kush po e ekzekuton serverin apo se kush ka qasje në të.

 2. Informacionet teknike jo personalisht të identifikueshme

 Informacionet e listuara më poshtë do të raportohen nëse Outline pëson ndërprerje aksidentale ose nëse ndodh një përjashtim fatal, ose nëse dërgon në mënyrë manuale komentet e tua nëpërmjet aplikacionit Outline. Këto informacione do të përdoren vetëm për të ndihmuar në identifikimin dhe në rregullimin e problemeve të qëndrueshmërisë apo të cilësisë së funksionimit.

- Shteti
- Gjuha
- Data dhe ora e ndërprerjes aksidentale/përjashtimit dhe deri në 100 ngjarje të mëparshme, si p.sh. hapja e seksionit "Informacione" nga përdoruesi
- Mesazhet e përjashtimeve të përpiluara në mënyrë statistikore
- Emri dhe versioni i sistemit operativ
- Modeli i telefonit (nëse zbatohet)
- Koha e nisjes së aplikacionit
- Shfletuesi
- Arkitektura
- Numri i versionit dhe ndërtimit të Outline

Këto informacione transferohen nëpërmjet HTTPS-së te Sentry ([sentry.io](https://sentry.io/)), një ofrues palë e tretë me burim të hapur për monitorimin e gabimeve. Sentry përdor një larmi shërbimesh dhe teknologjish standarde të kësaj industrie për të siguruar të dhënat e tua nga qasja e paautorizuar, zbulimi, përdorimi dhe humbja. Nëse ke ndonjë pyetje në lidhje me politikat e Sentry, vizito [https://sentry.io/security/](https://sentry.io/security/) dhe [https://sentry.io/privacy/](https://sentry.io/privacy/) ose kontakto me [security@sentry.io](mailto:security@sentry.io). Të gjitha të dhënat e Outline të ruajtura nga Sentry janë të kufizuara në mënyrë të tillë që vetëm anëtarët e ekipit të Outline mund të kenë qasje në to.

## Informacionet që marrim vetëm pas zgjedhjes sate
 Outline i raporton informacionet e mëposhtme tek ekipi i Outline pas zgjedhjes sate.

 1. Metrikat e përdorimit

 Çdo server i Outline mbledh automatikisht, për orën e fundit dhe në bazë çelësi qasjeje, numrin e bajtëve të transferuar, kohën që një përdorues ishte i lidhur me serverin, shtetet dhe sistemet autonome të origjinës të kredencialeve të përdorura dhe nëse ndonjë nga veçoritë ka qenë e aktivizuar ose e çaktivizuar. Përmbajtjet e komunikimeve dhe metadatat e identifikueshme personalisht (p.sh. identifikimet, email-et, ID-të e pajisjeve etj.) nuk regjistrohen. Të gjitha metrikat janë të lidhura me një ID serveri. Udhëzimet për ndryshimin e ID-së së serverit mund të gjenden [këtu](/manager/server-management/reset-server-id).

 Si parazgjedhje, serverët e Outline nuk i ndajnë këto metrika me ekipin e Outline. Nëse administratori i serverit zgjedh në mënyrë të qartë ndarjen e metrikave të përdorimit, këto informacione do t'i dërgohen në mënyrë të sigurt çdo orë ekipit të Outline. Pas 60 ditësh, metrika e përdorimit do të përmblidhet në nivel shteti. Administratorët e serverëve mund ta ndryshojnë në çdo kohë preferencën e tyre për ndarjen e metrikave të përdorimit duke vizituar menynë "Cilësimet" në Outline Manager.

 Ne e vlerësojmë që po ndan me ne metrikat anonime për përdorimin e serverit tënd, pasi ne i përdorim ato për të matur tendencat e përdorimit dhe për të përmirësuar produktin.

 Për shembull, nëse një administrator i serverit zgjedh të ndajë metrikat e përdorimit me ne, ne mund të marrim informacione që tregojnë se një server me ID-në 12345 është përdorur për 3 orë dje, duke transferuar në total 500 megabajtë të dhëna, nga tri çelësa të përdorur në Shtetet e Bashkuara dhe në Kanada, me veçorinë e kufijve të të dhënave të aktivizuar.

 2. Komentet dhe email-in tënd nëse dërgon komentet

 Aplikacionet Outline Manager dhe Outline të lejojnë t'i dërgosh komentet e tua ekipit. Ne rekomandojmë që të mos përfshish informacione të identifikueshme personalisht, por një fushë email-i ofrohet si opsion nëse dëshiron të marrësh një përgjigje nga ekipi. Ne mbledhim po ashtu automatikisht disa informacione bazë, në mënyrë që të mund të kuptojmë komentet e tua. Shiko artikullin 2 më sipër, nën “Informacionet që marrim automatikisht", për të parë se çfarë të dhënash mbledhim. Mëso më shumë për praktikat e sigurisë dhe të privatësisë të Outline [këtu](/about/security-and-privacy).

 Nëse po përdor një version beta të aplikacionit Outline në Android, ne mund të përdorim shërbimin [Firebase](https://firebase.google.com/) të Google për të mbledhur informacione të korrigjimit të defekteve në kod që mund të na ndihmojnë për të zbuluar problemet dhe për të përmirësuar Outline. Mund të mësosh më shumë në lidhje me politikat e privatësisë dhe të sigurisë të Firebase nga uebsajti i tyre: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Nëse nuk dëshiron që Outline t'i dërgojë këto informacione nëpërmjet Firebase, përdor versionin e prodhimit të aplikacionit.

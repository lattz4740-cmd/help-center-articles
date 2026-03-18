---
title: Siguria dhe privatësia gjatë përdorimit të Outline
sidebar_label: Siguria dhe privatësia gjatë përdorimit të Outline
---

Siguria dhe privatësia gjatë përdorimit të Outline

## Si i mbron Outline komunikimet e tua online

Trafiku i internetit mund të jetë më shumë objekt i monitorimit kur transmetohet nëpër rrjetin lokal ose kombëtar.

Outline ndihmon për t'i mbajtur komunikimet e tua private duke e enkriptuar trafikun tënd të internetit kur ai transmetohet në rrjetin tënd kombëtar dhe e mban të enkriptuar derisa të mbërrijë në serverin e Outline. Kur trafiku është i enkriptuar me Outline, monitoruesit e rrjetit nuk mund t'i kontrollojnë uebsajtet që viziton ti ose informacionet që transferon.

Outline mund të të ndihmojë po ashtu të rikuperosh qasjen në veglat e komunikimeve të sigurta nga skaji në skaj, të cilat mund të mos jenë të qasshme në një mënyrë tjetër në shtetin tënd.

## Standardet e enkriptimit

Outline i enkripton komunikimet mes pajisjes sate dhe serverit të Outline duke përdorur shifrimin AEAD 256-bitësh Chacha2020 IETF Poly 1305. Shifrimi AEAD ofron konfidencialitet, integritet dhe vërtetësi, si dhe ka një cilësi të shkëlqyer funksionimi në pajisjet moderne të harduerit.

## Auditet e sigurisë

Në vitin 2018, Outline është audituar nga Radically Open Security dhe Cure53, dy organizata të pavarura të sigurisë dixhitale që i rishikojnë softuerët sipas standardeve të tyre më të fundit të sigurisë. Radically Open Security kreu një audit tjetër në vitin 2022 dhe Cure53 kreu një auditim të Outline SDK në vitin 2024. Raportet mund t'i lexosh këtu:

- [Raporti i testit të depërtimit i Radically Open Security (mars 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [Testi i depërtimit dhe raporti i auditimit i Cure53 për Jigsaw Outline (dhjetor 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [Raporti i testit të depërtimit i Radically Open Security (dhjetor 2022)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [Raporti i testit të depërtimit i Cure53 për Jigsaw Outline VPN SDK (janar 2024)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Metrika anonime dhe evidencat

Outline monitoron gjerësinë e bandës që është përdorur, si "bajtë të transferuar" për çdo çelës qasjeje. Këto informacione i lejojnë administratorët e serverëve të rregullojnë abonimet e tyre të gjerësisë së bandës me ofruesit e serverëve të resë kompjuterike sipas nevojës, por nuk i lejojnë ata të shikojnë informacionet aktuale që kanë kaluar nëpër serverin e Outline.

Mëso më shumë për [mbledhjen e të dhënave dhe informacioneve](/about/data-collection) nga Outline.

---

## Pyetjet e shpeshta për sigurinë dhe privatësinë

## A mund të më bëjë Outline anonim online?

Jo, Outline nuk është një vegël anonimiteti. Outline mbron privatësinë tënde nga monitoruesit e mundshëm të rrjetit.

Outline nuk të ofron anonimitet të plotë në uebsajtet që viziton, pasi ato mund të të identifikojnë përsëri kur identifikohesh dhe ndonjëherë nëpërmjet teknikave të tilla si metoda e monitorimit me gjurmën e gishtit e shfletuesit. Për aplikacionet për celular, shumica e telefonave inteligjentë modernë kanë API që i lejojnë aplikacionet e instaluara ta marrin vendndodhjen tënde në mënyrë të pavarur nga serveri proxy, pasi mund të mbështeten në sistemin e integruar GPS.

Në përgjithësi, rrjetet VPN ofrojnë mbrojtje të rëndësishme, sidomos nga monitorimi në internet, por ka gjithmonë rreziqe me funksionimin online. Edhe me një VPN, nëse një ofrues i shërbimit të internetit ka tashmë njohuri për identitetin tënd dhe mund ta vëzhgojë trafikun tënd të rrjetit, ai mund të arrijë ta përcaktojë adresën IP të serverit tënd të Outline. Këto informacione mund të përdoren për të bllokuar qasjen në serverin e Outline ose për të mësuar motivet e përdorimit, si p.sh. kur je zakonisht online dhe ndoshta edhe vendndodhjen tënde të përafërt.

## A mund ta kuptojë dikush se po përdor Outline?

Ndoshta. Platformat dhe shërbimet ku ke qasje ka shumë mundësi të arrijnë të kuptojnë se lidhja jote po vjen nga një server në renë kompjuterike. Herë pas here, ata mund të kuptojnë se po përdor një rrjet VPN, por nuk do të mund të shikojnë përmbajtjet e trafikut tënd të internetit.

## A më mbron Outline nga të gjitha kërcënimet e mundshme kibernetike?

Jo. Asnjë vegël nuk do të të mbrojë nga të gjitha kërcënimet e mundshme kibernetike. Outline të jep qasje në internetin e hapur dhe rrit privatësinë tënde duke e enkriptuar trafikun, por ne rekomandojmë që të ndërmarrësh masa paraprake shtesë për të mbrojtur veten nga llojet e tjera të sulmeve, si p.sh. softuerët keqdashës dhe mashtrimi.

Për të forcuar mbrojtjen tënde online, ki parasysh të bashkëpunosh me ekspertin e sigurisë kibernetike të organizatës sate. Si alternativë, mund të marrësh udhëzime të personalizuara nga ekspertët më të mirë të sigurisë në [Security Planner](https://securityplanner.org/), një uebsajt i ndërtuar për të të ofruar udhëzime të qarta për zgjedhjen e veglave të duhura të sigurisë kibernetike në raport me shqetësimet e tua.

Mund të shikosh po ashtu produktet e tjera të sigurisë kibernetike nga [Jigsaw](https://jigsaw.google.com/), si p.sh. [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) dhe [Password Alert](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## A është e ligjshme të përdorësh një rrjet VPN?

Kontrollo ligjet, rregulloret lokale, si dhe "Kushtet e shërbimit" për ofruesin e shërbimit të resë kompjuterike që planifikon të përdorësh para se të vësh në funksionim Outline ose të përdorësh aplikacionin.

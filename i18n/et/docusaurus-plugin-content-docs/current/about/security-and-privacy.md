---
title: "Turvalisus ja privaatsus Outline'i kasutamisel"
sidebar_label: "Turvalisus ja privaatsus Outline'i kasutamisel"
---

Turvalisus ja privaatsus Outline'i kasutamisel

## Kuidas Outline teie veebipõhist sidet kaitseb?

Internetiliiklus on jälgimise suhtes kõige haavatavam ajal, mil see liigub läbi teie kohaliku või riikliku võrgu.

Outline aitab teie side privaatsust kaitsta, krüpteerides teie internetiliikluse ajal, mil see liigub teie riiklikus võrgus ja jõuab Outline'i serverini. Kui liiklus on Outline'iga krüpteeritud, ei saa võrgu jälgijad uurida teie külastatavaid veebisaite ega teie edastatavat teavet.

Samuti võib Outline aidata teil taastada juurdepääsu turvalistele otspunktkrüpteeritud sidetööriistadele, mis ei pruugi muidu teie riigis saadaval olla.

## Krüpteerimisstandardid

Outline krüpteerib side teie seadme ja Outline'i serveri vahel AEAD 256-bitise Chacha2020 IETF Poly 1305 šifriga. AEAD šifrid tagavad konfidentsiaalsuse, terviklikkuse ja ehtsuse ning toimivad tänapäevastes seadmetes suurepäraselt.

## Turbeauditid

Aastal 2018 auditeerisid Outline'i Radically Open Security ja Cure53 – kaks sõltumatut digiturbeorganisatsiooni, mis kontrollivad tarkvara uusimate turbestandardite alusel. Radically Open Security viis 2022. aastal läbi lisaauditi ja Cure53 viis 2024. aastal läbi Outline’i SDK auditi. Aruandeid saate lugeda siin.

- [Radically Open Security läbistuse testi aruanne (märts 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53 läbistuse testi ja auditi aruanne Jigsaw' Outline'i jaoks (detsember 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Radically Open Security läbistuse testi aruanne (detsember 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Cure53 läbistuse testi aruanne: Jigsaw’ Outline’i VPN-i SDK (jaanuar 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Anonüümsed mõõdikud ja logid

Outline jälgib iga pääsuvõtme puhul kasutatud ribalaiust ehk edastatud baitide hulka. See teave aitab serveriadministraatoritel kohandada vajaduse järgi oma ribalaiuse tellimusi pilveteenuste pakkuja juures, ent see ei võimalda neil näha teavet, mis Outline'i serverist läbi käis.

Vaadake lisateavet Outline'i [andmete ja teabe kogumise kohta](https://getoutline.org/policies/data-collection).

---

## Turvalisuse ja privaatsuse KKK-d

## Kas Outline suudab mind veebis anonüümseks muuta?

Ei, Outline ei ole anonüümsustööriist. Outline kaitseb teie privaatsust potentsiaalsete võrgujälgijate eest.

Outline ei paku teile külastatavatel veebisaitidel täielikku anonüümsust, kuna saidid saavad siiski tuvastada teie isiku, kui logite sisse, samuti võivad saidid selleks mõnikord kasutada ka teatud tehnikaid, näiteks brauseri digitaalset sõrmejälge. Mobiilirakenduse puhul on enamikul tänapäevastel nutitelefonidel API-d, mis võimaldavad installitud rakendustel hankida teie asukoha puhverserverist sõltumatult, kuna rakendused tuginevad sisseehitatud GPS-il.

Üldiselt pakuvad VPN-id olulisi kaitsemeetmeid, eriti internetis jälgimise eest, ent veebis tegutsemisega kaasnevad alati teatud riskid. Kui internetiteenuse pakkuja on juba teie isikust teadlik ja saab teie võrguliiklust jälgida, suudab see võib-olla tuvastada teie Outline'i serveri IP-aadressi, isegi kui kasutate VPN-i. Selle teabe abil saab blokeerida juurdepääsu Outline'i serverile või tuvastada kasutusmustreid, näiteks seda, millal tavaliselt võrgus olete, ning võib-olla ka teie ligikaudset asukohta.

## Kas keegi saab teada, et kasutan Outline'i?

Võib-olla. Platvormid ja teenused, millele juurde pääsete, saavad tõenäoliselt teada, et teie ühendus pärineb pilveserverist. Mõnikord saab sellest järeldada, et kasutate VPN-i, ent platvormid ja teenused ei näe teie internetiliikluse sisu.

## Kas Outline kaitseb mind kõikvõimalike küberohtude eest?

Ei. Mitte ükski tööriist ei kaitse teid kõigi küberohtude eest. Outline võimaldab juurdepääsu avatud Internetile ja suurendab teie privaatsust, krüpteerides teie liikluse, ent soovitame teil rakendada ka muid ettevaatusabinõusid, et kaitsta end muud tüüpi rünnakute, näiteks pahavara ja andmepüügi eest.

Teie veebipõhise kaitse tugevdamiseks võite teha koostööd oma organisatsiooni küberturbe eksperdiga. Võite ka hankida isikupärastatud juhiseid juhtivatelt turbeekspertidelt saidil [Security Planner](https://securityplanner.org/), mille eesmärk on anda selgeid juhiseid teie jaoks sobivate küberturbe tööriistade valimiseks.

Samuti võite vaadata muid [Jigsaw'](https://jigsaw.google.com/) küberturbetooteid, nagu [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) ja [Password Alert](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Kas VPN-i kasutamine on seaduslik?

Enne Outline'i käitamist või rakenduse kasutamist uurige kohalikke seadusi, määrusi ja soovitud pilveteenuste pakkuja teenusetingimusi.

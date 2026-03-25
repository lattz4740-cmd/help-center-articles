---
title: Drošība un konfidencialitāte programmatūras Outline lietošanas laikā
sidebar_label: Drošība un konfidencialitāte programmatūras Outline lietošanas laikā
---

Drošība un konfidencialitāte programmatūras Outline lietošanas laikā

## Kā programmatūra Outline aizsargā tiešsaistes sakarus

Interneta datplūsma ir visneaizsargātākā pret novērošanu, kamēr tā maršrutē vietējā vai valsts tīklā.

Programmatūra Outline palīdz saglabāt komunikācijas privātumu, šifrējot interneta datplūsmu, kamēr tā maršrutē valsts tīklā, un saglabā informāciju šifrētu, līdz tā sasniedz Outline serveri. Ja datplūsma tiek šifrēta programmatūrā Outline, tīkla skatītāji nevar kontrolēt jūsu apmeklētās tīmekļa vietnes vai pārsūtīto informāciju.

Outline var jums arī palīdzēt atgūt piekļuvi drošiem gala-gala sakaru rīkiem, kuri var nebūt pieejami jūsu valstī.

## Šifrēšanas standarti

Outline šifrē sakarus starp jūsu ierīci un Outline serveri, izmantojot AEAD 256 bitu Chacha2020 IETF Poly 1305 šifru. AEAD šifri nodrošina konfidencialitāti, integritāti un autentiskumu, un tiem piemīt izcila veiktspēja mūsdienu aparatūrā.

## Drošības audits

2018. gadā programmatūras Outline auditu veica divas neatkarīgas digitālās drošības organizācijas, Radically Open Security un Cure53, kas pārskata programmatūru atbilstību jaunākajiem drošības standartiem. Radically Open Security veica papildu auditu 2022. gadā, un Cure53 veica Outline SDK auditu 2024. gadā. Šo organizāciju pārskati ir pieejami šeit:

- [Radically Open Security Penetration Test Report (2018. gada marts)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53 Pentest & Audit Report Jigsaw Outline (2018. gada decembris)](https://getoutline.org/reports/cure53-report.pdf)
- [Redically Open Security Penetration Test Report (2022. gada decembris)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Cure53 Pentest Report Jigsaw Outline VPN SDK (2024. gada janvāris)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Anonīmie rādītāji un žurnāli

Outline izseko izmantoto joslas platumu kā “pārsūtītos baitus” katrai piekļuves atslēgai. Šī informācija ļauj serveru administratoriem atbilstoši pielāgot joslas platuma abonementus ar mākoņpakalpojumu sniedzējiem, taču neļauj tiem skatīt faktisko informāciju, kas tika pārraidīta caur Outline serveri.

Uzziniet vairāk par Outline [datu un informācijas vākšanu](https://getoutline.org/policies/data-collection).

---

## Bieži uzdotie jautājumi par drošību un konfidencialitāti

## Vai programmatūra Outline var padarīt mani anonīmu tiešsaistē?

Nē, Outline nav anonimitātes rīks. Outline aizsargā jūsu konfidencialitāti no potenciāliem tīkla skatītājiem.

Outline nepiedāvā pilnu anonimitāti tīmekļa vietnēs, kuras apmeklējat, jo tās jūs var identificēt, kad pierakstāties vai dažreiz izmantojot tādu tehniku kā pārlūkprogrammas ciparnospiedums. Kas attiecas uz mobilajām lietotnēm, vairākumam viedtālruņu ir API, kas ļauj instalētajām lietojumprogrammām izgūt jūsu atrašanās vietu atkarībā no jūsu starpniekservera, pamatojoties uz iegulto GPS.

Virtuālie privātie tīkli nodrošina svarīgu aizsardzību, it īpaši pret interneta novērošanu, taču darbojoties tiešsaistē, vienmēr pastāv risks. Pat izmantojot virtuālo privāto tīklu, ja interneta pakalpojumu sniedzējs jau zina jūsu identitāti un var novērot jūsu tīkla datplūsmu, tas varēs arī noteikt jūsu Outline servera IP adresi. Šī informācija var tikt izmantota, lai bloķētu piekļuvi Outline serverim vai uzzinātu lietojuma paradumus, piemēram, laiku, kad parasti esat tiešsaistē, un, iespējams, jūsu aptuvenu atrašanās vietu.

## Vai kāds var noteikt, vai es izmantoju programmatūru Outline?

Iespējams. Platformas un pakalpojumi, kuriem piekļūstat, visticamāk, spēj konstatēt, ka jūsu savienojums tiek iegūts no mākoņservera. Dažkārt tie var secināt, ka izmantojat virtuālo privāto tīklu, taču tie nevar redzēt jūsu interneta datplūsmas saturu.

## Vai Outline aizsargā mani no visiem iespējamajiem kiberdraudiem?

Nē. Neviens rīks nespēj nodrošināt aizsardzību pret visiem iespējamajiem kiberdraudiem. Outline nodrošina piekļuvi atvērtajam internetam un palielina konfidencialitāti, šifrējot jūsu datplūsmu, taču mēs iesakām veikt papildu piesardzības pasākumus, lai nodrošinātu aizsardzību pret citiem uzbrukumu veidiem, piemēram, ļaunprātīgu programmatūru un pikšķerēšanu.

Lai stiprinātu savu aizsardzību tiešsaistē, iesakām sadarboties ar jūsu organizācijas kiberdrošības ekspertu. Vai arī varat iegūt personalizētus norādījumus no vadošiem drošības ekspertiem tīmekļa vietnē [Security Planner](https://securityplanner.org/), kuras uzdevums ir sniegt skaidrus norādījumus par pareizo kiberdrošības rīku izvēli atbilstoši jūsu situācijai.

Varat arī apskatīt citus [Jigsaw](https://jigsaw.google.com/) kiberdrošības produktus, piemēram, [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) un [Paroles aizsardzība](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Vai virtuālā privātā tīkla izmantošana ir likumīga?

Pirms darbināt programmatūru Outline vai lietotni, lūdzu, pārbaudiet vietējos normatīvos aktus un tā mākoņpakalpojumu sniedzēja pakalpojumu sniegšanas noteikumus, kura pakalpojumus vēlaties izmantot.

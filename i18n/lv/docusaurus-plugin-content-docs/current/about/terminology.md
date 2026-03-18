---
title: Terminoloģija
sidebar_label: Terminoloģija
---

**Kas ir virtuālais privātais tīkls?**

 Virtuālais privātais tīkls (virtual private network — VPN) ir privāts savienojums starp jūsu ierīcēm un mitināšanas serveri. Kad izmantojat virtuālo privāto tīklu, jūsu datplūsma nav redzama jūsu interneta pakalpojumu sniedzējam. Virtuālo privāto tīklu ieteicams izmantot tālāk norādītajos gadījumos:

- Ja vēlaties aizsargāt savus datus, kad izmantojat publisku Wi-Fi tīklu
- Ja vēlaties, lai jūsu pārlūkošanas dati nav pieejami jūsu interneta pakalpojumu sniedzējam un valsts aģentūrām
- Ja vēlaties piekļūt necenzētam saturam no dažādiem avotiem visā pasaulē

**Kā Outline atšķiras no tradicionālajiem virtuālajiem privātajiem tīkliem?**

 Interneta pakalpojumu sniedzēji var viegli atklāt un bloķēt tradicionālos virtuālos privātos tīklus, atpazīstot biežāk sastopamos drošības protokolus un/vai datplūsmas apjoma modeļus. Programmatūra Outline ir labāk aizsargāta nekā tradicionālie virtuālie privātie tīkli, jo tās pamatā ir protokols, kurš ir izstrādāts ar mērķi apgrūtināt tā atklāšanu, tāpēc to ir grūtāk bloķēt. Programmatūra Outline ir aizsargāta pret dažādiem sarežģītiem cenzūras veidiem, piemēram, tīklā balstītu bloķēšanu un IP adrešu bloķēšanu.

**Kas ir Outline serveris?**

 Outline serveris darbina virtuālo privāto tīklu, ar kuru atļautie lietotāji izveido savienojumu. Ja veidojat jaunu tīklu, kā Outline serveri varat izmantot savu drošo serveri, ja jums tāds ir, vai mākoņpakalpojumu sniedzēju, piemēram:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Iestatiet savu serveri lietotnē Outline pārvaldnieks.

**Kas ir pakalpojuma pārvaldnieks?**

 Pakalpojuma pārvaldnieks ir persona, kas ir atbildīga par Outline servera uzstādīšanu un piekļuves atslēgu kopīgošanu ar lietotājiem. Pakalpojuma pārvaldnieks parasti ir atbildīgs par pakalpojuma lietošanas maksas noteikšanu. 

**Kas ir piekļuves atslēga?**

 Piekļuves atslēga tiek izmantota, lai piekļūtu esošam Outline serverim un izveidotu savienojumu ar virtuālo privāto tīklu. [Pakalpojuma pārvaldnieks](#servicemanager) jums piešķirs piekļuves atslēgu, vai arī varat patstāvīgi [uzstādīt Outline serveri](/manager/server-setup/setup-server). Tālāk ir sniegts piemērs, kā izskatās piekļuves atslēga (tā ir tikai piemērs, un tā nedarbojas). 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

**Kas ir Outline pārvaldnieks?**

 Outline pārvaldnieks ir datora lietojumprogramma, kurā pakalpojuma pārvaldnieks var uzstādīt Outline serveri, ģenerēt [piekļuves atslēgas](#accesskey) un iestatīt datu lietojuma ierobežojumus katrai atslēgai. Outline pārvaldnieka jaunāko versiju varat ielādēt [šeit](https://getoutline.org/get-started/#step-3) vai [šeit](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Kas ir Outline klients?**

 Outline klients ir datoriem un mobilajām ierīcēm paredzēta lietojumprogramma, ko varat izmantot, lai izveidotu savienojumu ar Outline serveri un piekļūtu virtuālajam privātajam tīklam, izmantojot piekļuves atslēgu. Outline klienta jaunāko versiju varat lejupielādēt [šeit](https://getoutline.org/get-started/#step-3) un [šeit](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Kas ir datu ierobežojumi?**

 Izmantojot Outline pārvaldnieku, pakalpojuma sniedzēji var piekļuves atslēgām iestatīt iepriekšējo 30 dienu datu lietojumam atbilstošu ierobežojumu, lai novērstu pārmērīgu lietojumu un palīdzētu prognozēt izmaksas. Pakalpojuma pārvaldnieki var iestatīt noklusējuma ierobežojumu, kas attieksies uz visām atslēgām, kā arī iestatīt atšķirīgu ierobežojumu kādai konkrētai atslēgai — šādā gadījumā noklusējuma ierobežojums tiks ignorēts. Tiklīdz ierobežojums tiek iestatīts, tas nekavējoties stājas spēkā un tiek piemērots katrai stundai.

Ja pakalpojuma pārvaldnieki vēlas kopīgot rādītājus ar Jigsaw komandu, viņiem ir jāskata [datu vākšanas politika](/about/data-collection), kurā ir informācija par to, kā tiks veidoti pārskati par datu ierobežojumu lietošanu.

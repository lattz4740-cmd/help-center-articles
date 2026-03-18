---
title: Programmatūras Outline darbības principi
sidebar_label: Programmatūras Outline darbības principi
---

**Servera instalēšana**

 ​Lai gan Outline servera instalēšana var šķist vienkārša, fonā tiek veikts sarežģītu darbību kopums, kas nodrošina servera instalēšanu. Kad tiek instalēta programmatūra Outline, instalēšanas skripts izpilda tālāk minētās darbības.

- Tiek izgūta Shadowbox attēla stabilā versija, kas tiek importēta, izmantojot Docker. Attēls tiek mitināts vietnes [Quay.io](https://quay.io/) sadaļā [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Šajā attēlā ir ietverts Outline serveris un Pārvaldības API, ko vēlāk Outline servera pārvaldības lietojumprogramma izmanto, lai izveidotu un noņemtu piekļuves atslēgas, izvēlētos/atceltu anonīmas metrikas iekļaušanu pārskatos utt.
- [Watchtower](https://github.com/v2tec/watchtower) tiek instalēts un konfigurēts, lai katru stundu pārbaudītu attēla atjauninājumus, tādējādi palīdzot nodrošināt, ka katrs Outline serveris tiek nepārtraukti atjaunināts ar jaunākajām funkcijām un drošības uzlabojumiem.
- Tīmekļa serveris, kas tiek izmantots, lai piekļūtu Pārvaldības API, tiek palaists slepena un nejauša ceļa nejaušā portā.
- Tiek izveidots [pašparakstīts SSL sertifikāts](https://en.wikipedia.org/wiki/Self-signed_certificate), lai Outline servera pārvaldība tiktu šifrēta, izmantojot TLS, kaut arī nav domēna nosaukuma. Lietojumprogrammā Outline pārvaldnieks tiek ģenerēts un glabāts arī unikāls šī sertifikāta ciparnospiedums, palīdzot novērst pārtvērējuzbrukumus.

Outline instalācijai nav nepieciešama nekāda konfigurācija pēc instalēšanas.

**Servera drošība**

 Outline ir atvērtā pirmkoda programmatūra, tādējādi ikviens var skatīt kodu un uzlabot to, ja tiek atklātas kādas ievainojamības. Mūsu kods tiek mitināts vietnē [GitHub](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline).

 Turklāt visi instalētie Outline serveri tiek automātiski atjaunināti ikreiz, kad tiek izlaista jauna versija, nodrošinot, ka neviens serveris nav atstāts darbojoties ar programmatūras vecām versijām.

 Lai pārvaldītu piekļuves atslēgas serverī, lietojumprogramma Outline pārvaldnieks mijiedarbojas ar pārvaldības pakalpojumu Outline serverī. Pārvaldības pakalpojums darbojas nejaušā slepena un unikāla ceļa portā. Pārvaldības pakalpojums pats ir izturīgs attiecībā uz zondēšanu, jo tas neatbild uz vaicājumiem, ja nav norādīts atbilstošs slepenais ceļš. Visbeidzot, visi sakari ar pārvaldības pakalpojumu tiek šifrēti, izmantojot [pašparakstītu SSL sertifikātu](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Turklāt Outline serverī netiek glabāti nekādi žurnāli, tādēļ, pat ja tas tiek apdraudēts, netiktu izpausti nekādi lietotāja dati. Uzziniet vairāk [šeit](https://support.getoutline.org/s/article/Security-and-privacy). 2018. gadā programmatūras Outline auditu veica organizācija [Radically Open Security](https://radicallyopensecurity.com/) un [Cure53](https://cure53.de/). Pārskati ir pieejami [šeit](https://support.getoutline.org/s/article/Security-and-privacy).

**UDP datplūsmas apstrāde**

 Outline var darboties kā sistēmisks VPN, tādējādi visa UDP datplūsma tiek tunelēta caur Outline serveri.

**DNS datplūsma**

Outline veic visu DNS uzmeklēšanu caur Outline serveri un aizsargā to, izmantojot to pašu šifrējumu, kas tiek izmantots visām pārējām tīkla darbībām. Jūsu DNS vaicājumi tiks virzīti caur Outline serveri uz Dyn interneta ceļvedi, OpenDNS, Cloudflare DNS vai Quad9 DNS. Outline nekad nereģistrē jūsu DNS uzmeklēšanu.

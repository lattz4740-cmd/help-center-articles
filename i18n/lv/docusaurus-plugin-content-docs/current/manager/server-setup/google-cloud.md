---
title: Google Cloud automatizēta iestatīšana
sidebar_label: Google Cloud automatizēta iestatīšana
---

## Kopsavilkums

Lietotnē Outline pārvaldnieks ir funkcija, kas Outline serveri ļauj automātiski konfigurēt serverī, kurš darbojas mākonī Google Cloud. Ja izvēlēsieties izmantot šo funkciju, lietotnē Outline pārvaldnieks jums tiks lūgts pierakstīties, izmantojot Google kontu, kas piešķirs noteiktas[OAuth](https://developers.google.com/identity/protocols/oauth2) atļaujas Outline pārvaldnieka lokālajai instalācijai, lai varētu konfigurēt jūsu Google Cloud kontu.

 Ja nevēlaties piešķirt šīs atļaujas, varat izpildīt papildu iestatīšanas norādījumus lietotnē Outline pārvaldnieks, lai programmatūru Outline palaistu pakalpojumā Google Cloud Platform.

## Piešķirtās atļaujas

Lai varētu veikt automatizētu iestatīšanu, lietotnei Outline pārvaldnieks ir jābūt tālāk norādītajām Google konta atļaujām.

## Google Cloud Platform

- Jūsu Google Compute Engine resursu skatīšana un pārvaldība
- Jūsu datu skatīšana dažādos Google Cloud pakalpojumos un jūsu Google konta e-pasta adreses skatīšana

## Konta pamatinformācija

- Jūsu primārā Google konta e-pasta adreses skatīšana
- Jūsu saistīšana ar personas informāciju Google tīklā

## Papildu piekļuve

- Jūsu Cloud Platform projektu pārvaldība
- Jūsu Google Cloud Platform norēķinu kontu skatīšana un pārvaldība
- Jūsu Google API pakalpojuma konfigurācijas pārvaldība

Šīs atļaujas ļauj atbalstīt jūsu Outline serveru papildu funkcionalitāti, tostarp:

- atļaušanu jums atlasīt pareizo norēķinu kontu;
- jauna projekta izveidi Outline serveru organizēšanai;
- pieejamo datu centru uzskaitīšanu;
- jaunu virtuālo mašīnu izveidi Outline palaišanai;
- jaunās virtuālās mašīnas konfigurēšanu, izmantojot Outline.

## Atļauju atsaukšana

Lietotnes Outline pārvaldnieks piekļuvi pakalpojumam Google Cloud Platform varat atsaukt sadaļā [Mans konts](https://myaccount.google.com/permissions). Ja atsauksiet piekļuvi, visi automatizētajā iestatīšanā izveidotie serveri joprojām darbosies, taču tie vairs netiks rādīti lietotnē Outline pārvaldnieks. Lai atjaunotu piekļuvi serveriem, vienkārši atkārtoti izveidojiet savienojumu ar pakalpojumu Google Cloud Platform, sākot automatizētās iestatīšanas plūsmu.

## Outline projektu organizēšana

Lai organizētu Outline serverus, Google Cloud automatizētajā iestatīšanā tiek izmantots atsevišķs [Google Cloud projekts](https://cloud.google.com/resource-manager/docs/creating-managing-projects). Projekts tiek izveidots, kad pirmoreiz tiek izmantota automatizētā iestatīšana, ar ieteikto projekta ID, kas sākas ar “Outline-” un tālāk ir nejaušu rakstzīmju virkne. Ja vēlaties, izveides laikā varat norādīt citu projekta ID. Projekta nosaukums būs “Outline serveri”.

## Norēķinu konts

Google Cloud projektiem ir nepieciešams saistīts “norēķinu konts”, kas definē maksājumu informāciju. Pirmo reizi izmantojot Google Cloud automatizēto iestatīšanu, jums tiks lūgts norādīt norēķinu kontu, ko saistīt ar jūsu Outline serveriem. Dažkārt serveris pārtrauks darboties, jo pastāvēs ar norēķinu kontu saistīta problēma. Šādā gadījumā jums ir jāpiesakās rīkā [Google Cloud Console](https://console.cloud.google.com/getting-started), jāatrod ar Outline saistītais Google Cloud projekts (ar nosaukumu “Outline serveri”) un jāatjaunina norēķinu iestatījumi.

## Serveru likvidēšana

Ja vēlaties likvidēt serverus, kas izveidoti, izmantojot automatizēto iestatīšanu, visvieglāk to var izdarīt lietotnē Outline pārvaldnieks. Taču, ja vēlaties patstāvīgi likvidēt serverus, varat pieteikties rīkā [Google Cloud Console](https://console.cloud.google.com/getting-started), atrast projektu, kas tika izveidots sākotnējās iestatīšanas laikā (ar nosaukumu “Outline serveri”), un vai nu izdzēst tajā esošos resursus, vai arī izslēgt projektu.

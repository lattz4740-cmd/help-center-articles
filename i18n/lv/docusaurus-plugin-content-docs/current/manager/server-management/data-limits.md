---
title: "Kā varu iestatīt datu ierobežojumus piekļuves atslēgām?"
sidebar_label: "Kā varu iestatīt datu ierobežojumus piekļuves atslēgām?"
---

Varat iestatīt datu ierobežojumu, kas tiks piemērots visām piekļuves atslēgām. Lai iestatītu ierobežojumu, atveriet lietotni Outline pārvaldnieks un pārejiet uz iestatījumiem. Tajos ir pieejams slēdzis Datu ierobežojumi, ar kuru var iestatīt ierobežojumu, ja slēdzis ir iespējots.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Kad ierobežojums ir iestatīts, piekļuves atslēgu lapā varat uzzināt, cik katram lietotājam ir atlicis līdz ierobežojuma sasniegšanai; joslu diagrammā tiek rādīts datu lietojums pēdējo 30 dienu laikā.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Varat ne tikai iestatīt ierobežojumu visām piekļuves atslēgām, bet arī piešķirt atsevišķu ierobežojumu katrai atslēgai. Šis iestatījums ignorē noklusējuma datu iestatījumus, taču, ja neesat iestatījis noklusējuma datu ierobežojumu, tik un tā varat iestatīt datu ierobežojumu jebkurai atslēgai. 

 Lai iestatītu atslēgas datu pārsūtīšanas ierobežojumu, atveriet lietotni Outline pārvaldnieks, pārejiet uz cilni Savienojumi, kurā atrodas iestatāmā atslēga, un noklikšķiniet uz izvēlnes, kas atrodas atslēgas rindas labajā malā. Pēc tam noklikšķiniet uz vienuma Datu ierobežojums. Lai mainītu datu ierobežojumu vienumam “Mana piekļuves atslēga”, noklikšķiniet uz ikonas Datu ierobežojumi ![Šis attēls nav pieejams tālāk norādīto iemeslu dēļ: jums nav atļauju to skatīt vai tas ir noņemts no sistēmas](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Atlasiet vienumu “Iestatīt pielāgotu datu ierobežojumu”. Kad būsiet atzīmējis šo izvēles rūtiņu, tiks parādīts lauks, kurā varēsiet iestatīt attiecīgās atslēgas pielāgoto datu ierobežojumu. Kad esat pabeidzis, noklikšķiniet uz pogas Saglabāt, lai saglabātu datu ierobežojumu.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Kad būsiet saglabājis atslēgas datu pārsūtīšanas ierobežojumu, tas tiks rādīts galvenajā ekrānā kopā ar katras atslēgas datu lietojuma vērtību (pēdējo 30 dienu laikā).

Lai piekļuves atslēgai noņemtu datu ierobežojumu, atkal atveriet atslēgas dialoglodziņu Datu ierobežojums, noņemiet atzīmi no izvēles rūtiņas “Iestatīt pielāgotu datu ierobežojumu” un noklikšķiniet uz pogas Saglabāt.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

****Bieži uzdotie jautājumi par datu ierobežojumu****

****Kas ir datu ierobežojums iepriekšējo 30 dienu laikā?****

 Iestatot datu ierobežojumu iepriekšējo 30 dienu laikā, tiek aprēķināts katras atslēgas kopējais lietojums iepriekšējo 30 dienu laikā un tiek gādāts, lai atslēgas lietojums šajā periodā nepārsniegtu ierobežojumu. Tādējādi lietojums nevar pārsniegt ierobežojumu nevienā 30 dienu periodā, tostarp kalendārajos mēnešos, kas nav garāki par 30 dienām. Praktiski tas nozīmē, ka katram lietotājam pieejamie dati katru dienu palielinās par tādu apjomu, kādu lietotājs patērēja pirms 31 dienas.

**Kādēļ lietojumprogrammā Outline tiek izmantoti iepriekšējam lietojumam atbilstoši ierobežojumi?**

 Iepriekšējam lietojumam atbilstoši ierobežojumi nodrošina garantiju katrā 30 dienu periodā. Tāpēc šādus ierobežojumus ir vieglāk konfigurēt nekā periodisku ierobežojumu (piemēram, ierobežojumu pielāgotai mēneša dienai), taču tie sniedz līdzīgas garantijas. Turklāt šie ierobežojumi atbilst pašreizējam datu lietojuma attēlojumam lietojumprogrammā Outline, kā arī plaši izplatītiem rīkiem, piemēram, analīzes pakalpojumiem un serveru statistikai.

**Kādi dati tiek iekļauti, aprēķinot datu ierobežojumu?**

 Tiek ieskaitīta katra reize, kad piekļuves atslēgas dati iziet no servera. Principā tas nozīmē datus, kas pēc atslēgas pieprasījuma tiek sūtīti gan prom no servera, gan arī atpakaļ uz klientu. Tomēr paredzams, ka šo aprēķinu rezultāts būs ļoti tuvs abu virzienu datplūsmas apjomam starp atslēgu un serveri, tāpēc ceram, ka tas atbildīs jūsu lietotāju aprēķiniem. Izvēlējāmies izejošo datu apjomu, jo par to pieprasa norēķinus mūsu izpētītie mākoņpakalpojumu sniedzēji.

**Vai lietotāji saņems paziņojumu, ja tiks sasniegts datu ierobežojums?**

 Šobrīd nē. Daudzi mākoņpakalpojumu sniedzēji piedāvā tādus ierobežojumus kā 1 TB mēnesī — ar to pietiek 10 lietotājiem, kas izmanto 100 GB, vai 100 lietotājiem, kas izmanto 10 GB. Tas ir liels datu apjoms, un maz ticams, ka ievērojama lietotāju daļa to sasniegs. Ceram, ka lietotāji sazināsies ar serveru pārvaldniekiem, ja sasniegs ierobežojumu. Tomēr labprāt uzklausīsim jūsu viedokli par to, kāpēc paziņojumi jūsu situācijā būtu noderīgi. Varat sazināties ar mums [šeit](https://support.getoutline.org/s/contactsupport).

**Vai lietotāji saņems paziņojumu, ja datu ierobežojums būs gandrīz sasniegts?**

 Lietotājam, kas būs gandrīz sasniedzis ierobežojumu, katru dienu būs pieejams cits datu apjoms, jo tas tiks aprēķināts atbilstoši lietojumam pirms 30 dienām. Uzskatām, ka šādi paziņojumi drīzāk samulsinātu galalietotājus, nevis būtu viņiem noderīgi. [Šeit](https://support.getoutline.org/s/contactsupport) labprāt uzklausīsim jūsu atsauksmes par mūsu lēmumu nesūtīt šādus paziņojumus.

**Vai varu atiestatīt lietotāja datu lietojumu?**

 Nē, lietotāja ierobežojumā vienmēr ir ietverts pēdējo 30 dienu datu lietojums. Taču varat mainīt atslēgas datu ierobežojumu vai izveidot jaunu atslēgu.

**Kādēļ daži lietotāji zaudēja piekļuvi, tiklīdz iespējoju datu ierobežojumus?**

 Datu ierobežojumi ir balstīti uz iepriekšējo 30 dienu laikā pārsūtīto datu apjomu, kas tiek reģistrēts neatkarīgi no tā, vai ierobežojumi ir iespējoti. Var gadīties, ka lietotāji jau ir pārsnieguši ierobežojumus, pirms tie tika iestatīti. Ņemiet vērā, ka tiek piemēroti visi datu ierobežojumi, pat ja maināt atsevišķas atslēgas datu ierobežojumu.

**Vai varu iestatīt ierobežojumu visam serverim, piemēram, “1 TB 30 dienās”?**

 Šobrīd nē. Mēs labprāt dzirdētu vairāk par jūsu lietošanas piemēru — lūdzu, pastāstiet par to [šeit](https://support.getoutline.org/s/contactsupport).

**Ja ir iestatīts gan noklusējuma datu ierobežojums, gan datu ierobežojums konkrētai atslēgai, kurš no tiem tiks piemērots?**

 Attiecīgās atslēgas datu ierobežojumam ir augstāka prioritāte nekā noklusējuma datu ierobežojumam (ja tādu esat iestatījis).

**Vai varu iestatīt datu ierobežojumu konkrētai atslēgai, nenosakot noklusējuma datu ierobežojumu?**

 Jā. Nav nepieciešams definēt noklusējuma ierobežojumu, lai iestatītu datu ierobežojumu vienai atslēgai. Piemēram, varat iestatīt ierobežojumu vienai atslēgai, kas, iespējams, tiks plaši izmantota, lai novērstu pārmērīgu datu pārsūtīšanu ar šo atslēgu.

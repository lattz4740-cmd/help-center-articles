---
title: "Hvordan angiver jeg datagrænser for adgangsnøgler?"
sidebar_label: "Hvordan angiver jeg datagrænser for adgangsnøgler?"
---

Du kan angive en datagrænse, der gælder for alle adgangsnøgler. Du kan angive denne grænse ved at åbne Outline Manager og gå til Indstillinger. Der kan du se kontakten Datagrænser, og du kan se en grænse, når kontakten er slået til.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Når du har angivet en grænse, kan du gå til siden med adgangsnøgler for at se, hvor tæt hver enkelt bruger er på grænsen. Et søjlediagram viser dataforbruget i løbet af de seneste 30 dage.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Foruden muligheden for at angive en grænse for alle dine adgangsnøgler, kan du tildele hver nøgle sin egen datagrænse. Denne indstilling tilsidesætter eventuelle standarddatagrænser, som du har angivet. Hvis du ikke har angivet en standarddatagrænse, kan du stadig angive en datagrænse for en hvilken som helst nøgle. 

 Hvis du vil angive en nøgles dataoverførselsgrænse, skal du åbne Outline Manager, navigere til fanen Forbindelser, som har den nøgle, du vil angive. Klik derefter på menuen til højre for nøglens række. Derfra skal du klikke på Datagrænse. Hvis du vil ændre datagrænsen under "Min adgangsnøgle", skal du klikke på ikonet for Datagrænse ![Ikon for datagrænser](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Vælg en tilpasset datagrænse. Når du har markeret dette afkrydsningsfelt, vises der et felt, hvor du kan angive den tilpassede datagrænse for den pågældende nøgle. Klik på knappen GEM, når du er færdig, for at gemme datagrænsen.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Når du har gemt din dataoverførselsgrænse for den valgte nøgle, vises grænsen på hovedskærmen sammen med dataforbruget (i løbet af de foregående 30 dage) for hver nøgle.

Hvis du vil fjerne datagrænsen fra en adgangsnøgle, skal du ligesom før navigere til dialogboksen Datagrænse for nøglen, fjerne markeringen i afkrydsningsfeltet med etiketten Angiv en tilpasset datagrænse. Klik derefter på knappen GEM.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

****Ofte stillede spørgsmål om datagrænser****

****Hvad er en datagrænse på 30 løbende dage?****

 En datagrænse på 30 løbende dage opsummerer brugen af de enkelte nøgler i løbet af de seneste 30 dage og holder brugen af nøglerne under grænsen i den pågældende periode. Resultatet er, at en nøgle ikke kan overskride grænsen i løbet af enhver periode på 30 dage, herunder kalendermåneder på 30 dage eller færre. Det betyder i praksis, at den tilgængelige mængde data for hver bruger stiger hver dag med den mængde, de brugte for 31 dage siden.

**Hvorfor bruger Outline løbende grænser?**

 Løbende grænser giver garantier i hver 30-dages periode, hvilket betyder, at de er enklere at konfigurere end en fast grænse (f.eks. en tilpasset dag på måneden) og giver samtidig tilsvarende garantier. De passer også til den eksisterende visning af Outline-dataforbrug samt almindelige værktøjer såsom analysetjenester og serverstatistik.

**Hvilke data tæller med i datagrænsen?**

 Hver adgangsnøgles udgående netværksdata fra serveren medtages i optællingen. Dette henviser konkret til de data, der sendes ud fra serveren på nøglens vegne og tilbage til klienten. I praksis bør dette stemme nøje overens med den trafik, der sendes fra nøglen til serveren og tilbage igen, så vi håber, at den vil stemme overens med tallene for dine brugere. Vi har valgt udgående netværksdata, da dette faktureres af de cloududbydere, vi har undersøgt.

**Bliver brugere underrettet, hvis de overskrider deres datagrænse?**

 Ikke på nuværende tidspunkt. Mange skyudbydere har en grænse på f.eks. 1 TB for hele måneden, hvilket kan understøtte 10 brugere med 100 GB eller 100 brugere med 10 GB. Det er ret store tal, og vi forventer ikke, at mange brugere vil ramme grænsen. Vi håber, at brugerne vil kontakte serveradministratorerne, hvis de når grænsen. Vi vil dog gerne høre din mening om, hvordan notifikationer kan hjælpe i dit tilfælde, og du kan kontakte os [her](/about/feedback).

**Bliver brugere underrettet, hvis de nærmer sig deres datagrænse?**

 Mængden af nye data, som modtages af en bruger, der nærmer sig sin grænse, varierer fra dag til dag, fordi den er baseret på brugerens forbrug for 30 dage siden. Vi mener, at en advarsel sandsynligvis forvirrer slutbrugerne mere, end den hjælper dem. Vi modtager gerne din feedback vedrørende denne adfærd [her](/about/feedback).

**Kan jeg nulstille en brugers dataforbrug?**

 Nej. En brugers grænse inkluderer altid de foregående 30 dages dataforbrug. Du kan dog hæve datagrænsen for brugerens nøgle eller oprette en ny nøgle til vedkommende.

**Hvorfor mistede nogle af mine brugere adgang, så snart jeg aktiverede datagrænser?**

 Datagrænser er baseret på brugeren dataoverførsler i de foregående 30 dage, og de registreres, uanset om brugeren har aktiveret datagrænser eller ej. Det er muligt, at den pågældende bruger allerede har overskredet grænsen, inden den blev angivet. Vær også opmærksom på, at alle datagrænser håndhæves, selv når en enkelt nøgles datagrænse ændres.

**Kan jeg angive en grænse for hele serveren, f.eks. "1 TB pr. 30 dage"?**

 Ikke på nuværende tidspunkt. Vi vil meget gerne høre mere om din brug [her](/about/feedback).

**Hvis der er en standarddatagrænse og en datagrænse for en specifik nøgle, hvilken grænse bliver så håndhævet?**

 Den specifikke nøgles datagrænse tilsidesætter en eventuel standarddatagrænse, som du måtte have angivet.

**Kan jeg angive en datagrænse for en specifik nøgle uden at have angivet en standarddatagrænse?**

 Ja. Du behøver ikke at have en standarddatagrænse for at angive en datagrænse for en nøgle. Du kan for eksempel angive en grænse for en nøgle, som du tror, der muligvis deles bredt, for at beskytte dig selv mod overdreven dataoverførsel gennem den pågældende nøgle.

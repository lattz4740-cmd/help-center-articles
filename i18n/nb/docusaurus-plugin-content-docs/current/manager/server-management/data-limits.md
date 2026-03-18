---
title: "Hvordan angir jeg datagrenser for tilgangsnøkler?"
sidebar_label: "Hvordan angir jeg datagrenser for tilgangsnøkler?"
---

Du kan angi en datagrense som gjelder for alle tilgangsnøkler. For å angi grensen må du åpne Outline-administrator og gå til Innstillinger. Der ser du bryteren Datagrenser, som du kan slå på for å angi en grense.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Når du har angitt en grense, kan du se hvor nær grensen hver bruker er, på Tilgangsnøkkel-siden. Der vises databruken de siste 30 dagene i et stolpediagram.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Du kan angi en grense for alle tilgangsnøklene dine og en egen datagrense for hver tilgangsnøkkel. Denne innstillingen overstyrer eventuelle standard datagrenser du har angitt, men hvis du ikke har angitt noen standardgrense, kan du likevel angi en datagrense for en hvilken som helst nøkkel. 

 For å angi en grense for dataoverføring for en nøkkel må du åpne Outline-administrator, gå til Tilkoblinger-fanen med den aktuelle nøkkelen og klikke på menyen til høyre for nøkkelraden. Der klikker du på Datagrense. For å endre datagrensen for «Min tilgangsnøkkel» må du klikke på datagrenseikonet ![Ikon for datagrenser](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Velg «Angi en egendefinert datagrense». Når du har merket av i avmerkingsboksen, dukker det opp et felt hvor du kan angi en egendefinert datagrense for nøkkelen. Når du er ferdig, klikker du på LAGRE-knappen for å lagre datagrensen.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Når du har lagret dataoverføringsgrensen for den valgte nøkkelen, vises grensen på hovedskjermen sammen med databruken (fra de siste 30 dagene) for hver nøkkel.

For å fjerne datagrensen for en tilgangsnøkkel må du gå til nøkkelens Datagrense-dialogboks som tidligere, fjerne avmerkingen i boksen «Angi en egendefinert datagrense» og klikke på LAGRE-knappen.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

****Vanlige spørsmål om datagrenser****

****Hva er en 30-dagers datagrense med sporing?****

 En 30-dagers datagrense med sporing summerer bruken av hver nøkkel de siste 30 dagene og hindrer at bruksgrensen for nøkkelen blir overskredet i den perioden. Dermed kan ikke nøkkelen overskride grensen i løpet av noen som helst 30-dagersperiode, inkludert kalendermåneder på 30 eller færre dager. I praksis betyr dette at hver brukers tilgjengelige data øker hver dag med den mengden hen brukte for 31 dager siden.

**Hvorfor bruker Outline grenser med sporing?**

 Grenser med sporing gir garantier for hver 30-dagersperiode, noe som betyr at de er enklere å konfigurere enn en gjentakende grense (for eksempel en dag i måneden som kan tilpasses), samtidig som de gir lignende garantier. De samsvarer også med den eksisterende visningen for bruk av Outline-data, i tillegg til vanlige verktøy som analysetjenester og tjenerstatistikk.

**Hvilke data teller med i en datagrense?**

 For hver enkelt tilgangsnøkkel blir data som sendes ut fra tjeneren, tatt med i beregningen. Dette betyr data som sendes ut fra tjeneren og tilbake til klienten ved bruk av nøkkelen. Dette skal i praksis tilsvare trafikken som sendes fra nøkkelen til tjeneren og tilbake, så vi håper at den samsvarer med brukernes tall. Vi valgte utgående data fordi nettskyleverandørene vi undersøkte, fakturerer for dette.

**Blir brukerne varslet hvis de overskrider datagrensen?**

 Ikke for øyeblikket. Mange nettskyleverandører har en grense, for eksempel 1 TB for hele måneden, som kan støtte 10 brukere med 100 GB hver, eller 100 brukere med 10 GB hver. Dette er ganske høye tall, og vi tror ikke at det er mange brukere som når disse grensene. Vi håper at brukerne kontakter tjeneradministratorene dersom de skulle nå grensen. Men vi setter pris på innspill fra deg om hvordan varsler kan være nyttige for bruksmønsteret ditt. Du kan kontakte oss [her](https://support.getoutline.org/s/contactsupport).

**Blir brukerne varslet når de nærmer seg datagrensen?**

 Mengden nye data som mottas av en bruker som nærmer seg grensen, varierer fra dag til dag fordi den er basert på hvor mye hen brukte for 30 dager siden. Vi tror varsler er mer egnet til å forvirre brukerne enn til å hjelpe dem. Gi oss gjerne tilbakemeldinger om denne funksjonaliteten [her](https://support.getoutline.org/s/contactsupport).

**Kan jeg tilbakestille brukeres databruk?**

 Nei, brukergrensene inkluderer alltid databruk fra de siste 30 dagene. Men du kan øke datagrensen for nøklene deres, eller du kan opprette en ny nøkkel for dem.

**Hvorfor mistet noen av brukerne tilgang så snart jeg aktiverte datagrenser?**

 Datagrensene er basert på brukernes dataoverføringer fra de siste 30 dagene. Denne informasjonen registreres uavhengig av om det er angitt datagrenser eller ikke. Det er mulig at brukerne det gjelder, allerede hadde overskredet grensen før den ble angitt. Vær også oppmerksom på at alle datagrenser gjelder, selv når du endrer datagrensen for enkeltnøkler.

**Kan jeg angi en grense som gjelder for hele tjeneren, for eksempel «1 TB per 30 dager»?**

 Ikke for øyeblikket. Fortell gjerne mer om bruksmønsteret ditt [her](https://support.getoutline.org/s/contactsupport).

**Hvis det er angitt en standard datagrense og en datagrense for en bestemt nøkkel, hvilken grense gjelder da?**

 Datagrensen for den bestemte nøkkelen overstyrer eventuelle standard datagrenser du har angitt.

**Kan jeg angi en datagrense for en bestemt nøkkel uten å angi en standard datagrense?**

 Ja. Du trenger ikke å angi en standardgrense for å kunne angi en datagrense for en bestemt nøkkel. Du kan for eksempel angi en grense for en nøkkel du tror kommer til å bli delt mye, for å forhindre overdreven dataoverføring via nøkkelen.

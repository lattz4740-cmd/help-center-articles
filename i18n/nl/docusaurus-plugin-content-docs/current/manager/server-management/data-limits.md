---
title: "Hoe stel ik een datalimiet in voor toegangssleutels?"
sidebar_label: "Hoe stel ik een datalimiet in voor toegangssleutels?"
---

Je kunt een datalimiet instellen die voor alle toegangssleutels geldt. Open hiervoor Outline Manager en ga naar Instellingen. Daar vind je de schakelaar Datalimieten. Als je deze op Aangezet zet, kun je een limiet instellen.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Nadat je een limiet hebt ingesteld, kun je op de pagina met toegangssleutels controleren hoe dicht elke gebruiker bij de limiet is. Een staafdiagram geeft het datagebruik van de afgelopen 30 dagen aan.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Je kunt niet alleen een datalimiet instellen voor al je toegangssleutels, maar ook voor elke sleutel apart. Deze instelling overschrijft de standaard datalimiet die je hebt ingesteld. Ook als je geen standaardlimiet hebt ingesteld, kun je een datalimiet instellen voor afzonderlijke sleutels. 

 Als je een datalimiet wilt instellen, open je Outline Manager. Ga naar het tabblad Verbindingen met de sleutel waarvoor je de limiet wilt instellen en klik rechts van de rij met de sleutel op het menu. Klik dan op Datalimiet. Als je de datalimiet voor Mijn toegangssleutel wilt wijzigen, klik je op het icoon Datalimieten ![icoon voor datalimieten](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Selecteer Een aangepaste datalimiet instellen. Nadat je dit vakje hebt aangevinkt, wordt er een veld getoond waarin je de aangepaste datalimiet kunt instellen voor die sleutel. Als je klaar bent, klik je op de knop OPSLAAN om de datalimiet op te slaan.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Nadat je de datalimiet voor de gekozen sleutel hebt opgeslagen, verschijnt deze op het hoofdscherm. Daar vind je ook het datagebruik (van de afgelopen 30 dagen) van elke sleutel.

Als je de datalimiet voor een toegangssleutel wilt verwijderen, ga je zoals eerder uitgelegd naar het dialoogvenster Datalimiet van de sleutel. Vink 'Een aangepaste datalimiet instellen' uit en klik op de knop OPSLAAN.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

## Veelgestelde vragen over datalimieten
## Wat is een totaallimiet van 30 dagen?
 Met een totaallimiet van 30 dagen wordt het gebruik van een sleutel in de afgelopen 30 dagen bij elkaar opgeteld en wordt gezorgd dat het gebruik van die sleutel onder de limiet blijft. Het gevolg is dat de limiet van de sleutel niet kan worden overschreden tijdens een periode van 30 dagen, waaronder kalendermaanden van 30 dagen of korter. Elke dag neemt dus de hoeveelheid beschikbare data voor een gebruiker toe met hoeveel data ze 31 dagen geleden hebben gebruikt.

## Waarom gebruikt Outline totaallimieten?
 Totaallimieten bieden een garantie voor elke periode van 30 dagen. Ze zijn dus makkelijker in te stellen dan een terugkerende limiet (zoals op een bepaalde dag van de maand), maar bieden vergelijkbare garanties. Ze komen ook overeen met de bestaande weergave voor datagebruik in Outline en veelgebruikte tools, zoals analyseservices en serverstatistieken.

## Welke gegevens tellen mee voor de datalimiet?
 Het uitgaande verkeer van de server van elke toegangssleutel wordt meegenomen in het totaal. Strikt genomen betekent dit zowel gegevens die namens de sleutel vanaf de server wordt gestuurd als gegevens terug naar de client. Dit komt in de meeste gevallen nauw overeen met het verkeer dat wordt verzonden van de sleutel naar de server en weer terug, dus we hopen dat dit overeenkomt met het totale gebruik van je gebruikers. We hebben gekozen voor uitgaand verkeer, omdat dit in rekening wordt gebracht door de cloudproviders waaronder we een enquête hebben gehouden.

## Krijgen gebruikers een melding als ze de datalimiet hebben overschreden?
 Op dit moment niet. Veel cloudproviders hebben een limiet, zoals 1 TB voor de hele maand. Dit kan bijvoorbeeld worden verdeeld over 10 gebruikers met elk 100 GB of 100 gebruikers met elk 10 GB. Dit zijn vrij grote limieten en we verwachten niet dat veel gebruikers die zullen bereiken. We hopen dat gebruikers contact opnemen met hun serverbeheerder als ze de limiet hebben bereikt. We stellen het op prijs als je ons laat weten hoe meldingen in jouw use case kunnen helpen. Je kunt [hier](/about/feedback) contact met ons opnemen.

## Krijgen gebruikers een melding als ze de datalimiet bijna hebben bereikt?
 De hoeveelheid nieuwe data die een gebruiker krijgt die de limiet bijna heeft bereikt, verschilt van dag tot dag. De limiet is namelijk gebaseerd op het gebruik van 30 dagen geleden. We denken dat waarschuwingen eindgebruikers eerder in verwarring brengen dan dat ze zullen helpen. Laat het ons [hier](/about/feedback) weten als je daar feedback over hebt.

## Kan ik het datagebruik van een gebruiker resetten?
 Nee, de limiet van een gebruiker bestaat altijd uit het datagebruik van de afgelopen 30 dagen. Je kunt wel de datalimiet van de sleutel van de gebruiker verhogen of een nieuwe sleutel maken.

## Waarom raakten sommige gebruikers meteen de toegang kwijt toen ik een datalimiet instelde?
 Datalimieten zijn gebaseerd op de gegevensoverdracht van de afgelopen 30 dagen van gebruikers. Deze wordt hoe dan ook opgeslagen, ook als datalimieten uitstaan. Het kan zijn dat deze gebruikers de limiet al hadden overschreden voordat je die instelde. Alle datalimieten worden afgedwongen, zelfs als je de datalimiet van een individuele sleutel wijzigt.

## Kan ik een limiet instellen voor de hele server, bijvoorbeeld 1 TB per 30 dagen?
 Dat kan op dit moment niet. Laat ons [hier](/about/feedback) meer weten over je use case hiervoor.

## Als er een standaard datalimiet is en er een datalimiet geldt voor een specifieke sleutel, welke wordt er dan afgedwongen?
 De datalimiet voor de specifieke sleutel overschrijft de standaard datalimiet die je (eventueel) hebt ingesteld.

## Kan ik een datalimiet instellen voor een specifieke sleutel zonder een standaard datalimiet in te stellen?
 Ja. Je hoeft geen standaardlimiet te hebben om een datalimiet in te stellen voor één sleutel. Je kunt bijvoorbeeld een limiet instellen voor een sleutel waarvan je denkt dat die door meer mensen wordt gedeeld. Zo kun je een extreme hoeveelheid gegevensoverdracht via die sleutel voorkomen.

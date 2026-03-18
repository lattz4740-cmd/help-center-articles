---
title: Hugtök
sidebar_label: Hugtök
---

**Hvað er VPN?**

 Sýndarnet (VPN) er lokuð tenging á milli tækis/tækja og hýsilþjóns. Þegar þú notar VPN getur netþjónustan þín ekki séð netvirknina þína. Þú kannt að vilja nota VPN í eftirfarandi tilfellum:

- Til að vernda gögnin þín þegar þú notar opið WiFi-net
- Til að fela vefskoðunargögnin þín fyrir netþjónustu og ríkisstofnunum
- Til að fá aðgang að óritskoðuðu efni frá ýmsum upplýsingaveitum um allan heim

**Hvernig er Outline frábrugðin hefðbundnum VPN-þjónustum?**

 Netþjónustur geta auðveldlega greint og lokað á hefðbundin VPN-net með því að bera kennsl á algengar öryggissamskiptareglur og/eða umfangsmynstur umferðar. Outline er öflugra en hefðbundin VPN vegna þess að það var þróað með samskiptareglu sem var hönnuð til að erfiðara væri að greina hana og þar með loka á hana. Outline stenst háþróaða ritskoðun á borð við netkerfislokun og IP-lokun.

**Hvað er Outline-þjónn?**

 Outline-þjónn keyrir VPN-netið sem notendur með heimild munu tengjast. Ef þú er að búa til nýtt netkerfi geturðu notað eigin öruggan þjón sem Outline-þjón ef þú ert með slíkan eða þú getur notað skýjaþjónustuaðila á borð við:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Þú setur þjóninn upp í Outline Manager.

## Hvað er þjónustustjóri? {#servicemanager}
 Þjónustustjóri er aðilinn sem ber ábyrgð á uppsetningu Outline-þjónsins og sér um að deila aðgangslyklum með notendum. Þjónustustjórinn er almennt ábyrgur fyrir kostnaðinum sem fellur til við notkun þjónsins. 

## Hvað er aðgangslykill? {#accesskey}
 Aðgangslykill er notaður til að fá aðgang að fyrirliggjandi Outline-þjóni og tengjast VPN-netinu. Þú getur fengið aðgangslykil hjá [þjónustustjóra](#servicemanager) eða [sett upp Outline-þjón](/manager/server-setup/setup-server) upp á eigin spýtur. Svona gæti aðgangslykill litið út (þetta er aðeins dæmi, lykillinn virkar ekki): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

**Hvað er Outline Manager?**

 Outline Manager er tölvuforrit sem gerir þjónustustjóra kleift að setja upp Outline-þjón, búa til [aðgangslykla](#accesskey) og stilla gagnamörk fyrir notkun hvers lykils. Þú getur sótt nýjustu útgáfu Outline Manager[hér](https://getoutline.org/get-started/#step-3) eða[hér](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Hvað er Outline Client?**

 Outline Client er forrit, í boði fyrir tölvur og snjalltæki, sem gerir þér kleift að tengjast Outline-þjóni og fá aðgang að VPN-neti með aðgangslykli. Þú getur sótt nýjustu útgáfu Outline Client[hér](https://getoutline.org/get-started/#step-3) eða[hér](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Hvað eru gagnamörk?**

 Outline Manager gerir þjónustustjórum kleift að stilla gagnamarkaferil fyrir aðgangslykla í 30 daga til að koma í veg fyrir ofnotkun og halda kostnaði innan marka. Þjónustustjórar geta stillt sjálfgefin mörk sem gilda fyrir alla lykla, en einnig er hægt að stilla mismunandi mörk fyrir staka lykla sem hnekkja sjálfgefnu mörkunum. Gagnamörk taka gildi um leið og þau eru stillt og er framfylgt á klukkutíma fresti.

Ef þjónustustjórar samþykkja að deila mæligildum með Jigsaw ættu þeir að skoða[reglur um gagnasöfnun](/about/data-collection) til að fá upplýsingar um hvernig notkun gagnamarka verður skráð.

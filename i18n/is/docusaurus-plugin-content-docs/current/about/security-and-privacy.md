---
title: Öryggi og persónuvernd við notkun Outline
sidebar_label: Öryggi og persónuvernd við notkun Outline
---

Öryggi og persónuvernd við notkun Outline

## Svona verndar Outline samskipti þín á netinu

Mesta hættan á eftirliti með netumferð er þegar hún fer í gegnum staðar- eða landsnet.

Outline hjálpar til við að halda samskiptunum þínum lokuðum með því að dulkóða netumferðina þína á meðan hún ferðast innan landsnetsins og heldur henni dulkóðaðri þar til hún nær til Outline-þjónsins. Þegar Outline dulkóðar umferð geta netvaktarar ekki séð vefsvæðin sem þú opnar eða upplýsingarnar sem þú flytur.

Outline kann einnig að gera þér kleift að endurheimta aðgang að öruggum samskiptaverkfærum sem virka frá upphafi til enda sem gætu annars verið ótiltæk í þínu landi.

## Dulkóðunarstaðlar

Outline dulkóðar samskipti á milli tækisins þíns og Outline-þjónsins með dulritunaraðferðinni AEAD 256-bita Chacha2020 IETF Poly 1305. AEAD-dulritunaraðferðir bjóða upp á trúnað, heilleika og áreiðanleika og skila frábærum afköstum á nútímavélbúnaði.

## Öryggisendurskoðun

Árið 2018 gekkst Outline undir endurskoðanir Radically Open Security og Cure53, tveggja óháðra fyrirtækja á sviði stafræns öryggis sem fara yfir hugbúnað til að athuga hvort hann standist nýjustu öryggisstaðla. Radically Open Security framkvæmdi viðbótarendurskoðun árið 2022 og Cure53 framkvæmdi endurskoðun á forritunarverkfærum Outline árið 2024. Hér geturðu lesið skýrslurnar:

- [Smokurprófunarskýrsla Radically Open Security (mars 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [Smokurprófunar- og endurskoðunarskýrsla Cure53 á Jigsaw Outline (desember 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [Smokurprófunarskýrsla Radically Open Security (desember 2022)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [Smokurprófunarskýrsla Cure53 á VPN-forritunarverkfærum Jigsaw Outline (janúar 2024)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Nafnlaus mæligildi og annálar

Outline skráir bandvíddarnotkun sem „flutt bæti“ fyrir hvern aðgangslykil. Þessar upplýsingar gera stjórnendum þjóna kleift að breyta bandvíddaráskriftum hjá skýjaþjónustum eftir þörfum en gerir þeim ekki kleift að sjá upplýsingarnar sjálfar sem fóru í gegnum Outline-þjóninn.

Nánar um [gagna- og upplýsingasöfnun](/about/data-collection) Outline.

---

## Algengar spurningar um öryggi og persónuvernd

## Getur Outline gert mig nafnlausa(n) á netinu?

Nei, Outline er ekki nafnleysingarverkfæri. Outline gætir persónuverndar þinnar gagnvart aðilum sem kunna að vakta netkerfið.

Outline býður ekki upp á fullt nafnleysi á vefsvæðunum sem þú opnar vegna þess að kerfið getur áfram borið kennsl á þig þegar þú skráir þig inn og stundum í gegnum tækni á borð við skráningu vafrafingrafars. Hvað varðar snjallforrit eru flestir nýlegir snjallsímar með forritaskil sem gera uppsettum forritum kleift að sækja staðsetningu þína óháð staðgengilsþjóni þar sem þau geta reitt sig á innbyggt GPS.

VPN-net bjóða almennt upp á mikilvæga vernd, einkum gegn netvöktun, en netnotkun fylgir alltaf ákveðin áhætta. Ef netþjónusta hefur þegar borið kennsl á þig og getur fylgst með netnotkun þinni er hugsanlegt að hún geti fundið IP-tölu Outline-þjónsins þíns jafnvel þótt VPN sé notað. Slíkar upplýsingar er hægt að nota til að loka á aðgang að Outline-þjóninum eða bera kennsl á notkunarmynstur, t.d. um hvenær þú ert yfirleitt á netinu og hugsanlega til að áætla staðsetningu þína gróflega.

## Geta aðrir séð hvort ég nota Outline?

Hugsanlega. Kerfin og þjónusturnar sem þú notar geta líklega séð að tengingin þín sé í gegnum skýjaþjónustu. Stundum geta þau ályktað að þú notir VPN en þau geta ekki séð innihald netumferðar þinnar.

## Verndar Outline mig gegn öllum hugsanlegum netógnum?

Nei. Ekkert eitt verkfæri getur verndað þig gegn öllum hugsanlegum netógnum. Outline veitir þér aðgang að opna internetinu og eflir persónuvernd þína með því að dulkóða umferðina þína en við mælum með að grípa til frekari varúðarráðstafana til varnar annars konar árásum, s.s. spilliforritum og vefveiðum.

Skoðaðu að vinna með netöryggissérfræðingi fyrirtækisins þíns eða stofnunarinnar til að efla netvarnirnar. Að öðrum kosti geturðu fengið sérsniðnar ráðleggingar frá leiðandi öryggissérfræðingum hjá [Security Planner](https://securityplanner.org/) en það er vefsvæði sem er gert til að veita skýrar leiðbeiningar varðandi val á netöryggisverkfærum sem henta hverju sinni.

Þú getur einnig skoðað aðrar netöryggisvörur frá [Jigsaw](https://jigsaw.google.com/), svo sem [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) og [Password Alert](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Er löglegt að nota VPN?

Vertu viss um að kynna þér staðbundin lög og reglugerðir og þjónustuskilmála skýjaþjónustunnar sem þú ætlar að nota áður en þú byrjar að nota Outline eða forritið.

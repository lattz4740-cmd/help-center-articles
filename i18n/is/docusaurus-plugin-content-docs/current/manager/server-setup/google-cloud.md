---
title: Sjálfvirk uppsetning á Google Cloud
sidebar_label: Sjálfvirk uppsetning á Google Cloud
---

## Yfirlit

Outline Manager felur í sér eiginleika sem gerir þér kleift að stilla Outline-þjón sjálfkrafa á þjóni sem keyrir á Google Cloud. Ef þú velur að nota þennan eiginleika mun Outline Manager biðja þig um að skrá þig inn með Google-reikningnum þínum en slíkt veitir tilteknar [OAuth-heimildir](https://developers.google.com/identity/protocols/oauth2) fyrir staðbundna uppsetningu Outline Manager í þeim tilgangi að stilla Google Cloud-reikninginn þinn.

 Ef þú vilt ekki veita þessar heimildir geturðu fylgt ítarlegum uppsetningarleiðbeiningum í Outline Manager til að keyra Outline á Google Cloud Platform.

## Heimildir veittar

Outline Manager krefst eftirfarandi heimilda frá Google-reikningnum þínum til að hægt sé setja upp sjálfvirkt.

## Google Cloud Platform

- Skoða og hafa umsjón með gögnum í Google Compute Engine
- Skoða gögnin þín í öllum Google Cloud-þjónustum og sjá netfang Google-reikningsins þíns

## Grunnupplýsingar reiknings

- Sjá aðalnetfang Google-reikningsins þíns
- Tengja þig við persónuupplýsingar þínar á Google

## Aukinn aðgangur

- Hafa umsjón með Cloud Platform-verkefnunum þínum
- Skoða og hafa umsjón með innheimtureikningum Google Cloud Platform
- Hafa umsjón með þjónustustillingunum þínum fyrir forritaskil Google

Þessar heimildir gera okkur kleift að styðja við ítareiginleika til að stjórna Outline-þjónum, þar á meðal:

- Gera þér kleift að velja réttan greiðslureikning
- Búa til nýtt verkefni til koma skipulagi á Outline-þjóna
- Skrá tiltæk gagnaver
- Búa til nýjar sýndarvélar til að keyra Outline
- Stilla nýja sýndarvél með Outline

## Afturköllun heimilda

Þú getur afturkallað aðgang Outline Manager að Google Cloud Platform með því að opna [Reikningurinn minn](https://myaccount.google.com/permissions). Ef þú afturkallar aðgang halda þjónar sem þú bjóst til með sjálfvirkri uppsetningu áfram að keyra en munu hætta að birtast í Outline Manager. Til að endurheimta aðgang að þeim skaltu einfaldlega tengjast Google Cloud Platform á ný með því að hefja sjálfvirka uppsetningarferlið.

## Verkefnaskipulag Outline

Sjálfvirk uppsetning Google Cloud notar stakt [Google Cloud-verkefni](https://cloud.google.com/resource-manager/docs/creating-managing-projects) til að flokka Outline-þjónana þína. Verkefnið er búið til við fyrstu notkun sjálfvirku uppsetningarinnar með tillögu að auðkenni verkefnis sem byrjar á „Outline-“ og endar á handahófsvalinni stafarunu. Þú getur valið annað auðkenni verkefnis þegar það er búið til ef þú vilt. Verkefnið fær heitið „Outline-þjónar“.

## Greiðslureikningur

Google Cloud-verkefni þurfa tengdan „greiðslureikning“ þar sem greiðsluupplýsingar eru tilgreindar. Þegar þú notar sjálfvirka uppsetningu Google Cloud í fyrsta sinn færðu beiðni um að gefa upp greiðslureikning til að tengja við Outline-þjónana þína. Stundum hættir þjónn að virka vegna vandamáls varðandi greiðslureikninginn. Ef það gerist skaltu skrá þig inn á [Google Cloud Console](https://console.cloud.google.com/getting-started), finna Google Cloud-verkefnið sem tengist Outline (með heitið „Outline-þjónar“) og uppfæra greiðslustillingarnar.

## Eyðilegging þjóna

Ef þú vilt eyðileggja þjóna sem voru búnir til með sjálfvirkri uppsetningu er einfaldast að gera það innan Outline Manager. Ef þú vilt hins vegar eyðileggja þjónana upp á eigin spýtur geturðu skráð þig inn á[Google Cloud Console](https://console.cloud.google.com/getting-started), fundið verkefnið sem var búið til við upphaflegu uppsetninguna (með heitið „Outline-þjónar“) og ýmist eytt gögnunum þar eða lokað verkefninu.

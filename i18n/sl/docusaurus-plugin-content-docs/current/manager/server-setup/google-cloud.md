---
title: Samodejna nastavitev Googla Cloud
sidebar_label: Samodejna nastavitev Googla Cloud
---

## Pregled

Upravitelj za Outline vključuje funkcijo, ki vam omogoča samodejno konfiguriranje strežnika Outline v strežniku, ki se izvaja v Googlu Cloud. Če se odločite za uporabo te funkcije, vas bo Upravitelj za Outline pozval, da se prijavite z računom Google, tako da bodo lokalni namestitvi Upravitelja za Outline dodeljena nekatera dovoljenja [OAuth](https://developers.google.com/identity/protocols/oauth2) za namene konfiguriranja računa za Google Cloud.

 Če ne želite zagotoviti teh dovoljenj, lahko za izvajanje storitve Outline v Googlu Cloud Platform upoštevate navodila za napredno nastavitev v Upravitelju za Outline.

## Dodeljena dovoljenja

Da Upravitelj za Outline izvede samodejno nastavitev, mu mora vaš račun Google dodeliti naslednja dovoljenja.

## Google Cloud Platform

- Ogled virov storitve Google Compute Engine in njihovo upravljanje.
- Ogled podatkov v storitvah Google Cloud in ogled e-poštnega naslova za račun Google.

## Osnovni podatki o računu

- Ogled glavnega e-poštnega naslova računa Google.
- Povezovanje vas in osebnih podatkov v Googlu.

## Dodatni dostop

- Upravljanje projektov Cloud Platform.
- Prikaz in upravljanje računov za obračunavanje za Google Cloud Platform.
- Upravljanje konfiguracije storitev Google API.

Ta dovoljenja nam omogočajo, da podpiramo napredne funkcije za upravljanje vaših strežnikov Outline, vključno z naslednjimi funkcijami:

- Omogočanje, da izberete pravilni račun za obračunavanje.
- Ustvarjanje novega projekta za organiziranje strežnikov Outline.
- Vnos podatkovnih središč, ki so na voljo.
- Ustvarjanje novih navideznih računalnikov za izvajanje storitve Outline.
- Konfiguriranje novega navideznega računalnika s storitvijo Outline.

## Preklic dovoljenj

Upravitelju za Outline lahko dostop do Googla Cloud Platform prekličete tako, da obiščete [Moj račun](https://myaccount.google.com/permissions). Če prekličete dostop, se bodo vsi strežniki, ki ste jih ustvarili prek samodejne nastavitve, še naprej izvajali, vendar ne bodo več prikazani v Upravitelju za Outline. Če želite obnoviti dostop do Googla Cloud Platform, preprosto znova vzpostavite povezavo z njim tako, da začnete samodejni postopek nastavitve.

## Organizacija projekta Outline

Pri samodejni nastavitvi Googla Cloud je za organiziranje strežnikov Outline uporabljen en [projekt Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects). Projekt je ustvarjen med prvo uporabo samodejne nastavitve, pri čemer pridobi predlagan ID projekta, ki se začne z »Outline-« in nadaljuje z nizom naključnih znakov. Po želji lahko pri ustvarjanju izberete drug ID projekta. Projekt bo poimenovan »strežniki Outline«.

## Račun za obračunavanje

Za projekte Google Cloud je potreben povezan »račun za obračunavanje«, ki določa podatke za plačilo. Ob prvi uporabi samodejne nastavitve storitve Google Cloud boste pozvani, da navedete račun za obračunavanje, ki bo povezan s strežniki Outline. Strežnik se bo včasih ob pojavitvi težave z računom za obračunavanje nehal izvajati. V tem primeru se prijavite v storitev [Google Cloud Console](https://console.cloud.google.com/getting-started), poiščite projekt Google Cloud, povezan s storitvijo Outline (imenovan »strežniki Outline«), in posodobite nastavitve obračunavanja.

## Uničevanje strežnikov

Če želite uničiti strežnike, ustvarjene s samodejno nastavitvijo, lahko to najpreprosteje storite v Upravitelju za Outline. Vendar se lahko prijavite v [Google Cloud Console](https://console.cloud.google.com/getting-started), poiščete projekt, ki je bil ustvarjen pri začetni nastavitvi (imenovan »strežniki Outline«), in v njem izbrišete vire ali zaustavite projekt, če želite strežnike uničiti sami.

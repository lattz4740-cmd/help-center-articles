---
title: "Kaip atnaujinti „Outline“ serverio programinę įrangą?"
sidebar_label: "Kaip atnaujinti „Outline“ serverio programinę įrangą?"
---

„Outline“ serveriai automatiškai atnaujinami taikant naujausius saugos patobulinimus, kad visada naudotumėte naujausią „Outline“ technologiją. Automatinio atnaujinimo procesas įgalinamas naudojant [„Watchtower“](https://github.com/v2tec/watchtower) – atvirojo šaltinio biblioteką, kuri reguliariai tikrina ir atnaujina „Docker“ vaizdą, apimantį „Outline“ programinę įrangą.

Be to, kai įdiegsite „Outline“, naudodami „Outline Manager“, nustatysime periodinę užduotį, kad serverio programinė įranga būtų automatiškai atnaujinta naudojant [Neprižiūrimą naujovinimą](https://wiki.debian.org/UnattendedUpgrades) („Ubuntu“) ir prireikus paleidžiama iš naujo. Atkreipkite dėmesį, kad tai netaikoma naudojant Išplėstinį režimą, kad būtų išsaugota esama konfigūracija darant prielaidą, kad priegloba yra naudojama kitais tikslais, o ne tik „Outline“ vykdymui.

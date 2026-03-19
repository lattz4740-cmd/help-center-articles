---
title: "Naka-automate na Pag-set Up ng Google Cloud"
sidebar_label: "Naka-automate na Pag-set Up ng Google Cloud"
---

## Pangkalahatang-ideya

Ang Outline Manager ay may kasamang feature na nagbibigay-daan sa iyong awtomatikong i-configure ang Outline Server sa isang server na tumatakbo sa Google Cloud. Kung pipiliin mong gamitin ang feature na ito, hihilingin sa iyo ng Outline Manager na mag-sign in gamit ang Google Account mo, na magbibigay ng ilang partikular na pahintulot ng [OAuth](https://developers.google.com/identity/protocols/oauth2) sa iyong lokal na pag-install ng Outline Manager para sa mga layunin ng pag-configure sa Google Cloud Account mo.

 Kung ayaw mong ibigay ang mga pahintulot na ito, puwede mong sundin ang mga tagubilin sa advanced na pag-set up sa Outline Manager para mapatakbo ang Outline sa Google Cloud Platform.

## Mga Pahintulot na Ibinibigay

Para maibigay ang naka-automate na pag-set up, kinakailangan ng Outline Manager ang mga sumusunod na pahintulot mula sa iyong Google Account.

## Google Cloud Platform

- Tingnan at pamahalaan ang iyong mga resource ng Google Compute Engine
- Tingnan ang iyong data sa mga serbisyo ng Google Cloud at tingnan ang email address ng Google Account mo

## Basic na impormasyon ng account

- Tingnan ang email address ng iyong pangunahing Google Account
- Iugnay ka sa iyong personal na impormasyon sa Google

## Karagdagang access

- Pamahalaan ang iyong mga proyekto sa Cloud Platform
- Tingnan at pamahalaan ang iyong mga account sa pagsingil sa Google Cloud Platform
- Pamahalaan ang configuration ng serbisyo ng iyong Google API

Binibigyang-daan kami ng mga pahintulot na ito na suportahan ang advanced na functionality para sa pamamahala ng iyong mga Outline server kasama ang:

- Pagbibigay-daan sa iyong piliin ang tamang account sa pagsingil
- Paggawa ng bagong proyekto para maayos ang iyong mga Outline server
- Paglilista ng mga available na data center
- Paggawa ng mga bagong virtual machine para mapatakbo ang Outline
- Pag-configure sa bagong virtual machine sa Outline

## Pagbawi ng Mga Pahintulot

Puwede mong bawiin ang access sa Google Cloud Platform para sa Outline Manager sa pamamagitan ng pagbisita sa [Aking Account](https://myaccount.google.com/permissions). Kung babawiin mo ang access, mananatiling tumatakbo pero hindi na lalabas sa Outline Manager ang anumang server na ginawa mo gamit ang naka-automate na pag-setup. Para ma-restore ang access sa mga ito, kumonekta lang ulit sa Google Cloud Platform sa pamamagitan ng pagsisimula sa daloy ng naka-automate na pag-set up.

## Pag-aayos ng Proyekto sa Outline

Gumagamit ang naka-automate na pag-set up ng Google Cloud ng isang [proyekto sa Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects) para maayos ang iyong mga Outline server. Ginagawa ang proyektong ito sa panahon ng unang paggamit sa naka-automate na pag-set up, na may iminumungkahing project ID na nagsisimula sa “Outline-” at sinusundan ng string ng mga random na character. Puwede kang pumili ng ibang project ID sa panahon ng paggawa kung gusto mo. Papangalanan ang proyekto na “mga Outline server.”

## Account sa Pagsingil

Nangangailangan ang mga proyekto sa Google Cloud ng naka-link na “account sa pagsingil” na tumutukoy sa impormasyon sa pagbabayad. Sa unang beses na gamitin mo ang naka-automate na pag-set up ng Google Cloud, hihilingin sa iyo na magbigay ka ng account sa pagsingil na iuugnay sa mga Outline server mo. Kung minsan, hihinto sa pagtakbo ang isang server dahil may problema sa account sa pagsingil. Sa ganitong sitwasyon, dapat ay mag-log in ka sa [Google Cloud Console](https://console.cloud.google.com/getting-started), hanapin ang proyekto sa Google Cloud na nauugnay sa Outline (pinangalanang "mga Outline server"), at i-update ang mga setting ng pagsingil.

## Pag-destroy sa Mga Server

Kung gusto mong i-destroy ang iyong mga server na ginawa gamit ang naka-automate na pag-set up, pinakamadaling gawin ito mula sa Outline Manager. Gayunpaman, kung gusto mong ikaw mismo ang mag-destroy sa mga server, puwede kang mag-log in sa [Google Cloud Console](https://console.cloud.google.com/getting-started), hanapin ang proyektong ginawa sa paunang pag-set up (pinangalanang “mga Outline server”), at i-delete ang mga resource doon o di kaya'y i-shut down ang proyekto.

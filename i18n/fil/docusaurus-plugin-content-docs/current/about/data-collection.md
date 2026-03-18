---
title: Pangongolekta ng Data at Impormasyon
sidebar_label: Pangongolekta ng Data at Impormasyon
---

Hindi nangongolekta ng personal na impormasyon ang Outline maliban na lang kung mag-o-opt in kang ibigay ito. Hindi rin nangongolekta ang Outline ng impormasyon tungkol sa mga website na binibisita mo, o kung kanino ka nakikipag-ugnayan, o kung ano ang ipinagbibigay-alam mo.

 Kung gumagawa ka ng o nagla-log in ka sa isang account sa isang third party na cloud provider sa pamamagitan ng Outline Manager, hindi namin kinukuha ang anumang impormasyong ibinibigay mo sa iyong cloud provider, tulad ng email address, pangalan, impormasyon sa pagsingil, at mga detalye ng pagbabayad mo.

****Impormasyong awtomatiko naming kinukuha****

 Dalawang uri ng impormasyon ang awtomatiko naming kinokolekta.

 1. Server IP

 Ang IP ng Outline server ay kinokolekta ng [Quay.io](http://quay.io/), at ginagawa nitong accessible sa amin ang IP ng Outline server kapag awtomatikong nag-update ang server sa mga pinakabagong pagpapahusay sa seguridad at feature. Posibleng matukoy ng IP ng Server ang cloud provider server at ang lungsod kung saan na-set up ang Outline server pero hindi ito nagbibigay ng impormasyon tungkol sa kung sino ang nagpapatakbo sa server at kung sino ang nag-a-access dito.

 2. Teknikal na impormasyong hindi nagbibigay ng personal na pagkakakilanlan

 Kung magka-crash ang Outline o magkakaroon ng fatal exception, o kung manual kang magpapadala ng feedback sa pamamagitan ng Outline app, iuulat ang impormasyong nakalista sa ibaba. Gagamitin lang ang impormasyong ito para tumulong sa pagtukoy at pag-aayos ng mga isyu sa katatagan o performance.

- Bansa
- Lokalidad
- Petsa at oras ng pag-crash / exception at hanggang 100 nakaraang event, tulad ng pagbubukas ng user sa seksyong 'Tungkol sa'
- Mga mensahe ng exception na nalipon sa static na paraan
- Pangalan at bersyon ng OS
- Modelo ng telepono (kung naaangkop)
- Oras ng pagsisimula ng app
- Browser
- Architecture
- Bersyon at build number ng Outline

Inililipat ang impormasyong ito gamit ang HTTPS sa Sentry ([sentry.io](http://sentry.io/)), isang third-party at open source na error tracking provider. Gumagamit ang Sentry ng iba't ibang teknolohiya at serbisyong ayon sa pamantayan ng industriya para i-secure ang iyong data mula sa hindi pinapahintulutang pag-access, pagsisiwalat, paggamit, at pagkawala. Kung mayroon kang anumang tanong tungkol sa mga patakaran ng Sentry, pakibisita ang [https://sentry.io/security/](https://sentry.io/security/) at [https://sentry.io/privacy/](https://sentry.io/privacy/), o makipag-ugnayan sa [security@sentry.io](mailto:security@sentry.io). Ang lahat ng data ng Outline na na-store ng Sentry ay pinaghihigpitan para ang mga miyembro lang ng Outline team ang puwedeng maka-access nito.

****Impormasyong kinukuha lang namin kapag nag-opt in****

 Iniuulat ng Outline sa Outline team ang mga sumusunod na impormasyon kapag nag-opt in.

 1. Mga sukatan sa paggamit

 Awtomatikong kinokolekta ng bawat Outline server, para sa nakalipas na isang oras at batay sa bawat access key, ang bilang ng mga inilipat na byte, kung ilang beses kumonekta sa server ang isang user, ang mga pinagmulang bansa at autonomous system ng mga ginamit na kredensyal, at kung may anumang feature na na-enable o na-disable. Hindi nila-log ang mga content ng pakikipag-ugnayan o ang anumang metadata na nagbibigay ng personal na pagkakakilanlan (hal. mga login, email, device ID, atbp.). Nauugnay sa isang server ID ang lahat ng sukatan. May makikitang mga tabugilin para sa pagbabago ng server ID [dito](/manager/server-management/reset-server-id).

 Bilang default, hindi ibinabahagi ng Mga Outline Server ang mga sukatang ito sa Outline team. Kung hayagang mag-o-opt in ang administrator ng Server sa pagbabahagi ng mga anonymous na sukatan, secure na ipapadala ang impormasyong ito sa Outline team bawat oras. Pagkatapos ng 60 araw, pagsasama-samahin ang mga sukatan ng paggamit ayon sa bansa. Puwedeng baguhin ng mga administrator ng server ang kanilang preference sa pagbabahagi ng mga anonymous na sukatan anumang oras sa pamamagitan ng pagbisita sa menu ng ‘Mga Setting’ sa Outline Manager.

 Pinapahalagahan namin ang pagbabahagi mo sa amin ng mga anonymous na sukatan tungkol sa iyong paggamit ng server dahil ginagamit namin ang mga ito para masukat ang mga trend sa paggamit at mapahusay ang produkto.

 Halimbawa, kung pipiliin ng isang administrator ng Server na magbahagi sa amin ng mga sukatan sa paggamit, puwede kaming makatanggap ng impormasyong nagsasaad na ang isang Server na may ID 12345 ay ginamit nang 3 oras kahapon, na naglipat ng kabuuang 500 megabytes na data, mula sa tig-tatlong key na ginamit sa United States at Canada, at naka-enable ang feature na mga limitasyon sa data.

 2. Ang iyong mga komento at email kung magsusumite ka ng feedback

 Nagbibigay-daan sa iyo ang Outline Manager App at Outline App na magsumite ng feedback sa team. Inirerekomenda naming huwag maglagay ng impormasyong nagbibigay ng personal na pagkakakilanlan, pero may opsyonal na available na field ng email kung gusto mong makatanggap ng sagot mula sa team. Awtomatiko rin kaming nangangalap ng ilang pangunahing impormasyon para maunawaan namin ang iyong feedback. Pakitingnan ang item 2 sa itaas, sa "Impormasyong awtomatiko naming kinukuha," para makita kung ano ang data na kinokolekta namin. Matuto pa tungkol sa mga kagawian sa seguridad at privacy ng Outline [dito](/about/security-and-privacy).

 Kung gumagamit ka ng beta version ng Outline app sa Android, puwede naming gamitin ang serbisyong [Firebase](https://firebase.google.com/) ng Google para mangolekta ng impormasyon sa pag-debug na makakatulong sa amin na mag-detect ng mga problema at pahusayin ang Outline. Puwede kang matuto pa tungkol sa mga patakaran sa privacy at seguridad ng Firebase mula sa website nila: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Kung ayaw mong ipadala ng Outline ang impormasyong ito sa pamamagitan ng Firebase, pakigamit ang production version ng app.

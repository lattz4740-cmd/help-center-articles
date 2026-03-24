---
title: Seguridad at privacy habang gumagamit ng Outline
sidebar_label: Seguridad at privacy habang gumagamit ng Outline
---

Seguridad at privacy habang gumagamit ng Outline

## Paano pinoprotektahan ng Outline ang iyong mga online na pakikipag-ugnayan

Pinakanamamasid ang internet traffic habang dumadaan ito sa iyong lokal o pambansang network.

Nakakatulong ang Outline na panatilihing pribado ang iyong mga pakikipag-ugnayan sa pamamagitan ng pag-encrypt sa internet traffic mo habang dumadaan ito sa loob ng iyong pambansang network at pinapanatili ito ng Outline na naka-encrypt hanggang sa makarating ito sa Outline server. Kapag naka-encrypt ang trapiko gamit ang Outline, hindi masusuri ng mga tumitingin sa network ang mga website na binibisita mo, o ang impormasyong inililipat mo.

Makakatulong din sa iyo ang Outline na mag-recover ng access sa mga secure na end-to-end na tool sa pakikipag-ugnayan na posibleng hindi naa-access sa iyong bansa.

## Mga pamantayan sa pag-encrypt

Ine-encrypt ng Outline ang mga pakikipag-ugnayan sa pagitan ng iyong device at ng Outline Server gamit ang AEAD 256-bit Chacha2020 IETF Poly 1305 cipher. Ang AEAD na mga cipher ay nag-aalok ng pagiging kumpidensyal, integridad, at pagiging tunay, at nagpapakita ito ng mahusay na performance sa modernong hardware.

## Mga pag-audit sa seguridad

Noong 2018, ang Outline ay na-audit ng Radically Open Security at Cure53, dalawang independent na organisasyon sa digital na seguridad na nagsusuri ng software batay sa mga pinakabagong pamantayan ng seguridad. Nagsagawa ng karagdagang pag-audit ang Radically Open Security noong 2022 at nagsagawa ang Cure53 ng pag-audit sa Outline SDK noong 2024. Mababasa mo ang mga ulat dito:

- [Radically Open Security Penetration Test Report (Marso 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53 Pentest & Audit Report Jigsaw Outline (Disyembre 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Radically Open Security Penetration Test Report (Disyembre 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Cure53 Pentest Report Jigsaw Outline VPN SDK (Enero 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Mga anonymous na sukatan at log

Sinusubaybayan ng Outline ang nagamit na bandwidth bilang "bytes transferred" para sa bawat access key. Nagbibigay-daan ang impormasyong ito sa mga administrator ng server na i-adjust ang kanilang mga subscription sa bandwidth sa kanilang mga cloud server provider kung kinakailangan pero hindi ito nagbibigay-daan sa kanila na makita ang aktwal na impormasyong dumaan sa Outline server.

Matuto pa tungkol sa [pangongolekta ng data at impormasyon](/about/data-collection) ng Outline.

---

## Mga FAQ tungkol sa seguridad at privacy

## Magagawa ba akong anonymous ng Outline online?

Hindi, ang outline ay hindi isang tool sa pagiging anonymous. Pinoprotektahan ng Outline ang iyong privacy mula sa mga potensyal na tumitingin sa network.

Hindi nagbibigay sa iyo ang Outline ng ganap na pagiging anonymous sa mga website na binibisita mo dahil puwede ka pa ring makilala ng mga ito kapag nag-log in ka o magagawa rin nila ito minsan, sa pamamagitan ng mga pamamaraang tulad ng pagkuha ng fingerprint ng browser. Para sa mga mobile app, may mga API ang karamihan ng mga modernong smartphone na nagbibigay-daan sa mga naka-install na app na makuha ang iyong lokasyon nang hindi umaasa sa proxy mo dahil puwedeng umasa ang mga ito sa naka-embed na GPS.

Sa pangkalahatan, nagbibigay ang mga VPN ng mahahalagang proteksyon, partikular mula sa pagmamasid sa internet ngunit palaging may panganib na gumawa ng mga operasyon online. Kahit na may VPN, kung alam na ng ISP ang iyong pagkakakilanlan at nagagawa nitong obserbahan ang trapiko sa network mo, posible nitong matukoy ang IP address ng iyong Outline server. Magagamit ang impormasyong ito para i-block ang access sa Outline server o alamin ang mga pattern ng paggamit, tulad ng kung kailan ka karaniwang online at posibleng pati na rin ang iyong tinatayang lokasyon.

## Malalaman ba ng iba na gumagamit ako ng Outline?

Posible. Malamang na matukoy ng mga platform at serbisyong ina-access mo na nanggagaling ang iyong koneksyon sa isang cloud server. Paminsan-minsan, malalaman nilang gumagamit ka ng VPN pero hindi nila makikita ang mga content ng internet traffic mo.

## Napoprotektahan ba ako ng Outline sa lahat ng posibleng banta sa cyberspace?

Hindi. Walang nag-iisang tool ang magpoprotekta sa iyo laban sa lahat ng posibleng banta sa cyberspace. Nagbibigay sa iyo ang Outline ng access sa bukas na internet at pinapaigting nito ang privacy mo sa pamamagitan ng pag-encrypt sa iyong trapiko, pero inirerekomenda naming gumawa ka ng mga karagdagang pag-iingat para maprotektahan ang iyong sarili laban sa iba pang uri ng mga atakte, tulad ng malware at phishing.

Para mapaigting ang iyong mga online na depensa, pag-isipang makipagtulugan sa eksperto sa cybersecurity ng iyong organisasyon. Bilang alternatibo, puwede kang humingi ng naka-personalize na gabay mula sa mga nangungunang eksperto sa seguridad sa [Security Planner](https://securityplanner.org/), isang website na ginawa para bigyan ka ng malilinaw na tagubilin sa pagpili sa mga tamang tool sa cybersecurity para sa iyong mga alalahanin.

Puwede mo ring tingnan ang iba pang produkto sa cybersecurity mula sa [Jigsaw](https://jigsaw.google.com/), tulad ng [Intra](https://getintra.org/), [Project Shield](https://g.co/shield), at [Password Alert](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Legal bang gumamit ng VPN?

Pakitingnan ang iyong mga lokal na batas, regulasyon, at Mga Tuntunin ng Serbisyo para sa cloud provider na pinaplano mong gamitin bago patakbuhin ang Outline o gamit ang app.

---
title: Paano Gumagana ang Outline
sidebar_label: Paano Gumagana ang Outline
---

## Pag-install ng server
 ​Bagama't mukhang simple ang pag-install ng Outline, may aktwal na kumplikadong hanay ng mga hakbang na nangyayari sa likod nito para ma-install ang iyong server. Sa tuwing ini-install ang Outline, pinapatakbo ng script sa pag-install ang mga sumusunod na hakbang:

- Kinukuha ang stable na bersyon ng image ng Shadowbox at ini-import ito gamit ang Docker. Naka-host ang image sa [Quay.io](https://quay.io/), sa [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). Nasa image na ito ang Outline server at Management API na gagamitin ng Outline Server Management application para gumawa at mag-alis ng mga access key, mag-opt in/mag-opt out sa mga anonymous na sukatan ng pag-uulat, atbp.
- Ini-install at kino-configure ang [Watchtower](https://github.com/v2tec/watchtower) para tingnan kung may mga update sa image kada oras, na nakakatulong na masiguradong palaging up-to-date ang bawat Outline server at makuha ng mga ito ang mga pinakabagong feature at pagpapahusay sa seguridad.
- May web server, na ginagamit para sa pag-access ng Management API, na sinisimulan sa isang random na port sa isang lihim at random na path.
- May ginagawang [self-signed na SSL certificate](https://en.wikipedia.org/wiki/Self-signed_certificate) para ma-encrypt ang pamamahala ng Outline server gamit ang TLS kahit na wala itong domain name. May binubuo ring natatanging fingerprint ng certificate na ito at sino-store ito sa Outline Manager application na nakakatulong sa pagpigil sa mga MITM na pag-atake.

Walang kailangang kahit anong pag-configure sa pag-install ng Outline pagkatapos ng pag-install

## Seguridad ng server
 Ang Outline software ay open source, na nangangahulugang puwedeng makita ng sinuman ang code at pahusayin ito kung may matuklasan mang kahinaan. Naka-host sa [GitHub](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline) ang aming code.

 Bukod pa rito, awtomatikong ina-update ang lahat ng naka-install na Outline server sa tuwing may inilalabas na bagong bersyon, na nagsisiguradong walang Outline server na nagpapatakbo ng mga lumang bersyon ng software.

 Para pamahalaan ang mga access key sa server, nakikipag-interact ang Outline Manager application sa isang Management Service sa Outline server. Tumatakbo ang Management Service sa isang random na port at sa isang lihim at natatanging path. Ang Management Service mismo ay hindi puwedeng masuri dahil hindi ito tumutugon sa mga query maliban na lang kung tutukuyin ang naaangkop na lihim na path. Panghuli, naka-encrypt sa pamamagitan ng [self-signed na SSL certificate](https://en.wikipedia.org/wiki/Self-signed_certificate) ang lahat ng pakikipag-ugnayan sa Management Service.

 Gayundin, hindi nagso-store ng mga log ang Outline server, kaya kahit na makompromiso ito, walang maihahayag na data ng user. Matuto pa [rito](/about/security-and-privacy). Na-audit ng [Radically Open Security](https://radicallyopensecurity.com/) at [Cure53](https://cure53.de/) ang Outline noong 2018. Tingnan [dito](/about/security-and-privacy) ang mga ulat.

## Pangangasiwa sa UDP na trapiko
 Puwede tumakbo ang Outline bilang VPN sa buong system, na nangangahulugang pinapadaan sa Outline server ang lahat ng UDP na trapiko.

## Trapiko sa DNS
Isinasagawa ng Outline ang lahat ng paghahanap ng DNS sa pamamagitan ng Outline server, at pinoprotektahan nito ang mga ito gamit ang parehong pag-encrypt na ginagamit para sa lahat ng iba pang aktibidad ng network. Ang iyong mga query sa DNS ay daraan sa server ng Outline papunta sa Dyn Internet Guide, OpenDNS, Cloudflare DNS, o Quad9 DNS. Hindi kailanman nila-log ng Outline ang iyong mga paghahanap ng DNS.

---
title: "Mga FAQ tungkol sa pag-set up ng Outline server"
sidebar_label: "Mga FAQ tungkol sa pag-set up ng Outline server"
---

**Magagamit ko ba ang Outline nang walang server?**

 Sa kasamaang-palad, hindi. Kinakailangan ng Outline software ng access sa isang server, ikaw, iyong organisasyon, o isang pinagkakatiwalaang third-party man ang namamahala rito.

## Gaano katagal mag-set up ng Outline server?

Kadalasan, hindi ito umaabot nang 5 minuto. Puwede mong i-install ang Outline sa anumang cloud server pero nakipagtulungan kami sa DigitalOcean para magbigay ng mas user-friendly at may gabay na experience sa pag-install kung saan mo puwedeng i-set up ang iyong server sa ilang pag-click—nang walang script.

Kung pinili mo ang AWS, GCP, o isang advanced na pag-set up, pinasimple namin ang proseso ng pag-install ng server sa isang script na pinapangasiwaan ang karamihan ng mga environment.

## Saan ako puwedeng mag-set up ng Outline server?

Puwede kang mag-set up ng Outline server sa karamihan ng mga cloud provider saanman tumatakbo ang mga ito.

Ang pinakamadaling opsyon ay i-set up ito sa DigitalOcean, dahil may mga server ito sa maraming lokasyon tulad ng Amsterdam, Toronto, San Francisco, at Singapore. Kung mas gusto mong mag-install sa ibang cloud provider o sa sarili mong imprastraktura, puwede mong piliin ang ‘Advanced Mode’ sa Outline Manager application at sundin ang mga tagubilin sa pag-install sa pamamagitan ng script ng setup.

## Saan ko dapat i-set up ang Outline server ko?

1. May ilang bagay kang dapat isaalang-alang kapag pumipili ng lokasyon para sa iyong Outline Server:
2. Nakakaapekto ang lokasyon ng Outline Server sa kung paano nararanasan ng mga user ang internet. Halimbawa, kung matatagpuan sa Amsterdam ang server, ang user na nag-a-access sa server na ito ay mararanasan ang internet na parang nasa Netherlands talaga siya. Posibleng magpakita sa wikang Dutch ang ilang website. Kadalasan, puwede mong i-override ang lokal na wika gamit ang isang selector ng wika sa website.
3. Posibleng makaapekto sa iyong mga bilis ang distansya sa pagitan ng mga user mo at ng Outline Server. Sa pangkalahatan, puwedeng makaapekto sa bilis ng internet ng mga user ang aktwal na distansya sa pagitan ng mga Outline user at server. Sa karamihan ng sitwasyon, puwede kang pumili ng lokasyon ng server na pinakamalapit sa kung saan naroroon ang mga inaasahan mong user, pero puwede mong suriin ang [Submarine Cable Map](https://www.submarinecablemap.com/) para makita kung aling mga internet cable ang kumonekta sa iyong bansa o rehiyon.
4. Posibleng makaapekto sa legal na framework ang lokasyon ng iyong VPN server. Pakitandaang hindi nila-log ng Outline software ang iyong trapiko. Matuto pa tungkol sa [Seguridad at privacy habang gumagamit ng Outline](/about/security-and-privacy).

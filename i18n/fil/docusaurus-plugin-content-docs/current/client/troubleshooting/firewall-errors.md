---
title: Mga error sa firewall
sidebar_label: Mga error sa firewall
---

May tatlong uri ng mga isyu sa firewall na puwede mong maranasan:

## Posible kang ma-block ng firewall ng network.

Kung sinusubukan mong i-install ang Outline habang nakakonekta sa isang network na may firewall, gaya ng kapag nasa paaralan o nasa iyong trabaho, subukan itong i-install habang nakakonekta sa ibang network.

Kung hindi ito gagana, makipag-ugnayan sa administrator ng network mo para payagan ang mga koneksyon sa pagitan ng network na may firewall at ng iyong Outline server. Kakailanganin mong malaman ang IP address ng iyong Outline server at ang mga port kung saan gumagana ang Outline, na nakasaad sa dulo ng script sa pag-install.

## Posible kang ma-block ng firewall ng device..

Kung may software ka sa iyong device na nagba-block sa mga palabas na koneksyon sa mga hindi standard na port, o kung may software kang hindi nakikilala, (ZoneAlarm ng CheckPoint), sumangguni sa dokumentasyon ng iyong device o software para alamin kung paano gumawa ng exception para sa Outline.

## Posible kang ma-block ng firewall ng server.

Ang cloud provider na napili mo ay posibleng iatas sa iyo na manual na gumawa ng mga exception sa firewall ng server mo, para mabuksan ang mga port kung saan tumatakbo ang Outline. Pagkatapos mong patakbuhin ang script sa pag-install, may ipapakita dapat sa iyo na dalawang random na napiling port kung saan tumatakbo ang Outline sa server mo. Sapat na dapat kapag binuksan ang dalawang port na ito.

 Para makagawa ng mga exception sa firewall ng iyong Server, inirerekomenda naming tingnan mo ang dokumentasyon para sa 'ufw' at 'iptables':

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

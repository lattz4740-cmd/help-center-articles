---
title: "Bakit hindi ako makakonekta sa serbisyo ng Outline?"
sidebar_label: "Bakit hindi ako makakonekta sa serbisyo ng Outline?"
---

May ilang dahilan kung bakit hindi ka makakonekta sa serbisyo ng Outline:

- **Ang iyong device ay**/client/troubleshooting/connection-issues#One[**nadiskonekta sa internet**](#Internetissues)[#Internetissues](#Internetissues)**.**Kung minsan, mapuputol ang koneksyon ng network ng iyong device at posibleng umabot nang ilang sandali bago nito ma-update ang mga icon ng network. Posible ring nakakonekta ang iyong device sa lokal na network, pero walang internet.
- **Bina-block**/client/troubleshooting/connection-issues#Two[**ng firewall ng network mo ang access**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[s](#FirewallIssues)a Outline server mo.**Karaniwan ito kung gumagamit ka ng pampublikong network, gaya ng wireless na network sa paaralan, trabaho, o libreng wireless network.
- **Ang iyong device ay may**/client/troubleshooting/connection-issues#Three[**firewall o antivirus software**](#SoftwareIssues)[#SoftwareIssues](#SoftwareIssues)**na nagba-block ng access sa iyong Outline server.**
- **Posibleng kailangang baguhin ang**[**mga setting ng device ng telepono**](#DeviceSettings)**mo.**
- **Posibleng na-destroy na ng iyong manager ng serbisyo**[**ang server o posibleng bina-block ng ISP mo ang iyong request**](#ServerIssues) .

## Mga isyu sa koneksyon sa internet: {#Internetissues}

### Paano i-test:

I-off ang Outline at tingnan kung na-restore ang koneksyon mo sa internet.

- Kung oo, tumingin ng higit pang opsyon sa pag-troubleshoot sa ibaba.
- Kung hindi, maghintay nang ilang sandali para makita kung mag-a-update nang kusa ang mga setting ng iyong koneksyon.

### Mga aayusin:

Gawing online ulit ang iyong device:

1. Magsuri ng ibang device para makita kung makakakonekta ito sa parehong network. Kung ayaw mag-online ng iba pang device, posibleng hindi gumagana ang network at kailangan mong hintaying bumalik ito o i-troubleshoot ito.
2. Kung nakakakonekta sa parehong network ang iba pang device, puwede mong subukan ang isa o higit pa sa mga sumusunod para ibalik ito online:
   1. Ilagay sa airplane mode ang device (mobile)
   2. I-restart ang device
   3. I-shut down ang device, maghintay nang 2 minuto, i-on ulit ang device

## Mga isyu sa firewall ng network: {#FirewallIssues}

### Paano i-test:

1. Magdiskonekta sa iyong kasalukuyang WiFi o wired network.
2. Kumonekta sa ibang network, tulad ng cellular na network.
3. Subukang kumonekta ulit sa Outline server

Kung nakakakonekta ka habang nasa ibang network, ito ang iyong isyu.

### Mga aayusin:

Makipag-ugnayan sa manager ng serbisyo at hilingin sa kanya na payagan ang access sa Outline server mo o kaya ay ipagpatuloy na lang ang paggamit sa kabilang network.

## Mga isyu sa firewall o antivirus software: {#SoftwareIssues}
### Paano i-test:
 Subukang kumonekta sa Outline mula sa ibang device.

Paalala: Tandaang kailangan mo ng access key at Outline app para magamit ang Outline sa ibang device.

### Mga aayusin:
Suriin ang mga setting ng iyong firewall o antivirus software para siguraduhing nakatakda ang mga ito na payagang dumaan ang trapiko ng VPN at Outline.

## Mga setting ng device: {#DeviceSettings}

## Mga titingnan: {#ServerIssues}
Para sa Android:

1. Buksan ang App na Mga Setting.
2. Hanapin ang **mga setting ng VPN** sa iyong device. (Ipapakita ng mga setting ng VPN ang lahat ng VPN app na kasalukuyang may access sa telepono mo.)
3. Kung wala kang makikitang Outline sa mga setting ng VPN, i-uninstall ang Outline at i-install ulit ito. Awtomatiko dapat na mabibigyan ng access ng device ang Outline kapag na-install na ito.

Siguraduhing wala kang kahit anong naka-install na screen overlay application sa iyong Android device, dahil posibleng dinadala nito sa background ang window ng mga pahintulot ng Outline kaya hindi ito nakikita sa foreground.

 Sa iyong Android device, pumunta sa Mga Setting > Mga App > Espesyal na access sa app. Pagkatapos, i-tap ang ‘Ipakita sa ibabaw ng iba pang app.’ Puwede mong alisin ang access sa anumang app na nagpapahintulot sa ganitong gawi.

 Para sa iOS: Basahin ang[suportang artikulong ito](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

### Mga isyu sa server:

### Paano i-test:
Kung mayroon kang access sa higit sa isang server, subukang kumonekta sa ibang server.

### Mga aayusin:

Makipag-ugnayan sa iyong manager ng serbisyo para tanungin kung na-destroy na ang server. Kung oo, humingi sa kanya ng[access key](/about/terminology) sa ibang server.

Kung ikaw ang nag-set up ng server, subukang kumonekta rito sa pamamagitan ng Outline Manager o ibang paraan tulad ng[SSH](https://en.wikipedia.org/wiki/Secure_Shell). Kung hindi iyon gagana, puwede mong subukang tingnan ang cloud provider console, kung mayroon, para makita kung online pa rin ang server.

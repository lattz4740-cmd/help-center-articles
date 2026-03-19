---
title: Terminolohiya
sidebar_label: Terminolohiya
---

## Ano ang VPN?
 Ang virtual private network (VPN) ay isang pribadong koneksyon sa pagitan ng (mga) device mo at ng isang host server. Kapag gumamit ka ng VPN, nakatago ang trapiko mo mula sa internet provider. Kung gusto mo, puwede kang gumamit ng VPN sa mga sumusunod na sitwasyon:

- Protektahan ang iyong data kapag gumagamit ng pampublikong Wi-Fi network
- Panatilihing pribado ang iyong data mula sa pag-browse mula sa internet provider mo at mga ahensya ng pamahalaan
- Mag-access ng mga uncensored na content mula sa iba't ibang source sa buong mundo

## Paano naiiba ang Outline sa mga tradisyonal na VPN?
 Madaling nade-detect at naba-block ng mga internet provider ang mga tradisyonal na VPN sa pamamagitan ng pagtukoy sa mga karaniwang panseguridad na protocol at/o mga pattern ng dami ng trapiko. Mas matatag ang Outline kaysa sa mga tradisyonal na VPN dahil binuo ito gamit ang isang protocol na idinisenyong maging mahirap ma-detect, kaya mas mahirap itong i-block. Matatag ang Outline laban sa mga kumplikadong anyo ng censorship kabilang ang pag-block na batay sa network o pag-block ng IP.

## Ano ang Outline server?
 Pinapatakbo ng Outline server ang VPN kung saan kokonekta ang mga pinapahintulutang user. Kung gumagawa ka ng bagong network, puwede kang gumamit ng sarili mong secure na server bilang iyong Outline server kung mayroon ka nito, o puwede kang gumamit ng cloud services provider gaya ng:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Ise-set up mo ang iyong server sa Outline Manager.

## Ano ang manager ng serbisyo? {#servicemanager}
 Ang isang manager ng serbisyo ay ang taong may tungkuling i-set up ang Outline server at i-share ang mga access key sa mga user. Ang manager ng serbisyo ang may pangkalahatang responsibilidad sa pagbabayad sa gastusin sa paggamit ng server. 

## Ano ang access key? {#accesskey}
 Gumagamit ng access key para mag-access ng dati nang Outline server at makakonekta sa VPN. May [manager ng serbisyo](#servicemanager) na magbibigay sa iyo ng access key o puwede kang[mag-set up ng Outline server](/manager/server-setup/setup-server) nang mag-isa. Narito ang isang halimbawa ng hitsura ng access key (sample lang; hindi gagana): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Ano ang Outline Manager?
 Ang Outline Manager ay isang application sa desktop na nagbibigay-daan sa isang manager ng serbisyo na mag-set up ng Outline server, bumuo ng [mga access key](#accesskey), at magtakda ng mga limitasyon sa data sa paggamit kada key. Puwede mong i-download ang pinakabagong bersyon ng Outline Manager[dito](https://getoutline.org/get-started/#step-3) o[rito](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Ano ang Outline Client?
 Ang Outline Client ay isang application na available para sa desktop at mobile, na nagbibigay-daan sa iyo na kumonekta sa isang Outline server at i-access ang VPN gamit ang isang access key. Puwede mong i-download ang pinakabagong bersyon ng Outline Client[dito](https://getoutline.org/get-started/#step-3) o[rito](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## Ano ang mga limitasyon sa data?
 Ang Outline Manager ay nagbibigay-daan sa mga manager ng serbisyo na magtakda ng trailing na 30 araw na limitasyon sa data sa mga access key para maiwasan ang labis na paggamit at makatulong na panatilihing nahuhulaan ang mga gastusin. Ang mga manager ng serbisyo ay puwedeng magtakda ng default na limitasyon na nalalapat sa bawat key, at puwede rin silang magtakda ng iba't ibang limitasyon sa anumang key para i-override ang default na limitasyon. Kapag nakatakda na ang isang limitasyon, magkakabisa ito kaagad at oras-oras itong ipinapatupad.

Kung mag-o-opt in ang mga manager ng serbisyo na mag-share ng mga sukatan sa Jigsaw, dapat nilang tingnan ang[patakaran sa pangongolekta ng data](/about/data-collection) para sa mga detalye tungkol sa kung paano iuulat ang paggamit ng mga limitasyon sa data.

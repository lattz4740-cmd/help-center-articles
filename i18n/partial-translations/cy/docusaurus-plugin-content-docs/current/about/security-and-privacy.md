---
title: Diogelwch a phreifatrwydd wrth ddefnyddio Outline
sidebar_label: Diogelwch a phreifatrwydd wrth ddefnyddio Outline
---

Diogelwch a phreifatrwydd wrth ddefnyddio Outline

## Sut mae Outline yn amddiffyn eich cyfathrebiadau ar-lein

Mae traffig rhyngrwyd yn fwyaf agored i wyliadwriaeth tra ei fod yn teithio trwy eich rhwydwaith lleol neu genedlaethol.

Mae Outline yn helpu i gadw'ch cyfathrebiadau'n breifat trwy amgryptio'ch traffig rhyngrwyd wrth iddo deithio y tu mewn i'ch rhwydwaith cenedlaethol a'i gadw wedi'i amgryptio nes iddo gyrraedd y gweinydd Outline. Pan fydd traffig wedi'i amgryptio gydag Outline, ni all gwylwyr rhwydwaith archwilio'r gwefannau rydych yn ymweld â nhw, na'r wybodaeth rydych yn ei throsglwyddo.

Gall Outline hefyd eich helpu i adfer mynediad at offer cyfathrebu diogel o un pen i’r llall y mae'n bosib na fyddent yn hygyrch yn eich gwlad fel arall.

## Safonau amgryptio

Mae Outline yn amgryptio cyfathrebiadau rhwng eich dyfais a'r Gweinydd Outline gan ddefnyddio'r seiffr AEAD 256-bit Chacha2020 IETF Poly 1305. Mae seiffrau AEAD yn cynnig cyfrinachedd, uniondeb a dilysrwydd, ac yn arddangos perfformiad rhagorol ar galedwedd fodern.

## Archwiliadau diogelwch

Yn 2018, archwiliwyd Outline gan Radically Open Security a Cure53, dau sefydliad diogelwch digidol annibynnol sy'n adolygu meddalwedd yn erbyn y safonau diogelwch diweddaraf. Cynhaliodd Radically Open Security archwiliad ychwanegol yn 2022 a chynhaliodd Cure53 archwiliad o Outline SDK yn 2024. Gallwch ddarllen yr adroddiadau yma:

- [Adroddiad Prawf Treiddiad Radically Open Security (Mawrth 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Adroddiad Prawf Treiddiad ac Archwilio Cure53 Jigsaw Outline (Rhagfyr 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Adroddiad Prawf Treiddiad Radically Open Security (Rhagfyr 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Adroddiad Prawf Treiddiad ac Archwilio Cure53 Jigsaw Outline VPN SDK (Ionawr 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Metrigau a logiau dienw

Mae Outline yn olrhain y lled band a ddefnyddiwyd, fel "beit wedi'i drosglwyddo" ar gyfer pob allwedd mynediad. Mae'r wybodaeth hon yn caniatáu i weinyddwyr gweinyddion addasu eu tanysgrifiadau lled band gyda'u darparwyr gweinydd cwmwl yn ôl yr angen, ond nid yw'n caniatáu iddynt weld yr wybodaeth wirioneddol a aeth trwy'r gweinydd Outline.

Dysgu rhagor am [gasglu data a gwybodaeth](https://getoutline.org/policies/data-collection) Outline.

---

## Cwestiynau Cyffredin diogelwch a phreifatrwydd

## A all Outline fy ngwneud yn anhysbys ar-lein?

Na, nid offeryn anhysbysrwydd yw Outline. Mae Outline yn amddiffyn eich preifatrwydd rhag gwylwyr rhwydwaith posib.

Nid yw Outline yn cynnig anhysbysrwydd llawn i chi ar y gwefannau yr ymwelwch â nhw, oherwydd gallant eich adnabod o hyd pan fyddwch yn mewngofnodi ac weithiau trwy dechnegau, megis olion bysedd porwr. Ar gyfer apiau symudol, mae gan y mwyafrif o ffonau clyfar modern APIs sy'n caniatáu i apiau sydd wedi'u gosod gael eich lleoliad yn annibynnol i'ch dirprwy weinydd gan y gallant ddibynnu ar y GPS sydd wedi'i fewnosod.

Mae VPNs yn gyffredinol yn cynnig amddiffyniadau pwysig, yn enwedig rhag gwyliadwriaeth rhyngrwyd, ond mae risgiau bob amser i weithredu ar-lein. Hyd yn oed gyda VPN, os yw ISP eisoes yn ymwybodol o'ch hunaniaeth ac yn gallu arsylwi ar eich traffig rhwydwaith, mae'n bosib y bydd yn gallu pennu cyfeiriad IP eich gweinydd Outline. Gellir defnyddio'r wybodaeth hon i rwystro mynediad at y gweinydd Outline neu ddysgu patrymau defnydd, fel pan fyddwch ar-lein fel arfer, ac o bosib eich lleoliad bras.

## A all rhywun wybod a ydw i'n defnyddio Outline?

Mae'n bosib. Mae'n debyg y bydd y platfformau a'r gwasanaethau rydych yn eu defnyddio yn gallu cael gwybod bod eich cysylltiad yn dod o weinydd cwmwl. O bryd i'w gilydd, gallant ganfod eich bod yn defnyddio VPN, ond ni fyddant yn gallu gweld cynnwys eich traffig rhyngrwyd.

## A yw Outline yn fy amddiffyn rhag pob bygythiad seiber posib?

Nac ydy. Ni fydd unrhyw offeryn yn eich amddiffyn rhag pob bygythiad seiber posib. Mae Outline yn rhoi mynediad at y rhyngrwyd agored i chi ac yn cynyddu eich preifatrwydd trwy amgryptio'ch traffig, ond rydym yn argymell eich bod yn cymryd rhagofalon ychwanegol i amddiffyn eich hun rhag mathau eraill o ymosodiadau, megis drwgwedd a gwe-rwydo.

Er mwyn cryfhau eich amddiffynfeydd ar-lein, ystyriwch weithio gydag arbenigwr seiberddiogelwch eich sefydliad. Fel arall, gallwch gael arweiniad personol gan arbenigwyr diogelwch blaenllaw yn [Security Planner](https://securityplanner.org/), gwefan a adeiladwyd i roi cyfarwyddiadau clir i chi ar ddewis yr offer seiberddiogelwch cywir ar gyfer eich pryderon.

Gallwch hefyd edrych ar y cynhyrchion seiberddiogelwch eraill o [Jigsaw](https://jigsaw.google.com/), megis [Intra](https://getintra.org/), [Project Shield](https://g.co/shield), a [Password Alert](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## A yw'n gyfreithlon defnyddio VPN?

Gwiriwch eich cyfreithiau, rheoliadau a Thelerau Gwasanaeth lleol ar gyfer y darparwr cwmwl rydych yn bwriadu ei ddefnyddio cyn gweithredu Outline neu ddefnyddio'r ap.

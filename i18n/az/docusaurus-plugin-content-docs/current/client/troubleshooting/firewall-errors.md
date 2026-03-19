---
title: Qoruyucu divar xətaları
sidebar_label: Qoruyucu divar xətaları
---

Qoruyucu divar ilə bağlı qarşılaşa biləcəyiniz üç növ problem mövcuddur:

## Qoruyucu divarı olan şəbəkə sizi bloklaya bilər.

Məktəbdə və ya iş yerinizdə olduğu kimi qoruyucu divarı olan şəbəkəyə qoşulmuş olduğunuz halda Outline quraşdırmağa çalışırsınızsa, başqa şəbəkədə quraşdırmağa cəhd edin.

Bu üsulla alınmırsa, qoruyucu divarı olan şəbəkə ilə Outline serveriniz arasında əlaqə yaratması üçün şəbəkə administratorunuzla əlaqə saxlayın. Quraşdırma skriptinin sonunda göstərilən Outline serverinizin IP ünvanını və Outline-ın işlədiyi portları bilməlisiniz.

## Qoruyucu divarı olan cihaz sizi bloklaya bilər.

Cihazınızda qeyri-standart portlarda gedən bağlantıları bloklayan proqram təminatı və ya naməlum proqram təminatı varsa (məsələn, CheckPoint üzrə ZoneAlarm), Outline üzrə istisna yaratmağı öyrənmək üçün cihaz və ya proqram təminatınızın sənədlərinə baxın.

## Qoruyucu divarı olan server sizi bloklaya bilər.

Seçdiyiniz bulud provayderi Outline-ın işlədiyi portları açmaq üçün sizdən qoruyucu divarı olan server üzrə manual şəkildə istisnalar yaratmağı tələb edə bilər. Quraşdırma skriptini işə saldıqdan sonra sizə serverinizdə Outline-ın işlədiyi təsadüfi seçilmiş iki port təqdim edilməlidir. Bu iki portu açmaq kifayətdir.

 Qoruyucu divarı olan Server üzrə istisnalar yaratmaq üçün "ufw" və "iptables" sənədlərinə baxmağınızı tövsiyə edirik:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

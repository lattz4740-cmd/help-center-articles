---
title: Güvenlik duvarı hataları
sidebar_label: Güvenlik duvarı hataları
---

Karşılaşabileceğiniz üç tür güvenlik duvarı sorunu vardır:

## Bir ağ güvenlik duvarı tarafından engellenebilirsiniz.

Okul veya iş yeri ağı gibi güvenlik duvarı bulunan bir ağa bağlıyken Outline'ı yüklemeye çalışıyorsanız başka bir ağa bağlanarak yüklemeyi deneyin.

 Bu işe yaramazsa lütfen ağ yöneticinize başvurarak güvenlik duvarı bulunan ağ ile Outline sunucunuz arasındaki bağlantılara izin vermesini isteyin. Outline sunucunuzun IP adresini ve Outline'ın çalıştığı bağlantı noktalarını bilmeniz gerekir. Bu bilgiler yükleme komut dosyasının sonunda yer alır.

## Bir cihaz güvenlik duvarı tarafından engellenebilirsiniz.

Cihazınızda, standart olmayan bağlantı noktalarında giden bağlantıları engelleyen veya tanınmayan bir yazılım (ör. CheckPoint'in ZoneAlarm yazılımı) varsa Outline için nasıl istisna oluşturacağınızı öğrenmek üzere cihazınızın veya yazılımın dokümanlarına bakın.

## Bir sunucu güvenlik duvarı tarafından engellenebilirsiniz.

Seçtiğiniz bulut sağlayıcısı, Outline'ın çalıştığı bağlantı noktalarını açmak için sunucu güvenlik duvarınıza yönelik istisnaları manuel olarak oluşturmanızı gerektirebilir. Yükleme komut dosyasını çalıştırmanızın ardından, sunucunuzda Outline'ın çalıştığı bağlantı noktaları arasından rastgele seçilmiş iki bağlantı noktası sunulacaktır. Bu iki bağlantı noktasını açmanız yeterlidir.

 Sunucu güvenlik duvarınıza yönelik istisnalar oluşturmak için "ufw" ve "iptables" dokümanlarına bakmanızı öneririz:

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

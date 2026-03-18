---
title: "Outline hizmetine neden bağlanamıyorum?"
sidebar_label: "Outline hizmetine neden bağlanamıyorum?"
---

Outline hizmetine bağlanamıyorsanız bunun birkaç nedeni olabilir:

- **Cihazınızın**[**internet bağlantısı kesilmiştir**](#internetissues)**.**Bazen cihazınızın ağ bağlantısı kesilir ve ağ simgelerinin güncellenmesi biraz zaman alabilir. Cihazınız yerel ağa bağlı olduğu halde internet bağlantısının kesilmiş olması da mümkündür.
- **Outline sunucunuza erişim,**[**ağınızdaki güvenlik duvarı tarafından engelleniyordur**](#firewallissues)**.**Okul ağı, iş ağı veya ücretsiz kablosuz ağ gibi herkese açık bir ağ kullanıldığı durumlarda buna sıkça rastlanır.
- **Cihazınızda, Outline sunucunuza erişimi engelleyen bir**[**güvenlik duvarı veya antivirüs yazılımı**](#softwareissues)**vardır.**
- [**Telefonunuzun cihaz ayarlarının**](#devsettings)**değiştirilmesi gerekiyordur.**
- **Hizmet yöneticiniz**[**sunucuyu silmiş veya İSS'niz isteğinizi engelliyor olabilir**](#serverissues)**.**

İnternet bağlantısı sorunları:

## Sorunları test etme:

Outline'ı kapatın ve internet bağlantınızın geri gelip gelmediğine bakın.

- Bağlantı varsa aşağıdaki diğer sorun giderme seçeneklerini inceleyin.
- Bağlantı yoksa bağlantı ayarlarınızın kendi kendine güncellenip güncellenmediğini görmek için birkaç dakika bekleyin.

## Sorunları düzeltme:

Cihazınızın tekrar internete bağlayın:

1. Başka bir cihazın aynı ağa bağlanıp bağlanamadığını kontrol edin. Başka cihazlar da internete bağlanamıyorsa ağ bağlantısı kesilmiş olabilir. Bu durumda bağlantının geri gelmesini bekleyebilir veya sorunu gidermeye çalışabilirsiniz.
2. Diğer cihazlar aynı ağa bağlanabiliyorsa internete tekrar bağlanmak için aşağıdakilerden birini veya birkaçını deneyebilirsiniz:
   1. Cihazı uçak moduna geçirin (mobil).
   2. Cihazı yeniden başlatın.
   3. Cihazı kapatıp 2 dakika bekleyin, ardından tekrar açın.

#### Ağ güvenlik duvarıyla ilgili sorunlar:

## Sorunları test etme:

1. Mevcut kablosuz veya kablolu ağınızın bağlantısını kesin.
2. Hücresel ağ gibi farklı bir ağa bağlanın.
3. Outline sunucusuna tekrar bağlanmayı deneyin.

Diğer ağ üzerinden internete bağlanabiliyorsanız sizin bağlantınızdan kaynaklanan bir sorun var demektir.

## Sorunları düzeltme:

Hizmet yöneticinizden Outline sunucunuza erişim izni vermesini isteyin veya bu ağ yerine diğer ağı kullanmaya devam edin.

**Güvenlik duvarı veya antivirüs yazılımıyla ilgili sorunlar:**

## Sorunları test etme:

Outline'a başka bir cihazdan bağlanmayı deneyin.

Not: Outline'ı başka bir cihazda kullanabilmek için erişim anahtarına ve Outline uygulamasına ihtiyacınız olduğunu unutmayın.

## Sorunları düzeltme:

Güvenlik duvarı veya virüsten koruma yazılımınızın ayarlarını kontrol ederek VPN ve Outline trafiğine izin verildiğinden emin olun.

Cihaz ayarları:

## Sorunları kontrol etme:

Android için:

1. Ayarlar uygulamasını açın.
2. Cihazınızın **VPN ayarlarını** bulun (VPN ayarlarında, şu anda telefonunuzda erişimi olan tüm VPN uygulamaları gösterilir).
3. VPN ayarlarında Outline'ı görmüyorsanız Outline'ı kaldırın ve yeniden yükleyin. Yüklendikten sonra Outline'a cihaz tarafından otomatik olarak erişim verilir.

Bir ekran yer paylaşımı uygulaması, Outline izinleri penceresini arka plana gönderiyor olabilir (Pencere bu durumda ön planda görünmez). Bu nedenle, Android cihazınızda böyle bir uygulamanın yüklü olmadığından emin olun.

Android cihazınızda Ayarlar > Uygulamalar > Özel uygulama erişimi'ne gidin. Ardından "Diğer uygulamaların üzerinde göster"e dokunun. Bu davranışa izin veren tüm uygulamalara erişimi kaldırabilirsiniz.

iOS için: [Bu destek makalesine](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web) göz atın.

Sunucuyla ilgili sorunlar:

## Sorunları test etme:

Birden fazla sunucuya erişiminiz varsa diğer sunucuya bağlanmayı deneyin.

## Sorunları düzeltme:

Sunucunun silinip silinmediğini öğrenmek için hizmet yöneticinizle iletişime geçin. Sunucu silindiyse hizmet yöneticinizden başka bir sunucunun [erişim anahtarını](/about/terminology) isteyin.

Sunucuyu siz oluşturduysanız Outline Manager aracılığıyla veya [SSH](https://en.wikipedia.org/wiki/Secure_Shell) gibi başka bir yöntemle sunucuya bağlanmayı deneyin. Bu çözüm işe yaramazsa sunucunun hâlâ internete bağlı olup olmadığını görmek için bulut sağlayıcı konsolunu (varsa) kontrol etmeyi deneyebilirsiniz.

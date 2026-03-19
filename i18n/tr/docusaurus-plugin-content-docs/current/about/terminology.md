---
title: Terminoloji
sidebar_label: Terminoloji
---

## VPN nedir?
 Sanal özel ağ (VPN), cihazlarınız ile ana bilgisayar sunucusu arasında kurulan özel bir bağlantıdır. VPN kullandığınızda trafiğiniz internet servis sağlayıcıdan gizlenir. Aşağıdaki nedenlerle VPN kullanmanızda fayda olabilir:

- Genel kablosuz ağ kullanıyorsanız verilerinizi korumak için
- Tarama verilerinizi internet servis sağlayıcınızdan ve devlet kurumlarından gizlemek için
- Dünyanın dört bir yanındaki çeşitli kaynaklardan sansürsüz içeriklere erişmek için

## Outline ile geleneksel VPN'ler arasındaki fark nedir?
 İnternet servis sağlayıcılar, sıkça kullanılan güvenlik protokollerini ve/veya trafik hacmi trendlerini algılayarak geleneksel VPN'leri kolayca tespit edip engelleyebilir. Outline'ın geleneksel VPN'lerden daha dirençli olmasının nedeni, kullandığı protokolün tespit edilmesinin ve bu sayede engellenmesinin de zor olmasıdır. Outline, ağ tabanlı engelleme ya da IP engelleme gibi karmaşık sansür biçimlerine karşı dirençlidir.

## Outline sunucuları nedir?
 Outline sunucuları, izin verilen kullanıcıların bağlanacağı VPN'i çalıştırır. Yeni bir ağ oluşturuyorsanız kendi güvenli sunucunuzu Outline sunucusu olarak kullanabilir ya da aşağıdaki gibi bulut servis sağlayıcılarından yararlanabilirsiniz:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Sunucunuzu Outline Manager'da ayarlarsınız.

## Hizmet yöneticisi nedir? {#servicemanager}
 Hizmet yöneticisi, Outline sunucusunu ayarlayıp erişim anahtarlarını kullanıcılarla paylaşmakla yükümlü kişidir. Hizmet yöneticisi genellikle sunucu kullanım masraflarıyla da ilgilenir. 

## Erişim anahtarı nedir? {#accesskey}
 Erişim anahtarı, mevcut Outline sunucularına erişmek ve VPN'e bağlanmak için kullanılır. Erişim anahtarını [hizmet yöneticisi](#servicemanager) sağlayabilir ya da [Outline sunucusunu kendiniz ayarlayabilirsiniz.](/manager/server-setup/setup-server) Erişim anahtarı örneği (Yalnızca örnek verme amaçlıdır ve kullanılamaz): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Outline Manager nedir?
 Outline Manager; hizmet yöneticisinin Outline sunucusu ayarlamasına, [erişim anahtarları](#accesskey) oluşturmasına ve her anahtarın kullanımı için veri sınırı belirlemesine olanak tanıyan bir masaüstü uygulamasıdır. Outline Manager'ın en yeni sürümünü [buradan](https://getoutline.org/get-started/#step-3) veya [buradan](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/) indirebilirsiniz.

## Outline istemcisi nedir?
 Outline istemcisi, Outline sunucularına bağlanmanıza ve erişim anahtarı aracılığıyla VPN'e erişmenize olanak tanıyan bir masaüstü ve mobil uygulamasıdır. Outline istemcisinin en yeni sürümünü [buradan](https://getoutline.org/get-started/#step-3) veya [buradan](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/) indirebilirsiniz.

## Veri sınırları nedir?
 Outline Manager, aşırı kullanımın önüne geçmek ve maliyetleri öngörmenize yardımcı olmak için hizmet yöneticilerinin erişim anahtarları için 30 günlük hareketli veri sınırı belirlemesine olanak tanır. Hizmet yöneticileri, her anahtarda geçerli olacak varsayılan sınırı belirleyebilir ya da varsayılan sınırı geçersiz kılacak farklı bir sınır ayarlayabilir. Belirlenen sınırlar anında geçerli olur ve saatte bir uygulanır.

Metriklerin Jigsaw ile paylaşılmasına izin veren hizmet yöneticileri, veri sınırı kullanımının nasıl raporlanacağıyla ilgili ayrıntılı bilgi edinmek için [veri toplama politikasını](/about/data-collection) inceleyebilir.

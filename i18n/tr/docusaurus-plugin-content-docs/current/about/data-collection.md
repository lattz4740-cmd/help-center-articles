---
title: Veri ve bilgi toplama
sidebar_label: Veri ve bilgi toplama
---

Outline, siz kişisel bilgi sağlamayı kabul etmediğiniz sürece kişisel bilgilerinizi toplamaz. Outline ayrıca, ziyaret ettiğiniz web siteleri veya kiminle ne hakkında iletişim kurduğunuz gibi bilgileri de toplamaz.

 Bir üçüncü taraf bulut sağlayıcıyla Outline Manager üzerinden hesap oluşturuyor veya bir hesaba giriş yapıyorsanız üçüncü taraf bulut sağlayıcınıza sunduğunuz bilgileri (ör. e-posta adresiniz, adınız, fatura bilgileriniz ve ödeme ayrıntıları) toplamayız.

****Otomatik olarak topladığımız bilgiler****

 İki tür bilgiyi otomatik olarak toplarız.

 1. Sunucu IP'si

 Outline sunucusunun IP'si [Quay.io](https://quay.io/) tarafından toplanır ve sunucu en son güvenlik ve özellik iyileştirmeleriyle otomatik olarak güncellendiğinde IP bilgisi bize iletilir. Sunucu IP'si, bulut sunucusu sağlayıcıyı ve Outline sunucusunun kurulduğu şehri tanımlayabilir. Ancak sunucuyu çalıştıran kişi veya sunucuya kimlerin eriştiği gibi bilgileri sağlamaz.

 2. Kimliği tanımlayabilecek bilgiler dışındaki teknik bilgiler

 Outline kilitlenirse veya önemli bir istisna oluşursa ya da Outline uygulaması üzerinden manuel olarak geri bildirim gönderirseniz aşağıda listelenen bilgiler bildirilir. Bu bilgiler yalnızca kararlılık veya performansla ilgili sorunların tanımlanmasına ve düzeltilmesine yardımcı olmaları amacıyla kullanılır.

- Ülke
- Yerel ayar
- Kilitlenmenin/istisnanın oluştuğu tarih ve saat ile öncesindeki en fazla 100 etkinlik (ör. bir kullanıcının "Hakkında" bölümünü açması)
- İstatistiksel olarak derlenmiş istisna mesajları
- OS adı ve sürümü
- Telefon modeli (uygunsa)
- Uygulama başlangıç zamanı
- Tarayıcı
- Mimari
- Outline sürümü ve derleme numarası

Bu bilgiler, HTTPS kullanılarak üçüncü taraf bir açık kaynak hata izleme sağlayıcısı olan Sentry'ye ([sentry.io](https://sentry.io/)) aktarılır. Sentry, verilerinizi yetkisiz erişim, paylaşım, kullanım ve kaybolmaya karşı korumak için endüstri standardında çeşitli teknolojiler ve hizmetler kullanır. Sentry'nin politikalarıyla ilgili sorularınız varsa lütfen [https://sentry.io/security/](https://sentry.io/security/) ve [https://sentry.io/privacy/](https://sentry.io/privacy/) adreslerini ziyaret edin veya [security@sentry.io](mailto:security@sentry.io) adresiyle iletişime geçin. Sentry tarafından depolanan tüm Outline verileri yalnızca Outline ekibi üyelerinin erişebileceği şekilde kısıtlanmıştır.

****Yalnızca onay verildiğinde topladığımız bilgiler****

 Outline, onay verildiğinde aşağıdaki bilgileri Outline ekibine bildirir.

 1. Kullanım metrikleri

 Outline sunucusu, her bir erişim anahtarı için son bir saat içindeki aktarılan bayt sayısı, kullanıcının sunucuya bağlı olduğu süre, kullanılan kimlik bilgilerinin menşe ülkeleri ile otonom sistemleri ve herhangi bir özelliğin etkinleştirilip etkinleştirilmediği bilgilerini otomatik olarak toplar. İletişimin içeriği veya kimliği tanımlayabilecek meta veriler (ör. giriş bilgileri, e-postalar, cihaz kimlikleri vs.) günlüğe kaydedilmez. Tüm metrikler bir sunucu kimliğine bağlıdır. Sunucu kimliğini değiştirme talimatlarına [buradan](/manager/server-management/reset-server-id) ulaşabilirsiniz.

 Varsayılan olarak, Outline sunucuları bu metrikleri Outline ekibiyle paylaşmaz. Sunucu yöneticisi kullanım metriklerini paylaşmayı açıkça seçerse bu bilgiler Outline ekibine her saat başı güvenli bir şekilde gönderilir. 60 günün sonunda, kullanım metrikleri ülke düzeyinde bir araya toplanır. Sunucu yöneticileri Outline Manager'daki "Settings" (Ayarlar) menüsüne giderek kullanım metriklerini paylaşma tercihlerini diledikleri zaman değiştirebilir.

 Sunucu kullanımınızla ilgili anonim metrikleri bizimle paylaşmanız bizim için çok değerlidir. Bu metrikler, kullanım trendlerinin ölçülmesi ve ürünün iyileştirilmesi amacıyla kullanılır.

 Örneğin, bir sunucu yöneticisi kullanım metriklerini bizimle paylaşmayı seçerse sunucu kimliği 12345 olan ve veri sınırları özelliği etkinleştirilmiş bir sunucunun önceki gün 3 saat kullanıldığını ve her biri ABD ile Kanada'da kullanılan üç anahtardan toplam 500 megabayt veri aktarıldığını gösteren bilgiler alabiliriz.

 2. Geri bildirim göndermeniz hâlinde yorumlarınız ve e-posta adresiniz

 Outline Manager ve Outline uygulamaları, ekibe geri bildirim göndermenize olanak tanır. Kimliği tanımlayabilecek bilgiler eklememenizi öneririz. Ancak ekipten yanıt almak istemeniz ihtimaline karşı isteğe bağlı bir e-posta adresi alanı vardır. Ayrıca, geri bildiriminizi anlayabilmek için otomatik olarak bazı temel bilgiler de toplarız. Hangi verileri topladığımızı öğrenmek için lütfen yukarıdaki "Otomatik olarak topladığımız bilgiler" bölümünde 2. maddeye bakın. Outline'ın güvenlik ve gizlilik uygulamaları hakkında daha fazla bilgiye [buradan](/about/security-and-privacy) ulaşabilirsiniz.

 Android cihazda Outline uygulamasının beta sürümünü kullanıyorsanız sorunları tespit edip Outline'ı iyileştirmemize yardımcı olabilecek hata ayıklama bilgilerini toplamak için Google'ın [Firebase](https://firebase.google.com/) hizmetinden yararlanabiliriz. Firebase'in gizlilik ve güvenlik politikaları hakkında daha fazla bilgiye ilgili web sitesinden ulaşabilirsiniz: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Outline'ın bu bilgileri Firebase üzerinden göndermesini istemiyorsanız lütfen uygulamanın üretim sürümünü kullanın.

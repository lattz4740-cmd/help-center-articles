---
title: "Erişim anahtarlarında veri sınırı belirlemek için ne yapmam gerekir?"
sidebar_label: "Erişim anahtarlarında veri sınırı belirlemek için ne yapmam gerekir?"
---

Tüm erişim anahtarlarına uygulanacak bir veri sınırı belirleyebilirsiniz. Veri sınırı belirlemek için Outline Manager'ı açın ve Ayarlar'a gidin. Burada Veri sınırları düğmesini görürsünüz. Bu düğmeyi etkinleştirdiğinizde sınır belirleyebilirsiniz.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Sınırı belirledikten sonra, erişim anahtarı sayfasında her kullanıcının sınıra ne kadar yaklaştığını görebilirsiniz. Bu sayfadaki çubuk grafikte son 30 güne ait veri kullanımı gösterilir.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Tüm erişim anahtarlarınız için sınır belirlemenin yanı sıra her anahtarın kendi veri sınırını da belirleyebilirsiniz. Bu ayar diğer tüm varsayılan veri sınırlarınızı geçersiz kılar. Ancak varsayılan veri sınırınız yoksa bile herhangi bir anahtar için veri sınırı belirleyebilirsiniz. 

 Bir anahtarın veri aktarımı sınırını belirlemek için Outline Manager'ı açın, ayarlamak istediğiniz anahtarın yer aldığı Bağlantılar sekmesine gidin ve anahtarın bulunduğu satırın sağ tarafındaki menüyü tıklayın. Daha sonra Veri Sınırı'nı tıklayın. "Erişim anahtarım" bölümündeki veri sınırını değiştirmek için Veri Sınırları simgesini ![Veri Sınırları simgesi](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw) tıklayın.

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

"Özel bir veri sınırı belirle" kutusunu işaretleyin. Bu onay kutusunu işaretledikten sonra söz konusu anahtar için özel veri sınırı belirlemek üzere kullanabileceğiniz bir alan görürsünüz. İşlemi tamamladıktan sonra veri sınırını kaydetmek için KAYDET düğmesini tıklayın.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Seçtiğiniz anahtar için belirlediğiniz veri aktarımı sınırını kaydettikten sonra her anahtarın ilgili sınırı, veri kullanımı (son 30 günlük) ile birlikte ana ekranda gösterilir.

Bir erişim anahtarının veri sınırını kaldırmak için ilgili anahtarın Veri Sınırı iletişim kutusuna tekrar gidin, "Özel bir veri sınırı belirle" kutusunun işaretini kaldırın ve KAYDET düğmesini tıklayın.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

## **Veri sınırıyla ilgili sık sorulan sorular**
## **30 günlük hareketli veri sınırı nedir?**
 30 günlük hareketli veri sınırı, her bir anahtarın son 30 gün içindeki toplam kullanımını hesaplar ve ilgili dönem boyunca anahtar kullanımını sınırın altında tutar. Böylece, anahtarın herhangi bir 30 günlük süre boyunca (30 gün veya daha kısa olan takvim ayları dahil) sınırı aşmaması sağlanır. Bu, her bir kullanıcının kullanılabileceği veri miktarının, 31 gün önce kullandıkları miktar ölçüsünde artacağı anlamına gelir.

## Outline, hareketli sınırları neden kullanır?
 Hareketli sınırlar, her 30 günlük dönem boyunca çeşitli avantajlar sunar. Yani, tekrarlı sınıra kıyasla yapılandırılması daha basittir (örneğin, ayın günü değiştirilebilir) ve tekrarlı sınıra benzer avantajlara sahiptir. Ayrıca, mevcut Outline veri kullanımı ekranının yanı sıra analiz hizmetleri ve sunucu istatistikleri gibi yaygın araçlarla da ortaklaşa çalışır.

## Veri sınırı hesaplamasına hangi veriler dahil edilir?
 Her erişim anahtarının sunucudan çıkışı hesaplamaya dahil edilir. Daha net ifade etmek gerekirse anahtar kimliğiyle sunucudan dışarı gönderilen veriler ve aynı zamanda tekrar istemciye giren veriler sayılır. Pratikte, bu hesaplamanın anahtardan sunucuya giden ve sunucudan geri dönen trafiği yansıtması ve kullanıcıların sayımlarıyla eşleşmesi beklenmektedir. Kriter olarak çıkışı seçmemizin nedeni, anketimize katılan bulut hizmeti sağlayıcıların da faturalandırma için bu kriteri kullanmasıdır.

## Veri sınırını aşan kullanıcılara bildirim gönderilecek mi?
 Şu anda gönderilmiyor. Birçok bulut sağlayıcısı, tüm ay için 1 TB gibi bir sınıra sahip. Bu sınır, 100 GB'tan 10 kullanıcıyı ya da 10 GB'tan 100 kullanıcıyı destekleyebiliyor. Bunlar oldukça büyük rakamlar ve çoğu kullanıcının bu tür rakamlara ulaşmasını beklemiyoruz. Kullanıcıların limite ulaştıklarında sunucu yöneticilerine ulaşacağını umuyoruz. Ancak sizin kullanım senaryonuzda bildirimlerin ne açıdan kullanışlı olacağını öğrenmek isteriz. Bize [buradan](/about/feedback) ulaşabilirsiniz.

## Veri sınırına yaklaşan kullanıcılara bildirim gönderilecek mi?
 Sınıra yaklaşan bir kullanıcının alacağı yeni veri miktarı, 30 gün önceki kullanımı temel aldığından günden güne değişiklik gösterecektir. Uyarıların son kullanıcılara yardımcı olmaktan ziyade kafa karışıklığına neden olacağını düşünüyoruz. Bu davranışla ilgili görüşlerinizi öğrenmeyi çok isteriz. Bize [buradan](/about/feedback) ulaşabilirsiniz.

## Bir kullanıcının veri kullanımını sıfırlayabilir miyim?
 Hayır. Bir kullanıcının sınırına daima son 30 günlük kullanımı dahil edilir. Ancak kullanıcının anahtarındaki veri sınırını artırabilir veya kendisi için yeni bir anahtar oluşturabilirsiniz.

## Veri sınırlarını etkinleştirdiğim anda neden bazı kullanıcılarımın erişimi kayboldu?
 Veri sınırları, kullanıcıların son 30 gün boyunca yaptıkları veri aktarımlarını temel alır. Bu veri aktarımları, veri sınırlarının etkinleştirilmesinden bağımsız olarak kaydedilir. Söz konusu kullanıcıların sınır uygulanmadan önce sınırı aşmış olması da mümkündür. Ayrıca, tek bir anahtarın veri sınırı değiştirildiğinde bile tüm veri sınırlarının uygulandığını unutmayın.

## Sunucu genelinde bir sınır (ör. "30 gün için 1 TB") belirleyebilir miyim?
 Şu anda bunu yapamazsınız. Kullanım alanınızla ilgili daha fazla bilgi edinmeyi çok isteriz. Bize [buradan](/about/feedback) ulaşabilirsiniz.

## Hem varsayılan bir veri sınırı hem belirli bir anahtarın veri sınırı varsa hangisi uygulanır?
 Belirli bir anahtarın veri sınırı, belirlediğiniz tüm varsayılan veri sınırlarını (varsa) geçersiz kılar.

## Varsayılan bir veri sınırı yoksa belirli bir anahtar için veri sınırı belirleyebilir miyim?
 Evet. Herhangi bir anahtar için veri sınırı belirlemeden önce varsayılan bir sınırı tanımlamış olmanız gerekmez. Örneğin, çok sayıda kullanıcıyla paylaşılacağını düşündüğünüz belirli bir anahtar için sınır belirleyerek kendinizi bu anahtar üzerinden yapılabilecek aşırı veri aktarımlarına karşı koruyabilirsiniz.

---
title: "Outline'ı kullanırken güvenlik ve gizlilik"
sidebar_label: "Outline'ı kullanırken güvenlik ve gizlilik"
---

Outline'ı kullanırken güvenlik ve gizlilik

## Outline'ın çevrimiçi iletişimlerinizi koruma şekli

İnternet trafiği, en çok yerel veya ulusal ağınız üzerinden dolaşırken takibe açık durumdadır.

Outline, internet trafiğini ulusal ağınız içinde dolaşırken şifreleyerek iletişimlerinizin gizli kalmasına yardımcı olur ve verileri Outline sunucusuna erişene kadar şifrelenmiş durumda tutar. Trafik Outline tarafından şifrelendiğinde, ağ izleyicileri ziyaret ettiğiniz web sayfalarını veya aktardığınız bilgileri denetleyemez.

Outline ayrıca ülkenizde başka türlü erişilemeyen uçtan uca güvenli iletişim araçlarına erişebilmenize de yardımcı olabilir.

## Şifreleme standartları

Outline, AEAD 256 bit Chacha2020 IETF Poly 1305 şifresini kullanarak cihazınızla Outline sunucusu arasındaki iletişimleri şifreler. AEAD şifreleri; gizliliği, doğruluğu ve özgünlüğü korurken modern donanımlarda mükemmel performans sergiler.

## Güvenlik denetimleri

Outline, 2018'de yazılımların en son güvenlik standartlarına uygunluğunu inceleyen iki bağımsız dijital güvenlik kuruluşu olan Radically Open Security ve Cure53 tarafından denetlenmiştir. Radically Open Security, 2022'de başka bir denetim daha gerçekleştirmiştir. Cure53 ise 2024'te Outline SDK'yı denetlemiştir. İlgili raporları aşağıda bulabilirsiniz:

- [Radically Open Security Penetration Test Report (Mart 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53 Pentest & Audit Report Jigsaw Outline (Aralık 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Radically Open Security Penetration Test Report (Aralık 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Cure53 Pentest Report Jigsaw Outline VPN SDK (Ocak 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Anonim metrikler ve günlükler

Outline her erişim anahtarı için kullanılan bant genişliğini ("aktarılan bayt sayısı" olarak) izler. Bu bilgiler, sunucu yöneticilerinin kendi bant genişliklerini bulut sunucusu sağlayıcılara göre gereken şekilde ayarlamasına olanak sağlar ancak Outline sunucusundan geçen gerçek bilgileri görmelerine izin vermez.

Outline'ın [veri ve bilgi toplama şekli](/about/data-collection) hakkında daha fazla bilgi edinin.

---

## Güvenlik ve gizlilik ile ilgili SSS

## Outline, internette anonim olmamı sağlayabilir mi?

Hayır, Outline bir anonimleştirme aracı değildir. Outline, gizliliğinizi olası ağ izleyicilerine karşı korur.

Outline, ziyaret ettiğiniz web sitelerinde tam anonimleştirme sunmaz. Ziyaret ettiğiniz siteler, giriş yaptığınızda ve bazen de tarayıcı parmak izini alma gibi tekniklerle sizi yine de tanımlayabilir. Mobil uygulamalar için, çoğu modern akıllı telefonda yerleşik GPS'e dayalı olabildiğinden yüklü uygulamaların proxy'nizden bağımsız olarak konum bilginizi almasına izin veren API'ler vardır.

Genel olarak VPN'ler, özellikle de internet takibine karşı önemli korumalar sunar, ancak çevrimiçi çalışma her zaman risklere açıktır. VPN kullanıldığında bile İSS'ler kimliğinizi zaten biliyor ve aynı zamanda ağ trafiğinizi gözlemleyebiliyorsa Outline sunucunuzun IP adresini belirleyebilirler. Bu bilgiler, Outline sunucusuna erişimi engellemek veya genellikle ne zaman çevrimiçi olduğunuz gibi kullanım kalıplarınızı ve yaklaşık olarak konumunuzu öğrenebilmek için kullanılabilir.

## Herhangi biri Outline kullanıp kullanmadığımı belirleyebilir mi?

Muhtemelen. Eriştiğiniz platformlar ve hizmetler büyük ihtimalle bağlantınızın bir bulut sunucusundan geldiğini belirleyebilir. Bazı durumlarda VPN kullandığınızı anlayabilirler ancak internet trafiğinizin içeriğini görmeleri mümkün değildir.

## Outline beni olası tüm siber tehditlere karşı korur mu?

Hayır. Hiçbir araç sizi olası tüm siber tehditlere karşı koruyamaz. Outline açık internete erişmenize olanak sağlar ve trafiğinizi şifreleyerek gizliliğinizi daha iyi korur. Ancak kötü amaçlı yazılım ve kimlik avı gibi diğer saldırı türlerine karşı korunmak için ek önlemler almanızı öneririz.

İnternetteki savunma önlemlerinizi güçlendirmek için lütfen kuruluşunuzun siber güvenlik uzmanına danışın. Alternatif olarak, [Security Planner](https://securityplanner.org/) web sitesindeki alanında lider güvenlik uzmanlarından kişiselleştirilmiş yardım alabilirsiniz. Security Planner, endişelerinize en iyi şekilde yanıt veren doğru siber güvenlik araçlarını seçmeniz için net talimatlar sunan bir web sitesidir.

Ayrıca [Jigsaw](https://jigsaw.google.com/)'un sunduğu [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) ve [Şifre Uyarısı](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?) gibi diğer siber güvenlik ürünlerine de göz atabilirsiniz.

## VPN kullanmak yasal mı?

Outline'ı çalıştırmadan veya uygulamayı kullanmadan önce, lütfen kullanmayı planladığınız bulut sağlayıcının Hizmet Şartları'na ek olarak yürürlükteki yasa ve düzenlemeleri de inceleyin.

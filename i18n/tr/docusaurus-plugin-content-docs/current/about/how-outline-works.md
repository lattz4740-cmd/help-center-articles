---
title: "Outline'ın çalışma şekli"
sidebar_label: "Outline'ın çalışma şekli"
---

## Sunucunun yüklenmesi
 ​Outline'ın yüklenmesi basit gibi görünse de sunucunuzun yüklenmesi için perde arkasında gerçekleşen bazı karmaşık adımlar vardır. Her Outline yüklemesinde bir komut dosyası aşağıdaki adımları çalıştırır:

- Shadowbox görüntüsünün kararlı sürümü Docker kullanılarak alınır ve içe aktarılır. Görüntü, [Quay.io](https://quay.io/)'daki [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags) adresinde barındırılır. Bu görüntüde Outline sunucusu ve Management API yer alır. Bu bilgiler daha sonra Outline Server Management uygulaması tarafından erişim anahtarlarını oluşturup kaldırmak, anonim metrikleri raporlamayı etkinleştirmek/devre dışı bırakmak vb. için kullanılır.
- [Watchtower](https://github.com/v2tec/watchtower) yüklenir ve saat başı görüntü güncellemesi olup olmadığını kontrol edecek şekilde yapılandırılır. Bu işlem, her Outline sunucusunu en son özellik ve güvenlik iyileştirmeleriyle sürekli olarak güncel tutar.
- Rastgele bir bağlantı noktasında ve rastgele oluşturulmuş gizli bir yolda, Management API'ye erişmek için kullanılan bir web sunucusu başlatılır.
- Bir alan adına sahip olmamasına rağmen, Outline sunucusu yönetiminin TLS kullanılarak şifrelenebilmesi için [kendinden imzalı bir SSL sertifikası](https://en.wikipedia.org/wiki/Self-signed_certificate) oluşturulur. MITM saldırılarının engellenmesine yardımcı olması için bu sertifikanın benzersiz bir parmak izi de Outline Manager uygulamasında oluşturulur ve depolanır.

Outline yüklendikten sonra herhangi bir yapılandırma işlemi gerekmez.

## Sunucu güvenliği
 Outline yazılımı açık kaynaktır. Bu, herkesin kodu görebileceği ve keşfedilen güvenlik açıkları varsa iyileştirebileceği anlamına gelir. Kodumuz [GitHub](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline)'da barındırılır.

 Ayrıca hiçbir Outline sunucusunun, yazılımın eski sürümlerini çalıştırmaması için yeni bir sürüm yayınlandığında tüm yüklü Outline sunucuları otomatik olarak güncellenir.

 Sunucudaki erişim anahtarlarının yönetilmesi için Outline Manager uygulaması Outline sunucusunda bir yönetim hizmeti ile etkileşimde bulunur. Yönetim hizmeti rastgele bir bağlantı noktasında ve gizli, benzersiz bir yolda çalışır. Yönetim Hizmeti, uygun gizli yol belirtilmediği sürece sorgulara yanıt vermediği için yoklamaya dayanıklıdır. Son olarak, yönetim hizmetine yönelik tüm iletişim [kendinden imzalı bir SSL sertifikasıyla](https://en.wikipedia.org/wiki/Self-signed_certificate) şifrelenir.

 Ayrıca Outline sunucusu herhangi bir günlük kaydı depolamadığından, güvenlik ihlali olsa bile kullanıcı verileri paylaşılmaz. [Daha fazla bilgi edinin.](/about/security-and-privacy) Outline, 2018'de [Radically Open Security](https://radicallyopensecurity.com/) ve [Cure53](https://cure53.de/) tarafından denetlenmiştir. Raporları [burada](/about/security-and-privacy) bulabilirsiniz.

## UDP trafiğini işleme
 Outline, sistem genelinde kullanılabilen bir VPN olarak çalıştırılabilir. Bu, tüm UDP trafiğinin Outline sunucusu üzerinden geçirildiği anlamına gelir.

## DNS trafiği
Outline, tüm DNS aramalarını Outline sunucusu üzerinden gerçekleştirir ve bunları diğer tüm ağ etkinlikleri için kullanılan şifrelemeyi kullanarak korur. DNS sorgularınız, Outline sunucusu üzerinden Dyn Internet Guide, OpenDNS, Cloudflare DNS veya Quad9 DNS'ye gider. Outline, DNS aramalarınızı günlüğe kaydetmez.

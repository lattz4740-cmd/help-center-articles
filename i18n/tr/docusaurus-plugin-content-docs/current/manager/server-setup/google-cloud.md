---
title: Google Cloud Otomatik Kurulumu
sidebar_label: Google Cloud Otomatik Kurulumu
---

## Genel Bakış

Outline Manager, Google Cloud'da kurulu sunucularda Outline Server'ı otomatik olarak yapılandırmanıza olanak tanıyan bir özellik içerir. Bu özelliği kullanmayı tercih ederseniz Outline Manager, Google Hesabınızla oturum açmanızı ister. Bu işlem, Google Cloud hesabınızı yapılandırmak amacıyla, yerel Outline Manager yüklemenize belirli [OAuth](https://developers.google.com/identity/protocols/oauth2) izinleri verir.

Bu izinleri vermek istemiyorsanız Outline'ı Google Cloud Platform'da çalıştırmak için Outline Manager'daki gelişmiş kurulum talimatlarını uygulayabilirsiniz.

## Verilen İzinler

Outline Manager'ın otomatik kurulum yapabilmesi için Google Hesabınızdan aşağıdaki izinleri alması gerekir.

## Google Cloud Platform

- Google Compute Engine kaynaklarınızı görüntüleme ve yönetme
- Google Cloud hizmetlerindeki verilerinizi görüntüleme ve Google Hesabınızın e-posta adresini görme

## Temel hesap bilgileri

- Birincil Google Hesabı e-posta adresinizi görme
- Sizi Google'daki kişisel bilgilerinizle ilişkilendirme

## Ek erişim

- Cloud Platform projelerinizi yönetme
- Google Cloud Platform faturalandırma hesaplarınızı görüntüleme ve yönetme
- Google API hizmet yapılandırmanızı yönetme

## Bu izinler, Outline sunucularınızı yönetmek için gelişmiş işlevleri desteklememize olanak tanır. Örneğin:

- Doğru faturalandırma hesabını seçmenize olanak tanıma
- Outline sunucularınızı organize etmek için yeni bir proje oluşturma
- Mevcut veri merkezlerini listeleme
- Outline'ı çalıştırmak için yeni sanal makineler oluşturma
- Yeni sanal makineyi Outline ile yapılandırma

## İzinleri İptal Etme

[Hesabım](https://myaccount.google.com/permissions) sayfasına giderek Outline Manager'ın Google Cloud Platform'a erişimini iptal edebilirsiniz. Erişimi iptal ederseniz otomatik kurulumla oluşturduğunuz sunucular çalışmaya devam eder ancak artık Outline Manager'da görünmez. Sunuculara tekrar erişebilmek için otomatik kurulum akışını başlatarak Google Cloud Platform'a tekrar bağlanmanız yeterlidir.

## Outline Proje Kuruluşu

Google Cloud otomatik kurulumu, Outline sunucularınızı organize etmek için tek bir [Google Cloud projesi](https://cloud.google.com/resource-manager/docs/creating-managing-projects) kullanır. Proje, otomatik kurulumun ilk kullanımı sırasında, önerilen bir proje kimliği kullanılarak oluşturulur. Söz konusu proje kimliğinin başında "Outline-" ifadesi, devamında ise rastgele karakterlerden oluşan bir dize bulunur. Dilerseniz oluşturma sırasında farklı bir proje kimliği seçebilirsiniz. Proje "Outline sunucuları" olarak adlandırılacaktır.

## Faturalandırma Hesabı

Google Cloud projeleri için ödeme bilgilerini tanımlayan bağlı bir "faturalandırma hesabı" gerekir. Google Cloud otomatik kurulumunu ilk kez kullandığınızda, Outline sunucularınızla ilişkilendirilecek bir faturalandırma hesabı sağlamanız istenir. Faturalandırma hesabıyla ilgili bir sorun olduğunda bazen sunucu çalışmayı durdurur. Bu durumda, [Google Cloud Console](https://console.cloud.google.com/getting-started)'a giriş yapmanız, Outline ile ilişkili Google Cloud projesini ("Outline sunucuları" adlı proje) bulmanız ve faturalandırma ayarlarını güncellemeniz gerekir.

## Sunucuları Kaldırma

Otomatik kurulumla oluşturulan sunucularınızı kaldırmak istiyorsanız bunu yapmanın en kolay yolu Outline Manager'ı kullanmaktır. Ancak sunucuları kendiniz kaldırmak istiyorsanız [Google Cloud Console](https://console.cloud.google.com/getting-started)'a giriş yapıp ilk kurulum sırasında oluşturulan projeyi ("Outline sunucuları" adlı proje) bulduktan sonra kaynakları buradan silebilir veya projeyi kapatabilirsiniz.

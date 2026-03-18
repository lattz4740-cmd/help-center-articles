---
title: Data və Məlumatların toplanması
sidebar_label: Data və Məlumatların toplanması
---

Outline təqdim etməyi seçmədiyiniz təqdirdə şəxsi məlumatlarınızı toplamır. Outline, həmçinin daxil olduğunuz veb-saytlar, əlaqə saxladığınız şəxs və ya bölüşdüyünüz informasiyalar haqqında məlumat toplamır.

 Outline Manager-də üçüncü tərəf bulud provayderi vasitəsilə hesab yaratsanız və ya daxil olsanız, e-poçt ünvanı, ad, faktura məlumatları və ödəniş təfərrüatları kimi üçüncü tərəf bulud provayderinə təqdim etdiyiniz məlumatları toplamırıq.

****Avtomatik topladığımız məlumatlar****

 İki növ məlumatı avtomatik toplayırıq.

 1. Server IP-si

 Outline server IP-si [Quay.io](http://quay.io/) tərəfindən toplanır və server avtomatik olaraq ən son təhlükəsizlik və funksiya təkmilləşdirmələri ilə yeniləndikdə bizim üçün əlçatan olur. Server IP-si bulud server provayderi və Outline serverinin quraşdırıldığı şəhəri müəyyən edə bilər, lakin bu zaman serveri kimin işlətdiyi və ya kimin daxil olduğu haqqında məlumat təqdim edilmir.

 2. Şəxsi olaraq kimliyi müəyyən etməyən texniki məlumatlar

 Outline nasazlıq səbəbilə işləməsə və ya qaçılmaz xəta baş versə, yaxud Outline tətbiqi ilə manual olaraq rəy göndərsəniz, aşağıdakı məlumatlar bildiriləcək: Bu məlumatlar yalnız stabillik və ya performans problemlərini müəyyən etmək və həll etmək üçün istifadə olunacaq.

- Ölkə
- Məkan
- Nasazlıq / xəta tarixi, vaxtı və "Haqqında" bölməsini açan istifadəçi kimi maksimum 100 sayda əvvəl baş verən hadisə
- Statik şəkildə tərtib edilmiş xəta mesajları
- Əməliyyat sisteminin adı və versiyası
- Telefon modeli (mümkünsə)
- Tətbiqin başladılma vaxtı
- Brauzer
- Arxitektura
- Outline versiyası və onun nömrəsi

Bu məlumat HTTPS vasitəsilə üçüncü tərəf olan Sentry ([sentry.io](http://sentry.io/)), yəni açıq mənbə xəta izləmə provayderinə ötürülür. Sentry datanızı icazəsiz giriş, açıqlama, istifadə və itkidən qorumaq üçün sənaye standartlarına cavab verən müxtəlif texnologiya və xidmətlərdən istifadə edir. Sentry siyasətləri ilə bağlı sualınız varsa, [https://sentry.io/security/](https://sentry.io/security/) və [https://sentry.io/privacy/](https://sentry.io/privacy/) ünvanlarına daxil olun və ya [security@sentry.io](mailto:security@sentry.io) ilə əlaqə saxlayın. Sentry-nin saxladığı bütün Outline datasına yalnız Outline komandası giriş edə bilər.

****Yalnız seçim edildikdən sonra əldə etdiyimiz məlumatlar****

 Outline seçim edildikdən sonra aşağıdakı məlumatı Outline komandasına bildirir:

 1. İstifadə göstəriciləri

 Hər bir Outline serveri avtomatik olaraq son bir saat ərzində və hər giriş açarı əsasında ötürülən baytların sayı, istifadəçinin serverə qoşulma müddəti, istifadə edilən giriş məlumatlarının mənşəyi üzrə ölkələr ilə anonim sistemlər və müəyyən funksiyanın aktiv və ya qeyri-aktiv edilib-edilmədiyi ilə bağlı məlumatları toplayır. Kommunikasiya kontentləri və ya şəxsi olaraq kimliyi müəyyən edən metadata (məs., girişlər, e-poçtlar, cihaz ID-ləri və s.) qeydə alınmır. Bütün göstəricilər server ID-si ilə bağlıdır. Server ID-sinin dəyişdirilməsi ilə bağlı təlimatları [burada](/manager/server-management/reset-server-id) tapa bilərsiniz.

 Defolt olaraq Outline Serverləri bu göstəriciləri Outline komandası ilə paylaşmır. Server administratoru aşkar formada istifadə göstəricilərinin paylaşılmasını seçibsə, bu məlumat Outline komandasına hər saat təhlükəsiz şəkildə göndəriləcək. 60 gün sonra istifadə göstəriciləri ölkə səviyyəsində toplanacaq. Server administratorları istifadə göstəricilərinin paylaşım tərcihlərini istənilən vaxt Outline Manager-də "Ayarlar" menyusuna daxil olmaqla dəyişə bilər.

 Server istifadəniz haqqında anonim göstəriciləri paylaşmağınız bizim üçün çox əhəmiyyətlidir. Bu, istifadə tendensiyalarını hesablamaq və məhsulu təkmilləşdirmək üçün istifadə edilir.

 Məsələn, Server administratoru istifadə göstəricilərini bizimlə paylaşmağı seçibsə, ID-si 12345 olan Serverin data limitləri funksiyası aktiv ikən dünən 3 saat ərzində istifadə edilərək hər biri Amerika Birləşmiş Ştatları və Kanadadakı 3 açardan ümumilikdə 500 meqabayt data ötürdüyünü göstərən məlumatı əldə edə bilərik.

 2. Rəy göndərdikdə şərhləriniz və e-poçtunuz

 Outline Manager və Outline Tətbiqləri komandaya şərh göndərməyinizə imkan verir. Şəxsi olaraq kimliyi müəyyən edən məlumatı daxil etməməyinizi tövsiyə edirik, lakin komandamızdan cavab gözləsəniz, istəyə görə e-poçt sahəsi əlçatan olacaq. Həmçinin rəyinizi aydınlaşdırmaq üçün bir neçə əsas məlumatları avtomatik toplayırıq. Topladığımız data haqqında məlumat üçün "Avtomatik əldə etdiyimiz məlumat" bölməsinin aşağısındakı 2-ci elementə baxın. Outline-ın təhlükəsizlik və məxfilik təcrübələri haqqında ətraflı məlumatı [burada](/about/security-and-privacy) əldə edin.

 Android-də Outline tətbiqinin beta versiyasından istifadə edirsinizsə, problemləri aşkarlamaq və Outline-ı təkmilləşdirməkdə bizə kömək edə biləcək sazlama məlumatlarını toplamaq üçün Google-un [Firebase](https://firebase.google.com/) xidmətindən istifadə edə bilərik. Firebase-in məxfilik və təhlükəsizlik siyasətləri haqqında veb-saytdan ətraflı məlumat əldə edə bilərsiniz: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Outline-ın bu məlumatı Firebase vasitəsilə göndərməsini istəmirsinizsə, tətbiqin istehsal versiyasından istifadə edin.

---
title: "Outline-ın işləmə qaydası"
sidebar_label: "Outline-ın işləmə qaydası"
---

## Serverin quraşdırılması
 ​Outline-nın quraşdırılması sadə görünə bilər, lakin əslində serverinizi quraşdırmaq üçün bir sıra mürəkkəb addımlar mövcuddur. Outline quraşdırıldıqda quraşdırma skripti aşağıdakı addımları yerinə yetirir:

- Shadowbox təsvirinin stabil versiyası Docker istifadə edərək əldə olunur və import edilir. Təsvir [Quay.io](https://quay.io/) serverində, [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags) ünvanında yerləşdirilib. Bu təsvirdə Outline serveri və Management API mövcuddur. O, daha sonra Outline Server Management tətbiqi tərəfindən giriş açarlarını yaratmaq və silmək, anonim göstəriciləri təqdim etməyi aktiv/deaktiv etmək və s. üçün istifadə edilir.
- [Watchtower](https://github.com/v2tec/watchtower) hər bir Outline serverinin ən son funksiyalar və təhlükəsizlik təkmilləşdirmələri ilə daim yenilənməsini təmin etmək, hər saat təsvir yeniləmələrini yoxlamaq üçün quraşdırılıb və konfiqurasiya edilib.
- Management API interfeysinə daxil olmaq üçün istifadə edilən veb-server ixtiyari portda quraşdırılır, eləcə də məxfi və ixtiyari yaradılmış ünvana sahib olur.
- Domen adı olmasa da, Outline serverinin idarə edilməsi TLS protokolundan istifadə etməklə şifrlənməsi üçün [öz-özünə imzalanan SSL sertifikatı](https://en.wikipedia.org/wiki/Self-signed_certificate) yaradılır. Bu sertifikatın unikal şifrləmə dəyəri də MITM hücumlarının qarşısını almaq üçün Outline Manager tətbiqində yaradılır və saxlanılır.

Outline-ı quraşdırdıqdan sonra konfiqurasiya etməyə ehtiyac yoxdur.

## Server təhlükəsizliyi
 Outline proqram təminatı açıq mənbədir, yəni hər kəs koda baxa və hər hansı qüsur aşkar edilərsə, onu təkmilləşdirə bilər. Kodumuz [GitHub](https://github.com/search?q=org%3AOutline-Foundation+outline&unscoped_q=outline) platformasında əlçatandır.

 Bundan əlavə, bütün quraşdırılmış Outline serverləri yeni versiya təqdim olunduqda avtomatik olaraq yenilənir və proqram təminatının köhnə versiyaları ilə işləyən heç bir Outline serverinin qalmaması təmin edilir.

 Serverdə giriş açarlarını idarə etmək üçün Outline Manager tətbiqi Outline serverindəki İdarəetmə Xidməti ilə qarşılıqlı əlaqə yaradır. İdarəetmə Xidməti ixtiyari portda, eləcə də məxfi və ixtiyari olaraq yaradılmış ünvanda işləyir. İdarəetmə Xidməti müvafiq məxfi ünvan göstərilmədiyi təqdirdə sorğuları nəzərə almadığı üçün yoxlanışa qarşı davamlıdır. Son olaraq, Management Service ilə bütün data mübadiləsi [öz-özünə imzalanan SSL sertifikatı](https://en.wikipedia.org/wiki/Self-signed_certificate) ilə şifrlənir.

 Həmçinin Outline serveri heç bir qeydi saxlamır, ona görə də təhlükəli vəziyyət yaransa belə, heç bir istifadəçi datası açıqlanmır. Ətraflı məlumatı [burada](/about/security-and-privacy) əldə edin. Outline 2018-ci ildə [Radically Open Security](https://radicallyopensecurity.com/) və [Cure53](https://cure53.de/) tərəfindən yoxlanılmışdır. Hesabatlara [burada](/about/security-and-privacy) baxın.

## UDP trafikinin idarə olunması
 Outline sistem səviyyəsində VPN kimi işləyə bilir, yəni bütün UDP trafiki Outline serveri vasitəsilə ötürülür.

## DNS trafiki
Outline bütün DNS axtarışlarını Outline serveri vasitəsilə həyata keçirir və onları bütün digər şəbəkə fəaliyyəti üçün istifadə edilən eyni şifrləmədən istifadə edərək qoruyur. DNS sorğularınız Outline serveri vasitəsilə Dyn Internet Guide, OpenDNS, Cloudflare DNS və ya Quad9 DNS serverlərinə ötürüləcək. Outline DNS axtarışlarınızı heç vaxt qeydə almır.

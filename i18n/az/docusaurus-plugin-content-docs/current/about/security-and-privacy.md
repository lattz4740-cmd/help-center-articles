---
title: Outline istifadəsi zamanı təhlükəsizlik və məxfilik
sidebar_label: Outline istifadəsi zamanı təhlükəsizlik və məxfilik
---

Outline istifadəsi zamanı təhlükəsizlik və məxfilik

## Outline onlayn kommunikasiyalarınızı necə qoruyur

İnternet trafikiniz ən çox yerli və ya milli şəbəkəniz vasitəsilə ötürülərkən nəzarətə qarşı qorunmasız olur.

Outline milli şəbəkəniz daxilində ötürülərkən internet trafikinizi şifrləməklə kommunikasiyalarınızı məxfi saxlamağa kömək edir və Outline serverinə çatdırılana qədər onu şifrlənmiş saxlayır. Trafik Outline ilə şifrləndikdə şəbəkə izləyiciləri daxil olduğunuz veb-saytları və ya ötürdüyünüz məlumatları yoxlaya bilməz.

Həmçinin Outline ölkənizdə başqa cür əlçatan olmayan təhlükəsiz ucdan-uca kommunikasiya vasitələrinə girişi bərpa etməyə kömək edə bilər.

## Şifrləmə standartları

Outline AEAD 256-bit Chacha2020 IETF Poly 1305 şifrindən istifadə edərək cihazınız və Outline Serveri arasındakı kommunikasiyaları şifrləyir. AEAD şifrləri məxfilik, bütövlük və orijinallıq təklif edir və müasir avadanlıqlarda üstün performans nümayiş etdirir.

## Təhlükəsizlik yoxlanışları

Outline 2018-ci ildə proqram təminatlarını ən son təhlükəsizlik standartlarına uyğun nəzərdən keçirən iki müstəqil rəqəmsal təhlükəsizlik təşkilatı olan Radically Open Security və Cure53 tərəfindən yoxlanılmışdır. Radically Open Security 2022-ci ildə əlavə yoxlama, Cure53 isə 2024-cü ildə Outline SDK üzrə yoxlama aparmışdır. Hesabatları burada oxuya bilərsiniz:

- [Radically Open Security tərəfindən Penetrasiya Testi üzrə Hesabat (2018-ci il mart)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53 Pentest və Jigsaw Outline Yoxlama Hesabatı (2018-ci il dekabr)](https://getoutline.org/reports/cure53-report.pdf)
- [Radically Open Security tərəfindən Penetrasiya Testi üzrə Hesabat (2022-ci il dekabr)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Cure53 tərəfindən Jigsaw Outline VPN SDK üzrə Penetrasiya Testi (2024-cü il yanvar)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Anonim göstəricilər və qeydlər

Outline hər bir giriş açarı üçün "ötürülmüş baytlar" kimi istifadə olunan zolaq genişliyini izləyir. Bu məlumat server administratorlarına öz bulud server provayderləri ilə zolaq genişliyi üzrə abunəliklərini lazım olduqda tənzimləməyə imkan verir, lakin onlara Outline serveri vasitəsilə ötürülən faktiki məlumatı görməyə imkan vermir.

Outline-da [data və məlumatların toplanması](/about/data-collection) haqqında ətraflı məlumat əldə edin.

---

## Təhlükəsizlik və məxfiliklə bağlı tez-tez verilən suallar

## Outline məni onlayn rejimdə anonim göstərə bilər?

Xeyr, Outline anonimləşdirmə aləti deyil. Outline məxfiliyinizi potensial şəbəkə izləyicilərindən qoruyur.

Veb-saytlara daxil olduğunuz zaman və bəzən brauzerin rəqəmsal barmaq izi kimi üsullar vasitəsilə kimliyiniz müəyyən edilə bildiyi üçün Outline daxil olduğunuz veb-saytlarda tam anonimlik təklif etmir. Mobil tətbiqlər üçün müasir smartfonların əksəriyyətində quraşdırılmış tətbiqlərə daxil edilmiş GPS-ə etibar edə bildikləri üçün proksidən asılı olmayaraq məkan məlumatlarınızı əldə etməyə imkan verən API-lər var.

Ümumilikdə VPN-lər, xüsusən də internet nəzarətindən əhəmiyyətli dərəcədə qorunma təklif edir, lakin onlayn işləmək hər zaman risklidir. Hətta VPN ilə belə ISP artıq kimliyinizdən xəbərdardırsa və şəbəkə trafikinizi müşahidə edə bilirsə, Outline serverinizin IP ünvanını müəyyən edə bilər. Bu məlumat Outline serverinə girişi bloklamaq və ya adətən onlayn olduğunuz zaman və ola bilsin ki, təxmini yerinizi öyrənmək üçün istifadə oluna bilər.

## Başqası Outline istifadə etdiyimi anlaya bilər?

Mümkündür. Daxil olduğunuz platforma və xidmətlər, çox güman ki, bağlantınızın bulud serverindən gəldiyini anlaya biləcəklər. Onlar bəzən VPN istifadə etdiyinizi təxmin edə bilsələr də, internet trafikinizin kontentlərini görə bilməzlər.

## Outline məni mümkün olan bütün kibertəhdidlərdən qoruyur?

Xeyr. Heç bir vasitə sizi mümkün olan bütün kibertəhdidlərdən qoruya bilməz. Outline sizə açıq internetə çıxış imkanı verir və trafikinizi şifrləməklə məxfiliyinizi artırır, lakin özünüzü zərərli proqram və fişinq kimi digər hücum növlərindən qorumaq üçün əlavə tədbirlər görməyi tövsiyə edirik.

Onlayn müdafiənizi gücləndirmək üçün təşkilatınızın kibertəhlükəsizlik üzrə mütəxəssisi ilə əməkdaşlıq edə bilərsiniz. Alternativ olaraq narahatlığınızla bağlı düzgün kibertəhlükəsizlik vasitələrinin seçilməsi üzrə sizə aydın təlimatlar təqdim etmək üçün hazırlanmış veb-sayt olan [Security Planner](https://securityplanner.org/) vasitəsilə aparıcı təhlükəsizlik mütəxəssislərindən fərdiləşdirilmiş təlimatlar əldə edə bilərsiniz.

Həmçinin [Jigsaw](https://jigsaw.google.com/) tərəfindən hazırlanmış [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) və [Password Alert](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?) kimi digər kibertəhlükəsizlik məhsulları ilə tanış ola bilərsiniz.

## VPN-dən istifadə etmək qanunidir?

Outline-ı başlatmazdan və ya tətbiqdən istifadə etməzdən əvvəl yerli qanun və qaydaları, həmçinin istifadə etməyi planlaşdırdığınız bulud provayderinin Xidmət Şərtlərini nəzərdən keçirin.

---
title: Google Cloud Avtomatlaşdırılmış Quraşdırma
sidebar_label: Google Cloud Avtomatlaşdırılmış Quraşdırma
---

## İcmal

Outline Manager Google Cloud-da işləyən serverdə Outline Serverini avtomatik konfiqurasiya etməyə imkan verən funksiyaya malikdir. Bu funksiyadan istifadə etməyi seçsəniz, Outline Manager Google Hesabı ilə daxil olmağınızı tələb edəcək, bu isə Google Cloud Hesabını konfiqurasiya etmək məqsədilə Outline Manager-in yerli quraşdırılması üçün müəyyən[OAuth](https://developers.google.com/identity/protocols/oauth2) icazələri verəcək.

 Bu icazələri vermək istəmirsinizsə, Outline-ı Google Cloud Platform-da işə salmaq üçün Outline Manager-dəki təkmil quraşdırma təlimatlarına əməl edə bilərsiniz.

## Qəbul edilən icazələr

Outline Manager avtomatlaşdırılmış quraşdırma təqdim etmək üçün Google Hesabınızdan aşağıdakı icazələri tələb edir:

## Google Cloud Platform

- Google Compute Engine resurslarına baxmaq və idarə etmək
- Google Cloud xidmətlərindəki datanıza və Google Hesabınızın e-poçt ünvanına baxmaq

## Əsas hesab məlumatları

- Əsas Google Hesabı e-poçt ünvanınıza baxmaq
- Fəaliyyətinizi Google-da şəxsi məlumatlarınız ilə əlaqələndirmək

## Əlavə giriş

- Cloud Platform layihələrinizi idarə etmək
- Google Cloud Platform billinq hesablarınızı görmək və idarə etmək
- Google API xidməti konfiqurasiyasını idarə etmək

Bu icazələr aşağıdakılar daxil olmaqla, Outline serverlərinizi idarə etmək üçün təkmil funksiyaları dəstəkləməyimizə imkan verir:

- Düzgün billinq hesabı seçmək
- Outline serverlərinizi təşkil etmək üçün yeni layihə yaratmaq
- Əlçatan data mərkəzlərini siyahıya almaq
- Outline-ı idarə etmək üçün yeni virtual cihazlar yaratmaq
- Outline ilə üçün yeni virtual cihazı konfiqurasiya etmək

## İcazələrin ləğv edilməsi

[Hesabım](https://myaccount.google.com/permissions) bölməsinə keçərək Outline Manager üçün Google Cloud Platform-a girişi ləğv edə bilərsiniz. Girişi ləğv etsəniz, avtomatlaşdırılmış quraşdırma ilə yaratdığınız bütün serverlər işləməyə davam edəcək, lakin artıq Outline Manager-də görünməyəcək. Serverlərə girişi bərpa etmək üçün avtomatik quraşdırma axınını başladaraq Google Cloud Platform-a yenidən qoşulun.

## Outline Layihəsinin Təşkili

Google Cloud avtomatlaşdırılmış quraşdırması Outline serverlərinizi qruplaşdırmaq üçün tək [Google Cloud layihəsindən](https://cloud.google.com/resource-manager/docs/creating-managing-projects) istifadə edir. Layihə avtomatlaşdırılmış quraşdırmanın ilk istifadəsi zamanı "Outline-" ilə başlayıb ardınca bir neçə təsadüfi simvol gələn təklif olunan layihə ID-si ilə yaradılır. Layihə yaradarkən fərqli bir layihə ID-si seçə də bilərsiniz. Layihə "Outline serverlər" adlanacaq.

## Billinq Hesabı

Google Cloud layihələri ödəniş məlumatlarını təyin edən əlaqələndirilmiş "billinq hesabı" tələb edir. Google Cloud avtomatlaşdırılmış quraşdırmasını ilk dəfə istifadə etdiyiniz zaman Outline serverləri ilə əlaqələndirmək üçün billinq hesabı təqdim etməyiniz tələb olunacaq. Bəzən billinq hesabında problem olduğu üçün server işləmir. Bu halda [Google Cloud Console-a](https://console.cloud.google.com/getting-started) daxil olmalı, Outline ("Outline serverləri" adlanır) ilə əlaqələndirilmiş Google Cloud layihəsini tapmalı və billinq ayarlarını yeniləməlisiniz.

## Serverlərin deaktiv edilməsi

Avtomatlaşdırılmış quraşdırma ilə yaradılan serverlərinizi deaktiv etmək istəyirsinizsə, Outline Manager-dən bunu asanlıqla icra edə bilərsiniz. Lakin serverləri özünüz deaktiv etmək istəyirsinizsə,[Google Cloud Console-a](https://console.cloud.google.com/getting-started) daxil ola, ilkin quraşdırma ("Outline serverləri" adlanır) zamanı yaradılmış layihəni tapa və oradakı resursları silə, yaxud layihəni bağlaya bilərsiniz.

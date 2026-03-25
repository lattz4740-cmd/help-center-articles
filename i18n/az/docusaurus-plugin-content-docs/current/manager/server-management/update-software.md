---
title: "Outline server proqram təminatını necə güncəlləyə bilərəm?"
sidebar_label: "Outline server proqram təminatını necə güncəlləyə bilərəm?"
---

Hər zaman ən yeni Outline texnologiyasından istifadə etməyiniz üçün Outline serverləri avtomatik olaraq ən son təhlükəsizlik təkmilləşdirmələri ilə güncəllənir. Avtomatlaşdırılmış güncəlləmə prosesi Outline proqram təminatının olduğu Docker təsvirini müntəzəm olaraq yoxlayan və yeniləyən [Watchtower](https://github.com/containrrr/watchtower) adlı açıq mənbəli kitabxanadan istifadə etməklə aktivləşdirilir.

Əlavə olaraq, Outline Manager-dən istifadə edərək Outline-ı quraşdırdığınız zaman [Avtomatik Təkmilləşdirmələr](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) ilə proqram təminatını avtomatik təkmilləşdirmək və lazım olduqda yenidən başlatmaq üçün cron tapşırığını quraşdıracağıq. Host cihazının Outline-ı işə salmaq ilə birgə başqa məqsədlər üçün istifadə edildiyini fərz etsək, bu proses mövcud konfiqurasiyanı qorumaq üçün Qabaqcıl Rejimdə baş vermir.

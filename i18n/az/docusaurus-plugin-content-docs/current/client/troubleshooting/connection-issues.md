---
title: "Nəyə görə Outline xidmətinə qoşula bilmirəm?"
sidebar_label: "Nəyə görə Outline xidmətinə qoşula bilmirəm?"
---

Outline xidmətinə qoşula bilməməyinizin bir neçə səbəbi ola bilər:

- **Cihazınızın**/client/troubleshooting/connection-issues#One[**internet bağlantısı kəsilib**](#Internetissues)[#Internetissues](#Internetissues)**.**Bəzən cihazın şəbəkə bağlantısında fasilə yarana bilər və şəbəkə ikonlarının yenilənməsi bir qədər vaxt apara bilər. Ola bilər ki, cihaz yerli şəbəkəyə qoşulub, lakin internet işləmir.
- **Sizin**/client/troubleshooting/connection-issues#Two[**şəbəkənizin qoruyucu divarı girişi bloklayır**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[#FirewallIssues](#FirewallIssues)və Outline serverinə daxil ola bilmirsiniz.**Məktəb, iş kimi ümumi şəbəkə və ya ödənişsiz simsiz şəbəkədən istifadə edirsinizsə, bu geniş yayılmış haldır.
- **Cihazınızda**/client/troubleshooting/connection-issues#Three[**qoruyucu və ya antivirus proqram təminatı**](#SoftwareIssues)[#SoftwareIssues](#SoftwareIssues)**var və onlar Outline serverinizə girişi bloklayır.**
- **Sizin**[**telefon cihazı ayarlarınız**](#DeviceSettings)**dəyişdirilməli ola bilər.**
- **Xidmət meneceriniz**[**serverinizi yox etmiş və ya ISP sorğunuzu bloklamış ola bilər**](#ServerIssues) .

## İnternet bağlantısında problemlər: {#Internetissues}

## Test etmək qaydası:

Outline-nı deaktiv edin və internet bağlantısının bərpa olunub-olunmadığını yoxlayın.

- Elədirsə, aşağıda problemin həll edilməsi üçün daha çox varianta baxın.
- Elə deyilsə, bağlantı ayarlarının öz-özünə yenilənib-yenilənmədiyinə baxmaq üçün bir neçə dəqiqə gözləyin.

## Edilməli olan düzəlişlər:

Cihazda yenidən onlayn rejimə keçin:

1. Başqa cihazın eyni şəbəkəyə qoşula bilib-bilmədiyini yoxlayın. Başqa cihazlar da onlayn rejimə keçmirsə, deməli, şəbəkə işləmir. Onun bərpa olunmasını gözləməli, yaxud problemi həll etməlisiniz.
2. Başqa cihazlar eyni şəbəkəyə qoşulursa, yenidən onlayn rejimə keçmək üçün aşağıdakı üsullardan birini və bir neçəsini sınaya bilərsiniz:
   1. Cihazı təyyarə rejiminə keçirin (mobil)
   2. Cihazı yenidən başladın
   3. Cihazı söndürüb 2 dəqiqə gözləyin və yenidən aktiv edin

## Qoruyucu divarı olan şəbəkə ilə bağlı problemlər: {#FirewallIssues}

## Test etmək qaydası:

1. Hazırda istifadə etdiyiniz Wi-Fi və simli şəbəkə ilə bağlantını kəsin.
2. Başqa şəbəkəyə (məs., mobil) qoşulun
3. Outline serverinə yenidən qoşulmağı sınayın

Başqa şəbəkədə olarkən qoşula bilirsinizsə, o zaman bu sizinlə bağlı problemdir.

## Edilməli olan düzəlişlər:

Xidmət administratoru ilə əlaqə saxlayaraq Outline serverinizə giriş icazəsi verməsi üçün sorğu göndərin və ya əvəzində digər şəbəkədən istifadə etməyə davam edin.

**Qoruyucu divar və ya antivirus proqram təminatı ilə bağlı problemlər:**

**Test etmək qaydası:**

 Başqa cihazdan Outline serverinə qoşulmağı sınayın.

Qeyd: Başqa cihazda Outline istifadə etmək üçün giriş açarı və Outline tətbiqiniz olmalıdır.

## Edilməli olan düzəlişlər: {#SoftwareIssues}
Qoruyucu divar və antivirus proqram təminatının ayarlarını yoxlayıb VPN və Outline trafiki icazəsinin aktiv olduğuna əmin olun.

## Cihaz ayarları: {#DeviceSettings}

## Yoxlanılası məqamlar: {#DeviceSettings}
Android üçün:

1. Ayarlar tətbiqini açın.
2. Cihazınızda **VPN ayarlarını** axtarın. (VPN ayarlarında telefonunuza hazırda giriş imkanı olan VPN tətbiqləri göstəriləcək.)
3. VPN ayarlarında Outline-ı görmədiyiniz təqdirdə Outline-ı sistemdən silib yenidən quraşdırın. Quraşdırıldıqdan sonra Outline-a cihaz tərəfindən avtomatik giriş icazəsi veriləcək.

Android cihazınızda quraşdırılmış ekran örtüyü tətbiqi olmadığına əmin olun, bu örtük Outline icazələri pəncərəsini arxa fona göndərdiyinə görə pəncərə ön fonda görünməyə bilər.

 Android cihazınızda Ayarlar > Təbiqlər > Xüsusi tətbiqə giriş icazəsi bölməsinə daxil olun. "Digər tətbiqlərin üzərində göstərin" düyməsinə toxunaraq bu əməliyyatı icra edən bütün tətbiqlərə giriş icazəsini silə bilərsiniz.

 iOS üçün: [bu dəstək məqaləsini](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web) oxuyun.

## Serverlə bağlı problemlər: {#ServerIssues}

## Test etmək qaydası: {#ServerIssues}
Bir serverdən daha çoxuna giriş imkanınız varsa, başqa serverə qoşulun.

## Edilməli olan düzəlişlər:

Serverin silinib-silinmədiyini yoxlamaq üçün xidmət meneceriniz ilə əlaqə saxlayın. Elədirsə, ondan başqa serverə[giriş açarı](/about/terminology) tələb edin.

Serveri siz quraşdırmısınızsa, Outline Manager vasitəsilə və ya [SSH](https://en.wikipedia.org/wiki/Secure_Shell) kimi fərqli metodla qoşulmağa çalışın. Bu alınmasa, serverin hələ onlayn olub-olmadığına baxmaq üçün bulud provayderi konsulunu yoxlaya bilərsiniz.

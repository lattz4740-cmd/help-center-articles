---
title: Outline ishlatishda xavfsizlik va maxfiylik
sidebar_label: Outline ishlatishda xavfsizlik va maxfiylik
---

Outline ishlatishda xavfsizlik va maxfiylik

## Outline onlayn maʼlumotlaringizni qanday himoya qiladi

Internet trafigi mahalliy yoki milliy tarmogʻingiz orqali oʻtayotganda kuzatuvga eng zaif hisoblanadi.

Outline milliy tarmogʻingizdan oʻtishda internet trafigingizni shifrlash orqali maʼlumotlaringizni maxfiy saqlashga yordam beradi va Outline serverigacha shifrlangan holda yetkazadi. Trafik Outline bilan shifrlansa, uchunchi shaxslar kezgan veb-saytlaringizni yoki uzatayotgan axborotingizni tekshira olmaydi.

Outline mamlakatingizda boshqa shaklda mavjud boʻlmagan xavfsiz maʼlumotlar uzatish vositalaridan foydalanishni tiklashga ham yordam beradi.

## Shifrlash standartlari

Outline qurilmangiz tomonidan Outline serveriga uzatiladigan maʼlumotlarni AEAD 256-bit Chacha2020 IETF Poly 1305 shifridan foydalanib shifrlaydi. AEAD shifrlari maxfiylik, yaxlitlik va haqiqiylikni taʼminlaydi hamda zamonaviy qurilmada ajoyib ishlashni namoyish etadi.

## Xavfsizlik tekshiruvlari

2018-yilda Outline xizmati dasturlarni eng yangi xavfsizlik standartlariga muvofiqligini tekshiradigan ikkita mustaqil tashkilot – Radically Open Security va Cure53 tomonidan tekshirilgan. Radically Open Security 2022-yilda qoʻshimcha tekshiruv oʻtkazdi va Cure53 2024-yilda Outline SDK tekshiruvini oʻtkazdi. Hisobotlarni bu yerda oʻqishingiz mumkin:

- [Singish testiga doir Radically Open Security hisoboti (2018-yil mart)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [Jigsaw Outline xizmatini singish testi va tekshiruviga oid Cure53 hisoboti (December 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [Singish testiga doir Radically Open Security hisoboti (2022-yil, dekabr)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [Jigsaw Outline VPN SDK xizmatini singish testiga oid Cure53 hisoboti (2024-yil, yanvar)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Anonim koʻrsatkichlar va jurnallar

Outline har bir kirish kaliti uchun “uzatilgan baytlar” sifatida foydalanilgan o‘tkazuvchanlik qobiliyatini kuzatadi. Bu axborot server administratorlariga zarur hollarda oʻzlarini bulutli server provayderlaridagi oʻtkazuvchanlik qobiliyati obunalarini oʻzgartirish imkonini beradi, lekin Outline serveri orqali oʻtgan mavjud axborotni koʻrish imkonini bermaydi.

[Outline xizmatining maʼlumotlar va axborotni jamlash](/about/data-collection) haqida batafsil.

---

## Xavfsizlik va maxfiylikka doir savol-javob

## Outline onlayn anonim boʻlishimni taʼminlay oladimi?

Yoʻq, Outline anonimlashtirish vositasi emas. Outline maxfiyligingizni tarmoqdagi ehtimoliy uchinchi shaxslardan himoyalaydi.

Outline kirgan veb-saytlaringizda anonimlikni taʼminlamaydi, chunki hisob bilan kirish yoki brauzer raqamli barmoq izi kabi kuzatish texnologiyalari yordamida sizni aniqlash mumkin. Mobil ilovalarda esa proksi-server ishlatsangiz ham, aksariyat zamonaviy smartfonlar joylangan GPS orqali joylashuvingizni kuzatish imkonini beruvchi APIʼlarga ega oʻrnatilgan ilovalar mavjud.

Umuman olganda, VPN Internetdagi maxfiy kuzatuvlardan asosiy himoyani taʼminlaydi, ammo onlayn ishlashda doim xavflar mavjud. Hatto VPN ishlatsangiz ham, agar provayderga shaxsiy axborotingiz maʼlum boʻlsa va tarmoq trafigingizni kuzata olsa, u Outline serveringiz IP manzilini ham aniqlashi mumkin. Bu axborot Outline serveriga kirishni bloklash yoki odatda onlayn boʻlish vaqtingiz va taxminiy joylashuvingiz kabi foydalanish shakllarini oʻrganish uchun ishlatilishi mumkin.

## Kimdir Outline xizmatidan foydalanayotganimni bilishi mumkinmi?

Bilishi mumkin. Kirgan platformalar va xizmatlaringiz bulutli server orqali ulanganingizni aniqlashi mumkin. Ayrim hollarda VPN ishlatayotganingizni aniqlashi mumkin, lekin internet trafigingiz kontentini koʻra olishmaydi.

## Outline meni barcha ehtimoliy kiber tahdidlardan himoya qiladimi?

Yoʻq. Hech qanday vosita sizni barcha ehtimoliy kiber tahdidlardan himoya qilmaydi. Outline sizga ochiq internetga kirish imkonini beradi va trafikni shifrlash orqali maxfiyligingizni oshiradi, lekin zararli dastur va fishing kabi boshqa turdagi hujumlardan himoyalanish uchun qoʻshimcha ehtiyot choralarini koʻrishni tavsiya qilamiz.

Onlayn himoyangizni kuchaytirish uchun tashkilotingizning kiberxavfsizlik boʻyicha mutaxassisiga murojaat qiling. Sizga mos kiberxavfsizlik vositalarini tanlashda aniq koʻrsatmalarni taqdim etish uchun moʻljallangan [Security Planner](https://securityplanner.org/) veb-saytida yetakchi xavfsizlik mutaxassislaridan individual maslahat olishingiz mumkin.

[Intra](https://getintra.org/), [Project Shield](https://g.co/shield) va [Password Alert](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?) kabi boshqa [Jigsaw](https://jigsaw.google.com/) kiberxavfsizlik mahsulotlari bilan tanishishingiz mumkin.

## VPN ishlatish qonunan mumkinmi?

Outline yoki ilovadan foydalanishdan oldin mahalliy qonunchiligingiz va ulanishni rejalashtirgan bulut provayderingizni xizmat shartlariga muvofiqlini tekshiring.

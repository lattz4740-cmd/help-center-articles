---
title: "Outline sunucumun yazılımını nasıl güncelleyebilirim?"
sidebar_label: "Outline sunucumun yazılımını nasıl güncelleyebilirim?"
---

Daima en yeni Outline teknolojilerini kullanabilmeniz için Outline sunucuları en son güvenlik iyileştirmeleri ile otomatik olarak güncellenir. Otomatik güncelleme işlemi [Watchtower](https://github.com/v2tec/watchtower) tarafından yapılır. Watchtower, Outline yazılımını içeren docker görüntüsünü düzenli olarak kontrol eden ve güncelleyen açık kaynaklı bir kitaplıktır.

Ayrıca, Outline'ı yüklemek için Outline Manager'ı kullanırsanız [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) aracılığıyla sunucudaki yazılımı otomatik olarak yükseltmek ve gerektiğinde yeniden başlatmak amacıyla bir cron işi oluştururuz. Ana bilgisayarın Outline'ı çalıştırmak dışında başka amaçlarla da kullanıldığı varsayıldığından, mevcut yapılandırmayı korumak amacıyla bu işlem Gelişmiş Mod'da yapılmaz.

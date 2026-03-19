---
title: "Outline Client Tətbiqinin Linux-da Quraşdırılması"
sidebar_label: "Outline Client Tətbiqinin Linux-da Quraşdırılması"
---

Outline Client 1.15 versiyasından başlayaraq növbəti bütün versiyalar Linux əməliyyat sistemləri üçün Debian paketləri kimi buraxılacaq. Hansı əməliyyat sistemlərini dəstəklədiyimiz haqqında ətraflı məlumat üçün [minimum sistem tələblərimizi](/client/getting-started/system-requirements) nəzərdən keçirin.

## Debian əsaslı Linux paylanmaları üçün Outline Client quraşdırın (tövsiyə olunur)

Aşağıdakı əmrləri icra edin:

1. Outline-ın depo açarını quraşdırın və depo əlavə edin.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Apt paket siyahısını yeniləyin və ən son Outline Client versiyasını quraşdırın.

```
sudo apt update
sudo apt install outline-client
```

Növbəti yeniləmələri yoxlamaq və ya quraşdırmaq üçün 2-ci addımdakı əmrləri yenidən icra edin. Nəzərə alın ki, 1.15 versiyasından başlayaraq Linux-da Outline Client üçün tətbiqdaxili avtomatik yeniləmə deaktiv edilib.

Outline Client proqramını silmək üçün aşağıdakı əmri icra edin:

```
sudo apt purge outline-client
```

## Alternativ Seçim

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) ünvanından ən son Outline Client Debian paketini endirin
2. Paketi quraşdırmaq üçün əmr sətrində aşağıdakı əmrləri icra edin

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. 1.15 versiyasından başlayaraq Linux-da Outline Client üçün tətbiqdaxili avtomatik yeniləmə deaktiv edildiyi üçün yeniləmələri manual olaraq yoxlamalısınız.

4. Outline Client proqramını silmək üçün əmr sətrində aşağıdakı əmri icra edin:

```
sudo apt purge outline-client
```

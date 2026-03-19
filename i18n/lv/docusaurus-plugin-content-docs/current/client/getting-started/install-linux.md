---
title: Outline klienta instalēšana Linux ierīcēs
sidebar_label: Outline klienta instalēšana Linux ierīcēs
---

ຕັ້ງແຕ່ລູກຂ່າຍ Outline ເວີຊັນ 1.15 ເປັນຕົ້ນໄປ, ເວີຊັນທັງໝົດໃນອະນາຄົດຈະເປີດຕົວເປັນແພັກເກດ Debian ສຳລັບລະບົບປະຕິບັດການ Linux. ກະລຸນາອ່ານ [ຂໍ້ກຳນົດຂັ້ນຕ່ຳຂອງລະບົບ](/client/getting-started/system-requirements) ສຳລັບຂໍ້ມູນເພີ່ມເຕີມກ່ຽວກັບລະບົບປະຕິບັດການທີ່ພວກເຮົາຮອງຮັບ.

## ຕິດຕັ້ງລູກຂ່າຍ Outline ສຳລັບລະບົບປະຕິບັດການທີ່ພັດທະນາຈາກ Debian (ແນະນຳ)

ເອີ້ນໃຊ້ຄຳສັ່ງຕໍ່ໄປນີ້:

1. ຕິດຕັ້ງກະແຈບ່ອນເກັບຂໍ້ມູນຂອງ Outline ແລະ ເພີ່ມບ່ອນເກັບຂໍ້ມູນ.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. ອັບເດດລາຍຊື່ແພັກເກດ apt ແລະ ຕິດຕັ້ງລູກຂ່າຍ Outline ເວີຊັນຫຼ້າສຸດ.

```
sudo apt update
sudo apt install outline-client
```

ເພື່ອກວດສອບ ຫຼື ຕິດຕັ້ງການອັບເດດໃນອະນາຄົດ, ໃຫ້ເອີ້ນໃຊ້ຄຳສັ່ງໃນຂັ້ນຕອນທີ 2 ອີກຄັ້ງ. ກະລຸນາຮັບຊາບວ່າລະບົບປິດການນຳໃຊ້ການອັບເດດອັດຕະໂນມັດໃນແອັບສຳລັບລູກຂ່າຍ Outline ຢູ່ Linux, ຕັ້ງແຕ່ເວີຊັນ 1.15 ເປັນຕົ້ນໄປ.

ເພື່ອຖອນການຕິດຕັ້ງລູກຂ່າຍ Outline, ໃຫ້ເອີ້ນໃຊ້ຄຳສັ່ງຕໍ່ໄປນີ້:

```
sudo apt purge outline-client
```

```
sudo apt purge outline-client
```

## ຕົວເລືອກສຳຮອງ

1. ດາວໂຫຼດແພັກເກດ Debian ຂອງລູກຂ່າຍ Outline ເວີຊັນຫຼ້າສຸດຈາກ [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. ເອີ້ນໃຊ້ຄຳສັ່ງຕໍ່ໄປນີ້ໃນແຖວຄຳສັ່ງເພື່ອຕິດຕັ້ງແພັກເກດ

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. ກະລຸນາກວດສອບການອັບເດດດ້ວຍຕົນເອງ, ເນື່ອງຈາກລະບົບປິດການນຳໃຊ້ການອັບເດດອັດຕະໂນມັດໃນແອັບສຳລັບລູກຂ່າຍ Outline ຢູ່ Linux, ຕັ້ງແຕ່ເວີຊັນ 1.15 ເປັນຕົ້ນໄປ.

4. ເພື່ອຖອນການຕິດຕັ້ງລູກຂ່າຍ Outline, ໃຫ້ເອີ້ນໃຊ້ຄຳສັ່ງຕໍ່ໄປນີ້ໃນແຖວຄຳສັ່ງ:

```
sudo apt purge outline-client
```

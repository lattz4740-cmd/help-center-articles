---
title: "Linux дээр Outline Client-г суулгах"
sidebar_label: "Linux дээр Outline Client-г суулгах"
---

Outline Client 1.15 хувилбараас эхлэн ирээдүйн бүх хувилбар нь Linux үйлдлийн системд зориулсан Debian багц хэлбэрээр гарах болно. Бидний дэмждэг үйлдлийн системүүдийн талаарх дэлгэрэнгүй мэдээлэл авах бол [системийн хамгийн бага шаардлагыг](/client/getting-started/system-requirements) шалгана уу.

## Debian-д суурилсан Linux түгээлтийн Outline Client-г суулгана уу (Санал болгосон)

Дараах тушаалуудыг ажиллуулна уу:

1. Outline-н хадгалах газрын түлхүүрийг суулгаж, хадгалах газрыг нэмнэ үү.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Apt багцын жагсаалтыг шинэчилж, Outline Client-н хамгийн сүүлийн хувилбарыг суулгана уу.

```
sudo apt update
sudo apt install outline-client
```

Ирээдүйд шинэчлэлтүүдийг шалгах эсвэл суулгахын тулд 2-р алхмын тушаалуудыг дахин ажиллуулна уу. 1.15 хувилбараас эхлэн Linux дээрх Outline Client-д аппын автомат шинэчлэлтийг идэвхгүй болгосон гэдгийг анхаарна уу.

Outline Client-г устгахын тулд дараах тушаалуудыг ажиллуулна уу:

```
sudo apt purge outline-client
```

## Өөр сонголт

1. Хамгийн сүүлийн үеийн Outline Client Debian багцыг [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)хаягаас татаж авна уу
2. Багцыг суулгахын тулд тушаалын мөрд дараах тушаалуудыг ажиллуулна уу

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Linux дээрх Outline Client-д 1.15 хувилбараас эхлэн аппын автомат шинэчлэлтийг идэвхгүй болгосон тул шинэчлэлтүүдийг гар аргаар шалгана уу.

4. Outline Client-г устгахын тулд тушаалын мөрд дараах тушаалыг ажиллуулна уу:

```
sudo apt purge outline-client
```

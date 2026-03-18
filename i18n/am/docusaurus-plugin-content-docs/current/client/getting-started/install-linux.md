---
title: Linux ላይ የOutline ደንበኛ መጫን
sidebar_label: Linux ላይ የOutline ደንበኛ መጫን
---

ከOutline ደንበኛ ሥሪት 1.15 ጀምሮ ሁሉም የወደፊት ሥሪቶች ለLinux ሥርዓተ ክወናዎች እንደ Debian ጥቅሎች ይለቀቃሉ። የትኛዎቹን ሥርዓተ ክወናዎች እንደምንደግፍ ለበለጠ መረጃ የእኛን [ዝቅተኛውን የሥርዓት መስፈርቶች](/client/getting-started/system-requirements) ይገምግሙ።

## በDebian-ላይ ለተመሰረቱ የLinux ሥርጭቶች የOutline ደንበኛ ይጫኑ (የሚመከር)

የሚከተሉትን ትዕዛዞች ያሂዱ፦

1. የOutlineውሂብ ማከማቻ ቁልፍ ይጫኑ እና ውሂብ ማከማቻውን ያክሉ።
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. የኤፒቲ የጥቅል ዝርዝርን ያዘምኑ እና የቅርብ ጊዜውን የOutline ደንበኛ ሥሪት ይጫኑ።
   ```
   sudo apt update
   sudo apt install outline-client
   ```

የወደፊት ዝመናዎችን ለመፈተሽ ወይም ለመጫን ትዕዛዞቹን በእርምጃ 2 እንደገና ያሂዱ። ከሥሪት 1.15 ጀምሮ የውስጠ-መተግበሪያ ራስ-ሰር ዝማኔ በLinux ላይ ለOutline ደንበኛ እንደተሰናከለ ልብ ይበሉ።

የOutline ደንበኛን ለማራገፍ፣ የሚከተለውን ትዕዛዝ ያሂዱ፦

```
sudo apt purge outline-client
```

## የተለየ አማራጭ

1. የቅርብ ጊዜውን የOutline ደንበኛ Debian ጥቅል [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) ላይ ያውርዱ
2. ጥቅሉን ለመጫን በትዕዛዝ መስመር ውስጥ የሚከተሉትን ትዕዛዞችን ያሂዱ፦
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. ከሥሪት 1.15 ጀምሮ የውስጠ-መተግበሪያ ራስ-ሰር ዝማኔ በLinux ላይ ለOutline ደንበኛ ስለተሰናከለ ዝማኔዎችን በእጅ ይፈትሹ።
4. የOutline ደንበኛን ለማራገፍ፣ የሚከተለውን ትዕዛዝ በትዕዛዙ መስመር ውስጥ ያሂዱ፦
   ```
   sudo apt purge outline-client
   ```

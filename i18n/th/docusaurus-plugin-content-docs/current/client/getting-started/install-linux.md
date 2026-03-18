---
title: การติดตั้งไคลเอ็นต์ Outline ใน Linux
sidebar_label: การติดตั้งไคลเอ็นต์ Outline ใน Linux
---

ตั้งแต่ไคลเอ็นต์ Outline เวอร์ชัน 1.15 เป็นต้นไป เวอร์ชันทั้งหมดในอนาคตจะเปิดตัวเป็นแพ็กเกจ Debian สำหรับระบบปฏิบัติการ Linux โปรดอ่าน[ข้อกำหนดขั้นต่ำของระบบ](/client/getting-started/system-requirements)เพื่อดูข้อมูลเพิ่มเติมเกี่ยวกับระบบปฏิบัติการที่เรารองรับ

## ติดตั้งไคลเอ็นต์ Outline สำหรับระบบปฏิบัติการ Linux ที่พัฒนาจาก Debian (แนะนำ)

เรียกใช้คำสั่งต่อไปนี้

1. ติดตั้งคีย์ที่เก็บของ Outline และเพิ่มที่เก็บ
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. อัปเดตรายการแพ็กเกจ apt และติดตั้งไคลเอ็นต์ Outline เวอร์ชันล่าสุด
   ```
   sudo apt update
   sudo apt install outline-client
   ```

หากต้องการตรวจสอบหรือติดตั้งการอัปเดตในอนาคต ให้เรียกใช้คำสั่งในขั้นตอนที่ 2 อีกครั้ง โปรดทราบว่าการอัปเดตอัตโนมัติในแอปจะปิดอยู่สำหรับไคลเอ็นต์ Outline ใน Linux ตั้งแต่เวอร์ชัน 1.15 เป็นต้นไป

หากต้องการถอนการติดตั้งไคลเอ็นต์ Outline ให้เรียกใช้คำสั่งต่อไปนี้

```
sudo apt purge outline-client
```

## ตัวเลือกอื่น

1. ดาวน์โหลดแพ็กเกจ Debian ของไคลเอ็นต์ Outline เวอร์ชันล่าสุดจาก [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. เรียกใช้คำสั่งต่อไปนี้ในบรรทัดคำสั่งเพื่อติดตั้งแพ็กเกจ
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. โปรดตรวจสอบการอัปเดตด้วยตนเอง เนื่องจากระบบปิดใช้การอัปเดตอัตโนมัติในแอปสำหรับไคลเอ็นต์ Outline ใน Linux ตั้งแต่เวอร์ชัน 1.15
4. หากต้องการถอนการติดตั้งไคลเอ็นต์ Outline ให้เรียกใช้คำสั่งต่อไปนี้ในบรรทัดคำสั่ง
   ```
   sudo apt purge outline-client
   ```

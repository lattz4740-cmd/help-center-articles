---
title: "איך מתקינים את אפליקציית הלקוח של Outline ב-Linux"
sidebar_label: "איך מתקינים את אפליקציית הלקוח של Outline ב-Linux"
---

החל מגרסה 1.15 של אפליקציית הלקוח של Outline, כל הגרסאות העתידיות יפורסמו כחבילות Debian להפצות השונות של מערכת ההפעלה Linux. ב[מאמר בנושא דרישות מערכת מינימליות](/client/getting-started/system-requirements) אתם יכולים לקרוא באילו מערכות הפעלה אנחנו תומכים.

## איך מתקינים את אפליקציית הלקוח של Outline בהפצות Linux שמבוססות על Debian (מומלץ)

מריצים את הפקודות הבאות:

1. כדי להתקין את מפתח המאגר של Outline ולהוסיף את המאגר:
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. כדי לעדכן את רשימת החבילות של מנהל החבילות (APT) ולהתקין את הגרסה העדכנית של אפליקציית הלקוח של Outline:
   ```
   sudo apt update
   sudo apt install outline-client
   ```

כדי לבדוק בהמשך אם יש עדכונים ולהתקין אותם, מריצים שוב את הפקודות שמופיעות בשלב 2. חשוב לדעת שהחל מגרסה 1.15, העדכון האוטומטי המובנה מושבת באפליקציית הלקוח של Outline ל-Linux.

כדי להסיר את אפליקציית הלקוח של Outline, מריצים את הפקודה הבאה:

```
sudo apt purge outline-client
```

## אפשרות חלופית

1. מורידים את חבילת Debian העדכנית של אפליקציית הלקוח של Outline מהכתובת הזו: [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. כדי להתקין את החבילה, מריצים את הפקודות הבאות בשורת הפקודה:
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. אפשר לבדוק אם יש עדכונים רק באופן ידני, כי העדכון האוטומטי המובנה מושבת החל מגרסה 1.15 של אפליקציית הלקוח של Outline ל-Linux.
4. כדי להסיר את אפליקציית הלקוח של Outline, מריצים את הפקודה הבאה בשורת הפקודה:
   ```
   sudo apt purge outline-client
   ```

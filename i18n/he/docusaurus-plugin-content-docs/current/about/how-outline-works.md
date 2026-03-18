---
title: איך שירות Outline פועל
sidebar_label: איך שירות Outline פועל
---

**התקנה של השרת**

 ​התקנת Outline היא תהליך פשוט מבחינת המשתמשים, אבל ברקע מתבצעות כמה וכמה פעולות מורכבות להתקנת השרת. כשמתקינים את Outline, סקריפט ההתקנה מבצע את הפעולות הבאות:

- הגרסה היציבה של קובץ האימג' של Shadowbox מאוחזרת ומיובאת באמצעות Docker. קובץ האימג' מתארח ב-[Quay.io](https://quay.io/) בכתובת [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). קובץ האימג' מכיל את שרת Outline ואת ה-Management API, שמשמש מאוחר יותר את אפליקציית ניהול השרת של Outline ליצירה ולהסרה של מפתחות גישה, להצטרפות או לביטול ההצטרפות לדיווח על מדדים אנונימיים וכו'.
- ‫[Watchtower](https://github.com/v2tec/watchtower) מותקנת ומוגדרת. התוכנה הזאת בודקת כל שעה אם יש עדכון לקובץ האימג', כדי שהשרת של Outline תמיד יהיה עדכני ויכלול את התכונות החדשות ושיפורי האבטחה.
- שרת אינטרנט, שמאפשר גישה לממשק ה-Management API, מופעל ביציאה אקראית ובנתיב אקראי וסודי.
- נוצר [אישור SSL בחתימה עצמית](https://en.wikipedia.org/wiki/Self-signed_certificate) כדי שיהיה אפשר להצפין את ניהול השרת של Outline באמצעות TLS למרות שאין לו שם דומיין. בנוסף, טביעת אצבע של האישור הזה נוצרת ואז מאוחסנת באפליקציית Outline Manager, כדי לעזור במניעת התקפות MITM ("אדם בתווך").

לא צריך להגדיר את Outline לאחר ההתקנה.

**אבטחת השרת**

 אפליקציית Outline כתובה בקוד פתוח. כלומר, כל אחד יכול לקרוא את הקוד ולשפר אותו אם מתגלות נקודות חולשה. הקוד שלנו מתארח ב-[GitHub](https://github.com/search?q=org%3AJigsaw-Code+outline&unscoped_q=outline).

 בנוסף, כל השרתים המותקנים של Outline מתעדכנים אוטומטית כשמשוחררת גרסת תוכנה חדשה, כדי שלא יהיה אף שרת עם גרסה ישנה.

 כדי לנהל את מפתחות הגישה בשרת, אפליקציית Outline Manager מתקשרת עם שירות הניהול בשרת של Outline. שירות הניהול פועל ביציאה אקראית ובנתיב אקראי וסודי. בנוסף, שירות הניהול מוגן מפני גישושים (probe), כי הוא לא עונה לשאילתות בלי שמציינים את הנתיב הסודי הנכון. לסיום, כל התקשורת עם שירות הניהול מוצפנת באמצעות [אישור SSL בחתימה עצמית](https://en.wikipedia.org/wiki/Self-signed_certificate).

 מעבר לכל זה, השרת של Outline לא מאחסן יומנים, כך שגם אם הוא נפרץ, נתוני המשתמש לא נחשפים. אפשר לקרוא מידע נוסף [כאן](/about/security-and-privacy). ‫Outline נבדקה על ידי [Radically Open Security](https://radicallyopensecurity.com/) ו-[Cure53](https://cure53.de/) ב-2018. [כאן](/about/security-and-privacy) אפשר לקרוא את הדוחות.

**טיפול בתנועת UDP**

 אפליקציית Outline מסוגלת לפעול כ-VPN כלל-מערכתי. כלומר, כל תנועת ה-UDP מועברת דרך השרת של Outline.

**תנועת DNS**

אפליקציית Outline מבצעת את כל חיפושי ה-DNS דרך השרת של Outline ומגנה עליהם באמצעות אותה הצפנה שמשמשת לשאר הפעילות ברשת. שאילתות DNS עוברות דרך השרת של Outline ל-Dyn Internet Guide,‏ OpenDNS,‏ Cloudflare DNS או Quad9 DNS. ‫Outline אף פעם לא שומרת חיפושי DNS.

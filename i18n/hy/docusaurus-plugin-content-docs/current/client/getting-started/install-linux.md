---
title: "Outline-ի սպասառուի տեղադրումը Linux-ում"
sidebar_label: "Outline-ի սպասառուի տեղադրումը Linux-ում"
---

Outline Client-ի 1.15 տարբերակից սկսած՝ բոլոր հաջորդող տարբերակները կթողարկվեն որպես Linux օպերացիոն համակարգի համար Debian փաթեթներ: Ծանոթացեք մեր՝ [համակարգի հանդեպ ներկայացվող նվազագույն պահանջներին](/client/getting-started/system-requirements) և իմացեք, թե որ օպերացիոն համակարգերն ենք մենք աջակցում:

## Տեղադրեք Outline Client-ը Debian-ի հիման վրա գործող Linux դիստրիբուցիաների համար (նախընտրելի)

Կիրառել հետևյալ հրահանգները.

1. Տեղադրեք Outline-ի պահոցային բանալին և ավելացրեք պահոցը:
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Թարմացրեք apt փաթեթի ցուցակը և տեղադրեք Outline-ի սպասառուի նոր տարբերակը։
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Առաջիկա թարմացումների առկայությունը ստուգելու կամ նոր տարբերակը տեղադրելու համար կրկին գործարկեք քայլ 2-ում ներկայացված հրամանները։ Նկատի ունեցեք, որ հավելվածի մեջ ավտոմատ թարմացումն անջատված է Linux-ի վրա գործող Outline-ի սպասառուի համար՝ սկսած տարբերակ 1.15-ից:

Outline-ի սպասառուն ապատեղադրելու համար գործարկեք հետևյալ հրամանը.

```
sudo apt purge outline-client
```

## Այլընտրանքային տարբերակ

1. Ներբեռնեք նոր Outline Client Debian փաթեթը [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Փաթեթը տեղադրելու համար հրամանատողում գործարկեք հետևյալ հրամանները․
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Թարմացումների առկայությունը ստուգեք ձեռքով, քանի որ թարմացումն անջատված է Linux-ի վրա գործող Outline-ի սպասառուի համար՝ սկսած տարբերակ 1.15-ից։
4. Outline-ի սպասառուն ապատեղադրելու համար հրամանատողում գործարկեք հետևյալ հրամանը.
   ```
   sudo apt purge outline-client
   ```

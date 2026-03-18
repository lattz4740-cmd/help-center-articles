---
title: Outline ကလိုင်းယင့်ကို Linux တွင် ထည့်သွင်းခြင်း
sidebar_label: Outline ကလိုင်းယင့်ကို Linux တွင် ထည့်သွင်းခြင်း
---

‘Outline ကလိုင်းယင့်’ ဗားရှင်း 1.15 မှစတင်၍ လာမည့်ဗားရှင်းအားလုံးကို Linux လည်ပတ်သည့်စနစ်များအတွက် Debian ပက်ကေ့ဂျ်များအဖြစ် ဖြန့်ချိပါမည်။ ကျွန်ုပ်တို့ ပံ့ပိုးသည့် လည်ပတ်သည့်စနစ်များရှိ နောက်ထပ်အချက်အလက်များအတွက် [အနည်းဆုံးစနစ်လိုအပ်ချက်များ](/client/getting-started/system-requirements) ကို စစ်ပါ။

## Debian အခြေပြု Linux ဖြန့်ဝေမှုများအတွက် ‘Outline ကလိုင်းယင့်’ ကို ထည့်သွင်းပါ (အကြံပြုထားသည်)

အောက်ပါကွန်မန်းများကို လုပ်ဆောင်ပါ-

1. Outline ၏ သိမ်းဆည်းရန်နေရာကီးကို ထည့်သွင်းပြီး သိမ်းဆည်းရန်နေရာ ထည့်ပါ။
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Apt ပက်ကေ့ဂျ်စာရင်းကို အပ်ဒိတ်လုပ်ပြီး ‘Outline ကလိုင်းယင့်’ နောက်ဆုံးဗားရှင်း ထည့်သွင်းပါ။
   ```
   sudo apt update
   sudo apt install outline-client
   ```

လာမည့်အပ်ဒိတ်များကို ကြည့်ရန် (သို့) ထည့်သွင်းရန်အတွက် ‘အဆင့် ၂’ ရှိ ကွန်မန်းများကို ထပ်မံလုပ်ဆောင်ပါ။ ဗားရှင်း 1.15 မှစတင်ပြီး Linux တွင် ‘Outline ကလိုင်းယင့်’ အတွက် အက်ပ်အတွင်း အလိုအလျောက်အပ်ဒိတ်လုပ်ခြင်းကို ပိတ်ထားကြောင်း သတိပြုပါ။

‘Outline ကလိုင်းယင့်’ ပရိုဂရမ်ကို ဖြုတ်ရန် အောက်ပါကွန်မန်းကို လုပ်ဆောင်ပါ-

```
sudo apt purge outline-client
```

## အခြားရွေးစရာ

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) မှ နောက်ဆုံး ‘Outline ကလိုင်းယင့်’ Debian ပက်ကေ့ဂျ်ကို ဒေါင်းလုဒ်လုပ်ပါ
2. ပက်ကေ့ဂျ် ထည့်သွင်းရန်အတွက် ကွန်မန်းအတန်းရှိ အောက်ပါကွန်မန်းများကို လုပ်ဆောင်ပါ
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. ဗားရှင်း 1.15 မှစတင်၍ Linux တွင် ‘Outline ကလိုင်းယင့်’ အတွက် အက်ပ်အတွင်း အလိုအလျောက်အပ်ဒိတ်လုပ်ခြင်းကို ပိတ်ထားသဖြင့် အပ်ဒိတ်များကို ကိုယ်တိုင် စစ်ဆေးပါ။
4. ‘Outline ကလိုင်းယင့်’ ပရိုဂရမ်ကို ဖြုတ်ရန် ကွန်မန်းအတန်းရှိ အောက်ပါကွန်မန်းကို လုပ်ဆောင်ပါ-
   ```
   sudo apt purge outline-client
   ```

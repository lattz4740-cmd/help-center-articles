---
title: "Outline-ის კლიენტის ინსტალაცია Linux-ზე"
sidebar_label: "Outline-ის კლიენტის ინსტალაცია Linux-ზე"
---

Outline-ის კლიენტის ვერსია 1.15-დან მოყოლებული, ყველა მომავალი ვერსია გამოეშვება Debian პაკეტების სახით Linux ოპერაციული სისტემებისთვის. გადახედეთ ჩვენს [სისტემის მინიმალურ მოთხოვნებს](/client/getting-started/system-requirements) იმის შესახებ დამატებითი ინფორმაციის მისაღებად, რომელ ოპერაციულ სისტემებს ვუჭერთ მხარს.

## დააყენეთ Outline-ის კლიენტი Debian-ის ბაზაზე შექმნილი Linux დისტრიბუციებისთვის (რეკომენდებულია)

გაუშვით შემდეგი ბრძანებები:

1. დააინსტალირეთ Outline-ის საცავის გასაღები და დაამატეთ საცავი.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. განაახლეთ apt პაკეტის სია და დააინსტალირეთ Outline Client-ის უახლესი ვერსია.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

მომავალი განახლებების შესამოწმებლად და დასაინსტალირებლად ხელახლა გაუშვით მე-2 ნაბიჯში მოცემული ბრძანებები. გაითვალისწინეთ, რომ აპსშიდა განახლება გათიშულია Outline-ის კლიენტისთვის Linux-ზე, ვერსია 1.15-დან მოყოლებული.

Outline-ის კლიენტის დეინსტალაციისთვის გაუშვით შემდეგი ბრძანება:

```
sudo apt purge outline-client
```

## ალტერნატიული ვარიანტი

1. ჩამოტვირთეთ Outline-ის კლიენტის უახლესი Debian პაკეტი [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)-დან
2. პაკეტის დასაინსტალირებლად ბრძანების ზოლში გაუშვით შემდეგი ბრძანებები:
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. ხელით შეამოწმეთ განახლებები, რადგან ვერსია 1.15-დან მოყოლებული აპსშიდა ავტომატური განახლება გათიშულია Outline-ის კლიენტისთვის Linux-ზე.
4. Outline-ის კლიენტის დეინსტალაციისთვის ბრძანების ზოლში გაუშვით შემდეგი ბრძანება:
   ```
   sudo apt purge outline-client
   ```

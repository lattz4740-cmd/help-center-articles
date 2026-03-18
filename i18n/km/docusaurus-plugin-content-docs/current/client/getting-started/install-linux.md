---
title: ការដំឡើង​កម្មវិធីភ្ញៀវ​សម្រាប់ Outline នៅលើ Linux
sidebar_label: ការដំឡើង​កម្មវិធីភ្ញៀវ​សម្រាប់ Outline នៅលើ Linux
---

ចាប់ពី​កម្មវិធីភ្ញៀវ​សម្រាប់ Outline កំណែ 1.15 ឡើងទៅ កំណែ​ទាំងអស់​នាពេលខាងមុខ​នឹងត្រូវបាន​ចេញផ្សាយជា​កញ្ចប់ Debian សម្រាប់​ប្រព័ន្ធ​ប្រតិបត្តិការ Linux។ សូម​ពិនិត្យមើល[លក្ខខណ្ឌតម្រូវ​ប្រព័ន្ធ​អប្បបរមា](/client/getting-started/system-requirements) ដើម្បីដឹង​ព័ត៌មាន​បន្ថែម​អំពី​ប្រព័ន្ធ​ប្រតិបត្តិការ​ដែលយើង​អាចប្រើបាន។

## ដំឡើង​កម្មវិធី​ភ្ញៀវសម្រាប់ Outline ចំពោះ​កំណែចែកចាយ Linux ដែល​ផ្អែកលើ Debian (បានណែនាំ)

ដំណើរការ​ឃ្លាបញ្ជា​ខាងក្រោម៖

1. ដំឡើង​កូដឃ្លាំង​របស់ Outline និង​បញ្ចូល​ឃ្លាំងនោះ។
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. ធ្វើបច្ចុប្បន្នភាព​បញ្ជី​កញ្ចប់ apt រួចដំឡើង​កំណែ​កម្មវិធី​ភ្ញៀវសម្រាប់ Outline ចុងក្រោយបំផុត។
   ```
   sudo apt update
   sudo apt install outline-client
   ```

ដើម្បី​ពិនិត្យ​រកមើល ឬ​ដំឡើង​កំណែថ្មីៗ​នាពេលខាងមុខ សូម​ដំណើរការ​ឃ្លាបញ្ជា​នៅក្នុង​ជំហានទី 2 ម្ដងទៀត។ សូម​ចំណាំថា ការដំឡើងកំណែ​ដោយស្វ័យប្រវត្តិ​នៅក្នុង​កម្មវិធី​ត្រូវបានបិទ​សម្រាប់​កម្មវិធីភ្ញៀវ​សម្រាប់ Outline នៅលើ Linux ចាប់ពី​កំណែ 1.15 ឡើងទៅ។

ដើម្បីលុប​កម្មវិធី​ភ្ញៀវសម្រាប់ Outline សូម​ដំណើរការ​ឃ្លាបញ្ជា​ខាងក្រោម៖

```
sudo apt purge outline-client
```

## ជម្រើស​ជំនួស

1. ទាញយក​កញ្ចប់ Debian នៃ​កម្មវិធីភ្ញៀវ​សម្រាប់ Outline ចុងក្រោយ​បំផុតពី [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. ដំណើរការ​ឃ្លាបញ្ជា​ខាងក្រោម​នៅក្នុង​ជួរឃ្លាបញ្ជា ដើម្បី​ដំឡើង​កញ្ចប់នោះ
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. ពិនិត្យ​រកមើល​កំណែថ្មីៗ​ដោយផ្ទាល់ដៃ ដោយសារ​ការដំឡើងកំណែ​ដោយស្វ័យប្រវត្តិ​នៅក្នុង​កម្មវិធី​ត្រូវបានបិទ​សម្រាប់​កម្មវិធីភ្ញៀវ​សម្រាប់ Outline នៅលើ Linux ចាប់ពី​កំណែ 1.15 ឡើងទៅ។
4. ដើម្បីលុប​កម្មវិធី​ភ្ញៀវសម្រាប់ Outline សូម​ដំណើរការ​ឃ្លាបញ្ជាខាងក្រោម​នៅក្នុង​ជួរឃ្លាបញ្ជា៖
   ```
   sudo apt purge outline-client
   ```

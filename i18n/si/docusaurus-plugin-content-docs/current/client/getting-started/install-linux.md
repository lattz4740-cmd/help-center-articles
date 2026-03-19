---
title: Linux මත Outline සේවාලාභීයා ස්ථාපනය කිරීම
sidebar_label: Linux මත Outline සේවාලාභීයා ස්ථාපනය කිරීම
---

දළ සටහන් සේවාලාභීයා අනුවාදය 1.15 සමඟින් ආරම්භ වන අතර, අනාගත අනුවාදයන් සියල්ලම Linux මෙහෙයුම් පද්ධති සඳහා Debian පැකේජ ලෙස නිකුත් කෙරේ. අපි සහාය දක්වන මෙහෙයුම් පද්ධති පිළිබඳ වැඩිදුර තොරතුරු සඳහා අපගේ [අවම පද්ධති අවශ්‍යතා](/client/getting-started/system-requirements) සමාලෝචනය කරන්න.

## Debian-පාදක Linux බෙදාහැරීම් සඳහා දළ සටහන් සේවාලාභීයා ස්ථාපනය කරන්න (නිර්දේශිතයි)

පහත විධානයන් ක්‍රියාත්මක කරන්න:

1. Outline හි ගබඩා යතුර ස්ථාපනය කර ගබඩාව එක් කරන්න.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. apt පැකේජ ලැයිස්තුව යාවත්කාලීන කර දළ සටහන් සේවාලාභීයාහි නවතම අනුවාදය ස්ථාපනය කරන්න.

```
sudo apt update
sudo apt install outline-client
```

අනාගත යාවත්කාලීන කිරීම් පරීක්ෂා කිරීමට හෝ ස්ථාපනය කිරීමට, පියවර 2 හි විධාන නැවත ක්‍රියාත්මක කරන්න. 1.15 අනුවාදයෙන් ආරම්භ වන Linux හි දළ සටහන් සේවාලාභීයා සඳහා යෙදුම තුළ ස්වයංක්‍රීය යාවත්කාලීන කිරීම අබල කර ඇති බව සලකන්න.

දළ සටහන් සේවාලාභීයා අස්ථාපනය කිරීමට, පහත විධානය ක්‍රියාත්මක කරන්න:

```
sudo apt purge outline-client
```

## විකල්ප විකල්පය

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) මඟින් නවතම දළ සටහන් සේවාලාභීයා Debian පැකේජය බාගන්න
2. පැකේජය ස්ථාපනය කිරීම සඳහා විධාන රේඛාවේ පහත විධානයන් ධාවනය කරන්න.

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. 1.15 අනුවාදයෙන් ආරම්භ වන Linux හි දළ සටහන් සේවාලාභීයා සඳහා යෙදුම තුළ ස්වයංක්‍රීය යාවත්කාලීන කිරීම අක්‍රිය කර ඇති බැවින්, යාවත්කාලීන කිරීම් සඳහා අතින් පරීක්ෂා කරන්න.

4. දළ සටහන් සේවාලාභීයා අස්ථාපනය කිරීමට, විධාන රේඛාවේ පහත විධානය ක්‍රියාත්මක කරන්න:

```
sudo apt purge outline-client
```

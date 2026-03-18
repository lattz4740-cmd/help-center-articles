---
title: Linuxରେ Outline Client ଇନଷ୍ଟଲ କରିବା
sidebar_label: Linuxରେ Outline Client ଇନଷ୍ଟଲ କରିବା
---

Outline Client ଭର୍ସନ 1.15ରୁ ଆରମ୍ଭ କରି ଭବିଷ୍ୟତର ସମସ୍ତ ଭର୍ସନ Linux ଅପରେଟିଂ ସିଷ୍ଟମ ପାଇଁ Debian ପେକେଜ ଭାବେ ରିଲିଜ କରାଯିବ। ଆମେ ସପୋର୍ଟ କରୁଥିବା ଅପରେଟିଂ ସିଷ୍ଟମ ବିଷୟରେ ଅଧିକ ସୂଚନା ପାଇଁ ଆମ [ସର୍ବନିମ୍ନ ସିଷ୍ଟମ ଆବଶ୍ୟକତାଗୁଡ଼ିକ](/client/getting-started/system-requirements)ର ସମୀକ୍ଷା କରନ୍ତୁ।

## Debian-ଆଧାରିତ Linux ଡିଷ୍ଟ୍ରିବ୍ୟୁସନ ପାଇଁ Outline Client ଇନଷ୍ଟଲ କରନ୍ତୁ (ସୁପାରିଶ କରାଯାଇଛି)

ନିମ୍ନୋକ୍ତ କମାଣ୍ଡଗୁଡ଼ିକୁ ଚଲାନ୍ତୁ:

1. Outlineର ରିପୋଜିଟୋରୀ କୀ ଇନଷ୍ଟଲ କରି ରିପୋଜିଟୋରୀ ଯୋଗ କରନ୍ତୁ।
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. ଏପିଟି ପେକେଜ ତାଲିକା ଅପଡେଟ କରି Outline Clientର ନବୀନତମ ଭର୍ସନ ଇନଷ୍ଟଲ କରନ୍ତୁ।

```
sudo apt update
sudo apt install outline-client
```

ଭବିଷ୍ୟତର ଅପଡେଟଗୁଡ଼ିକୁ ଯାଞ୍ଚ କରିବା କିମ୍ବା ଇନଷ୍ଟଲ କରିବାକୁ, ଷ୍ଟେପ 2ରେ କମାଣ୍ଡଗୁଡ଼ିକୁ ପୁଣି ଚଲାନ୍ତୁ। ଧ୍ୟାନ ଦିଅନ୍ତୁ ଯେ ଭର୍ସନ 1.15ରୁ ଆରମ୍ଭ ହେଉଥିବା Linuxରେ Outline Client ପାଇଁ ଇନ-ଆପ ସ୍ୱତଃ-ଅପଡେଟକୁ ଅକ୍ଷମ କରାଯାଇଛି।

Outline Clientକୁ ଅନଇନଷ୍ଟଲ କରିବା ପାଇଁ ନିମ୍ନୋକ୍ତ କମାଣ୍ଡଗୁଡ଼ିକୁ ଚଲାନ୍ତୁ:

```
sudo apt purge outline-client
```

## ଅନ୍ୟ ବିକଳ୍ପ

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)ରୁ ନବୀନତମ Outline Client Debian ପେକେଜ ଡାଉନଲୋଡ କରନ୍ତୁ
2. ପେକେଜ ଇନଷ୍ଟଲ କରିବାକୁ କମାଣ୍ଡ ଲାଇନରେ ନିମ୍ନୋକ୍ତ କମାଣ୍ଡଗୁଡ଼ିକୁ ଚଲାନ୍ତୁ

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. ଭର୍ସନ 1.15ରୁ ଆରମ୍ଭ ହେଉଥିବା Linuxରେ Outline Client ପାଇଁ ଇନ-ଆପ ସ୍ୱତଃ-ଅପଡେଟକୁ ଅକ୍ଷମ କରାଯାଇଥିବା ଭାବେ ମାନୁଆଲୀ ଅପଡେଟ ଯାଞ୍ଚ କରନ୍ତୁ।

4. Outline Clientକୁ ଅନଇନଷ୍ଟଲ କରିବା ପାଇଁ କମାଣ୍ଡ ଲାଇନରେ ଥିବା ନିମ୍ନୋକ୍ତ କମାଣ୍ଡଗୁଡ଼ିକୁ ଚଲାନ୍ତୁ:

```
sudo apt purge outline-client
```

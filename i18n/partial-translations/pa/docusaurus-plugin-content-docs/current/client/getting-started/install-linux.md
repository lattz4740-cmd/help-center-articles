---
title: "Linux 'ਤੇ ਆਊਟਲਾਈਨ ਕਲਾਇੰਟ ਨੂੰ ਸਥਾਪਤ ਕਰਨਾ"
sidebar_label: "Linux 'ਤੇ ਆਊਟਲਾਈਨ ਕਲਾਇੰਟ ਨੂੰ ਸਥਾਪਤ ਕਰਨਾ"
---

ਆਊਟਲਾਈਨ ਕਲਾਇੰਟ ਵਰਜਨ 1.15 ਨਾਲ ਸ਼ੁਰੂ ਕਰਦੇ ਹੋਏ, ਸਾਰੇ ਭਵਿੱਖੀ ਵਰਜਨਾਂ ਨੂੰ Linux ਓਪਰੇਟਿੰਗ ਸਿਸਟਮਾਂ ਲਈ ਡੇਬੀਅਨ ਪੈਕੇਜਾਂ ਵਜੋਂ ਰਿਲੀਜ਼ ਕੀਤਾ ਜਾਵੇਗਾ। ਅਸੀਂ ਕਿਹੜੇ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮਾਂ ਦਾ ਸਮਰਥਨ ਕਰਦੇ ਹਾਂ, ਇਸ ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ ਸਾਡੀਆਂ [ਘੱਟੋ-ਘੱਟ ਸਿਸਟਮ ਸੰਬੰਧੀ ਲੋੜਾਂ](/client/getting-started/system-requirements) ਦੀ ਸਮੀਖਿਆ ਕਰੋ।

## ਡੇਬੀਅਨ-ਆਧਾਰਿਤ Linux ਡਿਸਟ੍ਰਿਬਿਊਸ਼ਨ (ਸਿਫ਼ਾਰਸ਼ੀ) ਲਈ ਆਊਟਲਾਈਨ ਕਲਾਇੰਟ ਨੂੰ ਸਥਾਪਤ ਕਰਨਾ

ਅੱਗੇ ਦਿੱਤੇ ਆਦੇਸ਼ਾਂ ਨੂੰ ਚਲਾਓ:

1. ਆਊਟਲਾਈਨ ਦੀ ਡਾਟਾ-ਭੰਡਾਰ ਕੁੰਜੀ ਨੂੰ ਸਥਾਪਤ ਕਰੋ ਅਤੇ ਡਾਟਾ-ਭੰਡਾਰ ਸ਼ਾਮਲ ਕਰੋ।
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. apt ਪੈਕੇਜ ਸੂਚੀ ਅੱਪਡੇਟ ਕਰੋ ਅਤੇ ਆਊਟਲਾਈਨ ਕਲਾਇੰਟ ਦੇ ਨਵੀਨਤਮ ਵਰਜਨ ਨੂੰ ਸਥਾਪਤ ਕਰੋ।

```
sudo apt update
sudo apt install outline-client
```

ਭਵਿੱਖੀ ਅੱਪਡੇਟਾਂ ਨੂੰ ਦੇਖਣ ਜਾਂ ਸਥਾਪਤ ਕਰਨ ਲਈ, ਪੜਾਅ 2 ਵਿੱਚ ਦਿੱਤੇ ਆਦੇਸ਼ਾਂ ਨੂੰ ਦੁਬਾਰਾ ਚਲਾਓ। ਨੋਟ ਕਰੋ ਕਿ ਵਰਜਨ 1.15 ਤੋਂ, Linux 'ਤੇ ਆਊਟਲਾਈਨ ਕਲਾਇੰਟ ਲਈ ਐਪ-ਅੰਦਰ ਸਵੈਚਲਿਤ-ਅੱਪਡੇਟ ਨੂੰ ਬੰਦ ਕੀਤਾ ਗਿਆ ਹੈ।

ਆਊਟਲਾਈਨ ਕਲਾਇੰਟ ਨੂੰ ਅਣਸਥਾਪਤ ਕਰਨ ਲਈ, ਅੱਗੇ ਦਿੱਤੇ ਆਦੇਸ਼ ਨੂੰ ਚਲਾਓ:

```
sudo apt purge outline-client
```

## ਵਿਕਲਪਿਕ ਵਿਕਲਪ

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) ਤੋਂ ਨਵੀਨਤਮ ਆਊਟਲਾਈਨ ਕਲਾਇੰਟ ਦੇ ਡੇਬੀਅਨ ਪੈਕੇਜ ਨੂੰ ਡਾਊਨਲੋਡ ਕਰੋ
2. ਪੈਕੇਜ ਨੂੰ ਸਥਾਪਤ ਕਰਨ ਲਈ, ਆਦੇਸ਼ ਲਾਈਨ ਵਿੱਚ ਅੱਗੇ ਦਿੱਤੇ ਆਦੇਸ਼ਾਂ ਨੂੰ ਚਲਾਓ

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. ਅੱਪਡੇਟਾਂ ਦੀ ਹੱਥੀਂ ਜਾਂਚ ਕਰੋ ਕਿਉਂਕਿ ਵਰਜਨ 1.15 ਤੋਂ, Linux 'ਤੇ ਆਊਟਲਾਈਨ ਕਲਾਇੰਟ ਲਈ ਐਪ-ਅੰਦਰ ਸਵੈਚਲਿਤ-ਅੱਪਡੇਟ ਨੂੰ ਬੰਦ ਕੀਤਾ ਗਿਆ ਹੈ।

4. ਆਊਟਲਾਈਨ ਕਲਾਇੰਟ ਨੂੰ ਅਣਸਥਾਪਤ ਕਰਨ ਲਈ, ਆਦੇਸ਼ ਲਾਈਨ ਵਿੱਚ ਅੱਗੇ ਦਿੱਤੇ ਆਦੇਸ਼ ਨੂੰ ਚਲਾਓ:

```
sudo apt purge outline-client
```

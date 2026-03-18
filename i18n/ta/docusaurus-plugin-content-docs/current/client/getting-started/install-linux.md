---
title: Linuxஸில் Outline Clientடை நிறுவுதல்
sidebar_label: Linuxஸில் Outline Clientடை நிறுவுதல்
---

Outline கிளையண்ட் பதிப்பு 1.15 முதல், Linux ஆப்ரேட்டிங் சிஸ்டங்களுக்கான பதிப்புகள் எல்லாம் இனி Debian தொகுப்புகளாக வெளியிடப்படும். நாங்கள் ஆதரிக்கும் ஆப்ரேட்டிங் சிஸ்டங்கள் தொடர்பான கூடுதல் தகவல்களுக்கு எங்கள் [குறைந்தபட்ச சிஸ்டம் தேவைகளைப்](/client/getting-started/system-requirements) பாருங்கள்.

## Debian அடிப்படையிலான Linux டிஸ்ட்ரிபியூஷன்களுக்கான Outline கிளையண்ட்டை நிறுவுதல் (பரிந்துரைக்கப்படுகிறது)

இந்தக் கட்டளைகளை இயக்கவும்:

1. Outlineனின் தரவு சேமிப்பகக் கீயை நிறுவி தரவு சேமிப்பகத்தைச் சேர்க்கவும்.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. apt தொகுப்புப் பட்டியலைப் புதுப்பித்து Outline கிளையண்ட்டின் சமீபத்திய பதிப்பை நிறுவவும்.

```
sudo apt update
sudo apt install outline-client
```

இனிவரும் புதுப்பிப்புகளைப் பார்க்கவோ நிறுவவோ படி 2ல் உள்ள கட்டளைகளை மீண்டும் இயக்கவும். 1.15 பதிப்பு முதல், Linuxஸில் Outline கிளையண்ட்டிற்கு ஆப்ஸ் தானியங்குப் புதுப்பிப்பு முடக்கப்பட்டிருக்கும் என்பதை நினைவில்கொள்ளவும்.

Outline கிளையண்ட்டை நிறுவல் நீக்க, இந்தக் கட்டளையை இயக்கவும்:

```
sudo apt purge outline-client
```

## மாற்று வழி

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) தளத்தில் இருந்து சமீபத்திய Outline கிளையண்ட் Debian தொகுப்பைப் பதிவிறக்கவும்
2. தொகுப்பை நிறுவ, கட்டளை வரியில் இந்தக் கட்டளைகளை இயக்கவும்

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. 1.15 பதிப்பு முதல், Linuxஸில் Outline கிளையண்ட்டிற்கு ஆப்ஸ் தானியங்குப் புதுப்பிப்பு முடக்கப்பட்டிருக்கும் என்பதால் நீங்களாகவே புதுப்பிப்பு இருக்கிறதா என்று பார்க்கவும்.

4. Outline கிளையண்ட்டை நிறுவல் நீக்க, கட்டளை வரியில் இந்தக் கட்டளையை இயக்கவும்:

```
sudo apt purge outline-client
```

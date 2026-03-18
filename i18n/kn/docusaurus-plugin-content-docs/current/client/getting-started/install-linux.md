---
title: Linux ನಲ್ಲಿ ಔಟ್‌ಲೈನ್ ಕ್ಲೈಂಟ್ ಅನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಲಾಗುತ್ತಿದೆ
sidebar_label: Linux ನಲ್ಲಿ ಔಟ್‌ಲೈನ್ ಕ್ಲೈಂಟ್ ಅನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಲಾಗುತ್ತಿದೆ
---

ಔಟ್‌ಲೈನ್ ಕ್ಲೈಂಟ್ ಆವೃತ್ತಿ 1.15 ರಿಂದ ಪ್ರಾರಂಭಿಸಿ, ಎಲ್ಲಾ ಭವಿಷ್ಯದ ಆವೃತ್ತಿಗಳನ್ನು Linux ಆಪರೇಟಿಂಗ್ ಸಿಸ್ಟಮ್‌ಗಳಿಗಾಗಿ Debian ಪ್ಯಾಕೇಜ್‌ಗಳಾಗಿ ಬಿಡುಗಡೆ ಮಾಡಲಾಗುತ್ತದೆ. ನಾವು ಯಾವ ಆಪರೇಟಿಂಗ್ ಸಿಸ್ಟಮ್‌ಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತೇವೆ ಎಂಬುದರ ಕುರಿತು ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗಾಗಿ ನಮ್ಮ ಕನಿಷ್ಠ [ಸಿಸ್ಟಂ ಅಗತ್ಯತೆಗಳನ್ನು](/client/getting-started/system-requirements) ಪರಿಶೀಲಿಸಿ.

## Debian ಆಧಾರಿತ Linux ವಿತರಣೆಗಳಿಗಾಗಿ ಔಟ್‌ಲೈನ್ ಕ್ಲೈಂಟ್ ಅನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ (ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ)

ಈ ಕೆಳಗಿನ ಕಮಾಂಡ್‌‌ಗಳನ್ನು ರನ್ ಮಾಡಿ:

1. ಔಟ್‌ಲೈನ್‌ನ ರೆಪೊಸಿಟರಿ ಕೀಯನ್ನು ಇನ್‌ಸ್ಟಾಮ್ ಮಾಡಿ ಮತ್ತು ರೆಪೊಸಿಟರಿಯನ್ನು ಸೇರಿಸಿ.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. ಎಪಿಟಿ ಪ್ಯಾಕೇಜ್ ಪಟ್ಟಿಯನ್ನು ಅಪ್‌ಡೇಟ್‌ ಮಾಡಿ ಮತ್ತು ಔಟ್‌ಲೈನ್ ಕ್ಲೈಂಟ್‌ನ ಇತ್ತೀಚಿನ ಆವೃತ್ತಿಯನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ.

```
sudo apt update
sudo apt install outline-client
```

ಭವಿಷ್ಯದ ಅಪ್‌ಡೇಟ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಲು ಅಥವಾ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಲು, ಹಂತ 2 ರಲ್ಲಿನ ಕಮಾಂಡ್‌ಗಳನ್ನು ಮತ್ತೊಮ್ಮೆ ರನ್ ಮಾಡಿ. ಆವೃತ್ತಿ 1.15 ರಿಂದ ಪ್ರಾರಂಭವಾಗುವ Linux ನಲ್ಲಿ ಔಟ್‌ಲೈನ್ ಕ್ಲೈಂಟ್‌ಗಾಗಿ ಆ್ಯಪ್‌ನಲ್ಲಿ ಆಟೋ-ಅಪ್‌ಡೇಟ್ ಅನ್ನು ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಲಾಗಿದೆಯೆ ಎಂಬುದನ್ನು ಗಮನಿಸಿ.

ಔಟ್‌ಲೈನ್ ಕ್ಲೈಂಟ್ ಅನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಲು, ಈ ಕೆಳಗಿನ ಕಮಾಂಡ್ ಅನ್ನು ರನ್ ಮಾಡಿ:

```
sudo apt purge outline-client
```

## ಆಲ್ಟರ್ನೇಟಿವ್ ಆಯ್ಕೆ

1. ಇತ್ತೀಚಿನ ಔಟ್‌ಲೈನ್ ಕ್ಲೈಂಟ್ ಡೆಬಿಯನ್ ಪ್ಯಾಕೇಜ್ ಅನ್ನು [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb) ನಿಂದ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ
2. ಪ್ಯಾಕೇಜ್ ಅನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಲು ಕಮಾಂಡ್ ಸಾಲಿನಲ್ಲಿ ಈ ಕೆಳಗಿನ ಕಮಾಂಡ್‌ಗಳನ್ನು ರನ್ ಮಾಡಿ

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. ಆವೃತ್ತಿ 1.15 ರಿಂದ ಪ್ರಾರಂಭವಾಗುವ Linux ನಲ್ಲಿ ಔಟ್‌ಲೈನ್ ಕ್ಲೈಂಟ್‌ಗಾಗಿ ಆ್ಯಪ್‌ನಲ್ಲಿ ಆಟೋ ಅಪ್‌ಡೇಟ್ ಅನ್ನು ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಲಾಗಿರುವುದರಿಂದ, ಅಪ್‌ಡೇಟ್‌‌ಗಳಿಗಾಗಿ ಮ್ಯಾನುಯಲ್ ಆಗಿ ಪರಿಶೀಲಿಸಿ.

4. ಔಟ್‌ಲೈನ್ ಕ್ಲೈಂಟ್ ಅನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಲು, ಕಮಾಂಡ್ ಲೈನ್‌‌ನಲ್ಲಿ ಈ ಕೆಳಗಿನ ಕಮಾಂಡ್ ಅನ್ನು ರನ್ ಮಾಡಿ:

```
sudo apt purge outline-client
```

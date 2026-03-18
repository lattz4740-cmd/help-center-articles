---
title: Linux에서 Outline 클라이언트 설치하기
sidebar_label: Linux에서 Outline 클라이언트 설치하기
---

Outline 클라이언트 버전 1.15부터 향후 모든 버전이 Linux 운영체제용 Debian 패키지로 출시됩니다. 지원되는 운영체제에 관한 자세한 내용은 [최소 시스템 요구사항](/client/getting-started/system-requirements)을 참고하세요.

## Debian 기반 Linux 배포판용 Outline 클라이언트 설치하기(권장)

다음 명령어를 실행합니다.

1. Outline의 저장소 키를 설치하고 저장소를 추가합니다.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. apt 패키지 목록을 업데이트하고 최신 버전의 Outline 클라이언트를 설치합니다.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

향후 업데이트를 확인하거나 설치하려면 2단계의 명령어를 다시 실행합니다. 버전 1.15부터 Linux의 Outline 클라이언트에서는 인앱 자동 업데이트가 사용 중지된다는 점을 참고하세요.

Outline 클라이언트를 제거하려면 다음 명령어를 실행합니다.

```
sudo apt purge outline-client
```

## 대체 옵션

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)에서 최신 Outline 클라이언트 Debian 패키지를 다운로드합니다.
2. 명령줄에서 다음 명령어를 실행하여 패키지를 설치합니다.
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. 버전 1.15부터 Linux의 Outline 클라이언트에서 인앱 자동 업데이트가 사용 중지되므로 업데이트를 수동으로 확인합니다.
4. Outline 클라이언트를 제거하려면 명령줄에서 다음 명령어를 실행합니다.
   ```
   sudo apt purge outline-client
   ```

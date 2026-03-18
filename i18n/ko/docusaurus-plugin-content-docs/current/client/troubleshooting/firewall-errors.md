---
title: 방화벽 오류
sidebar_label: 방화벽 오류
---

방화벽 문제에는 다음과 같은 세 가지 유형이 있을 수 있습니다.

## 네트워크 방화벽에 의해 차단되는 경우

학교나 직장과 같이 방화벽이 있는 네트워크에 연결된 상태에서 Outline을 설치하려는 경우 다른 네트워크에서 설치를 진행해 보세요.

 이 방법으로 문제가 해결되지 않으면 네트워크 관리자에게 방화벽이 있는 네트워크에서 Outline 서버에 연결할 수 있는지 문의하세요. Outline 서버의 IP 주소와 Outline이 실행되는 포트(설치 스크립트 마지막 부분에 표시됨)를 알아야 합니다.

## 기기 방화벽에 의해 차단되는 경우

기기에 비표준 포트 또는 인식할 수 없는 소프트웨어의 발신 연결을 차단하는 소프트웨어(예: CheckPoint의 ZoneAlarm)가 있는 경우 기기 또는 소프트웨어 문서에서 Outline에 적용할 예외를 만드는 방법이 있는지 확인하세요.

## 서버 방화벽에 의해 차단되는 경우

사용 중인 클라우드 공급업체에서 Outline이 실행되는 포트를 열기 위해 사용자에게 서버 방화벽 예외를 직접 만들도록 요청할 수 있습니다. 설치 스크립트 실행을 마치면 서버에 Outline이 실행되는 포트 2개가 무작위로 선택되어 표시되어야 합니다. 이 포트 2개를 열면 충분합니다.

 서버 방화벽 예외를 만들 때는 'ufw' 및 'iptables' 도움말을 참고하세요.

- UFW: [https://help.ubuntu.com/community/UFW](/client/troubleshooting/firewall-errors)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](/client/troubleshooting/firewall-errors)

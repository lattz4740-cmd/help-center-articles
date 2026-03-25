---
title: "Outline 서버 소프트웨어를 업데이트하려면 어떻게 해야 하나요?"
sidebar_label: "Outline 서버 소프트웨어를 업데이트하려면 어떻게 해야 하나요?"
---

Outline 서버는 최신 보안 개선사항이 자동 업데이트되므로 항상 최신 Outline 기술을 사용할 수 있습니다. 자동 업데이트 프로세스는 Outline 소프트웨어가 포함된 도커 이미지를 정기적으로 확인하고 업데이트하는 오픈소스 라이브러리인 [Watchtower](https://github.com/containrrr/watchtower)를 통해 진행됩니다.

또한 Outline Manager를 사용하여 Outline을 설치하면 [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades)(Ubuntu)를 사용하여 서버에서 소프트웨어를 자동으로 업그레이드하고 필요할 때 재부팅하도록 크론 작업을 설정합니다. 호스트가 Outline 실행 외에 다른 용도로 사용되고 있다는 가정하에, 고급 모드에서는 기존 구성을 보존하기 위해 이 작업을 수행하지 않습니다.

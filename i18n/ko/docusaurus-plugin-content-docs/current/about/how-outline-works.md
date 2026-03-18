---
title: Outline의 작동 원리
sidebar_label: Outline의 작동 원리
---

### 서버 설치

Outline 설치 과정은 간단해 보일 수 있지만 사실 복잡한 일련의 단계를 거쳐야 서버를 설치할 수 있습니다.

Outline이 설치될 때마다 설치 스크립트는 다음 단계를 실행합니다.

- Docker를 통해 안정적인 버전의 Shadowbox 이미지를 검색해 가져옵니다. 이미지는 [Quay.io](https://support.getoutline.org/s/article/how-outline-works?language=ko)([https://quay.io/repository/outline/shadowbox?tab=tags](https://support.getoutline.org/s/article/how-outline-works?language=ko))에 호스팅되어 있습니다. 이 이미지에는 Outline 서버 및 Management API가 포함되어 있으며, 이 API는 나중에 Outline Server Management 애플리케이션에서 액세스 키를 생성 및 삭제하고, 익명처리된 측정항목 보고서를 선택 또는 선택 해제할 때 사용됩니다.
- 매시간 이미지 업데이트를 확인하도록 [Watchtower](https://support.getoutline.org/s/article/how-outline-works?language=ko)가 설치 및 구성되므로 모든 Outline 서버는 지속적으로 최신 기능 및 보안 개선 사항을 받아 최신 상태를 유지할 수 있습니다.
- Management API에 액세스하는 데 사용되는 웹 서버가 비공개 고유 경로를 통해 랜덤 포트에서 시작됩니다.
- 도메인 이름 없이도 TLS를 사용해 Outline 서버 관리 내역을 암호화할 수 있도록 [자체 서명된 SSL 인증서](https://support.getoutline.org/s/article/how-outline-works?language=ko)가 생성됩니다. 이 인증서에 사용할 고유 디지털 지문이 생성되고 Outline Manager 애플리케이션에 저장되기 때문에 MITM 공격을 방지하는 데 도움이 됩니다.

Outline은 설치가 완료된 후 따로 구성할 필요가 없습니다.

### 서버 보안

Outline 소프트웨어는 오픈소스이므로 누구나 코드를 보고 취약점이 발견되는 경우 이를 개선할 수 있습니다. Outline의 코드는

에 호스팅되어 있습니다.

또한 설치된 모든 Outline 서버는 새 버전이 출시될 때마다 자동으로 업데이트되므로 이전 버전의 소프트웨어를 실행 중인 Outline 서버가 남아 있지 않도록 보장합니다.

Outline Manager 애플리케이션은 서버에서 액세스 키를 관리하기 위해 Outline 서버의 관리 서비스와 상호작용합니다. 관리 서비스는 랜덤 포트와 비공개 고유 경로에서 실행됩니다. 적절한 비공개 경로가 지정되지 않으면 쿼리에 응답하지 않기 때문에 관리 서비스는 자체적으로 탐색에 강합니다. 마지막으로 관리 서비스로의 모든 통신은

로 암호화됩니다.

Outline 서버는 어떤 로그도 저장하지 않으므로 서버가 해킹되는 경우에도 사용자 데이터는 공개되지 않습니다.

에서 자세히 알아보세요.

및

에서는 2018년에 Outline을 대상으로 감사를 실시했습니다.

에서 보고서를 확인하세요.

### UDP 트래픽 처리

Outline은 시스템 차원의 VPN으로 작동할 수 있습니다. 즉, 모든 UDP 트래픽이 Outline 서버를 통해 터널링됩니다.

### DNS 트래픽

Outline은 Outline 서버를 통해 모든 DNS 조회를 처리하고 다른 모든 네트워크 활동에 사용되는 것과 동일한 암호화를 사용하여 보호합니다. DNS 쿼리가 Outline 서버를 통과해 Dyn Internet Guide 또는 OpenDNS로 이동합니다.

Outline은 사용자의 DNS 조회를 절대 기록하지 않습니다.

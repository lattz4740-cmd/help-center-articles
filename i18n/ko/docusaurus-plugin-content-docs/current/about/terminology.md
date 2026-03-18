---
title: 용어
sidebar_label: 용어
---

## VPN이 무엇인가요?

가상 사설망(VPN)은 기기와 호스트 서버 간의 비공개 연결입니다. VPN을 사용하면 트래픽이 인터넷 제공업체로부터 숨겨집니다.

다음 시나리오에서 VPN을 사용할 수 있습니다.

- 공용 Wi-Fi 네트워크 사용 시 데이터 보호
- 인터넷 공급자 및 정부 기관으로부터 인터넷 사용 기록을 비공개로 유지
- 전 세계의 다양한 소스에서 검열되지 않은 콘텐츠에 액세스

## Outline은 기존 VPN과 어떻게 다른가요?

인터넷 서비스 제공업체는 일반적인 보안 프로토콜이나 트래픽 볼륨 패턴을 인식함으로써 기존의 VPN을 쉽게 감지하고 차단할 수 있습니다. Outline은 감지하기 어려워 차단하기도 까다롭게 설계된 프로토콜을 사용해 개발되었으므로 기존 VPN에 비해 탄력성이 더 우수합니다. Outline은 네트워크 기반의 차단 및 IP 차단과 같은 복잡한 형태의 검열도 우회합니다.

## Outline 서버란 무엇인가요?

Outline 서버는 허가된 사용자가 연결할 수 있는 VPN을 실행합니다.

사용자가 새로운 네트워크를 만드는 경우 사용자는 자체 보안 서버를 Outline 서버로 사용할 수 있으며, 다음과 같은 클라우드 서비스 제공업체를 사용할 수도 있습니다.

- DigitalOcean
- Google Cloud Platform(GCP)
- Amazon Web Services(AWS)

Outline Manager에서 서버를 설정할 수 있습니다.

## 서비스 관리자는 누구인가요? {#servicemanager}

서비스 관리자는 Outline 서버를 설정하고 사용자에게 액세스 키를 공유하는 담당자입니다. 서비스 관리자는 일반적으로 서버 사용 비용을 관리하는 일을 맡습니다.

## 액세스 키란 무엇인가요? {#accesskey}

액세스 키는 기존 Outline 서버에 액세스하고 VPN에 연결하는 데 사용됩니다. [서비스 관리자](#servicemanager)가 액세스 키를 제공할 수도 있고 사용자가 직접 [Outline 서버를 설정](/manager/server-setup/setup-server)할 수도 있습니다.

다음은 액세스 키의 예입니다(샘플 전용, 작동하지 않음).

ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## Outline Manager란 무엇인가요?

Outline Manager는 서비스 담당자가 Outline 서버를 설정하고, [액세스 키](#accesskey)를 생성하고, 키 1개당 사용 가능한 데이터 한도를 설정하도록 도와주는 데스크톱 애플리케이션입니다. [여기](https://getoutline.org/get-started/#step-1) 또는 [여기](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/)에서 최신 버전의 Outline Manager를 다운로드할 수 있습니다.

## Outline 클라이언트란 무엇인가요?

Outline 클라이언트는 데스크톱 및 모바일에서 사용할 수 있는 애플리케이션으로, 사용자가 Outline 서버에 연결하고 액세스 키를 사용하여 VPN에 액세스하도록 도와줍니다. [여기](https://getoutline.org/get-started/#step-3) 또는 [여기](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/)에서 최신 버전의 Outline 클라이언트를 다운로드할 수 있습니다.

## 데이터 한도란 무엇인가요?

서비스 담당자는 과잉 사용을 방지하고 비용을 예측 가능한 수준으로 유지하기 위해 Outline Manager를 사용하여 액세스 키에 30일 연속 데이터 한도를 설정할 수 있습니다. 서비스 담당자는 모든 키에 적용되는 기본 한도를 설정할 수 있으며, 특정 키에 기본 한도를 초과하는 별도의 한도를 설정할 수도 있습니다. 한도가 설정되면 효력이 즉시 발생하며 시간별로 시행됩니다.

Jigsaw와 측정항목을 공유하겠다고 선택한 서비스 담당자는 [데이터 수집 정책](/about/data-collection)에서 데이터 한도 사용이 어떻게 보고되는지에 관한 자세한 내용을 확인해야 합니다.

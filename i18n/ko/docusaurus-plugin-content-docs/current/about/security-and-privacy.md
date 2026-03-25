---
title: Outline 사용 시 보안 및 개인 정보 보호
sidebar_label: Outline 사용 시 보안 및 개인 정보 보호
---

Outline 사용 시 보안 및 개인 정보 보호

## Outline에서 온라인 통신을 보호하는 방법

인터넷 트래픽의 감시는 지역 또는 국가 네트워크를 통과할 때 가장 취약해집니다.

Outline은 인터넷 트래픽이 국가 네트워크에서 이동하고 Outline 서버에 도달할 때까지 트래픽을 암호화하여 보안을 유지합니다. Outline을 통해 트래픽이 암호화되면 네트워크 관찰자는 사용자가 방문한 웹사이트 또는 전송하는 정보를 검사할 수 없습니다.

또한 Outline을 사용하면 사용자의 국가에서 액세스할 수 없는 안전한 엔드 투 엔드 통신 도구에 대한 액세스가 가능해질 수도 있습니다.

## 암호화 표준

Outline은 AEAD 256비트 Chacha2020 IETF Poly 1305 암호화를 사용해 기기와 Outline 서버 간의 통신을 암호화합니다. AEAD 암호화는 기밀성, 무결성, 신뢰성을 제공하며, 최신 하드웨어에서 뛰어난 성능을 보여줍니다.

## 보안 감사

소프트웨어가 최신 보안 표준에 맞는지 검토하는 두 곳의 독립 디지털 보안 조직인 Radically Open Security 및 Cure53에서 2018년에 Outline의 감사를 실시했습니다. Radically Open Security에서 2022년에 추가 감사를 실시했으며 Cure53에서 Outline SDK에 대한 감사를 2024년에 실시했습니다. 여기에서 보고서를 확인해 보세요.

- [Radically Open Security의 침투 시험 보고서(2018년 3월)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53의 Jigsaw Outline에 대한 침투 시험 및 감사 보고서(2018년 12월)](https://getoutline.org/reports/cure53-report.pdf)
- [Radically Open Security의 침투 시험 보고서(2022년 12월)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Cure53 침투 시험 보고서 Jigsaw Outline VPN SDK(2024년 1월)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## 익명 처리된 측정항목 및 로그

Outline에서는 각 액세스 키에 '전송된 바이트 수', 즉 사용된 대역폭 추적이 이뤄집니다. 서버 관리자는 이 정보를 사용해 필요에 따라 클라우드 서버 제공업체의 대역폭 사용을 조정할 수 있지만, Outline 서버를 통과한 실제 정보를 볼 수는 없습니다.

Outline의 [데이터 및 정보 수집](https://getoutline.org/policies/data-collection)에 관해 자세히 알아보세요.

---

## 보안 및 개인 정보 보호 FAQ

## Outline을 사용하면 온라인에서 익명으로 활동할 수 있나요?

아니요. Outline은 익명성을 확보하기 위한 도구가 아닙니다. Outline을 사용하면 잠재적인 네트워크 관찰자로부터 사용자의 개인정보를 보호할 수 있습니다.

웹사이트에서는 브라우저 지문 인식과 같은 기술을 통해 또는 로그인할 때 사용자를 식별할 수 있으므로 Outline을 사용해도 방문하는 웹사이트에서 완전한 익명성이 보장되지 않습니다. 대부분의 최신 스마트폰에는 설치된 모바일 앱이 프록시와는 별도로 내장 GPS에 따라 사용자의 위치 정보를 가져올 수 있는 API가 있습니다.

일반적으로 VPN은 인터넷 감시 등에 대한 중요 보호 기능을 제공하지만 온라인 운영에는 항상 위험이 따릅니다. VPN을 사용하더라도 ISP에서 사용자의 신원을 알고 있고 네트워크 트래픽을 관찰할 수 있는 경우 Outline 서버의 IP 주소를 파악할 수 있습니다. 이 정보는 Outline 서버에 대한 액세스를 차단하거나, 사용자가 일반적으로 온라인 상태가 되는 시기와 같은 사용 패턴 및 사용자의 대략적인 위치를 파악하는 데 사용될 수 있습니다.

## 다른 사람이 내가 Outline을 사용 중인지 알 수 있나요?

그럴 수도 있습니다. 사용자가 액세스하는 플랫폼 및 서비스는 사용자의 연결이 클라우드 서버에서 비롯함을 알 수 있을 가능성이 큽니다. 이 플랫폼과 서비스에서 사용자가 VPN을 사용하고 있음을 유추할 수도 있지만 인터넷 트래픽의 내용을 볼 수는 없습니다.

## Outline을 사용하면 모든 사이버 위협으로부터 보호받을 수 있나요?

아니요. 하나의 도구로 모든 사이버 위협을 막을 수는 없습니다. Outline은 개방된 인터넷에 대한 액세스를 제공하면서 트래픽 암호화를 통해 개인 정보 보호 수준을 높입니다. 하지만 멀웨어나 피싱과 같은 다른 유형의 공격에 대비해 추가적인 예방 조치를 취하는 것이 좋습니다.

온라인 방어를 강화하려면 조직의 사이버 보안 전문가와 협력하세요. 또는 [Security Planner](https://securityplanner.org/)에서 업계 최고 보안 전문가로부터 맞춤형 안내를 받을 수 있습니다. 이 웹사이트는 사용자가 우려하는 사안에 맞는 적합한 사이버 보안 도구를 선택할 수 있도록 명확한 안내를 제공합니다.

[Intra](https://getintra.org/), [Project Shield](https://g.co/shield), [비밀번호 경보](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?)와 같은 [Jigsaw](https://jigsaw.google.com/)의 다른 사이버 보안 제품도 확인해 보세요.

## VPN 사용은 합법인가요?

Outline을 운영하거나 Outline 앱을 사용하기 전에 사용하려는 클라우드 제공업체의 서비스 약관과 현지 법규 및 규정을 확인하세요.

---
title: 在使用 Outline 时确保安全和隐私
sidebar_label: 在使用 Outline 时确保安全和隐私
---

在使用 Outline 时确保安全和隐私

## Outline 如何保护您的在线通讯

网络流量在本地或国内网络传输时，最容易受到监视。

Outline 会在网络流量在国内网络传输的途中，对其进行加密，直至它们到达 Outline 服务器，从而保护您的通讯隐私。Outline 对流量加密后，网络监听者就无法检测到您正在访问的网站或者正在传输的信息。

Outline 还可以帮助您访问安全的端到端通讯工具（在您所在的国家/地区可能原本无法访问该工具）。

## 加密标准

Outline 使用 256 位 AEAD Chacha2020 IETF Poly 1305 加密算法来加密您的设备和 Outline 服务器之间的通讯。AEAD 加密算法可确保机密性、完整性和真实性，在现代硬件上展现出了优越的性能。

## 安全审核

2018 年，Outline 通过了 Radically Open Security 和 Cure53 的审核。这是两家独立的数字安全机构，采用最新的安全标准审核软件。2022 年，Radically Open Security 又进行了一次额外的审核，Cure53 在 2024 年对 Outline SDK 进行了审核。您可点击下方链接查看这些报告：

- [Radically Open Security 渗透测试报告（2018 年 3 月）](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [Cure53 渗透测试和审核报告 - Jigsaw Outline（2018 年 12 月）](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [Radically Open Security 渗透测试报告（2022 年 12 月）](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [Cure53 渗透测试报告 Jigsaw Outline VPN SDK（2024 年 1 月）](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## 匿名指标和日志

Outline 会跟踪所占用的带宽，将其记录为针对每个访问密钥“传输的字节数”。此信息可帮助服务器管理员根据需要调整从云服务器提供商处订阅的带宽，但不允许管理员查看经过 Outline 服务器的实际信息。

详细了解 Outline 的[数据和信息收集过程](/about/data-collection)。

---

## 安全和隐私常见问题解答

## Outline 可以让我匿名访问网络吗？

不可以，Outline 不是匿名工具。Outline 会保护您的隐私不受潜在网络监听者的侵害。

Outline 无法确保您在访问网站时完全匿名，因为各网站仍能在您登录时识别您，或是通过浏览器指纹等技术识别您。对于移动应用，现今大多数智能手机都拥有 API，可允许已安装的应用检索您的位置信息。此操作无需依赖代理，因为它们可以使用嵌入的 GPS。

VPN 通常会提供重要的保护措施，尤其是针对互联网监听的措施，但在线操作总是存在风险。即使是 VPN，如果 ISP 已知道您的身份，并且还能检测您的网络流量，那么它或许就能够确定您的 Outline 服务器的 IP 地址。利用这一信息，它可以禁止您访问 Outline 服务器，或了解您的使用行为模式（例如您通常在线的时间），甚至可能掌握您的大致位置信息。

## 如果我正在使用 Outline，其他人是否会知道？

有可能。您访问的平台和服务很可能能分辨出您是通过云服务器进行连接的。有时，它们可以推断出您使用了 VPN，但无法看到网络流量的内容。

## Outline 能否保护我免受所有潜在网络威胁的侵害？

不能。没有任何工具可以确保万无一失。Outline 让您可以访问开放的互联网，并通过加密您的数据流量来进一步保护您的隐私，但我们建议您采取额外的预防措施，以保护自己免受各种类型的攻击，例如恶意软件和网上诱骗。

为增强您的在线防御能力，我们建议您与您单位的网络安全专家协作。您也可以请 [Security Planner](https://securityplanner.org/) 网站上众多出色的安全专家为您提供个性化的安全指南。该网站可根据您的需求，明确指导您选择合适的网络安全工具。

您还可以查看 [Jigsaw](https://jigsaw.google.com/) 的其他网络安全产品，例如 [Intra](https://getintra.org/)、[Project Shield](https://g.co/shield) 和 [Password Alert](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?)。

## 使用 VPN 是否合法？

在使用 Outline 服务或使用 Outline 应用之前，请先了解当地法律法规，以及您将使用的云服务提供商的服务条款。

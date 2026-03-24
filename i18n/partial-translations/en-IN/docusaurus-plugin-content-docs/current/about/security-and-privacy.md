---
title: Security and privacy while using Outline
sidebar_label: Security and privacy while using Outline
---

Security and privacy while using Outline

## How Outline protects your online communications

Internet traffic is most vulnerable to surveillance while it's traveling through your local or national network.

Outline helps keep your communications private by encrypting your internet traffic while it travels inside your national network and keeps it encrypted until it reaches the Outline server. When traffic is encrypted with Outline, network onlookers cannot inspect the websites you visit, or the information you’re transferring.

Outline may also help you recover access to secure end-to-end communications tools that may not be otherwise accessible in your country.

## Encryption standards

Outline encrypts communications between your device and the Outline Server using the AEAD 256-bit Chacha2020 IETF Poly 1305 cipher. AEAD ciphers offer confidentiality, integrity, and authenticity, and exhibits excellent performance on modern hardware.

## Security audits

In 2018, Outline was audited by Radically Open Security and Cure53, 2 independent digital security organisations that review software against the latest security standards. Radically Open Security conducted an additional audit in 2022 and Cure53 conducted an audit of the Outline SDK in 2024. You can read the reports here:

- [Radically Open Security Penetration Test Report (March 2018)](https://getoutline.org/reports/ros-report.pdf)
- [Cure53 Pentest & Audit Report Jigsaw Outline (December 2018)](https://getoutline.org/reports/cure53-report.pdf)
- [Radically Open Security Penetration Test Report (December 2022)](https://getoutline.org/reports/ros-report-2022.pdf)
- [Cure53 Pentest Report Jigsaw Outline VPN SDK (January 2024)](https://getoutline.org/reports/cure53-report-SDK-2024.pdf)

## Anonymous metrics and logs

Outline tracks the bandwidth used, as "bytes transferred" for each access key. This information allows server administrators to adjust their bandwidth subscriptions with their cloud server providers as needed, but does not allow them to see the actual information that went through the Outline server.

Learn more about Outline's [data and information collection](/about/data-collection).

---

## Security and privacy FAQs

## Can Outline make me anonymous online?

No, Outline is not an anonymity tool. Outline protects your privacy from potential network onlookers.

Outline does not offer you full anonymity on the websites you visit, because they can still identify you when you log in and sometimes through techniques, like browser fingerprinting. For mobile apps, most modern smartphones have APIs that allow installed apps to retrieve your location independent to your proxy as they can rely on the embedded GPS.

VPNs in general offer important protections, particularly from internet surveillance, but there are always risks to operating online. Even with a VPN, if an ISP is already aware of your identity and able to observe your network traffic, it may be able to determine the IP address of your Outline server. This information can be used to block access to the Outline server or learn usage patterns, like when you’re typically online, and possibly your rough location.

## Can someone tell if I'm using Outline?

Possibly. The platforms and services you access will most likely be able to tell that your connection is coming from a cloud server. Occasionally, they can deduce that you are using a VPN, but they will not be able to see the contents of your internet traffic.

## Does Outline protect me from all possible cyber threats?

No. No one tool will protect you against all possible cyber threats. Outline gives you access to the open internet and increases your privacy by encrypting your traffic, but we recommend that you take additional precautions to protect yourself against other types of attacks, like malware and phishing.

In order to strengthen your online defenses, please consider working with your organisation’s cybersecurity expert. Alternatively, you can obtain personalised guidance from leading security experts at [Security Planner](https://securityplanner.org/), a website built to provide you with clear instructions on choosing the right cybersecurity tools for your concerns.

You can also check out the other cybersecurity products from [Jigsaw](https://jigsaw.google.com/), like [Intra](https://getintra.org/), [Project Shield](https://g.co/shield), and [Password Alert](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Is it legal to use a VPN?

Please check your local laws, regulations, and the Terms of Service for the cloud provider you plan to use before operating Outline or using the app.

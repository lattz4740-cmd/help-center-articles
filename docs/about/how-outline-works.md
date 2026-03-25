---
title: How Outline Works
sidebar_label: How Outline Works
---

## Server installation
 ​Although Outline installation may seem simple, there’s actually a complex set of steps happening behind the scenes to get your server installed. Whenever Outline is installed, an installation script runs the following steps:

- The stable version of the Shadowbox image is retrieved and imported using Docker. The image is hosted on [Quay.io](https://quay.io/), in [https://quay.io/repository/outline/shadowbox?tab=tags](https://quay.io/repository/outline/shadowbox?tab=tags). This image contains the Outline server and Management API which is later used by the Outline Server Management application to create and remove access keys, opt in/out of reporting anonymous metrics, etc.
- [Watchtower](https://github.com/containrrr/watchtower) is installed and configured to check for image updates every hour, helping ensure that every Outline server is constantly up-to-date with the latest features and security improvements.
- A web server, used for accessing the Management API, is started on a random port on a secret and random path.
- A [self-signed SSL certificate](https://en.wikipedia.org/wiki/Self-signed_certificate) is created so that the management of the Outline server can be encrypted using TLS despite not having a domain name. A unique fingerprint of this certificate is also generated and stored in the Outline Manager application, helping prevent MITM attacks.

The Outline installation doesn’t need any configuration after installation

## Server security
 Outline software is open source, meaning that anyone can see the code and improve it if there are any discovered vulnerabilities. Our code is hosted on [GitHub](https://github.com/search?q=org%3AOutlineFoundation+outline&unscoped_q=outline).

 Furthermore, all installed Outline servers are automatically updated whenever a new version is released, ensuring no Outline server is left running old versions of the software.

 In order to manage the access keys on the server, the Outline Manager application interacts with a Management Service on the Outline server. The Management Service runs on a random port and on a secret and unique path. The Management Service itself is probing resistant since it doesn’t respond to queries unless the appropriate secret path is specified. Finally, all communication to the Management Service is encrypted with a [self-signed SSL certificate](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Also, the Outline server does not store any logs, so even if it were compromised, no user data would be disclosed. Learn more [here](/about/security-and-privacy). Outline was audited by [Radically Open Security](https://radicallyopensecurity.com/) and [Cure53](https://cure53.de/) in 2018. See the reports [here](/about/security-and-privacy).

## Handling UDP traffic
 Outline is able to operate as a system-wide VPN, meaning that all UDP traffic is tunneled through the Outline server.

## DNS traffic
Outline performs all DNS lookups through the Outline server, and protects them using the same encryption that’s used for all other network activity. Your DNS queries will go through the Outline server to the Dyn Internet Guide, OpenDNS, Cloudflare DNS or Quad9 DNS. Outline never logs your DNS lookups.

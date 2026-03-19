---
title: Terminology
sidebar_label: Terminology
---

## What is a VPN?
 A virtual private network (VPN) is a private connection between your device(s) and a host server. When you use a VPN, your traffic is hidden from the internet provider. You may want to use a VPN in the following scenarios:

- Protect your data when using a public Wi-Fi network
- Keep your browsing data private from your internet provider and government agencies
- Access uncensored content from various sources around the world

## How is Outline different from traditional VPNs?
 Internet providers can easily detect and block traditional VPNs by recognizing common security protocols and/or traffic volume patterns. Outline is more resilient than traditional VPNs because it's built using a protocol that is designed to be difficult to detect and therefore harder to block. Outline is resistant to sophisticated forms of censorship including network-based blocking and IP blocking.

## What is an Outline server?
 An Outline server runs the VPN that permitted users will connect to. If you’re creating a new network, you can use your own secure server as your Outline server if you have one, or you can use a cloud services provider such as:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

You’ll set up your server in Outline Manager.

## What is a service manager? {#servicemanager}

 A service manager is the person responsible for setting up the Outline server and sharing access keys with users. The service manager is generally responsible for the cost of the server use.

## What is an access key? {#accesskey}

 An access key is used to access an existing Outline server and connect to the VPN. A [service manager](#servicemanager) will give you an access key, or you can[set up an Outline server](/manager/server-setup/setup-server) yourself. Here is an example of what an access key looks like (sample only; will not work): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## What is Outline Manager?
 Outline Manager is a desktop application that allows a service manager to set up an Outline server, generate [access keys](#accesskey), and set data limits on usage per key. You can download the latest version of Outline Manager[here](https://getoutline.org/get-started/#step-3) or[here](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## What is Outline Client?
 Outline Client is an application, available for desktop and mobile, that allows you to connect to an Outline server and access the VPN using an access key. You can download the latest version of the Outline Client[here](https://getoutline.org/get-started/#step-3) or[here](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## What are data limits?
 Outline Manager allows service managers to set a trailing 30-day data limit on access keys to prevent overuse and help keep costs predictable. Service managers can set a default limit that applies to every key, and also set a different limit on any key to override the default limit. Once a limit is set, it goes into effect immediately and is enforced hourly.

If service managers opt in to share metrics with Jigsaw, they should view the[data collection policy](/about/data-collection) for details on how the use of data limits will be reported.

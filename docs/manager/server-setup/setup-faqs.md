---
title: Outline server setup FAQs
sidebar_label: Setup FAQs
---

## Can I use Outline without a server?
 Unfortunately, no. Outline software requires access to a server, whether it’s managed by you, your organization, or a trusted third-party.

## How long does it take to setup an Outline server?

In most cases, less than 5 minutes. You can install Outline on any cloud server, but we worked with DigitalOcean to offer a more user-friendly, guided installation experience where you can set up your server with a few clicks—no scripts.

If you chose the AWS, GCP or an advanced setup, we’ve simplified the server installation process to a single script that handles most environments.

## Where can I set up an Outline server?

You can set up an Outline server on most cloud providers where ever they operate.

The easiest option is to set it up on DigitalOcean, as it has servers in multiple locations, like Amsterdam, Toronto, San Francisco, and Singapore. If you prefer to install on another cloud provider or on your own infrastructure, you can choose the ‘Advanced Mode’ in the Outline Manager application and follow installation instructions using a setup script.

## Where should I set up my Outline server?

1. There are a few considerations you should make when selecting a location for your Outline Server:
2. The Outline Server location impacts how users experience the internet. For example, if the server is located in Amsterdam, the user accessing this server will experience the internet as if they were physically located in the Netherlands. Some websites may even display in Dutch. Typically, you can override the local language using a language selector on the website.
3. Distance between your users and the Outline Server may affect your speeds. In general, the physical distance between Outline users and the server can impact users’ internet speeds. In most cases, you can choose a server location closest to where your expected users will be, but you can check the [Submarine Cable Map](https://www.submarinecablemap.com/) to see which internet cables connect with your country or region.
4. Where your VPN server is located may affect the legal framework. Please note that Outline software doesn’t log your traffic. Learn more about [Security and privacy while using Outline](/about/security-and-privacy).

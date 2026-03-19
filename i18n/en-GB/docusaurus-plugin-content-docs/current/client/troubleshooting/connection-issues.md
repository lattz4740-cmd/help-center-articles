---
title: "Why can't I connect to the Outline service?"
sidebar_label: "Why can't I connect to the Outline service?"
---

There are a few reasons why you may not be able to connect to the Outline service:

- **Your device is**[**disconnected from the Internet**](#Internetissues)**.**Sometimes, your device will experience a break in network connection and it may take a moment for it to update the network icons. It's also possible that your device is connected to the local network, but that the Internet is down.
- **Your**[**network firewall is blocking access**](#FirewallIssues)**to your Outline server.**This is common if you're using a public network, like a school, work or free wireless network.
- **Your device has a**[**firewall or antivirus software**](#SoftwareIssues)**that's blocking access to your Outline server.**
- **Your**[**phone device settings**](#DeviceSettings)**may need to be changed.**
- **Your service manager may have**[**destroyed the server or your ISP may be blocking your request**](#ServerIssues)**.**

## Internet connection issues: {#Internetissues}

### How to test:
Turn off Outline and see if your connection to the Internet is restored.

- If yes, see more troubleshooting options below.
- If not, wait a few moments to see if your connection settings update themselves.

### Things to fix:

Get your device back online:

1. Check another device to see if it can connect to the same network. If other devices cannot get online, the network may be down and you'll need to wait for it to return or troubleshoot it.
2. If other devices can get on the same network, you can try one or more of the following to get it back online:
   1. Put the device in aeroplane mode (mobile)
   2. Restart the device
   3. Shut down the device, wait 2 minutes, turn the device back on

Network firewall issues:

### How to test:

1. Disconnect from your current Wi-Fi or wired network.
2. Connect to a different network, like a mobile one
3. Try to reconnect to the Outline server

If you're able to connect while on the other network, then this is your issue

### Things to fix:
Contact the service manager and request them to allow access to your Outline server or continue using the other network instead.

Firewall or antivirus software issues:

### How to test:

Try connecting to Outline from another device.

Note: Remember that you'll need an access key and the Outline app to use Outline on another device.

### Things to fix:

Check your firewall or antivirus software settings to make sure that they're set to allow VPN and Outline traffic through.

## Device settings: {#FirewallIssues}

## Things to check: {#SoftwareIssues}
For Android:

1. Open the Settings app.
2. Look for the **VPN settings** on your device. (The VPN settings will show you all the VPN apps that currently have access on your phone.)
3. If you don't see Outline in the VPN settings, uninstall Outline and reinstall it. Outline should automatically be given access by the device once installed.

Make sure that you don't have any screen overlay application installed on your Android device, as this may be sending the Outline permissions window to the background so that it isn't visible in the foreground.

On your Android device, go to Settings > Apps > Special app access. Then tap 'Display over other apps'. You can remove access to any apps that allow this behaviour.

For iOS: Read [this support article](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

## Server issues: {#DeviceSettings}

### How to test:

## If you have access to more than one server, try connecting to the other one. {#ServerIssues}

### Things to fix:
Contact your service manager to see if the server has been destroyed. If so, ask them for an [access key](/about/terminology) to another server.

If you set up the server, try connecting to it through the Outline Manager or another method such as [SSH](https://en.wikipedia.org/wiki/Secure_Shell). If that doesn't work, you can try checking the cloud provider console, if any, to see if the server is still online.

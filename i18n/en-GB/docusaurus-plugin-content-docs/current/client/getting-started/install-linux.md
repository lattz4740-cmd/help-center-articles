---
title: Installing Outline client on Linux
sidebar_label: Installing Outline client on Linux
---

Starting with Outline client version 1.15, all future versions will be released as Debian packages for Linux operating systems. Review our [minimum system requirements](/client/getting-started/system-requirements) for more information on which operating systems we support.

## Install Outline client for Debian-based Linux distributions (recommended)

Run the following commands:

1. Install Outline's repository key and add the repository.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Update the apt package list and install the latest version of Outline client.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

To check for or install future updates, run the commands in Step 2 again. Please note that in-app auto-update is disabled for Outline client on Linux, from version 1.15 onwards.

To uninstall Outline client, run the following command:

```
sudo apt purge outline-client
```

## Alternative option

1. Download the latest Outline client Debian package from [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Run the following commands in the command line to install the package
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Check for updates manually, as in-app auto-update is disabled for Outline client on Linux, from version 1.15 onwards.
4. To uninstall Outline client, run the following command in the command line:
   ```
   sudo apt purge outline-client
   ```

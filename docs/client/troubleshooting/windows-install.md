---
title: "Why can't I install Outline Client on Windows?"
sidebar_label: Windows install issues
---

You may see this error message: “Sorry, it looks like Outline is not properly installed. Please try installing it again. If that doesn’t work, please [submit feedback](/about/feedback).”

If you’re using Outline on Windows, occasionally, you may run into an unexpected error. In most cases, the Outline TAP adapter (driver) needs to be deleted and Outline should be reinstalled.

The steps may vary based on your Windows operating system version, but below are general steps for how to uninstall the TAP adapter and Outline and then reinstall Outline.

1. Uninstall the TAP adapter for Outline Client
   - Go to **Device Managers**, then **Network Adapters**
   - Find the **TAP-Windows Adapter V9** file or the TAP adapter associated with Outline
   - Uninstall or delete this adapter. Keep in mind that this could affect other VPN apps that you have installed.
2. Uninstall Outline Client
   - Go to **Programs & Features**, then to **Uninstall Program**
   - Find the Outline Client app and uninstall Outline Client
   - [Download the latest version of Outline Client](https://getoutline.org/get-started/#step-3) and reinstall it on your Windows device. The new installation should automatically install a new TAP adapter.

If you’re still having trouble, [contact support](/about/feedback).

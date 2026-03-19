---
title: Google Cloud Automated Setup
sidebar_label: Google Cloud setup
---

## Overview

Outline Manager includes a feature that allows you to automatically configure Outline Server on a server running on the Google Cloud. If you choose to use this feature, Outline Manager will ask you to sign in with your Google Account, which will grant certain [OAuth](https://developers.google.com/identity/protocols/oauth2) permissions to your local installation of the Outline Manager for the purposes of configuring your Google Cloud Account.

 If you do not wish to provide these permissions, you can follow the advanced setup instructions in the Outline Manager to run Outline on Google Cloud Platform.

## Permissions Granted

In order to provide automated setup, Outline Manager requires the following permissions from your Google Account.

## Google Cloud Platform

- View and manage your Google Compute Engine resources
- View your data across Google Cloud services and see the email address of your Google Account

## Basic account info

- See your primary Google Account email address
- Associate you with your personal info on Google

## Additional access

- Manage your Cloud Platform projects
- View and manage your Google Cloud Platform billing accounts
- Manage your Google API service configuration

These permissions allow us to support advanced functionality for managing your Outline servers including:

- Allowing you to select the correct billing account
- Creating a new project to organize your Outline servers
- Listing available data centers
- Creating new virtual machines to run Outline
- Configuring the new virtual machine with Outline

## Revoking Permissions

You can revoke access to Google Cloud Platform for the Outline Manager by visiting [My Account](https://myaccount.google.com/permissions). If you revoke access, any servers you’ve created with the automated setup will remain running but will no longer appear in the Outline Manager. To restore access to them, simply reconnect to Google Cloud Platform by beginning the automated setup flow.

## Outline Project Organization

Google Cloud automated setup uses a single [Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects) to organize your Outline servers. The project is created during the first use of the automated setup, with a suggested project ID that begins with “Outline-” followed by a string of random characters. You can choose a different project ID at creation if you prefer. The project will be named “Outline servers”.

## Billing Account

Google Cloud projects require a linked “billing account” that defines payment information. When you first use Google Cloud automated setup, you will be asked to provide a billing account to associate with your Outline servers. Sometimes a server will stop running because there is a problem with the billing account. In this case, you should log in to the [Google Cloud Console](https://console.cloud.google.com/getting-started), locate the Google Cloud project associated with Outline (named “Outline servers”), and update the billing settings.

## Destroying Servers

If you wish to destroy your servers created using the automated setup, the easiest way to do so is from within the Outline Manager. However, if you wish to destroy the servers yourself, you may log into the [Google Cloud Console](https://console.cloud.google.com/getting-started), find the project that was created during initial setup (named “Outline servers”), and either delete the resources there or shut down the project.

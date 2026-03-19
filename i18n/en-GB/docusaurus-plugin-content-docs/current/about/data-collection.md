---
title: Data and information collection
sidebar_label: Data and information collection
---

Outline doesn't collect personal information unless you opt in to provide it. Outline also doesn't collect information about the websites that you visit or with whom or what you communicate.

 If you are creating or logging in to an account with a third-party cloud provider through the Outline Manager, we don't obtain any information that you provide to your third-party cloud provider, such as your email address, name, billing information and payment details.

## Information that we obtain automatically
 We collect two types of information automatically.

 1. Server IP

 The Outline server IP is collected by [Quay.io](https://quay.io/), and made accessible to us when the server automatically updates with the latest security and feature improvements. The server IP may identify the cloud server provider and the city in which the Outline server has been set up, but this doesn't provide information about who's running the server or who is accessing it.

 2. Non-personally identifiable technical information

 If Outline crashes or a fatal exception occurs, or if you manually send feedback through the Outline app, the information listed below will be reported. This information will only be used to help identify and fix stability or performance issues.

- Country
- Locale
- Date and time of crash/exception and up to 100 prior events, like that of a user opening the 'About' section
- Statically compiled exception messages
- OS name and version
- Phone model (if applicable)
- App start time
- Browser
- Architecture
- Outline version and build number

This information is transferred using HTTPS to Sentry ([sentry.io](https://sentry.io/)), a third-party, open source error tracking provider. Sentry uses a variety of industry-standard technologies and services to secure your data from unauthorised access, disclosure, use and loss. If you have any questions about Sentry's policies, please visit [https://sentry.io/security/](https://sentry.io/security/) and [https://sentry.io/privacy/](https://sentry.io/privacy/), or contact [security@sentry.io](mailto:security@sentry.io). All Outline data stored by Sentry is restricted such that only members of the Outline team can access it.

## Information that we obtain only upon opt-in
 Outline reports the following information to the Outline team upon opt-in.

 1. Usage metrics

 Each Outline server automatically collects, for the last hour and on a per access key basis, the number of bytes transferred, the amount of time that a user was connected to the server, the countries and autonomous systems of origin of the credentials used and whether any features have been enabled or disabled. Neither the contents of the communication nor any personally identifiable metadata (e.g. logins, emails, device IDs, etc.) is logged. All metrics are tied to a server ID. Instructions for changing the server ID can be found [here](/manager/server-management/reset-server-id).

 By default, Outline servers do not share these metrics with the Outline team. If the server administrator explicitly opts in to sharing usage metrics, this information will be securely sent to the Outline team every hour. After 60 days, the usage metrics will be aggregated to the country level. Server administrators can change their usage metrics sharing preference at any time by visiting the 'Settings' menu in the Outline Manager.

 We appreciate you sharing anonymous metrics with us about your server usage, as we use them to measure usage trends and to improve the product.

 For example, if a server administrator opts in to sharing usage metrics with us, we could receive information indicating that a server with ID 12345 was used for three hours yesterday, transferring a total of 500 megabytes of data, from three keys each used in the United States and Canada, with the data limits feature enabled.

 2. Your comments and email if you submit feedback

 The Outline Manager and Outline apps allow you to submit feedback to the team. We recommend not including personally identifiable information, but an email field is available as an option if you would like a response from the team. We also automatically gather some basic information, so that we can understand your feedback. Please see item 2 above, under 'Information that we obtain automatically', to see what data we collect. Learn more about Outline's security and privacy practices [here](/about/security-and-privacy).

 If you are using a beta version of the Outline app on Android, we may use Google's [Firebase](https://firebase.google.com/) service to collect debugging information that can help us detect problems and improve Outline. You can learn more about Firebase's privacy and security policies from their website: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). If you do not want Outline to send this information through Firebase, please use the production version of the app.

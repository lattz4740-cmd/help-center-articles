---
title: "How do I set data limits on access keys?"
sidebar_label: Data limits
---

You can set a data limit that will apply to all access keys. To set the limit, open Outline Manager and navigate to Settings. There you will see a Data limits toggle that, when enabled, lets you set a limit.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Once you set a limit, you can see how close each user is to the limit on the access key page, where a bar graph shows the data usage over the last 30 days.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

In addition to being able to set a limit for all of your access keys, you can grant each key its own data limit. This setting will override any default data limit you have set, but if you have not set a default data limit, you can still set a data limit for any key. 

 To set a key's data transfer limit, open the Outline Manager, navigate to the Connections tab that contains the key you want to set, and click on the menu on the right side of the key's row. From there, click on Data Limit. To change the data limit on "My access key", click the Data Limits icon ![Data limits icon](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Select Set a custom data limit. Once you've selected this checkbox, a field will appear where you can set the custom data limit for that key. Click on the SAVE button when you're done to save the data limit.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Once you've saved your data transfer limit for the chosen key, the limit will show on the main screen, alongside the data usage (over the past 30 days) for each key.

To remove the data limit from an access key, navigate to the key's Data Limit dialog as before, uncheck the box labeled Set a custom data limit, and click the SAVE button.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

## Data Limit FAQs
## What is a 30-day trailing data limit?
 A 30-day trailing data limit will sum each key’s usage over the past 30 days and keep the key’s usage over that period below the limit. The effect is that the key cannot go over the limit during any 30 day period, including calendar months of 30 days or less. In effect, this means that each user’s available data will increase each day by the amount they used 31 days ago.

## Why does Outline use trailing limits?
 Trailing limits provide guarantees over every 30 day period, which means they’re simpler to configure than a recurring limit (such as a customizable day of the month) while providing similar guarantees. They also match the existing display for Outline data use, as well as common tools such as analytics services and server statistics.

## What data is counted in a data limit?
 Each access key’s egress from the server is included in the tally. Strictly speaking this means data sent on the key’s behalf out of the server, as well as back to the client. Practically, this should closely align to the traffic sent from the key to the server and back, so we hope it will match your users’ tallies. We chose egress since that is what the cloud providers we surveyed bill for.

## Will users be notified if they’ve run over their data limit?
 Not at the moment. Many cloud providers include a limit such as 1TB for the whole month, which can support 10 users at 100 GB or 100 users at 10 GB. These are pretty big numbers, and we don’t expect many users will hit them. We hope that users will reach out to server managers when they hit their limit. However, we’d appreciate your insight into how notifications might help for your use case, and you can contact us[here](/about/feedback).

## Will users be notified if they approach their data limit?
 The amount of new data that a user approaching their limit will receive will vary from day to day because it’s based on their use 30 days ago. We think a warning is more likely to confuse end users than to help them. We’d appreciate your feedback on this behavior[here](/about/feedback).

## Can I reset a user’s data usage?
 No, a user’s limit always includes the past 30 days of data use. However, you can raise their key's data limit or create a new key for them.

## Why did some of my users lose access as soon as I enabled data limits?
 Data limits are based on users’ prior 30 days of data transfer, which is recorded whether or not data limits have been enabled. It’s possible that the users in question had already exceeded the limit before it was put in place. Also note that all data limits are enforced, even when changing a single key’s data limit.

## Can I set a server-wide limit, such as “1 TB per 30 days”?
 Not at the moment. We’d love to hear more about your use case[here](/about/feedback).

## If there’s a default data limit and a data limit on a specific key, which one will be enforced?
 The specific key's data limit will override whatever default data limit (if any) you have set.

## Can I set a data limit for a specific key without having a default data limit set?
 Yes. You don’t need a default limit defined in order to set a data limit on one key. For example, you could set a limit on one key which you think may be shared broadly in order to protect yourself from excessive data transfer through that key.

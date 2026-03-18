---
title: "Linux-ൽ Outline Client ഇൻസ്റ്റാൾ ചെയ്യുന്നു"
sidebar_label: "Linux-ൽ Outline Client ഇൻസ്റ്റാൾ ചെയ്യുന്നു"
---

Outline Client പതിപ്പ് 1.15 മുതൽ, ഭാവിയിലെ എല്ലാ പതിപ്പുകളും Linux ഓപ്പറേറ്റിംഗ് സിസ്റ്റങ്ങൾക്കായുള്ള Debian പാക്കേജുകളായി റിലീസ് ചെയ്യും. ഞങ്ങൾ പിന്തുണയ്ക്കുന്ന ഓപ്പറേറ്റിംഗ് സിസ്റ്റങ്ങളെക്കുറിച്ചുള്ള ഞങ്ങളുടെ [ഏറ്റവും കുറഞ്ഞ സിസ്റ്റം ആവശ്യകതകൾ](/client/getting-started/system-requirements) അവലോകനം ചെയ്യുക.

## Debian അടിസ്ഥാനമാക്കിയുള്ള Linux ഡിസ്ട്രിബ്യൂഷനുകൾക്കായി Outline Client ഇൻസ്റ്റാൾ ചെയ്യുക (നിർദ്ദേശിക്കുന്നത്)

ഇനിപ്പറയുന്ന കമാൻഡുകൾ റൺ ചെയ്യുക:

1. Outline-ന്റെ റിപ്പോസിറ്ററി കീ ഇൻസ്റ്റാൾ ചെയ്ത് റിപ്പോസിറ്ററി ചേർക്കുക.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. നിങ്ങളുടെ apt പാക്കേജ് ലിസ്റ്റ് അപ്ഡേറ്റ് ചെയ്ത് Outline Client-ന്റെ ഏറ്റവും പുതിയ പതിപ്പ് ഇൻസ്റ്റാൾ ചെയ്യുക.

```
sudo apt update
sudo apt install outline-client
```

ഭാവിയിലെ അപ്‌ഡേറ്റുകൾ പരിശോധിക്കാനോ ഇൻസ്റ്റാൾ ചെയ്യാനോ ഘട്ടം 2-ലെ കമാൻഡുകൾ വീണ്ടും റൺ ചെയ്യുക. പതിപ്പ് 1.15-ൽ ആരംഭിക്കുന്ന, Linux-ലെ Outline Client-നായി ആപ്പിനുള്ളിലെ സ്വയമേവയുള്ള അപ്‌ഡേറ്റ് പ്രവർത്തനരഹിതമാക്കിയിട്ടുണ്ടെന്ന കാര്യം ശ്രദ്ധിക്കുക.

Outline Client അൺഇൻസ്റ്റാൾ ചെയ്യാൻ, ഇനിപ്പറയുന്ന കമാൻഡ് റൺ ചെയ്യുക:

```
sudo apt purge outline-client
```

## ഇതര ഓപ്ഷൻ

1. [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)-ൽ നിന്ന് ഏറ്റവും പുതിയ Outline Client Debian പാക്കേജ് ഡൗൺലോഡ് ചെയ്യുക
2. പാക്കേജ് ഇൻസ്റ്റാൾ ചെയ്യാൻ കമാൻഡ് ലൈനിൽ ഇനിപ്പറയുന്ന കമാൻഡുകൾ റൺ ചെയ്യുക

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. പതിപ്പ് 1.15-ൽ ആരംഭിക്കുന്ന, Linux-ലെ Outline Client-നായി ആപ്പിനുള്ളിലെ സ്വയമേവയുള്ള അപ്‌ഡേറ്റ് പ്രവർത്തനരഹിതമാക്കിയതിനാൽ, അപ്‌ഡേറ്റുകൾ നേരിട്ട് പരിശോധിക്കുക.

4. Outline Client അൺഇൻസ്റ്റാൾ ചെയ്യാൻ, കമാൻഡ് ലൈനിൽ ഇനിപ്പറയുന്ന കമാൻഡ് റൺ ചെയ്യുക:

```
sudo apt purge outline-client
```

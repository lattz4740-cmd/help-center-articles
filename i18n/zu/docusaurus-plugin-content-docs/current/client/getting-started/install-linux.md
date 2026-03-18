---
title: Ifaka Iklayenti Lohlaka kuLinux
sidebar_label: Ifaka Iklayenti Lohlaka kuLinux
---

Ukuqala ngohlobo 1.15 Lweklayenti Lohlaka, zonke izinhlobo zesikhathi esizayo zizokhishwa njengamaphakheji eDebian wama-app weLinux. Buyekeza [ubuncane bokudingekayo ohlelweni](/client/getting-started/system-requirements) ukuze uthole ulwazi olwengeziwe ngokuthi yimaphi ama-app esiwasekelayo.

## Faka Iklayenti Lohlaka lokusatshalaliswa kweLinux elisekelwe kuDebian (Kuyanconywa)

Qalisa imiyalo elandelayo:

1. Faka ukhiye wekhosombe Lohlaka bese ufaka ikhosombe.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Buyekeza uhlu lwephakheji elifanelekile futhi ufake uhlobo lwakamuva Lweklayenti Lohlaka.

```
isibuyekezo sesudo apt
faka iklayenti lohlaka lwe-sudo apt
```

Ukuze uhlole noma ufake izibuyekezo zesikhathi esizayo, sebenzisa imiyalo Esinyathelweni sesi-2 futhi. Qaphela ukuthi ukubuyekezwa okuzenzakalelayo kwangaphakathi nohlelo kukhutshaziwe Kuklayenti Lohlaka lweLinux, kuqala kuhlobo 1.15.

Ukuze ukhiphe Iklayenti Lohlaka, sebenzisa umyalo olandelayo:

```
sudo apt purge outline-client
```

## Okunye Okungakhethwa Kukho

1. Dawuniloda iphakheji yakamuva Yeklayenti Lohlaka lweDebian kokuthi [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Qalisa imiyalo elandelayo emugqeni womyalo ukuze ufake iphakheji

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Bheka izibuyekezo mathupha, njengoba ukubuyekezwa okuzenzekelayo kwangaphakathi nohlelo kukhutshaziwe Kuklayenti Lohlaka kuLinux, ukusukela kuhlobo 1.15.

4. Ukuze ukhiphe Iklayenti Lohlaka, sebenzisa umyalo olandelayo emugqeni womyalo:

```
sudo apt purge outline-client
```

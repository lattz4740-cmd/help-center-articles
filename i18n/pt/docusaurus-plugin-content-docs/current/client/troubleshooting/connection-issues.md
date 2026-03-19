---
title: "Porque não consigo estabelecer ligação ao serviço do Outline?"
sidebar_label: "Porque não consigo estabelecer ligação ao serviço do Outline?"
---

Existem alguns motivos pelos quais pode não conseguir estabelecer ligação ao serviço do Outline:

- **O seu dispositivo**/client/troubleshooting/connection-issues#One[**não está ligado à Internet**](#Internetissues)[#Internetissues](#Internetissues)**.**Por vezes, o dispositivo sofre interrupções na ligação de rede e pode demorar algum tempo a atualizar os ícones de rede. Também é possível que o dispositivo esteja ligado à rede local, mas a Internet esteja indisponível.
- **A sua**/client/troubleshooting/connection-issues#Two[**firewall de rede está a bloquear o acesso**](#FirewallIssues)[#FirewallIssues](#FirewallIssues)**[#FirewallIssues](#FirewallIssues)ao servidor do Outline.**Isto é comum se estiver a usar uma rede pública, como a rede da escola ou do trabalho, ou uma rede sem fios gratuita.
- **O seu dispositivo tem um**/client/troubleshooting/connection-issues#Three[**software antivírus ou firewall**](#SoftwareIssues)[#SoftwareIssues](#SoftwareIssues)**que está a bloquear o acesso ao servidor do Outline.**
- **As**[**definições do dispositivo do seu telemóvel**](#DeviceSettings)**podem ter de ser alteradas.**
- **O gestor do serviço pode ter**[**destruído o servidor ou o seu ISP pode estar a bloquear o pedido**](#ServerIssues).

## Problemas de ligação à Internet: {#Internetissues}

## Como testar:

Desative o Outline e verifique se a ligação à Internet é reposta.

- Se for reposta, consulte abaixo mais opções de resolução de problemas.
- Se não for reposta, aguarde alguns momentos para verificar se as definições de ligação são atualizadas automaticamente.

## Aspetos a corrigir:

Restabeleça a ligação do dispositivo:

1. Use outro dispositivo para verificar se consegue estabelecer ligação à mesma rede. Se não conseguir estabelecer ligação a outros dispositivos, a rede pode estar indisponível, e tem de esperar que volte a ficar disponível ou tentar resolver o problema.
2. Se conseguir estabelecer ligação à mesma rede com outros dispositivos, pode experimentar uma ou mais das seguintes instruções para restabelecer a ligação:
   1. Coloque o dispositivo no modo de avião (telemóvel)
   2. Reinicie o dispositivo
   3. Desligue o dispositivo, aguarde dois minutos e volte a ligá-lo

## Problemas com a firewall de rede: {#FirewallIssues}

## Como testar:

1. Desligue a ligação atual à rede Wi-Fi ou com fios.
2. Estabeleça ligação a uma rede diferente, como uma rede móvel.
3. Tente restabelecer a ligação ao servidor do Outline.

Se conseguir estabelecer ligação através de outra rede, então o seu problema é este.

## Aspetos a corrigir:

Contacte o gestor do serviço para lhe pedir que autorize o acesso ao seu servidor do Outline ou, em alternativa, continue a usar a outra rede.

## Problemas com o software antivírus ou firewall:
## Como testar:
 Tente estabelecer ligação ao Outline noutro dispositivo.

Nota: lembre-se de que precisa de uma chave de acesso e da app Outline para usar o Outline noutro dispositivo.

## Aspetos a corrigir: {#SoftwareIssues}
Verifique as definições do software antivírus ou firewall para garantir que permitem tráfego VPN e do Outline.

## Definições do dispositivo: {#DeviceSettings}

## Aspetos a confirmar: {#DeviceSettings}
Android:

1. Abra a app Definições.
2. Procure as **definições de VPN** no seu dispositivo. (As definições de VPN apresentam todas as apps de VPN que têm atualmente acesso ao seu telemóvel.)
3. Se o Outline não estiver incluído nas definições de VPN, desinstale-o e, em seguida, reinstale-o. Após a instalação, o dispositivo deve conceder automaticamente acesso ao Outline.

Certifique-se de que não tem nenhuma aplicação de sobreposição de ecrã instalada no dispositivo Android, uma vez que pode estar a enviar a janela de autorizações do Outline para segundo plano, impedindo que fique visível em primeiro plano.

 No dispositivo Android, aceda a Definições > Apps > Acesso especial para apps. A seguir, toque em "Sobrepor a outras apps". Pode remover o acesso às apps que permitem este comportamento.

 iOS: leia[este artigo do apoio técnico](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

## Problemas com o servidor: {#ServerIssues}

## Como testar: {#ServerIssues}
Se tiver acesso a mais de um servidor, tente estabelecer ligação a outro servidor.

## Aspetos a corrigir:

Contacte o gestor do serviço para verificar se o servidor foi destruído. Se for o caso, peça-lhe uma [chave de acesso](/about/terminology) a outro servidor.

Se configurou o servidor, tente estabelecer ligação através do Gestor Outline ou de outro método, como [SSH](https://pt.wikipedia.org/wiki/Secure_Shell). Se esta solução não funcionar, pode tentar consultar a consola do fornecedor de nuvem, se aplicável, para verificar se o servidor ainda está online.

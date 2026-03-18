---
title: "Por que não consigo me conectar ao serviço do Outline?"
sidebar_label: "Por que não consigo me conectar ao serviço do Outline?"
---

Esse problema pode ter alguns motivos:

- **O dispositivo está**[**desconectado da Internet**](#Internetissues)**.**Às vezes, o dispositivo se desconecta da rede e demora para atualizar os ícones. Também é possível que ele esteja conectado à rede local, mas que a Internet esteja fora do ar.
- **O**[**firewall de rede está bloqueando acesso**](#FirewallIssues)**ao servidor do Outline.**Isso é comum em redes públicas, como uma rede sem fio aberta, da escola ou do trabalho.
- **O dispositivo tem um**[**software de firewall ou antivírus**](#SoftwareIssues)**que está bloqueando o acesso ao servidor do Outline.**
- **Pode ser necessário alterar as**[**configurações do smartphone.**](#DeviceSettings)**.**
- **O gerente de serviço pode ter**[**destruído o servidor ou o ISP pode estar bloqueando sua solicitação**](#ServerIssues)**.**

## Problemas de conexão de Internet: {#Internetissues}

## Como testar: {#Internetissues}
Desative o Outline e verifique se a conexão com a Internet foi restaurada.

- Nesse caso, acesse mais opções de solução de problemas abaixo.
- Caso contrário, aguarde alguns instantes para saber se as configurações de conexão serão atualizadas.

## O que corrigir:

Restaure a conexão do dispositivo seguindo estas etapas:

1. Verifique se outro dispositivo se conecta à mesma rede. Se isso não acontecer, talvez a rede esteja fora do ar, e você precisará esperar que ela volte ou resolver o problema.
2. Se outros dispositivos acessarem a mesma rede, adote uma ou mais medidas para restaurar a conexão do seu dispositivo:
   1. Coloque o dispositivo móvel no modo avião.
   2. Reinicie o dispositivo.
   3. Desligue, aguarde dois minutos e ligue o dispositivo de novo.

## AProblemas no firewall da rede: {#FirewallIssues}

## Como testar:

1. Saia da rede Wi-Fi ou com fio.
2. Entre em uma rede diferente, por exemplo, de celular.
3. Tente se conectar ao servidor do Outline

Se você consegue se conectar enquanto está na outra rede, o problema está aqui

## O que corrigir: {#FirewallIssues}
Entre em contato com o gerenciador de serviço e solicite acesso ao servidor do Outline ou continue usando a outra rede.

## Problemas no software do antivírus ou firewall: {#SoftwareIssues}

## Como testar:

Use outro dispositivo para acessar o Outline.

Observação: você precisa de uma chave de acesso e do app Outline para usar esse software em outro dispositivo.

## O que corrigir:

Verifique as configurações do software de firewall ou antivírus e descubra se elas permitem o tráfego da VPN e do Outline.

## Configurações do dispositivo: {#DeviceSettings}

## Itens a serem verificados: {#ServerIssues}
Para Android:

1. Abra o app "Configurações".
2. Busque as **configurações de VPN** do dispositivo, que mostram todos os apps de VPN com acesso ao smartphone
3. Se o Outline não estiver nas configurações de VPN, desinstale e reinstale-o. Ele deve receber acesso do dispositivo automaticamente após a instalação.

Verifique se não há nenhum aplicativo de sobreposição de tela instalado no dispositivo Android, já que esse recurso pode enviar a janela de permissões do Outline para o segundo plano e ocultá-la em primeiro plano.

No dispositivo Android, acesse Configurações > Apps > Acesso especial para apps. Toque em "Sobrepor a outros apps". Você pode remover acesso a todos os apps que permitem esse comportamento.

Para iOS: leia [este artigo de suporte](https://support.apple.com/guide/deployment/vpn-settings-overview-dep2d2adb35d/web).

**Problemas do servidor:**

## Como testar:

Se você tiver acesso a mais de um servidor, tente se conectar ao outro.

## O que corrigir: {#DeviceSettings}
Entre em contato com o gerente de serviço para saber se o servidor foi destruído. Em caso positivo, peça uma [chave de acesso](https://docs.google.com/document/d/1Mp-hH49D0bn02LO-MkgVVh95O7FrG-6XXCjX49WA3nE/edit#heading=h.2dn8xnck0993) a outro servidor.

Se você for responsável pela configuração do servidor, conecte-se a ele pelo Outline Manager ou de outra forma, como [SSH](https://en.wikipedia.org/wiki/Secure_Shell). Se isso não funcionar, verifique o console do provedor de nuvem, se houver, para saber se o servidor ainda está on-line.

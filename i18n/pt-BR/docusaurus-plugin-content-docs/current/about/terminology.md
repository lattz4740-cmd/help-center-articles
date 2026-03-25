---
title: Terminologia
sidebar_label: Terminologia
---

## O que é uma VPN?

Uma rede privada virtual (VPN) é uma conexão privada entre seu dispositivo e um servidor host. Quando você usa uma VPN, seu tráfego fica oculto do provedor de Internet.

Use uma VPN para:

- Proteger seus dados ao usar uma rede Wi-Fi pública
- Impedir que seus dados de navegação particulares sejam acessados pelo provedor de Internet ou por órgãos governamentais
- Acessar conteúdo sem censura de várias fontes ao redor do mundo

## Qual a diferença entre o Outline e as VPNs tradicionais?

Os provedores de Internet podem detectar e bloquear as VPNs tradicionais facilmente ao reconhecer protocolos de segurança comuns e/ou padrões de volume de tráfego. O Outline é mais eficiente que as VPNs tradicionais porque foi criado com base em um protocolo que dificulta a detecção e o bloqueio por parte dos provedores. Esse software resiste a formas avançadas de censura, como bloqueio de IP ou baseado na rede.

## O que é um servidor do Outline?

Um servidor do Outline executa a VPN a que usuários com permissão vão se conectar.

Se você estiver criando uma nova rede, é possível usar seu próprio servidor seguro como servidor do Outline, ou usar um provedor de serviços de nuvem, como:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Você poderá configurar seu servidor no Outline Manager.

## O que é um administrador do serviço? {#servicemanager}

Um administrador do serviço é uma pessoa responsável por configurar o servidor do Outline e compartilhar as chaves de acesso com os usuários. Ele também controla o custo de uso do servidor, em geral.

## O que é uma chave de acesso? {#accesskey}

Essas chaves são usadas para acessar um servidor do Outline e estabelecer uma conexão com a VPN. Um [administrador do serviço](#servicemanager) fornece a chave de acesso, mas você também pode [configurar um servidor do Outline](/manager/server-setup/setup-server) por conta própria.

Aqui está um exemplo de como é uma chave de acesso (isso é apenas uma amostra e não vai funcionar):

ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## O que é o Outline Manager?

O Outline Manager é um aplicativo para computadores que permite que um administrador do serviço configure um servidor do Outline, gerencie [chaves de acesso](#accesskey) e defina limites de dados com base no uso por chave. Faça o download da versão mais recente do Outline Manager [aqui](https://getoutline.org/get-started/#step-3) ou acessando [este link](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## O que é o app cliente do Outline?

Esse aplicativo está disponível para computadores e dispositivos móveis e permite que você se conecte a um servidor do Outline e acesse a VPN usando uma chave de acesso. Faça o download da versão mais recente do app cliente do Outline [aqui](https://getoutline.org/get-started/#step-3) ou acessando [este link](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## O que são os limites de dados?

Com o Outline Manager, os administradores do serviço podem configurar limites de dados de 30 dias para evitar o uso em excesso e manter os custos previsíveis. Os administradores podem definir um limite padrão que se aplique a todas as chaves, mas também é possível configurar um limite diferente em qualquer chave para substituir o padrão. Quando essa informação é definida, a configuração entra em vigor imediatamente e é aplicada a cada hora.

Se o administrador do serviço ativar o compartilhamento de métricas com o Jigsaw, deve ler a [política de coleta de dados](https://getoutline.org/policies/data-collection) para entender como o uso dos limites de dados é relatado.

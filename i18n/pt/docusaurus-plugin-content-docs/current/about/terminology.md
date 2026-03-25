---
title: Terminologia
sidebar_label: Terminologia
---

## O que é uma VPN?
 Uma rede privada virtual (VPN) é uma ligação privada entre os seus dispositivos e um servidor anfitrião. Quando usa uma VPN, o seu tráfego é ocultado do fornecedor de Internet. É recomendável usar uma VPN para:

- Proteger os seus dados quando usa uma rede Wi-Fi pública
- Manter os seus dados de navegação ocultados do fornecedor de Internet e de organismos governamentais
- Aceder a conteúdo sem censura proveniente de várias fontes em todo o mundo

## O que distingue o Outline das VPNs tradicionais?
 Os fornecedores de Internet podem detetar e bloquear facilmente as VPNs tradicionais através do reconhecimento de protocolos de segurança comuns e/ou padrões no volume de tráfego. O Outline é mais resiliente do que as VPNs tradicionais porque foi desenvolvido com base num protocolo concebido para dificultar a deteção, sendo mais difícil de bloquear. O Outline é resistente a formas sofisticadas de censura, incluindo o bloqueio baseado na rede ou o bloqueio de IP.

## O que é um servidor do Outline?
 Os servidores do Outline executam a VPN à qual os utilizadores autorizados se ligam. Se estiver a criar uma nova rede e tiver o seu próprio servidor seguro, pode usá-lo como servidor do Outline. Caso contrário, pode usar um fornecedor de serviços de nuvem como:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Pode configurar o seu servidor no Gestor Outline.

## O que é um gestor de serviço? {#servicemanager}
 O gestor de serviço é a pessoa responsável por configurar o servidor do Outline e partilhar as chaves de acesso com os utilizadores. Geralmente, o gestor de serviço também é responsável pelos custos da utilização do servidor. 

## O que é uma chave de acesso? {#accesskey}
 As chaves de acesso são usadas para aceder a um servidor do Outline existente e estabelecer ligação à VPN. O [gestor de serviço](#servicemanager) partilha consigo uma chave de acesso. Em alternativa, pode [configurar o seu próprio servidor do Outline](/manager/server-setup/setup-server). Segue-se um exemplo de uma chave de acesso (apenas ilustrativo, não funciona): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## O que é o Gestor Outline?
 O Gestor Outline é uma aplicação para computador que permite aos gestores de serviço configurar um servidor do Outline, gerar [chaves de acesso](#accesskey) e definir limites de dados em função da utilização de cada chave. Pode transferir a versão mais recente do Gestor Outline [aqui](https://getoutline.org/get-started/#step-3) ou [aqui](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## O que é a app cliente Outline?
 O cliente Outline é uma aplicação, disponível para computador e dispositivos móveis, que lhe permite estabelecer ligação a um servidor do Outline e aceder à VPN com uma chave de acesso. Pode transferir a versão mais recente do cliente Outline [aqui](https://getoutline.org/get-started/#step-3) ou [aqui](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

## O que são limites de dados?
 O Gestor Outline permite aos gestores de serviço definir um limite de dados adaptável de 30 dias nas chaves de acesso para evitar uma utilização excessiva e ajudar a manter os custos previsíveis. Os gestores de serviço podem predefinir um limite que se aplica a todas as chaves. Além disso, também podem definir um limite diferente numa chave para substituir o limite predefinido. Depois de definidos, os limites entram imediatamente em vigor e são aplicados de hora em hora.

Os gestores de serviço que optarem por aceitar a partilha de métricas com a Jigsaw devem consultar a [Política de Recolha de Dados](https://getoutline.org/policies/data-collection) para acederem a detalhes sobre a forma como a utilização de limites de dados é comunicada.

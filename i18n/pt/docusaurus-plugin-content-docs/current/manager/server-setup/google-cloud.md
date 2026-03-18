---
title: Configuração automática do Google Cloud
sidebar_label: Configuração automática do Google Cloud
---

## Vista geral

O Gestor Outline inclui uma funcionalidade que lhe permite configurar automaticamente o servidor do Outline num servidor em execução no Google Cloud. Se optar por usar esta funcionalidade, o Gestor Outline vai pedir-lhe que inicie sessão com a sua Conta Google, o que vai conceder determinadas autorizações de [OAuth](https://developers.google.com/identity/protocols/oauth2) à instalação local do Gestor Outline com a finalidade de configurar a sua conta do Google Cloud.

 Se não quiser conceder estas autorizações, pode seguir as instruções de configuração avançada no Gestor Outline para executar o Outline na Google Cloud Platform.

## Autorizações concedidas

Para disponibilizar a configuração automática, o Gestor Outline requer as seguintes autorizações da sua Conta Google.

## Google Cloud Platform

- Ver e gerir os seus recursos do Google Compute Engine
- Ver os seus dados em todos os serviços do Google Cloud e ver o endereço de email da sua Conta Google

## Informações básicas da conta

- Ver o endereço de email principal da sua Conta Google
- Associar o seu nome às suas informações pessoais na Google

## Acesso adicional

- Gerir os seus projetos da Cloud Platform
- Ver e gerir as suas contas de faturação da Google Cloud Platform
- Gerir a sua configuração do serviço de APIs do Google

Estas autorizações permitem-nos suportar funcionalidades avançadas para gerir os seus servidores do Outline, incluindo:

- Permitir-lhe selecionar a conta de faturação correta
- Criar um novo projeto para organizar os seus servidores do Outline
- Indicar os centros de dados disponíveis
- Criar novas máquinas virtuais para executar o Outline
- Configurar a nova máquina virtual com o Outline

## Revogar autorizações

Pode revogar o acesso à Google Cloud Platform para o Gestor Outline ao visitar [A minha conta](https://myaccount.google.com/permissions). Se revogar o acesso, todos os servidores que criou com a configuração automática permanecerão em execução, mas deixarão de ser apresentados no Gestor Outline. Para restaurar o acesso aos mesmos, basta ligar-se novamente à Google Cloud Platform ao iniciar o fluxo de configuração automática.

## Organização de um projeto do Outline

A configuração automática do Google Cloud utiliza um único [projeto do Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects) para organizar os seus servidores do Outline. O projeto é criado durante a primeira utilização da configuração automática, com um ID do projeto sugerido que começa por "Outline" seguido de uma string de carateres aleatórios. Se preferir, pode escolher um ID do projeto diferente no momento da criação. O projeto terá o nome "Servidores do Outline".

## Conta de faturação

Os projetos do Google Cloud requerem uma "conta de faturação" associada que define as informações de pagamento. Quando utilizar a configuração automática do Google Cloud pela primeira vez, ser-lhe-á pedido que forneça uma conta de faturação para associar aos seus servidores do Outline. Por vezes, um servidor deixa de funcionar porque existe um problema com a conta de faturação. Neste caso, deve iniciar sessão na [Google Cloud Console](https://console.cloud.google.com/getting-started), localizar o projeto do Google Cloud associado ao Outline (denominado "Servidores do Outline") e atualizar as definições de faturação.

## Destruir servidores

Se quiser destruir os servidores criados através da configuração automática, a forma mais fácil de o fazer é a partir do Gestor Outline. No entanto, se pretender destruir pessoalmente os servidores, pode iniciar sessão na [Google Cloud Console](https://console.cloud.google.com/getting-started), localizar o projeto criado durante a configuração inicial (denominado "Servidores do Outline") e eliminar os recursos aí presentes ou encerrar o projeto.

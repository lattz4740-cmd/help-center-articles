---
title: "Configuração automatizada do Google Cloud"
sidebar_label: "Configuração automatizada do Google Cloud"
---

## Visão geral

O Outline Manager inclui um recurso que permite configurar automaticamente o servidor do Outline em um servidor em execução no Google Cloud. Se você usar esse recurso, o Outline Manager pedirá que faça login com sua Conta do Google, o que concederá determinadas permissões [OAuth](https://developers.google.com/identity/protocols/oauth2) à instalação local do Outline Manager para configurar sua conta do Google Cloud.

Se não quiser conceder essas permissões, siga as instruções de configuração avançada no Outline Manager para executar o Outline no Google Cloud Platform.

## Permissões concedidas

Para fornecer a configuração automatizada, o Outline Manager precisa das seguintes permissões da sua Conta do Google.

## Google Cloud Platform

- Ver e gerenciar seus recursos do Google Compute Engine
- Ver seus dados nos serviços do Google Cloud e o endereço de e-mail da sua Conta do Google

## Informações básicas da conta

- Ver o endereço de e-mail principal da sua Conta do Google
- Associar suas informações pessoais a você no Google

## Acesso adicional

- Gerenciar seus projetos do Cloud Platform
- Ver e gerenciar suas contas de faturamento do Google Cloud Platform
- Gerenciar a configuração do serviço da Google API

Com essas permissões, conseguimos oferecer funções avançadas para o gerenciamento dos seus servidores do Outline, incluindo os seguintes recursos:

- Permitir que você selecione a conta de faturamento correta
- Criar um novo projeto para organizar seus servidores do Outline
- Listar os data centers disponíveis
- Criar novas máquinas virtuais para executar o Outline
- Configurar a nova máquina virtual com o Outline

## Revogar permissões

Para revogar o acesso do Outline Manager ao Google Cloud Platform, acesse [Minha conta](https://myaccount.google.com/permissions). Se você fizer isso, os servidores criados com a configuração automatizada vão continuar em execução, mas não serão mais exibidos no Outline Manager. Para restaurar o acesso, inicie o fluxo de configuração automatizada para se reconectar ao Google Cloud Platform.

## Organização do projeto do Outline

A configuração automatizada do Google Cloud usa um único [projeto do Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects) para organizar os servidores do Outline. O projeto é criado durante o primeiro uso da configuração automatizada, com um ID sugerido que começa com "Outline-" seguido por uma string de caracteres aleatórios. Se preferir, você pode escolher outro ID para o projeto durante a criação. Ele será nomeado como "Servidores do Outline".

## Conta de faturamento

Os projetos do Google Cloud precisam de uma "conta de faturamento" vinculada que defina as informações de pagamento. Ao usar a configuração automatizada do Google Cloud pela primeira vez, será solicitado que você informe uma conta de faturamento para associar aos seus servidores do Outline. Às vezes, um servidor para de funcionar porque há um problema com a conta de faturamento. Nesse caso, faça login no [Console do Google Cloud](https://console.cloud.google.com/getting-started), encontre o projeto do Google Cloud associado ao Outline (chamado de "Servidores do Outline") e atualize as configurações de faturamento.

## Destruir servidores

Se quiser destruir os servidores criados com a configuração automatizada, a forma mais fácil de fazer isso é no Outline Manager. No entanto, se quiser destruir os servidores por conta própria, faça login no [Console do Google Cloud](https://console.cloud.google.com/getting-started), encontre o projeto criado durante a configuração inicial (chamado de "Servidores do Outline") e exclua os recursos dele ou encerre o projeto.

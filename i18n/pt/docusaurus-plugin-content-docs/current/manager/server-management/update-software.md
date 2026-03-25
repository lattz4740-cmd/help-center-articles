---
title: "Como posso atualizar o software do servidor do Outline?"
sidebar_label: "Como posso atualizar o software do servidor do Outline?"
---

Os servidores do Outline são atualizados automaticamente com as últimas melhorias de segurança, de forma a usar sempre a tecnologia Outline mais recente. O processo de atualização automática é ativado através do [Watchtower](https://github.com/containrrr/watchtower), uma biblioteca de código aberto que verifica e atualiza regularmente a imagem Docker que contém o software Outline.

Além disso, quando instala o Outline através do Gestor Outline, configuramos uma tarefa cron para atualizar automaticamente o software do servidor através de [atualizações automáticas](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) e reiniciá-lo quando necessário. Tenha em atenção que isto não acontece no Modo avançado para preservar a configuração existente, assumindo que o anfitrião está a ser usado para outras finalidades além da execução do Outline.

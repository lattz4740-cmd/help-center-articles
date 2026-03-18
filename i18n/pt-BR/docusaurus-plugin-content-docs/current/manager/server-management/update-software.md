---
title: "Como faço para atualizar o software servidor do Outline?"
sidebar_label: "Como faço para atualizar o software servidor do Outline?"
---

Os servidores do Outline são atualizados automaticamente com as melhorias de segurança mais recentes para você sempre executar a tecnologia mais atual. O processo de atualização automatizado é realizado pela [Watchtower](https://github.com/v2tec/watchtower), uma biblioteca de código aberto que verifica e atualiza com frequência a imagem Docker que contém o Outline.

Além disso, quando você instala o software usando o Outline Manager, configuramos um cron job para fazer automaticamente o upgrade do software no servidor com [Upgrades autônomos](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) e reinicializar esse software quando necessário. Isso não ocorre no Modo avançado para preservar a configuração atual, supondo que o host esteja sendo usado para outras finalidades além de executar o Outline.

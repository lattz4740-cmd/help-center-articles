---
title: "¿Cómo actualizo el software de mi servidor de Outline?"
sidebar_label: "¿Cómo actualizo el software de mi servidor de Outline?"
---

Los servidores de Outline se actualizan automáticamente con las mejoras de seguridad más recientes para que siempre ejecutes la tecnología de Outline más reciente. El proceso de actualización automatizado se habilita a través de [Watchtower](https://github.com/v2tec/watchtower), una biblioteca de código abierto que verifica y actualiza con regularidad la imagen de Docker que contiene el software de Outline.

Asimismo, cuando instales Outline por medio de Outline Manager, configuraremos un trabajo cron para actualizar automáticamente el software del servidor con las [actualizaciones sin supervisión](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) y reiniciarlo cuando sea necesario. Ten en cuenta que esto no ocurre en el Modo avanzado para preservar la configuración existente, según la premisa de que el host se usa para otros propósitos además de ejecutar Outline.

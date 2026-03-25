---
title: "¿Cómo puedo actualizar el software del servidor de Outline?"
sidebar_label: "¿Cómo puedo actualizar el software del servidor de Outline?"
---

Los servidores de Outline se actualizan automáticamente con las últimas mejoras de seguridad, de forma que siempre dispongas de la tecnología más reciente del software. Estas actualizaciones automáticas se llevan a cabo mediante [Watchtower](https://github.com/containrrr/watchtower), una biblioteca de código abierto que consulta y actualiza periódicamente la imagen Docker que contiene el software Outline.

Además, cuando instales el software con el Administrador de Outline, configuraremos una tarea cron para que se actualice automáticamente el software en el servidor usando las [actualizaciones automáticas](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) y se reinicie cuando sea necesario. Esto no sucede en el modo avanzado para preservar la configuración actual, suponiendo que el host se use para otros fines aparte de ejecutar Outline.

---
title: Instala el cliente de Outline en Linux
sidebar_label: Instala el cliente de Outline en Linux
---

A partir de la versión 1.15 del cliente de Outline, todas las versiones futuras se lanzarán como paquetes Debian para sistemas operativos Linux. Consulta nuestros [requisitos mínimos del sistema](/client/getting-started/system-requirements) para obtener más información sobre los sistemas operativos compatibles.

## Cómo instalar el cliente de Outline para distribuciones de Linux basadas en Debian (recomendado)

Ejecuta los siguientes comandos:

1. Instala la clave del repositorio de Outline y agrégalo.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Actualiza la lista de paquetes apt e instala la versión más reciente del cliente de Outline.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Para buscar o instalar actualizaciones futuras, vuelve a ejecutar los comandos del paso 2. Ten en cuenta que, a partir de la versión 1.15, la actualización automática en la app está inhabilitada para el cliente de Outline en Linux.

Para desinstalar el cliente de Outline, ejecuta el siguiente comando:

```
sudo apt purge outline-client
```

## Alternativa

1. Descarga el paquete Debian más reciente del cliente de Outline desde [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb).
2. Ejecuta lo siguiente en la línea de comandos para instalar el paquete.
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Busca actualizaciones de forma manual, ya que, a partir de la versión 1.15, la actualización automática en la app está inhabilitada para el cliente de Outline en Linux.
4. Para desinstalar el cliente de Outline, ejecuta lo siguiente en la línea de comandos:
   ```
   sudo apt purge outline-client
   ```

---
title: Instalar o cliente de Outline en Linux
sidebar_label: Instalar o cliente de Outline en Linux
---

As versións 1.15 e posteriores do cliente de Outline lanzaranse como paquetes Debian para os sistemas operativos Linux. Se necesitas máis información sobre os sistemas operativos compatibles, bótalles unha ollada aos [requisitos mínimos do sistema](/client/getting-started/system-requirements).

## Instalar o cliente de Outline para distribucións de Linux baseadas en Debian (opción recomendada)

Executa os seguintes comandos:

1. Engade o almacén de Outline despois de instalar a súa clave.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```

2. Actualiza a lista de paquetes apt e instala a versión máis recente do cliente de Outline.

```
sudo apt update
sudo apt install outline-client
```

Para comprobar se hai actualizacións ou instalalas no futuro, volve executar os comandos do paso 2. Ten presente que, a partir da versión 1.15, a opción de actualización automática na aplicación está desactivada para o cliente de Outline en Linux.

Para desinstalar o cliente de Outline, executa o seguinte comando:

```
sudo apt purge outline-client
```

## Opción alternativa

1. Descarga a versión máis recente do paquete Debian do cliente de Outline en [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Para instalalo, executa na liña correspondente os comandos que se indican a continuación:

```
wget -O ./outline-client.deb https://s3.amazonaws.com/outline-      releases/client/linux/stable/outline-client_amd64.deb
sudo apt install ./outline-client.deb
```

3. Busca as actualizacións manualmente, xa que a opción automática da aplicación está desactivada para o cliente de Outline en Linux a partir das versións 1.15 e posteriores.

4. Para desinstalar o cliente de Outline, executa o seguinte comando na liña de comandos:

```
sudo apt purge outline-client
```

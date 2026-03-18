---
title: Instalar o cliente Outline no Linux
sidebar_label: Instalar o cliente Outline no Linux
---

A partir da versão 1.15 do cliente Outline, todas as versões futuras vão ser lançadas como pacotes Debian para sistemas operativos Linux. Consulte os nossos [requisitos mínimos de sistema](/client/getting-started/system-requirements) para ver mais informações sobre os sistemas operativos compatíveis.

## Instale o cliente Outline para distribuições Linux baseadas em Debian (recomendado)

Execute os seguintes comandos:

1. Instale a chave do repositório do Outline e adicione o repositório.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Atualize a lista de pacotes apt e instale a versão mais recente do cliente Outline.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Para verificar ou instalar atualizações futuras, execute novamente os comandos no passo 2. Tenha em atenção que a atualização automática na app está desativada para o cliente Outline no Linux, a partir da versão 1.15.

Para desinstalar o cliente Outline, execute o seguinte comando:

```
sudo apt purge outline-client
```

## Opção alternativa

1. Transfira o pacote Debian do cliente Outline mais recente a partir de [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Execute os seguintes comandos na linha de comandos para instalar o pacote
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Verifique se existem atualizações manualmente, uma vez que a atualização automática na app está desativada para o cliente Outline no Linux, a partir da versão 1.15.
4. Para desinstalar o cliente Outline, execute o seguinte comando na linha de comandos:
   ```
   sudo apt purge outline-client
   ```

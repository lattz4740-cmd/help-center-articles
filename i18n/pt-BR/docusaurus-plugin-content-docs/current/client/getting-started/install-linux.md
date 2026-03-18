---
title: Instalar o app cliente do Outline no Linux
sidebar_label: Instalar o app cliente do Outline no Linux
---

A partir da versão 1.15, todas as versões do app cliente do Outline serão lançadas como pacotes Debian para sistemas operacionais Linux. Consulte os [requisitos do sistema](/client/getting-started/system-requirements) para saber quais sistemas operacionais são compatíveis.

## Instalar o app cliente do Outline para distribuições Linux baseadas em Debian (recomendado)

Execute os comandos a seguir:

1. Instale a chave do repositório do Outline e adicione o repositório.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Atualize a lista de pacotes do apt e instale a versão mais recente do app cliente do Outline.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

No futuro, para instalar ou verificar se há atualizações, execute outra vez os comandos na etapa 2. A partir da versão 1.15, a atualização automática no app está desativada para o app cliente do Outline no Linux.

Para desinstalar o app cliente do Outline, execute o comando a seguir:

```
sudo apt purge outline-client
```

## Solução alternativa

1. Faça o download do pacote Debian mais recente do app do cliente do Outline em [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Para instalar o pacote, execute estes comandos na linha de comando.
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. A partir da versão 1.15, as atualizações automáticas no app cliente do Outline no Linux foram desativadas. Por isso, você precisa verificar manualmente se há alguma atualização disponível.
4. Para desinstalar o app cliente do Outline, execute este comando na linha de comando:
   ```
   sudo apt purge outline-client
   ```

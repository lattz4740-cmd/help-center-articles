---
title: Como o Outline funciona
sidebar_label: Como o Outline funciona
---

### Instalação do servidor

A instalação do Outline pode parecer simples, mas há um conjunto complexo de etapas ocorrendo nos bastidores para isso.

Sempre que o Outline é instalado, um script de instalação executa as seguintes etapas:

- A versão estável da imagem do Shadowbox é recuperada e importada com o Docker. A imagem é hospedada no [Quay.io](/about/how-outline-works), em [https://quay.io/repository/outline/shadowbox?tab=tags](/about/how-outline-works). Ela contém o servidor do Outline e a API Management, que depois é usada pelo aplicativo Outline Server Management para criar e remover as chaves de acesso, aceitar/recusar a geração de relatórios de métricas anônimas etc.
- A [Watchtower](/about/how-outline-works) é instalada e configurada, verificando se há as atualizações de imagem a cada hora. Assim, os servidores do Outline são constantemente atualizados com os recursos e as melhorias de segurança mais recentes.
- Um servidor da Web usado para acessar a API Management é iniciado em uma porta aleatória, em um caminho secreto e aleatório.
- Um [certificado SSL autoassinado](/about/how-outline-works) é criado para o gerenciamento do servidor do Outline ser criptografado com TLS, mesmo que não haja um nome de domínio. Uma impressão digital exclusiva desse certificado também é gerada e armazenada no aplicativo Outline Manager, evitando ataques MITM.

Após a instalação do Outline, nenhuma configuração é necessária.

### Segurança do servidor

Como o software Outline é de código aberto, qualquer pessoa pode vê-lo e melhorá-lo se vulnerabilidades forem descobertas. Nosso código está hospedado na plataforma

.

Além disso, todos os servidores do Outline instalados são atualizados automaticamente sempre que uma nova versão é lançada, garantindo que nenhum deles use versões antigas do software.

Para gerenciar as chaves de acesso no servidor, o aplicativo Outline Manager interage com um Serviço de gerenciamento no servidor do Outline. Esse serviço é executado em uma porta aleatória e em um caminho secreto e exclusivo. O próprio Serviço de gerenciamento está se mostrando resistente, porque não responde a consultas, a menos que o caminho secreto apropriado seja especificado. Por fim, toda a comunicação com o Serviço de gerenciamento é criptografada com um

.

Além disso, o servidor do Outline não armazena registros, portanto, mesmo se ele fosse comprometido, nenhum dado do usuário seria divulgado.

.

O Outline foi auditado pela

e a

em 2018. Veja os

.

### Processar o tráfego UDP

O Outline funciona como uma VPN geral do sistema, ou seja, são criados túneis para todo o tráfego UDP pelo servidor do Outline.

### Tráfego DNS

O Outline faz as buscas DNS pelo servidor do Outline e as protege com a mesma criptografia usada para outras atividades da rede. Suas consultas DNS passarão pelo servidor Outline até o Dyn Internet Guide ou o OpenDNS.

O Outline nunca registra suas buscas DNS.

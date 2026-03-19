---
title: Coleta de dados e informações
sidebar_label: Coleta de dados e informações
---

O Outline não coleta informações pessoais, a menos que você permita, nem armazena dados sobre os sites que você acessa, as pessoas com quem se comunica e o conteúdo dessas comunicações.

 Quando você cria uma conta ou faz login com um provedor de nuvem de terceiro pelo Outline Manager, não recebemos as informações fornecidas, como seu endereço de e-mail, nome, informações de faturamento e detalhes de pagamento.

## Informações que recebemos automaticamente
 Coletamos dois tipos de informação automaticamente.

 1. IP do servidor

 O IP do servidor do Outline é coletado pelo [Quay.io](https://quay.io/) e disponibilizado para nós quando o servidor é atualizado automaticamente com as melhorias de segurança e os recursos mais recentes. Ele identifica o provedor do servidor na nuvem e a cidade em que o servidor do Outline foi configurado, mas ele não tem informações sobre quem usa ou acessa a máquina.

 2. Informações técnicas que não são de identificação pessoal

 Se ocorrer uma falha ou exceção fatal no Outline, ou se você enviar feedback manualmente pelo app Outline, as informações abaixo serão relatadas. Elas serão usadas apenas para identificar e corrigir problemas de estabilidade ou desempenho.

- País
- Localidade
- Data e hora da falha/exceção e até cem eventos anteriores como, por exemplo, quando o usuário abre a seção "Sobre"
- Mensagens de exceção compiladas estaticamente
- Nome e versão do SO
- Modelo do smartphone (se houver)
- Horário de início do app
- Navegador
- Arquitetura
- Versão e número de compilação do Outline

Essas informações são transferidas por HTTPS para o Sentry ([sentry.io](https://sentry.io/)), um provedor de rastreamento de erros de código aberto de terceiros. Ele usa várias tecnologias e serviços padrão do setor para proteger seus dados contra operações não autorizadas, como acesso, divulgação, uso e perda. Se você tiver dúvidas sobre as políticas do Sentry, acesse [https://sentry.io/security/](https://sentry.io/security/) e [https://sentry.io/privacy/](https://sentry.io/privacy/)ou entre em contato pelo e-mail [security@sentry.io](mailto:security@sentry.io). Os dados do Outline armazenados pelo Sentry são restritos, ou seja, só os membros da equipe do Outline podem acessá-los.

## Informações que recebemos somente com permissão
 A equipe do Outline recebe as seguintes informações sob permissão.

 1. Métricas de uso

 Cada servidor do Outline coleta automaticamente, na última hora e por chave de acesso a quantidade de tempo em que um usuário ficou conectado, os países e sistemas autônomos de origem das credenciais usadas e se algum recurso foi ativado ou desativado. O conteúdo da comunicação e os metadados de identificação pessoal (por exemplo, logins, e-mails, IDs dos dispositivos etc.) não são registrados. As métricas estão vinculadas a um código do servidor. Veja as instruções para [alterar o ID do servidor](/manager/server-management/reset-server-id).

 Por padrão, os servidores do Outline não compartilham essas métricas com a equipe. Se o administrador do servidor aceitar explicitamente compartilhar as métricas de uso, elas serão enviadas com segurança à equipe do Outline a cada hora. Após 60 dias, elas serão agregadas ao nível do país. Os administradores de servidores podem alterar as preferências de compartilhamento das métricas de uso a qualquer momento no menu "Configurações" do Outline Manager.

 O compartilhamento de métricas anônimas sobre o uso do servidor é útil para medirmos tendências de utilização e melhorarmos o produto.

 Por exemplo, se o administrador do servidor aceitar compartilhar métricas de uso, poderemos receber informações indicando que um servidor com o código 12345 foi usado por três horas no dia anterior, transferindo um total de 500 megabytes de dados de três chaves usadas nos Estados Unidos e no Canadá, com o recurso de limites de dados ativado.

 2. Seus comentários e e-mails se você enviar feedback

 Você pode enviar feedback para a equipe com os apps Outline Manager e Outline. Recomendamos não incluir informações de identificação pessoal, mas há a opção de preencher o campo de e-mail se quiser receber uma resposta da equipe. Também coletamos automaticamente algumas informações básicas para entender seu feedback. Veja o item 2 acima, em “Informações que recebemos automaticamente”, para saber quais são esses dados. Saiba mais sobre as [práticas de segurança e privacidade](/about/security-and-privacy) do Outline.

 Se você estiver usando uma versão Beta do app Outline no Android, poderemos usar o serviço [Firebase](https://firebase.google.com/) do Google para coletar informações de depuração que nos ajudam a detectar problemas e melhorar o Outline. Saiba mais sobre as políticas de privacidade e segurança do Firebase no site [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Se você não quiser que o Outline envie essas informações pelo Firebase, use a versão de produção do app.

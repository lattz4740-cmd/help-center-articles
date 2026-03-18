---
title: Erros de firewall
sidebar_label: Erros de firewall
---

Existem três tipos de problemas de firewall que pode encontrar:

## A sua ligação pode estar bloqueada por uma firewall de rede.

Se estiver a tentar instalar o Outline enquanto tem uma ligação estabelecida a uma rede com firewall, como na escola ou no local de trabalho, experimente instalar o Outline numa rede diferente.

Se isto não funcionar, contacte o administrador da rede para permitir ligações entre a rede com firewall e o servidor do Outline. Tem de conhecer o endereço IP do servidor do Outline e as portas em que o Outline está a ser executado, que estão indicadas no final do script de instalação.

**A sua ligação pode estar bloqueada por uma firewall de dispositivo**.

Se tiver software no seu dispositivo que bloqueie ligações de saída em portas não padrão ou bloqueie software não reconhecido (ZoneAlarm da CheckPoint), consulte a documentação do dispositivo ou software para saber como criar uma exceção para o Outline.

## A sua ligação pode estar bloqueada por uma firewall de servidor.

O fornecedor de nuvem que escolheu pode exigir que crie manualmente exceções para a firewall do servidor para abrir as portas em que o Outline está a ser executado. Depois de executar o script de instalação, devem ser apresentadas duas portas selecionadas aleatoriamente nas quais o Outline está a ser executado no seu servidor. Abrir estas duas portas deve ser suficiente.

 Para criar exceções para a sua firewall de servidor, recomendamos que consulte a documentação sobre "ufw" e "iptables":

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

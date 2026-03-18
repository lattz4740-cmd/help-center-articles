---
title: Shromažďování dat a informací
sidebar_label: Shromažďování dat a informací
---

Outline neshromažďuje osobní údaje, pokud se výslovně nerozhodnete je poskytovat. Neshromažďuje ani informace o webech, které navštívíte, nebo o tom, s kým a o čem komunikujete.

 Pokud si přes Správce Outline vytvoříte účet u externího poskytovatele cloudu nebo se do takového účtu přihlašujete, nezískáme žádné údaje, které svému poskytovateli sdělujete. Jedná se o informace, jako je vaše e‑mailová adresa, jméno, fakturační údaje nebo údaje o platbě.

****Informace, které získáváme automaticky****

 Dva typy informací shromažďujeme automaticky.

 1. IP adresa serveru

 IP serveru Outline shromažďuje služba [Quay.io](http://quay.io/) a my k ní máme přístup, když se server automaticky aktualizuje, aby využíval nejnovější zabezpečení a vylepšení funkcí. IP adresa serveru může identifikovat poskytovatele cloudového serveru a město, kde byl server Outline nastaven, ale neukazuje, kdo server provozuje a kdo k němu získává přístup.

 2. Technické informace, které vás osobně neidentifikují

 Pokud Outline selže nebo dojde k fatální výjimce a v případě, že v aplikaci Outline ručně pošlete zpětnou vazbu, budou nahlášeny údaje uvedené níže. Ty slouží výhradně k identifikaci a opravě problémů se stabilitou a výkonem. Jedná se o tyto informace:

- země,
- národní prostředí,
- datum a čas selhání/výjimky a až 100 předchozích událostí (například že uživatel otevřel sekci O aplikaci),
- staticky shromážděné zprávy o výjimkách,
- název a verze operačního systému,
- model telefonu (pokud je dostupný),
- čas spuštění aplikace,
- prohlížeč,
- architektura,
- verze a číslo sestavení aplikace Outline.

Tyto informace jsou přenášeny pomocí protokolu HTTPS do služby Sentry ([sentry.io](http://sentry.io/)), což je externí opensourcová služba pro sledování chyb. Sentry chrání vaše data před neautorizovaným přístupem, zveřejněním, použitím a ztrátou. Využívá k tomu celou škálu technologií a služeb splňujících oborové standardy. Pokud máte nějaké otázky ohledně zásad služby Sentry, navštivte stránky [https://sentry.io/security/](https://sentry.io/security/) a [https://sentry.io/privacy/](https://sentry.io/privacy/), případně se obraťte e‑mailem na adresu [security@sentry.io](mailto:security@sentry.io). Přístup ke všem datům z aplikace Outline uloženým službou Sentry je omezený tak, že je můžou zobrazit jen členové týmu Outline.

****Informace, které získáváme jen s vaším výslovným souhlasem****

 Pokud to schválíte, aplikace Outline předává týmu Outline tyto informace.

 1. Metriky využití

 Každý server Outline automaticky shromažďuje množství přenesených bajtů (za poslední hodinu) a dobu, po kterou byl uživatel připojen k serveru, země a autonomní systémy původu použitých přihlašovacích údajů (na základě přístupového klíče) a dále to, zda byly aktivovány nebo deaktivovány nějaké funkce. Neukládá se ani obsah komunikace, ani žádná metadata, která vás můžou osobně identifikovat (například přihlášení, e‑mailové adresy, ID zařízení atd.). Všechny metriky jsou spojené s identifikátorem serveru. Pokyny ke změně ID serveru najdete [tady](/manager/server-management/reset-server-id).

 Ve výchozím nastavení servery Outline tyto metriky s týmem Outline nesdílejí. Pokud se správce serveru výslovně přihlásí ke sdílení metrik využití, budou tyto informace týmu Outline bezpečně odesílány každou hodinu. Po 60 dnech se metriky využití shrnou na úroveň země. Správce serveru může nastavení sdílení metrik kdykoli změnit v nabídce Nastavení ve Správci Outline.

 Oceňujeme, pokud s námi anonymní metriky o využití serveru sdílíte. Používáme je totiž k měření trendů využívání a ke zlepšování služby.

 Pokud se správce serveru přihlásí ke sdílení metrik využití, můžeme například obdržet informace, že server s ID 12345 se včera používal tři hodiny a přenesl dohromady 500 MB dat ze tří klíčů, z nichž každý byl použit v USA a Kanadě, s aktivovanou funkcí datového limitu.

 2. Vaše komentáře a e-mailovou adresu, když nám pošlete zpětnou vazbu

 Správce Outline a Aplikace Outline vám umožňují poslat týmu zpětnou vazbu. Doporučujeme vám do ní nezahrnovat údaje, které by vás osobně identifikovaly, ale můžete vyplnit e-mailovou adresu, pokud chcete od týmu dostat odpověď. Zároveň automaticky shromažďujeme některé základní informace, abychom vaší zpětné vazbě lépe porozuměli. Jaká data shromažďujeme, se dozvíte výše v 2. části sekce Informace, které získáváme automaticky. Další informace o zásadách zabezpečení a postupech v oblasti ochrany soukromí aplikace Outline najdete [tady](/about/security-and-privacy).

 Pokud používáte beta verzi aplikace Outline v Androidu, můžeme pomocí služby [Firebase](https://firebase.google.com/) od Googlu shromažďovat informace pro ladění, které nám pomáhají odhalovat problémy a vylepšovat Outline. Další informace o zásadách ochrany soukromí a zabezpečení služby Firebase najdete na jejím webu: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy). Pokud nechcete, aby aplikace Outline tyto informace přes službu Firebase posílala, používejte běžnou verzi aplikace.

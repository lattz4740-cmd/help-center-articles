---
title: "Jak nastavím u přístupových klíčů datové limity?"
sidebar_label: "Jak nastavím u přístupových klíčů datové limity?"
---

Můžete nastavit datový limit platný pro všechny přístupové klíče. Pokud to chcete udělat, otevřete Správce Outline a přejděte do nastavení. Tam najdete přepínač Datové limity, který můžete zapnout. Pak nastavíte požadovaný limit.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

Jakmile limit nastavíte, uvidíte, nakolik se mu jednotliví uživatelé přiblížili. Tyto informace najdete na stránce s přístupovým klíčem, kde pruhový graf ukazuje využití dat za posledních 30 dní.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Vedle možnosti nastavit limit pro všechny přístupové klíče můžete taky každému klíči přidělit vlastní datový limit. Toto nastavení přepíše výchozí datový limit, který jste případně určili. Pokud jste výchozí limit nenastavili, můžete pořád nastavit datový limit pro kterýkoli z klíčů. 

 Pokud chcete nastavit limit klíče pro přenos dat, otevřete Správce Outline, přejděte na kartu Připojení, která obsahuje požadovaný klíč, a klikněte na nabídku v pravé části řádky klíče. Z nabídky vyberte možnost Datový limit. Datový limit pro daný přístupový klíč změníte po kliknutí na ikonu Datové limity ![Tento obrázek není k dispozici, protože nemáte oprávnění ho zobrazit nebo byl ze systému odstraněn](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw).

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Vyberte možnost „Nastavit vlastní datový limit“. Když toto políčko zaškrtnete, zobrazí se pole, kde můžete určit limit pro daný klíč. Až všechno nastavíte, kliknutím na tlačítko ULOŽIT datový limit uložte.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Jakmile limit pro přenos dat pro vybraný klíč uložíte, zobrazí se na hlavní obrazovce spolu s využitím dat (za posledních 30 dní).

Pokud chcete datový limit z přístupového klíče odebrat, podle pokynů výše přejděte do dialogového okna Datový limit, zrušte zaškrtnutí políčka „Nastavit vlastní datový limit“ a klikněte na tlačítko ULOŽIT.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

****Časté dotazy k datovému limitu****

****Co je 30denní klouzavý limit?****

 Třicetidenní klouzavý limit sčítá využití dat u jednotlivých klíčů za posledních 30 dnů a udržuje využití klíče za toto období pod limitem. Výsledkem je, že klíč během žádného období 30 dnů (včetně kalendářních měsíců se 30 a méně dny) nemůže překročit limit. Vlastně to znamená, že se dostupná data každého uživatele každý den zvýší o množství, které využil před 31 dny.

**Proč se v Outline používají klouzavé limity?**

 Klouzavé limity poskytují záruku pro každé 30denní období. Jsou tak jednodušší na konfiguraci než opakující se limit (například vybraný den v měsíci), a přitom poskytují obdobné záruky. Navíc odpovídají stávajícímu zobrazení využívání dat v Outline i v běžných nástrojích, jako jsou analytické služby nebo statistiky serverů.

**Jaká data se do datového limitu započítávají?**

 Zaznamenává se každý výchozí přenos přístupového klíče ze serveru. Přísně vzato to znamená, že jde o data odeslaná na základě klíče ze serveru i zpět do klienta. V praxi by se to mělo velmi blížit provozu odesílanému z klíče na server a zpět, proto doufáme, že to bude odpovídat záznamům vašich uživatelů. Zvolili jsme výchozí přenos, protože podle těch účtují poskytovatelé cloudových služeb, mezi kterými jsme provedli průzkum.

**Dostanou uživatelé upozornění, když vyčerpají limit?**

 V tuto chvíli ne. Řada poskytovatelů cloudových služeb nabízí limit například 1 TB na celý měsíc, který může čerpat 10 uživatelů po 100 GB nebo 100 uživatelů po 10 GB. To jsou celkem velké objemy a neočekáváme, že jich mnoho uživatelů dosáhne. Doufáme, že se uživatelé v případě dosažení limitu obrátí na správce serverů. Oceníme nicméně vaše postřehy, jak by vám upozornění ve vašem konkrétním případě pomohla. Můžete se s námi spojit [tady](/about/feedback).

**Dostanou uživatelé upozornění, když se budou blížit vyčerpání limitu?**

 Množství nových dat, které uživatel blížící se limitu dostane k dispozici, se bude den ode dne lišit, protože vychází z jeho využití před 30 dny. Myslíme si, že takové varování by koncovým uživatelům příliš nepomohlo a spíše by je mátlo. Oceníme ale vaši zpětnou vazbu k tomuto chování, kterou nám můžete poslat [tady](/about/feedback).

**Můžu konkrétnímu uživateli resetovat využití dat?**

 Ne, limit uživatele vždy zahrnuje využití dat za posledních 30 dní. Můžete ale zvýšit datový limit klíče nebo pro uživatele vytvořit nový klíč.

**Proč po aktivaci datových limitů někteří z našich uživatelů okamžitě přišli o přístup?**

 Datové limity vycházejí z přenosů dat u uživatele za posledních 30 dní. Ty se přitom sledují bez ohledu na to, jestli jsou zapnuté datové limity. Je tak možné, že někteří uživatelé datový limit překročili ještě před jeho zavedením. Připomínáme také, že jsou vynucovány všechny datové limity, i když třeba změníte limit jediného klíče.

**Mohu nastavit limit na úrovni serveru, například 1 TB na 30 dní?**

 Momentálně ne. Rádi bychom se o vašem konkrétním scénáři dozvěděli víc. Napište nám [sem](/about/feedback).

**Pokud existuje výchozí datový limit a limit pro určitý klíč, který z nich se bude uplatňovat?**

 Limit pro konkrétní klíč přepíše případný výchozí datový limit, který jste nastavili.

**Můžu nastavit datový limit pro konkrétní klíč, když nemám nastavený výchozí datový limit?**

 Ano. K nastavení datového limitu pro jeden klíč není nutné definovat výchozí limit. Můžete například nastavit limit pro jeden klíč, o kterém předpokládáte, že se bude intenzivně sdílet, a chránit se tak pro případ rozsáhlých přenosů dat přes tento klíč.

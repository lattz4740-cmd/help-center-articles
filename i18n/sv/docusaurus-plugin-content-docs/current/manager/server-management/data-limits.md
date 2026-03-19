---
title: "Hur ställer jag in datagränser för åtkomstnycklar?"
sidebar_label: "Hur ställer jag in datagränser för åtkomstnycklar?"
---

Du kan ställa in en datagräns som gäller för alla åtkomstnycklar. Om du vill ställa in en gräns öppnar du Outline Manager och navigerar till Inställningar. Där finns ett reglage som heter Datagränser. När det är aktiverat kan du ange en gräns.

![Data limits setting in Outline Manager](/images/snippet-15787036.png)

När du har ställt in en gräns kan du se hur nära gränsen varje användare är på sidan för åtkomstnycklar. Där visas ett stapeldiagram med dataanvändningen under de senaste 30 dagarna.

![Outline Manager's Access Key page](/images/snippet-15787037.png)

Du kan antingen ställa in en gräns för alla åtkomstnycklar eller ge varje nyckel en egen datagräns. Den här inställningen åsidosätter datagränser som är angivna som standard. Om du inte har ställt in någon datagräns som standard kan du fortfarande ställa in en datagräns för en nyckel. 

 Du ställer in en dataöverföringsgräns för en nyckel genom att öppna Outline Manager, klicka på den Anslutningar-flik där den nyckel som du vill ställa in finns och sedan klicka på menyn till höger om nyckelns rad. Klicka sedan på Datagräns. Klicka på datagränsikonen ![Ikon för datagränser](https://lh7-us.googleusercontent.com/docsz/AD_4nXc2jByBppEN1yHPjbK2BxNuYxwmfW98eYRyJGiDmg4lSLNLxf5aav2971IntWOfqF8oJ1zhW7RVdaxJVxkdZkpsDeSgnBbJfNisidjKbcRh3FheoVjQNSZHHEgUz155B1_wRjlB2mAIa6Qfs5k7Mg_i6YJhYle80EPoZVkdl09uvBbSxUgfLvPserKL8dSCElVSLcuo7uF232qnTKFKM4gt_f0iDQ?key=oLpwwvDVb_5YbZSyjC9Agw) om du vill ändra datagränsen på Min åtkomstnyckel.

![Selecting the data limit setting icon for an individual access key](/images/snippet-15787423.png)

Markera Ställ in en anpassad datagräns. När du har markerat den här kryssrutan visas ett fält där du kan ställa in en anpassad datagräns för nyckeln. Klicka på knappen SPARA när du är färdig så sparas datagränsen.

![Setting a data limit for an individual access key](/images/snippet-15788959.png)

Gränsen visas på huvudskärmen när du har sparat dataöverföringsgränsen för den valda nyckeln. Här visas även dataanvändning under de senaste 30 dagarna för varje nyckel.

Ta bort datagränsen för en åtkomstnyckel genom att navigera till dialogrutan Datagräns för nyckeln, precis som förut, avmarkera den ruta som heter Ställ in en anpassad datagräns och klicka på knappen SPARA.

![Removing the data limit on an individual access key](/images/snippet-15788414.png)

## Vanliga frågor om datagränser
## Vad innebär en löpande datagräns på 30 dagar?
 En löpande datagräns på 30 dagar innebär att användningen av varje nyckel under de senaste 30 dagarna läggs ihop och begränsas så att användningen under den perioden inte överskrider gränsen. Då går det inte att överskrida gränsen med nyckeln under någon 30-dagarsperiod, även under månader som är 30 dagar eller kortare. Rent praktiskt innebär detta att användarens tillgängliga datamängd ökar för varje dag med samma mängd som användes för 31 dagar sedan.

## Varför används löpande gränser i Outline?
 Med löpande gränser går det att garantera att gränsen inte överskrids under en 30-dagarsperiod. Det gör att de är enklare att konfigurera än regelbundna gränser (till exempel en viss dag i månaden) och ger liknande garantier. De passar även in i den befintliga visningen av dataanvändning i Outline samt i vanliga verktyg för analystjänster och serverstatistik.

## Vilken data räknas in i en datagräns?
 Varje åtkomstnyckels utgående data från servern tas med i sammanräkningen. Detta innebär datan som skickas från servern med hjälp av nyckeln och tillbaka till klienten. I praktiken bör detta överensstämma med trafiken som skickas till och från servern med hjälp av nyckeln, så vi hoppas att datamängden liknar dina användares beräkningar. Vi valde utgående data eftersom det är vad molnleverantörerna som vi har undersökt tar betalt för.

## Meddelas användarna om de överskrider datagränsen?
 Inte just nu. Många molnleverantörer har en gräns, till exempel 1 TB för hela månaden som kan fördelas med 100 GB på 10 användare eller 10 GB på 100 användare. Det är ganska stora mängder och vi tror inte att särskilt många använder så mycket data. Vi hoppas att användare som når sin gräns kontaktar den ansvariga för servern. Vi vill dock gärna veta hur aviseringar kan underlätta användningen för dig. Du kan kontakta oss [här](/about/feedback).

## Meddelas användarna när de närmar sig datagränsen?
 Mängden ny data som en användare får när gränsen närmar sig varierar från dag till dag då den grundar sig på användningen för 30 dagar sedan. Vi tror att det blir förvirrande snarare än användbart för användarna att få en varning. Vi vill gärna ha din feedback om detta [här](/about/feedback).

## Kan jag nollställa en användares dataanvändning?
 Nej, användares gränser bygger alltid på dataanvändningen under de senaste 30 dagarna. Du kan dock höja datagränsen för respektive nyckel eller skapa nya nycklar åt dem.

## Varför förlorade några av användarna åtkomsten när jag aktiverade datagränser?
 Datagränser baseras på användares dataöverföring under de föregående 30 dagarna, vilket registreras vare sig datagränser är igång eller inte. Det kan hända att användarna i fråga har överskridit gränsen redan innan den ställdes in. Tänk också på att alla datagränser tillämpas, även när du ändrar datagränsen för en enda nyckel.

## Går det att ställa in en gräns för hela servern, till exempel 1 TB per 30 dagar?
 Inte just nu. Vi vill gärna veta mer om hur du skulle använda det [här](/about/feedback).

## Vilken datagräns används om det finns en som är standard och en för en specifik nyckel?
 Datagränser för specifika nycklar åsidosätter datagränser som har ställts in som standard (om det finns några).

## Kan jag ställa in en datagräns för en specifik nyckel utan att ha ställt in en standardgräns?
 Ja. Du behöver inte ha ställt in en standardgräns för att kunna ställa in en datagräns för en nyckel. Du kan till exempel att ställa in en gräns för en nyckel som du tror kommer att delas av många och på så sätt undgå allt för hög dataöverföring med den nyckeln.

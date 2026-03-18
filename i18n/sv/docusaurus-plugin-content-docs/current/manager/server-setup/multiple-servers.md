---
title: "Så här konfigurerar du flera Outline-servrar"
sidebar_label: "Så här konfigurerar du flera Outline-servrar"
---

Konfigurera ytterligare Outline-servrar genom att klicka på plustecknet i navigeringspanelen till vänster i Outline Manager-appen. Anvisningarna för att lägga till en ny server är samma som för att installera den första.

- Det finns ingen begränsning för hur många Outline-servrar du kan skapa.
- Det måste finnas en motsvarande virtuell dator för varje Outline-server du skapar.
- Om du skapar ytterligare virtuella datorer eller servrar (s.k. Droplets) kan molnleverantörens avgift öka. Kontrollera prispaketet hos molnleverantören så att du vet vad du kan förvänta dig.

## Skapa ytterligare en Outline-server hos DigitalOcean

När du har klickat på plustecknet och valt att installera servern hos DigitalOcean följer du samma anvisningar som när du konfigurerade den första servern. Eftersom Outline Manager är integrerat med DigitalOcean kan vi dessutom skapa en droplet åt dig utan att du behöver stänga Outline Manager-appen.

Observera att Outline Manager endast har stöd för ett DigitalOcean-konto åt gången. Om du vill lägga till eller skapa andra Outline-servrar från andra DigitalOcean-konton måste du lägga till dem som en avancerad konfiguration.

## Skapa en Outline-server till på GCP, AWS eller en annan leverantör av molntjänster.

Börja med att skapa en ny virtuell dator hos den valda molnleverantören. Öppna sedan Outline Manager och följ anvisningarna för avancerad installation, precis som du kanske gjorde den första gången.

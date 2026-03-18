---
title: "Varför går det inte att installera Outline Client på Windows?"
sidebar_label: "Varför går det inte att installera Outline Client på Windows?"
---

Du kan se felmeddelandet ”Det verkar som att Outline inte har installerats korrekt. Testa att installera det igen. Om det inte fungerar kan du [skicka feedback](https://support.getoutline.org/s/contactsupport?).”

Om du använder Outline på Windows kan det hända att du stöter på ett oväntat fel. I de flesta fall måste Outline TAP-adaptern (drivrutinen) raderas och Outline ominstalleras.

Hur du gör detta varierar beroende på vilken version av Windows operativsystem du använder, men nedan ser du allmänna anvisningar för hur du avinstallerar TAP-adaptern och Outline och sedan ominstallerar Outline.

1. Avinstallera TAP-adaptern för Outline
   - Gå till **Enhetshanterare** och sedan **Nätverkskort**.
   - Leta reda på filen **TAP-Windows Adapter V9** eller den TAP-adapter som är kopplad till Outline.
   - Avinstallera eller radera den här adaptern. Tänk på att det här kan påverka andra VPN-appar som du har installerat.
2. Avinstallera Outline Client
   - Gå till **Program och funktioner** och sedan till **Avinstallera program**.
   - Leta reda på Outline Client-appen och avinstallera Outline Client.
   - [Ladda ned den senaste versionen av Outline Client](https://getoutline.org/get-started/#step-3) och ominstallera den på din Windows-enhet. Den nya installationen ska installera en ny TAP-adapter automatiskt.

Om du fortfarande har problem kan du [kontakta support](https://support.getoutline.org/s/contactsupport?).

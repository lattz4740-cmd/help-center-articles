---
title: Gabimet e murit mbrojtës
sidebar_label: Gabimet e murit mbrojtës
---

Ka tri lloje problemesh të murit mbrojtës që mund të ndeshësh:

## Mund të bllokohesh nga një mur mbrojtës i rrjetit.

Nëse po përpiqesh ta instalosh Outline ndërkohë që je i lidhur me një rrjet me mur mbrojtës, si p.sh. në një shkollë ose në vendin tënd të punës, provo ta instalosh ndërkohë që je në një rrjet tjetër.

Nëse kjo nuk funksionon, kontakto me administratorin e rrjetit për të lejuar lidhjet mes rrjetit me mur mbrojtës dhe serverit tënd të Outline. Do të duhet të dish adresën IP të serverëve të Outline dhe portat ku ekzekutohet Outline, të cilat jepen në skriptin e instalimit.

## Mund të bllokohesh nga një mur mbrojtës i pajisjes.

Nëse ke një softuer në pajisjen tënde që bllokon lidhjet dalëse në portat jostandarde ose një softuer jo të njohur (p.sh. ZoneAlarm nga CheckPoint), këshillohu me dokumentacionin e pajisjes ose softuerit për të mësuar se si të krijosh një përjashtim për Outline.

## Mund të bllokohesh nga një mur mbrojtës i serverit.

Ofruesi i shërbimit të resë kompjuterike që ke zgjedhur mund të kërkojë që të krijosh në mënyrë manuale përjashtime në murin mbrojtës të serverit për të hapur portat në të cilat ekzekutohet Outline. Pasi të kesh ekzekutuar skriptin e instalimit, duhet të të jenë paraqitur dy porta të zgjedhura rastësisht ku ekzekutohet Outline në serverin tënd. Hapja e këtyre dy portave do të jetë e mjaftueshme.

 Për të krijuar përjashtime në murin mbrojtës të serverit tënd, ne rekomandojmë që të shikosh dokumentacionin për "ufw" dhe "iptables":

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

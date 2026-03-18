---
title: "Si të përditësoj softuerin e serverit tim të Outline?"
sidebar_label: "Si të përditësoj softuerin e serverit tim të Outline?"
---

Serverët e Outline përditësohen automatikisht me përmirësimet më të fundit të sigurisë, kështu që je gjithmonë duke përdorur teknologjinë më të fundit të Outline. Procesi i automatizuar i përditësimit mundësohet nga [Watchtower](https://github.com/v2tec/watchtower), një bibliotekë me burim të hapur që kontrollon dhe përditëson rregullisht imazhin e Docker që përmban softuerin e Outline.

Përveç kësaj, kur instalon Outline duke përdorur Outline Manager, ne do të konfigurojmë një detyrë cron për të përditësuar automatikisht softuerin në server duke përdorur [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) dhe për ta rindezur kur është e nevojshme. Ki parasysh se kjo nuk ndodh në "Modalitetin e përparuar" për të ruajtur konfigurimin ekzistues, duke supozuar se pritësi po përdoret edhe për qëllime të tjera përveç ekzekutimit të Outline.

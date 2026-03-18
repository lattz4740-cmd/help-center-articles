---
title: 術語
sidebar_label: 術語
---

## 什麼是 VPN？

虛擬私人網路 (VPN) 是你的裝置和主機伺服器之間的私人連線。使用 VPN 時，你的流量將對網際網路服務供應商隱藏。

以下是 VPN 的用途：

- 在使用公用 Wi-Fi 網路時保護個人資料
- 防止網際網路服務供應商和政府機關取得你的瀏覽資料
- 從全球各種來源取得未經審查的內容

## Outline 與傳統 VPN 有何差異？

網際網路服務供應商可以辨識常見的安全通訊協定和/或流量模式，輕而易舉偵測並封鎖傳統 VPN。相較於傳統 VPN，Outline 更可靠穩定，因為這項服務採用的通訊協定相當難以偵測，所以較不容易受到封鎖。Outline 可防範複雜精密的審查方式，包括網路封鎖或 IP 封鎖。

## 什麼是 Outline 伺服器？

Outline 伺服器會執行 VPN，讓獲得許可的使用者連線。

建立新網路時，可以使用自己的安全伺服器 (如果有的話) 做為 Outline 伺服器，或者選擇下列雲端服務供應商：

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

如要設定伺服器，請在 Outline Manager 中操作。

## 什麼是服務管理員？ {#servicemanager}

服務管理員負責設定 Outline 伺服器及提供存取金鑰給使用者，通常也需要支付伺服器使用費。

## 什麼是存取金鑰？ {#accesskey}

存取金鑰的用途為存取現有 Outline 伺服器及連線至 VPN。你可以向[服務管理員](#servicemanager)索取這類金鑰，也可以自行[設定 Outline 伺服器](/manager/server-setup/setup-server)。

存取金鑰的格式如下 (這個範例金鑰無法正常運作)：

ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

## 什麼是 Outline Manager？

Outline Manager 是電腦應用程式，可讓服務管理員設定 Outline 伺服器、產生[存取金鑰](#accesskey)，以及設定每個金鑰的數據用量上限。如要下載最新版 Outline Manager，請點選[這個連結](https://getoutline.org/get-started/#step-1)或[這個連結](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/)。

## 什麼是 Outline 用戶端？

Outline 用戶端是提供電腦版與行動版的應用程式，可讓你連線至 Outline 伺服器，以及透過存取金鑰使用 VPN。如要下載最新版 Outline 用戶端，請點選[這個連結](https://getoutline.org/get-started/#step-3)或[這個連結](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/)。

## 什麼是數據用量上限？

透過 Outline Manager，服務管理員可以設定存取金鑰的 30 天追蹤數據用量上限，藉此避免使用過多數據，並將費用控制在可預測的範圍內。這類管理員能夠設定每個金鑰套用的預設上限，也能為任何金鑰設定不同上限，覆寫預設上限。設定完成的上限會立即生效，並且每小時強制套用。

如果服務管理員選擇將指標提供給 Jigsaw，應瀏覽[資料收集政策](/about/data-collection)，進一步瞭解數據用量上限使用情形的回報方式。

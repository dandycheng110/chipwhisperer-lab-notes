# 「別人報價 5 萬、我收 299 起」Threads 創業日記貼文：行銷與內容機制拆解（台灣，2025–2026）

> 研究說明（2026-10-19）：這次環境的對外連線政策擋掉了 WebFetch 和 curl（代理對 newtalk、LTN、YouTube、LINE TODAY 等網域回 403，WebFetch 每個網域都 DNS 失敗）。依代理 README 指示沒有繞過。所以下面每一條「Cited Findings」都只取自 WebSearch 回傳的搜尋結果摘要與片段，沒開過原頁逐字核對。摘要若把好幾頁混在一起、分不出出自哪一頁，會標「（歸屬未逐頁確認）」。依指示只蒐集原發文者的公開商業資訊，沒蒐集任何個人資料；最後也沒找到原貼文（見第 5 節）。

---

## 1. Threads 在台灣：用戶規模、演算法獎勵什麼、接案者怎麼從 Threads 拿到客戶

### Takeaway
台灣是 Threads 全球最「重度」的市場之一：Meta 高層點名台灣是前三活躍國家，第三方估計台灣約佔全球流量 21–22%。不過 Meta 沒公布台灣用戶數，「約 350 萬月活」是業界估計，「9,486 萬帳號」已確認是誤算。演算法方面，依第三方整理與 Mosseri 的公開發言，最看重的是「回覆／對話」，也偏好追蹤關係與穩定發文。Threads 在接案生態裡比較像漏斗頂端：曝光和信任在 Threads 建立，成交多半移到私訊或 LINE。

### Cited Findings
**用戶規模與市場地位**
- Threads 一週年亞太媒體活動上，Threads 產品副總裁 Emily Dalton Smith 把印度、日本、台灣列為全球最活躍的前三個國家（說這話的是 Meta 高管，不是 Mosseri）— [VERSE](https://www.verse.com.tw/article/threads-popular-in-taiwan)
- 工商時報產業特刊觀點稿（元智大學管理學院助理教授朱訓麒，2025-10-17）：台灣月活約 350 萬，平均使用時間約為美國的 22 倍；台灣人口不到全球 0.5%，卻貢獻超過 22% 的全球流量。作者認為 Threads 滿足了台灣人「和陌生人自由、真誠對話」的需求，年輕人厭倦影像平台的修圖與人設，想回到文字溝通（數據原始出處未核實）— [中時新聞網／工商時報](https://www.chinatimes.com/newspapers/20251017000194-260210)；[工商時報](https://www.ctee.com.tw/news/20251017700100-439901)
- 搜尋摘要引述 Similarweb 2025 年 3 月數據：台灣流量佔比 22.02%，美國 14.81%（歸屬未逐頁確認）— [風傳媒](https://www.storm.mg/lifestyle/11073329)；[小丰子3C](https://tel3c.tw/blog/post/47475)
- QSearch 2026 年統計：台灣佔 Threads 全球流量 21.08%，排全球第一 — [LINE TODAY 轉載](https://today.line.me/tw/v3/article/nX3ep8K)；[QSearch Blog 2026/03](https://www.qsearch.cc/blog/2026/03/threads-stats-2026-taiwan/)；QSearch 2025 年系列也稱台灣為「Threads 全球第一重鎮」— [QSearch 2025/06](https://www.qsearch.cc/blog/2025/06/taiwan-threads-marketing-decoded-1/)；[QSearch 2025/08](https://www.qsearch.cc/blog/2025/08/threads-analytics-taiwan-market/)
- 較早的報導說台灣流量「佔全球第二」，和上面的「第一」衝突，應該是不同時點的數據 — [UpToGo](https://uptogo.com.tw/%E7%A7%91%E6%8A%80/%E8%BB%9F%E9%AB%94%E5%92%8Capp/%E7%A4%BE%E7%BE%A4%E5%AA%92%E9%AB%94/%E7%82%BA%E4%BB%80%E9%BA%BCthreads%E5%9C%A8%E5%8F%B0%E7%81%A3%E9%80%99%E9%BA%BC%E7%B4%85%EF%BC%9F/)
- RAR 設計攻略（設計師 Riven 的自家課程行銷文）：Threads 2026 年 4.5 億 MAU、行動端日活 1.43 億（已超越 X），台灣約 350 萬活躍用戶（估值）— [RAR 設計攻略](https://rar.design/posts/threads-traffic-window-2026-designer)
- 「台灣 9,486 萬個 Threads 帳號」是誤算。這個數字出自美國市調公司 Resourcera 的報告，該公司事後表示數據是「流量」不是「用戶」，並撤下該段；事實查核中心也指出 Meta 沒公開各國帳號數 — [新頭殼](https://newtalk.tw/news/view/2026-05-06/1033636)；[自由時報（生活）](https://news.ltn.com.tw/news/life/breakingnews/5427331)；[自由時報（政治）](https://news.ltn.com.tw/news/politics/breakingnews/5410210)
- 全球規模：Wikipedia 列 2025-08-12 為 4 億 MAU — [Wikipedia](https://en.wikipedia.org/wiki/Threads_(social_network))。Meta 在 2026 年 6 月宣布 Threads 月活突破 5 億，約為祖克柏三年前定下的 10 億目標的一半 — [聯合新聞網](https://udn.com/news/story/6811/9572928)；[自由財經 2026-06-18](https://ec.ltn.com.tw/article/breakingnews/5476049)
- Threads 負責人 Connor Hayes 受彭博訪問時特別點名台灣，說「一場關鍵的選舉」是 Threads 在台灣爆紅、躍升主流社群的重大功臣。彭博同時指出，外部估計顯示 Threads 用戶在減少，和官方說法相反 — [聯合新聞網](https://udn.com/news/story/6811/9572928)；[NOWNEWS](https://www.nownews.com/news/6847472)；[ETtoday 2026-06-17](https://www.ettoday.net/news/20260617/3184842.htm)；[風傳媒](https://www.storm.mg/lifestyle/11142241)
- 私訊：手機 App 前一年就支援私訊；2026 年 4 月報導網頁版將開放私訊，Connor Hayes 證實正在測試網頁版改版 — [自由時報 3C](https://3c.ltn.com.tw/news/65753)
- 「脆」是年輕族群取的暱稱，因為短文字、容易散播等特性迅速走紅（2024）— [T 客邦](https://www.techbang.com/posts/116794-is-it-crispy-today-decrypt-thread-features)

**演算法獎勵什麼（多為第三方整理，非 Meta 官方權重）**
- Meta 沒公布加權後的排序訊號清單。Meta 透明度中心描述的是用 AI 系統依使用者過往行為與興趣替候選貼文打分；常被引用的預測項目有按讚機率、回覆互動、追蹤機率、點進個人檔案機率、滑過機率 — [Threads Dashboard](https://www.threadsdashboard.com/blog/threads-algorithm-how-it-works)；[BlackTwist](https://blacktwist.app/blog/how-the-threads-algorithm-works-in-2026-based-on-meta-s-updates)（歸屬未逐頁確認）
- 多數 2026 年第三方整理認為「回覆」是最強的互動訊號。據稱 Mosseri 說過回覆的總價值約等於貼文的總價值、回覆比按讚重要，也建議創作者「回覆多於發文」；常互動的追蹤者回覆權重可能較高，但這點不在 Meta 公開資料裡 — [PostEverywhere](https://posteverywhere.ai/blog/how-the-threads-algorithm-works)；[Postory](https://postory.io/blog/threads-algorithm)；[MomentumHive](https://momentumhive.app/blog/threads-algorithm-2026-how-it-works-and-why)；[NateCue](https://www.natecue.com/en/learn/marketing/threads-algorithm-seo-2026/)（歸屬未逐頁確認）
- Mosseri 公開表示 Meta 正在降權「nice post」這類低成本的 engagement bait 回覆；2024 年 11 月也說要重新平衡，多推追蹤對象的內容、少推無關聯的推薦內容 — 同上來源群（歸屬未逐頁確認）
- 有爭議或未證實的說法：連結會不會被降權（有來源說 Mosseri 反而提高了含 URL 貼文的價值）、發文後 30–60 分鐘決定觸及、圖片比純文字好 60%（引 Buffer 數據，未驗證）— [Threads Dashboard](https://www.threadsdashboard.com/blog/threads-algorithm-how-it-works)；[Postory 2026](https://postory.io/blog/what-works-on-threads-2026)
- 報導標題提到 Threads 推出「Your Algo」個人化演算法設定（只看到標題，內容未核）— [mezha](https://mezha.net/ch/?p=1783750)
- RAR 認為「隨便發都有觸及」的早期階段已經結束，但廣告版位剛開放、演算法仍偏向自然流量，還留有短暫窗口；競爭邏輯從「先到先贏」轉成「品味取勝」（單一作者觀點）— [RAR 設計攻略](https://rar.design/posts/threads-traffic-window-2026-designer)；同調觀點：「現在才開始經營脆…還沒太晚，但窗口正在關」— [日日脆 daypost](https://vocus.cc/article/6a43ca3afd89780001894848)
- 實務建議：新帳號常在前兩週過度發文，之後斷更；建議維持穩定頻率，每天花時間留言互動 — [richsong112](https://richsong112.com/threads-30-day-strategy-guide/)
- 一份 30 天實測（2026 年 2 月中到 3 月中）：約 47 萬瀏覽、7,229 次互動，粉絲只成長 85 人；作者把成效歸因於主題與互動設計 — [vocus](https://vocus.cc/article/69b81df3fd89780001474308)
- 行銷業者把 Threads 形容成「廢文聚集地」並談「議題操作」（只看到標題）— [SHOPLINE Blog](https://blog.shopline.tw/ads-article-threads-marketing/)

**接案者／一人公司怎麼從 Threads 拿到客戶**
- 2024 年 3–6 月，作者透過 Threads 聯繫到 20 位關鍵客戶（創作者），其中 3 人交流後用 Portaly 做到單月數十萬的變現；另一則貼文讓 100 張年會門票 24 小時內售完，營收約 30 萬（作者自述）— [數位時代](https://www.bnext.com.tw/article/81784/threads-engage-strategy)；[關鍵評論網](https://www.thenewslens.com/article/247119)
- 官方獎勵計畫仍是邀請制，發文本身不產生收入；Threads 主要負責獲客，變現發生在自己的產品或服務上，例如業配、數位產品、顧問接案 — [社群加速站](https://fansboosts.com/blog/threads-make-money)；[幕創行銷](https://beingmovestrong.com/threads-make-money/)
- 脆不會按觀看次數付錢，收入要靠注意力轉換；Threads 適合當漏斗最上層的放大器，接案服務可以靠它讓陌生人認識並信任你 — [日日脆 daypost](https://vocus.cc/article/6a41f378fd89780001eddfa9)
- 行銷顧問的看法：Threads 適合當流量入口，不適合當成交平台。常見路徑是先在 Threads 互動，再導到 IG 或 LINE，最後在 LINE 完成諮詢或購買。很多帳號的問題是「有流量卻沒有下一步設計」。接案與顧問業是主要受益者，因為在問答文化裡，每個專業回答都是一次免費的獲客展示（「單月 6 位數」等案例未經獨立驗證）— [yofish](https://yofish.site/blog/threads-monetize-sales-funnel-2026/)；[Tobie Huang](https://tobiehuang.com/en/threads-private-traffic/)；[幕創行銷](https://beingmovestrong.com/threads-marketing/)（歸屬未逐頁確認）
- 有文章提到，接案與顧問型變現靠內容展現專業，「幾千粉就有人私訊詢價」（歸屬未逐頁確認）— [幕創行銷](https://beingmovestrong.com/threads-make-money/)；[yofish](https://yofish.site/blog/threads-monetize-sales-funnel-2026/)
- 接案平台文章認為 Threads 越來越像「下一個接案資訊場域」，品牌方與創作者會在貼文中徵人 — [storyofdream](https://storyofdream.com/freelance-platform/)
- 一則 Threads 連載貼文整理了接案案源：自己網站的作品集、104「外包接案」職缺、PRO360（點數報價）、Tasker（抽成制）、FB 接案社團（免費提案但容易被洗版）— [Threads 公開貼文](https://www.threads.com/@tobie_talks/post/C6I6kBeve7y)

**風險環境（會影響受眾對「Threads → 私訊／LINE」路徑的信任）**
- 設計師在 Threads 示警：最近很多帳號在 Threads 上「徵設計師」或「發包設計案」，一步步索取公司與個人資料，甚至要求看帳戶餘額 — [Threads 公開貼文](https://www.threads.com/@hansdesign69/post/DWJlTI4D7oJ)
- 2026 年 7 月報導：詐騙集團假扮投顧老師在 Threads 發文，再把人導到 LINE；這批 AI 傀儡帳號第一週「絕對不談錢」— [中時新聞網](https://www.chinatimes.com/realtimenews/20260713000846-260412)；Threads 另有假冒賣家騙保證金的「骨牌式詐騙」— [CAVA](https://cava.tw/topic/fun-fact/264123)

### Inferences
- 台灣 Threads 受眾規模不算大（官方未公布，估計值約數百萬），但互動密度極高，又是文字優先。一篇中小店家看得懂的文字貼文，有機會在很短時間內觸及「LINE 群組開團」這類微型賣家。
- 回覆是公認最強的訊號，所以「別人 5 萬、我 299」這種對比式價格鉤子同時會引來支持者（「求私訊」）和批評者（「破壞行情」）。兩種回覆都算互動，貼文的擴散反而受惠於爭議。這是從第三方演算法整理推出來的，沒有 Meta 官方證據說「爭議」本身被獎勵；Mosseri 降權的是低品質的 engagement bait 回覆。
- 連續 31 天的「Day N」系列符合實務上「穩定頻率＋每天互動」的建議，也在追蹤者心中建立「明天還會更新」的期待，強化追蹤關係這個排序訊號。
- 詐騙常走「Threads → 私訊／LINE、先不談錢」的路徑，受眾對同樣路徑的接案者會有戒心。公開具體個案、連續日更、明碼「299 起」，在這個環境裡可以當作「我不是詐騙」的反向訊號。
- 最穩妥的台灣數據表述是：「Meta 高層點名前三活躍市場」加上「第三方估算約佔全球流量 21–22%」。「350 萬月活」只能當估計，「9,486 萬」不可引用。

### Gaps
- Meta 沒公布台灣 MAU／DAU；「350 萬」和「使用時間為美國 22 倍」都找不到原始出處。
- 沒有 Meta 官方的加權排序清單；「回覆權重」「早期互動」等說法都是第三方整理加 Mosseri 零星發言。
- 找不到台灣接案者「Threads 貼文 → 私訊 → 成交」轉換率的量化資料；現有案例都是自述。
- 受網路政策限制，沒能讀到 VERSE、QSearch、工商時報等原文全文。

---

## 2. 「創業 Day N／戰報」日記與營收透明格式：台灣案例、build in public 根源、為何能建立信任與執行力

### Takeaway
「創業 Day N＋戰報（客戶數、進帳）」是把國際獨立開發者的 build in public／open startup（公開 MRR、營收、流量）搬到 Threads 文字文化的版本。它建立信任的機制有三個：連續性（難以造假的日更）、具體數字，以及「讓人看見工作過程」（labor illusion／operational transparency）。不過自報營收無法驗證；國際上也已經有創辦人怕被抄而停止公開。台灣這種完全同格式的案例，這次沒找到可驗證的實例。

### Cited Findings
**國際根源（build in public／open startups）**
- Build in Public 的定義：在開發過程中公開分享進度、數據與失敗，常見平台是 X/Twitter — [IndieWait](https://indiewait.com/indie-dictionary)
- 有來源認為這波運動由 Buffer 和 Ghost 開始，Baremetrics 把它簡化（Open Startups），Pieter Levels（Nomad List、RemoteOK）把它普及（二手整理）— [Open Startups（collectednotes）](https://collectednotes.com/levygaston/open-startups-english-version)
- Buffer 把「Default to transparency」列為核心價值，公開營收、薪資、薪資公式、員工多元性統計和開源程式碼；有二手資料說，Buffer 2013 年公開薪資後 30 天內，職缺應徵數從 1,263 增加到 2,866（未核對原始來源）— [Freemius](https://freemius.com/blog/building-in-public-transparent-software-product-creation/)；[Indie Hackers](https://www.indiehackers.com/post/transparency-as-a-strategy-the-power-of-building-in-public-5ed4608582)（歸屬未逐頁確認）
- Baremetrics 帶頭推 Open Startups，有 20 多家公司公開指標；Pieter Levels 自 2014 年起公開 Nomad List 的流量與營收；Indie Hackers 社群裡大家分享產品更新、營收統計、成長曲線（二手整理）— 同上來源群
- 公開的動機包括當責（accountability）、行銷、被收購時的能見度、吸引用戶與員工、證明不靠外部資金也能獲利 — [FeedBear](https://www.feedbear.com/blog/how-to-build-in-public)；[Dodo Payments](https://dodopayments.com/blogs/build-in-public)；[Freemius](https://freemius.com/blog/building-in-public-transparent-software-product-creation/)（歸屬未逐頁確認）
- 反向趨勢：Indie Hackers 近期文章說，一些曾經高調推崇透明的創辦人正在「go dark」：刪掉 MRR 更新、從 bio 拿掉產品網址、轉入隱身模式，為的是防止抄襲。文章建議分階段：成長期公開，MRR 到 1 萬美元以上轉私密，3 萬美元以上只分享關鍵里程碑（文章部分付費牆）— [Indie Hackers](https://www.indiehackers.com/post/is-this-the-end-of-build-in-public-heres-why-top-indie-hackers-are-suddenly-disappearing-IhSJQBnXNuNwSuNTuz4t)
- 可驗證的對照組：TrustMRR 透過支付系統 API 同步營收，MRR 不靠創辦人手動填寫 — [知乎介紹](https://zhuanlan.zhihu.com/p/2014622142122181201)；[TrustMRR](https://trustmrr.com/startup/built-in-public)
- 華人圈也在談 Build in Public，例如用它解決產品冷啟動（中國獨立開發者社群）— [CSDN](https://opc.csdn.net/69845fb67bbde9200b984374.html)

**為什麼「讓人看見過程」會提高價值（學術證據）**
- Buell & Norton (2011)《The Labor Illusion: How Operational Transparency Increases Perceived Value》，*Management Science* 57(9):1564–1579：五個模擬服務實驗（線上旅遊、線上交友）顯示，讓人看見背後的工作能提高知覺價值，有時人們甚至寧可多等也要選透明的網站，即使結果完全相同。機制是互惠感：看得見的努力引發回報心理。旅遊搜尋實驗中，透明顯示讓整體服務價值高約 8% — [RePEc](https://ideas.repec.org/a/inm/ormnsc/v57y2011i9p1564-1579.html)；[Marketing Week](https://www.marketingweek.com/richard-shotton-labour-illusion/)
- 限制：這個效果會放大既有評價，不會反轉評價。交友網站版本中，透明呈現努力反而讓拿到不適配結果的使用者更不滿 — 同上
- 後續研究 Buell, Kim & Tsay (2017, *Management Science*)：消費者與生產者之間的視覺透明可以創造價值 — [RePEc](https://ideas.repec.org/a/inm/ormnsc/v63y2017i6p1673-1695.html)

**台灣相近的「日記／連載／挑戰」格式案例（不是完全相同的營收戰報）**
- 2024 年 vocus「創業小白如何使用脆？…Threads 的第一天紀錄」：作者每天統計 IG 和脆的追蹤人數，並記錄貼文內容 — [vocus](https://vocus.cc/article/669cb961fd89780001f732b8)
- vocus「9527 分潤日記」系列（Threads 變現主題的日記式連載）— [vocus](https://vocus.cc/article/6a7702d9fd8978000160b226)
- Threads 上的編號連載「沒有經驗的我，是怎麼找到接案工作呢？-9」，並預告「下次最終篇」— [Threads 公開貼文](https://www.threads.com/@tobie_talks/post/C6I6kBeve7y)
- 公開數據的 30 天經營實測（47 萬瀏覽、7,229 互動、+85 粉）— [vocus](https://vocus.cc/article/69b81df3fd89780001474308)

**一人公司背景**
- 天下雜誌：「一人公司」在 AI 時代爆炸成長，中國這類公司已超過 1,600 萬家，創辦人多為 Z 世代 — [天下雜誌](https://www.cw.com.tw/article/5142362)
- PRO360 統計：平台上員工只有 1 人的公司佔 62%；很多接案者先兼職，案源穩定後才離職創業 — [PRO360](https://www.pro360.com.tw/blog/2024-may/)
- 中國一位 AI 教培一人公司創業者，五個月服務 100 多位客戶，約三分之一來自老客戶推薦 — [鈦媒體](https://www.tmtpost.com/7925842.html)

### Inferences
- 「創業 Day 31」就是在地化的 build in public。不同處在於台灣版本主打的不是 SaaS 的 MRR，而是「接案客戶數＋當期進帳」；用的語言是「戰報」，借自業務／遊戲圈的每日戰績板。以下為推論，沒有找到語源考證。
- 為什麼建立信任：
  1. 連續性是昂貴訊號：31 天不間斷公開，很難憑空捏造。
  2. 具體數字：「19 位客戶、29,280 元」比「很多客戶」可信，學術依據見第 3 節的精確數字研究。
  3. 過程透明：「35 種情況」「改 73 次」是在展示工作量，符合 labor illusion。
  4. 數字不大反而像真的：29,280 元不是炫富等級，降低了「割韭菜／賣課」的聯想。
  但這些都是自報，沒有像 TrustMRR 那樣的第三方驗證；懷疑者只能從個案細節和一致性去判斷。
- 為什麼帶來執行力：公開計數器是一種承諾裝置，斷更會被看見，形成自我壓力。每個新客戶又會變成隔天的內容素材，於是「接案 → 內容 → 曝光 → 接案」自成飛輪。
- 風險：
  1. 抄襲：會暴露利基，例如「LINE 群組開團的海鮮小店」和做法，同業可以直接複製。國際上已有創辦人因此停止公開。
  2. 數字停滯時，戰報會變成負面訊號。
  3. labor illusion 只放大既有評價：對已經覺得「AI 拼裝便宜貨」的人，展示「改 73 次」也可能被讀成「需求控管失敗」。

### Gaps
- 沒找到可驗證、台灣、Threads 上「創業 Day N＋客戶數＋進帳」這種完全同格式的其他實例，也沒有這類貼文成效的數據。
- Buffer、Baremetrics 的細節（應徵數、參與公司數）都來自二手整理，沒核對一手來源。
- 「戰報」一詞在台灣網路文化的使用沒有找到文獻來源。

---

## 3. 逐句拆解貼文文案 × 說服／定價概念對照

### Takeaway
這篇貼文幾乎每一句都對應到一個已知的說服或定價機制：極端錨點（5 萬 vs 299）、尾數定價加「起」價、先發制人處理反對意見（便宜沒好貨）、價值堆疊（功能清單）、勞動錯覺（35 種情況、73 次）、把低價歸因於外部變化、坦白式雙面訊息，以及低門檻的比價 CTA。它和 Hormozi「Grand Slam Offer」的關鍵差別在於：Hormozi 是用價值堆疊撐起「高價、不可比較」的方案，這篇是用價值堆疊撐起「低價、主動邀請比價」。

### Cited Findings
**錨定與尾數定價（299）**
- 錨定捷思（anchoring）是 Kahneman 與 Tversky 提出的捷思之一。Thomas & Morwitz (2005) 提出「left-digit effect」，認為多位數比較時人們會錨定最左邊的位數 — [Wikipedia: Psychological pricing](https://en.wikipedia.org/wiki/Psychological_pricing)
- Stiving & Winer (1997) 把尾數效果拆成「形象效果」（聯想到特價）和「水準效果」（錨定最左位數而低估金額）；Anderson & Simester (2003) 的型錄實驗中，同一商品標 39 美元比標 34 美元賣得更好；Data Colada 的重製顯示方向成立，但效果只達邊際顯著、比原研究小；Snir & Levy (2021) 用 8 年、9,800 萬筆交易的掃描資料發現，尾數略低於整數的價格「通常反而比平均價高」— [Wikipedia: Psychological pricing](https://en.wikipedia.org/wiki/Psychological_pricing)；[NYU Stern](https://w4.stern.nyu.edu/sternbusiness/fall_2005/pennySaved.html)；[Kolenda](https://kolenda.io/tactics/charm-prices)（歸屬未逐頁確認）

**精確數字（29,280、35 種、73 次）**
- Janiszewski & Uy (2008, *Psychological Science* 19:121–127)：精確錨點造成的調整幅度比整數錨點小，即使兩者數值很接近。他們分析佛州 Alachua 郡 25,564 筆房屋交易，發現開價精確的賣方成交價更接近開價；受試者也認為整數價格的加成較高 — [Marketing Week](https://www.marketingweek.com/richard-shotton-precise-prices/)；[Wikipedia: Precision bias](https://en.wikipedia.org/wiki/Precision_bias)；[APS](https://www.psychologicalscience.org/news/releases/pricing-and-the-brain-why-things-cost-19-95.html)
- Zhang & Schwarz：數字的精確度只有在說話者被視為合作、專業、可信時才會被當成資訊；一旦可信度受質疑，精確度就不再有說服力 — [USC（Zhang & Schwarz PDF）](https://dornsife.usc.edu/norbert-schwarz/wp-content/uploads/sites/231/2023/11/13_jesp_zhang___schwarz_precise_numbers.pdf)

**「便宜沒好貨」＝價格－品質推論**
- Rao & Monroe (1989) 統合分析：價格與知覺品質之間有正向且統計顯著的關係，實驗設計與價格操弄強度會影響效果大小；二手資料說他們分析了 54 組關係，平均 η² = 0.12 — [Rao & Monroe 1989（UMN PDF）](https://carlsonschool.umn.edu/sites/carlsonschool.umn.edu/files/2024-06/Rao%20and%20Monroe%201989.pdf)；[MSI](https://www.msi.org/working-papers/the-effect-of-price-brand-name-and-store-name-on-buyers-perceptions-of-product-quality-an-integrative-review/)
- 涵蓋 1989–2006 年研究的後續統合分析：價格對知覺品質的效果已經減弱，在高價產品和受試者內設計中較強 — [HAL：The price-perceived quality relationship: A meta-analytic review](https://hal-normandie-univ.archives-ouvertes.fr/hal-02990424)

**雙面訊息／坦白（「有些錢我真的不敢漫天喊價，因為實際真的沒做什麼」）**
- 2022 年 *International Journal of Consumer Studies* 研究引用 Eisend (2006)、Crowley & Hoyer (1994)、Pechmann (1992)，指出雙面廣告訊息通常比較可信；它本身的實驗發現，雙面訊息會透過提高可信度來提高購買意願，但只對較懷疑廣告的消費者有效 — [When transparency pays off（USP PDF）](https://edisciplinas.usp.br/pluginfile.php/7947675/mod_resource/content/1/2022%20Int%20J%20Consumer%20Studies%20When%20transparency%20pays%20off%20Enticing%20sceptical%20consumers%20with%20two%E2%80%90sided.pdf)

**勞動錯覺／營運透明（「金額測了 35 種情況、一週改了 73 次」）**
- 見第 2 節 Buell & Norton (2011)：可見的努力提高知覺價值，但只會放大既有評價 — [RePEc](https://ideas.repec.org/a/inm/ormnsc/v57y2011i9p1564-1579.html)；[Marketing Week](https://www.marketingweek.com/richard-shotton-labour-illusion/)

**價值堆疊（功能清單）與 Hormozi**
- Hormozi 的價值方程式：Value = (Dream Outcome × Perceived Likelihood of Achievement) / (Time Delay × Effort & Sacrifice)。做法是用社會證明、保證、成功證據提高「達成可能性」，讓過程又快又省事來降低時間與力氣成本 — [SuperSummary](https://www.supersummary.com/100m-offers/summary/)；[Autymate](https://www.autymate.com/book-summary/100m-offers)
- Grand Slam Offer 的定義是「一個無法和市面上任何產品服務比較的方案」，組成包括吸引人的促銷、無法匹敵的價值主張、高價（premium price）、無敵保證；價值堆疊的做法是把問題拆成所有子問題，每個子問題各給一個解法 — [SuperSummary](https://www.supersummary.com/100m-offers/summary/)（歸屬未逐頁確認）

**低價入口（tripwire／low-ticket offer）**
- Tripwire 是低價的第一筆交易，主要任務是把潛在客戶變成付費客戶，讓人在大額購買前先試用。行情說法不一：5–50 美元（多數低於 20 美元）或 1–49 美元；也有人說核心產品 1,000 美元的話，前端方案可以到 200 美元。機制是第一筆小額購買會建立後續購買的承諾感。「買過 tripwire 的人購買核心方案的機率高 10 倍」這個說法來源不明，要保守看待。設計原則是 tripwire 應比 lead magnet 更有價值、比核心方案便宜，而且要和核心方案相連 — [Spiffy](https://spiffy.co/glossary/tripwire/)；[WPFunnels](https://getwpfunnels.com/tripwire-offer/)；[Bit.ai](https://blog.bit.ai/tripwires/)；[Power Digital](https://powerdigitalmarketing.com/?p=755)；[Rich & Niche](https://richandniche.notion.site/7-Tripwire-Offer-61059bfb596e43bd855c6450d8e591a2)（歸屬未逐頁確認）
- 術語區分：tripwire 放在留資料後的感謝頁；low-ticket offer（LTO）是把流量直接導到同一產品，當作漏斗第一頁 — [Castfox（podcast）](https://www.castfox.net/podcast/million-dollar-grit-6519128/episode/tripwire-vs-lto-the-funnel-terms-nobody-actually-explains-704500)

**「起」價＝基本價＋加價（partitioned pricing）**
- Morwitz, Greenleaf & Johnson (1998)〈Divide and Prosper〉，*Journal of Marketing Research* 35(4):453–463：研究消費者如何處理「基本價＋附加費」的分拆價格，以及這對記憶價格與需求的影響 — [MSI](https://www.msi.org/working-papers/divide-and-prosper-effects-of-partitioned-prices-on-consumers-price-recall-and-demand/)
- 後續回顧指出，消費者不一定會完整處理所有價格資訊，常低估總價；美國參議院商業委員會的文件也這樣摘述：買方常低估總價，而且更可能完成購買 — [Greenleaf, Johnson, Morwitz & Shalev 回顧（Columbia PDF）](https://business.columbia.edu/sites/default/files-efs/pubfiles/26031/Morwitz%20Greenleaf%20Shalev%20Johnson%20JCP%2015%2000002%20R1%20April%2019%202015%20.pdf)；[US Senate Commerce](https://www.commerce.senate.gov/services/files/31CC9415-0371-476F-9041-992CEE3A217F)
- 43 篇研究的統合分析：附加費的「知覺效益」和該品類「分拆計價是否常見」是影響需求的穩健調節變數 — [UMD DRUM](https://drum.lib.umd.edu/handle/1903/16560)

**「別人報價 5 萬」這個錨點在台灣是否合理**
- 2026 年行情：一頁式約 1–5 萬、形象網站約 4–7 萬、購物網站 6–8 萬、全客製 10 萬到 100 萬以上 — [出任務 Tasker](https://www.tasker.com.tw/articles/detail/1374)
- 其他 2026 年業者指南：一頁式 1.5–5 萬；套版一頁式 1–3 萬、標準客製一頁式 3–8 萬；企業形象官網多落在 4–10 萬或 5–20 萬（歸屬未逐頁確認）— [rab.tw](https://rab.tw/website-design-cost-guide/)；[Newscan](https://www.newscan.com.tw/blog/reasonable-website-fee.htm)；[元伸](https://www.ozchamp.com/insights/web-design-pricing-guide)；[安邦](https://anbon.tw/web-design-cost-taiwan-guide/)；[立德](https://leaderweb.com.tw/web-design/webdesign-fee/)

### Inferences
文案逐句對照表。各概念的出處見上方 Cited Findings；「作用」和「風險」兩欄是推論。

| # | 原文元素 | 對應概念 | 作用（推論） | 可能反效果（推論） |
|---|---|---|---|---|
| 1 | 標題「別人報價 5 萬 我收 299 起」 | 極端錨定＋對比；尾數定價（299 而非 300）；「起」＝分拆價格的入口價 | 5 萬落在台灣一頁式／形象網站的常見區間，錨點有可信度；5 萬 ÷ 299 ≈ 167 倍，製造巨大的划算感；爭議性高，會引來大量回覆 | 啟動「便宜沒好貨」的價格－品質推論；同業被激怒；「起」被質疑是話術（實際平均客單約 1,541，見第 4 節） |
| 2 | 「創業 Day 31 — 今天又進帳 5000；30 天 19 個客戶 29280」 | Build in public、社會證明（客戶數）、精確數字、連續性 | 精確數字比整數更像真的；「Day 31」暗示持續性與動能 | 自報無法驗證；當日 5,000 約是 30 天日均（976）的 5 倍，屬挑選好日子當標題；總額和當日進帳的關係有歧義（見第 4 節） |
| 3 | 「一直有人說便宜沒好貨」 | 先發制人處理反對意見（prebuttal）；雙面訊息 | 把讀者心中的質疑先說出來，提高對懷疑型讀者的可信度 | 重複負面框架，讓沒想到這點的讀者也開始懷疑 |
| 4 | 「拿今天手上的案子給你看：LINE 群組開團賣海鮮的小店」 | 個案研究；具體性；目標客群自我投射 | 同類微型賣家（LINE 團購主）立刻對號入座：「我也需要這個」 | 個案曝光要先取得客戶同意；利基被同業看見 |
| 5 | 「一個禮拜我做了（長串功能清單）」 | 價值堆疊（Hormozi 式拆解子問題）；提高夢想結果、降低時間成本 | 把 299 起的感知價值撐大；一週交付也表示時間延遲很低 | 讓客戶預期「299 也有這麼多功能」，埋下需求膨脹與議價的種子 |
| 6 | 「光金額就測了 35 種情況，一週改了 73 次每次都測過才上」 | 勞動錯覺／營運透明；精確數字；品質訊號 | 回應「便宜沒好貨」：便宜但不偷工 | 「一週改 73 次」對同業和有經驗的業主像是沒有修改上限、需求控管失敗；勞動錯覺只放大既有印象 |
| 7 | 「我便宜是因應市場變化，不是因為廉價」 | 重新框架；把低價歸因於外部成本結構改變（AI） | 切斷「低價＝低品質」的推論鏈 | 「市場變化」若被讀成「AI 做的」，懷疑者會更確信是 AI 拼裝 |
| 8 | 「有些錢我真的不敢漫天喊價，因為實際真的沒做什麼」 | 坦白（雙面訊息）；「我們 vs 漫天喊價的業者」對立框架；公平訴求 | 對覺得被代理商坑過的中小店家很有共鳴，建立「老實人」人設 | 等於說同業收 5 萬但沒做什麼，最容易引爆同業反彈；也可能讓人覺得自己的工作不值錢 |
| 9 | 「看看市場的報價…願打願挨，但下次可以先找我比價~」 | 低門檻 CTA；比價邀請；錨點回收 | 不要求立刻購買，只要「比價時想到我」，降低行動門檻 | 主動邀請比價，正好和 Hormozi 的「做出不可比較的方案」相反，會吸引價格導向的客人 |
| 10 | 頁尾「Day 31 戰報：客戶 19 進帳 29280」 | 系列化品牌標記；累積社會證明；記分板 | 每篇固定格式方便追蹤、形成期待；數字累加有動能感 | 數字停滯或下滑時會被看見；所有人都能算出平均客單 |

- 和 Hormozi 的對照：這篇用了「價值堆疊」和「降低時間成本」（一週交付），但配的是低價，邀請比價，也沒有明示的保證或風險反轉（只有「每次都測過才上」的品質承諾）。Hormozi 的設計是「堆疊＋高價＋保證＋不可比較」，這篇則接近「堆疊＋超低入口價＋可比較」。前者篩選出高意願客戶，後者擴大漏斗頂端，但吸引價格敏感客群。
- 以 tripwire 的語言來說，「299 起」比較像直接投放給流量的 LTO，而不是留資料後才出現的 tripwire；它在漏斗裡的作用是讓第一筆交易零心理負擔。
- 價格－品質推論在高價品類較強、近年整體有減弱趨勢，再加上 AI 讓簡單網站成本下降成為公共認知（見第 6 節），所以這篇貼文的「便宜但不廉價」框架在 2026 年比過去容易被接受。不過仍會被對品質敏感的業主篩掉。

### Gaps
- 沒找到專門研究「起」價（starting-at／from pricing）用語的實證；最接近的是分拆價格與 drip pricing 研究。
- 「起」價廣告在台灣《公平交易法》下的標示規範沒查（屬合規研究範圍）。
- 原貼文的互動數據（讚、回覆、轉發）無法取得，沒辦法驗證「爭議帶動擴散」在這篇上是否成立。
- Hormozi《$100M Offers》只讀到二手摘要，沒核對原書措辭。

---

## 4. 「299 起」低價入口怎麼轉成較高客單：可能漏斗、算術與常見陷阱

### Takeaway
光看貼文自己公布的數字，平均每位客戶約 NT$1,541，是 299 的 5.15 倍，至少約 80.6% 營收來自 299 以上的加購或較高方案。所以「299 起」在實務上是入口錨點，不是主力價格。但 30 天總進帳 29,280 元毛額，只有 2026 年基本工資月薪 29,500 元的約 99.3%（還沒扣工具、主機、稅），這個模式要能長久，關鍵在後續的維護月費、加購功能和流程產品化，而不是建置費。

### Cited Findings
**台灣網站與維護行情（轉高客單的參照）**
- 2026 年建置行情見第 3 節：一頁式約 1–5 萬、形象網站 4–7 萬等 — [出任務 Tasker](https://www.tasker.com.tw/articles/detail/1374)
- 一篇整理 PTT／Dcard 網友經驗的業者文章把價位分三帶：低價帶約 5,000–15,000 元、中價帶 15,000–60,000 元、高價帶 60,000 元以上；低價方案有人滿意，也有人用到盜版佈景主題，被原作者寄律師函 — [GOT YOU DESIGN（hostswp）](https://hostswp.com/web-design-pricing-analysis/)
- 套版型網站約 NT$20,000 以下，智慧型網站約 20,000–50,000 — [eztrust](https://www.eztrust.com.tw/%E5%81%9A%E4%B8%80%E5%80%8B%E7%B6%B2%E7%AB%99%E6%9C%83%E7%94%A2%E7%94%9F%E7%9A%84%E8%B2%BB%E7%94%A8%E6%9C%89%E9%82%A3%E4%BA%9B)
- 網域、主機、SSL 通常是每年持續的費用，例如 .com 每年約 500–800 元、.tw 約 800–1,200 元；報價單只寫「網站製作一式」容易產生追加費用爭議（歸屬未逐頁確認）— [rab.tw](https://rab.tw/website-design-cost-guide/)；[元伸](https://www.ozchamp.com/insights/web-design-pricing-guide)；[安邦](https://anbon.tw/web-design-cost-taiwan-guide/)
- 維護費：月費約 3,000–5,000 元、年費約 20,000–40,000 元 — [PRO360](https://www.pro360.com.tw/price/website_maintenance)；常見 NT$3,000–15,000 以上／月 — [makewebsites.tw](https://makewebsites.tw/posts/website-maintenance-cost/)。依接案型態分：個人接案 1,500–5,000／月、工作室 3,000–10,000、專業公司 5,000–20,000；年度維護約 20,000–180,000 元以上，小型企業網站多在 20,000–60,000；基礎主機每月約 1,000 元起，含更新與資安檢查約 3,000–5,000（歸屬未逐頁確認）— [元伸：維護成本](https://www.ozchamp.com/insights/custom-website-maintenance-cost)；[GOT YOU DESIGN：維護費](https://hostswp.com/website-maintenance-cost/)；[ftdesign](https://ftdesign.tw/how-much-does-website-hosting-cost-understand-hosting-and-at/)；[GOT YOU DESIGN：代管](https://hostswp.com/wordpress-managed-hosting-cost/)

**LINE 團購賣家的替代方案成本（目標客群的痛點）**
- 有設計工作室在 Threads 估算：LINE 開店幫手要用得順，每月約 3,000 元（官方帳號升級、訊息費、金流抽成），一年三萬多；並主張自建官網可以把客人資料、回購、Google 搜尋留在自己手上 — [Threads 公開貼文（設計工作室）](https://www.threads.com/@mo__design.studio/post/DadRmacE7eR)
- LINE 宣布擴充 LINE Premium，部分原本免費的功能預計從 2026 年第四季到 2027 年上半年陸續改為付費會員限定 — [瘋先生](https://mrmad.com.tw/line-premium-features-paid-changes)
- 市面已有多套 LINE 團購系統（飛比、樂樂、buy+1、OrderPally），各有跨平台與訂單管理特色 — [巴哈姆特](https://home.gamer.com.tw/artwork.php?sn=6093751)

**低價接案的虧損點與定價建議**
- 新手常用「別人報多少」來報價；建議先從想要的時薪倒推價格，並把工具訂閱成本和修改次數寫進報價單 — [夜羽凌（vocus）](https://vocus.cc/article/6ab37381fd89780001fd3e41)
- 新手容易一次訂閱多個 AI 工具，月費累積起來，接不到案就先虧 — [楓羽](https://maplefeather.com/article/how-to-make-money-with-ai-2026)
- 自己用 AI 或套版做網站的隱形成本：搜尋不到、客戶不信任、改版重做，往往比建置費更高 — [everflow](https://www.everflow.cc/blog/hidden-cost-of-diy-website)
- 工程公司觀點：報價不是用「這個功能多少錢」算，而是看整體時程、人力、營運成本與專案風險；模組之間會互相牽動，例如改一個報名系統，後台、權限、資料庫都要跟著調 — [益盛科技 FAQ](https://des13.com/faq/ai.html)
- AI 生成網站的破綻正在消失，對 AI 接案者是機會也是價格戰訊號；報價若停在「AI 接案水位」，會被拿去和五位數報價的工作室比。建議依客戶看到的結果定價，例如一次性官網重建約 3–8 萬（未經查證）— [vibecodingcoursemastery](https://vibecodingcoursemastery.com/blog/ai-website-slop-killed-freelance-pricing-2026)
- YouTube 影片〈AI 做網站 199 元起跳：接案新手最容易虧錢的四個地方〉：作者在 Threads 看到有人用 199 元接做網站，認為有了 Claude Code、Codex、Cursor，「把網站做出來」越來越便宜（只取得開頭簡介，四點內容沒拿到）— [YouTube](https://www.youtube.com/watch?v=6M0TBCIyzR4)

**算術的外部基準**
- 2026 年（民國 115 年）基本工資：月薪 29,500 元、時薪 196 元，2026-01-01 起實施，比 2025 年的 28,590 元調高 3.18% — [Human Resources Online](https://www.humanresourcesonline.net/taiwan-to-raise-monthly-minimum-wage-to-nt-29-500-from-1-january-2026-chi)；[公視新聞](https://news.pts.org.tw/article/772417)；[Workstem](https://www.workstem.com/tw/?p=17104)

**低價入口的轉換機制（通則）**
- 第一筆小額購買會對後續購買產生承諾感；低價入口要和核心方案相連，常見做法是把核心產品的一個元件拆出來當入口 — [Bit.ai](https://blog.bit.ai/tripwires/)；[WPFunnels](https://getwpfunnels.com/tripwire-offer/)（歸屬未逐頁確認）
- 分拆價格會讓消費者低估總價、提高成交 — [US Senate Commerce](https://www.commerce.senate.gov/services/files/31CC9415-0371-476F-9041-992CEE3A217F)

### Inferences
**算術（全部以貼文自報數字計算）**
- 平均客單：29,280 ÷ 19 ≈ **NT$1,541／客戶**，是 299 入口價的約 **5.15 倍**。
- 就算 19 位客戶都只付 299，也只有 19 × 299 = 5,681 元。所以至少 23,599 元（約 **80.6%**）來自 299 以上的加購或高階方案。「起」字承擔了大部分的定價彈性。
- 錨點落差：標題的對比是 5 萬 vs 299（約 167 倍），實際平均是 5 萬 vs 1,541（約 32 倍）。後者仍是極大差距，但標題放大了 5 倍以上的划算感。
- 日均進帳：29,280 ÷ 30 ≈ 976 元／天；「今天又進帳 5,000」約是日均的 5 倍，是挑好日子當標題。
- 歧義：標題說「30 天 19 個客戶 29280」，頁尾說「Day 31 戰報：客戶 19 進帳 29280」。可能有兩種解讀：(a) 今天的 5,000 還沒算進總額；(b) 5,000 已算進去，但客戶數沒變，代表這筆錢來自既有客戶（例如海鮮店的加購或分期款）。若是 (b)，本身就是「入口價 → 既有客戶追加付費」的證據。原文無法判斷。
- 和基本工資比：29,280 元毛額約是 2026 年基本工資月薪的 **99.3%**，而且還沒扣 AI 工具訂閱、網域主機、稅、勞健保。損益兩平工時約 29,280 ÷ 196 ≈ **149 小時／月**（30 天每天約 5 小時）。如果實際工時超過這個數字，有效時薪就低於法定最低時薪。
- 單一個案：海鮮店案做了「一個禮拜」、「改了 73 次」。假設這案收 5,000 元（原文沒說），工時只要超過 5,000 ÷ 196 ≈ **25.5 小時**，時薪就低於 196 元。
- 規模化門檻：以平均 1,541 元計，月營收要到 5 萬需要約 32–33 位客戶／月。如果每案都要「一週改 73 次」，人力上不可能。所以必須產品化：模板化元件（訂單、金額計算、團購表單）、修改次數上限、標準化方案。
- 經常性收入的槓桿：用行情最低端「個人接案維護 1,500 元／月」算，一位維護客戶一年 18,000 元，約等於 11.7 位「平均建置客戶」的營收。低價建置的商業邏輯，很可能是「用建置費當獲客成本，用維護、代管、加購回收」。這是推論，貼文沒提維護方案。

**可能的漏斗（推論；方向有「Threads 當入口、私域成交」的通則證據支持）**
1. 曝光：Threads 文字貼文。「別人 5 萬 vs 我 299」引來回覆與引用，回覆是最強排序訊號。
2. 信任：Day N 連續性、真實個案（LINE 團購海鮮店）、測試數字，加上明碼「299 起」，和「先不談錢」的詐騙路徑形成反差。
3. 承接：留言區回覆，再到個人檔案連結、Threads 私訊或 LINE 一對一。
4. 需求訪談與報價：299 基本版，加上依功能加價（訂單／金額計算／團購表單等），分拆計價讓總價感受較低。
5. 交付：AI 輔助快速建置、高頻迭代（一週內多次上版）。
6. 加購與留存：自訂功能、網域／主機代管、維護月費、改版；一間店的成功案例可以在同一個 LINE 團購圈帶出轉介紹。
7. 再內容化：每個案子變成隔天的戰報素材，回到第 1 步，形成飛輪。

**典型陷阱（推論，對應上方證據）**
- 價格敏感客群：主動邀請比價、以低價入口吸客，吸到的多半是會議價、會用「AI 一下就好」砍價的客人（見第 6 節設計師的經驗）。
- 範疇蔓延與無上限修改：「一週改 73 次」本身就是警訊；實務建議把修改次數寫進報價。
- 支援負荷：每位客戶平均只付約 1,541 元，客服、改版、主機問題的時間會快速吃光毛利。
- 價格錨定反噬自己：公開喊過「299 起」，以後要漲價時，自己的錨點會變成阻力（anchoring 對自己的定價也成立）。
- 可信度與法律風險：低價常被聯想到盜版佈景主題、AI 拼裝；個案曝光需要客戶同意；金流與個資屬合規範圍。
- 同業反彈：「削價競爭／破壞行情」的指控，以及對高端客戶的品牌傷害（見第 6 節）。
- 被模仿：公開利基和做法，同業可以直接抄；國際 build in public 圈已經出現「轉為不公開」的趨勢。

### Gaps
- 不知道「299 起」實際包含什麼、有沒有維護月費或代管方案、加購項目怎麼定價（見第 5 節）。
- 不知道發文者的實際工時、工具成本、退款或保證政策，所以有效時薪只能做敏感度推算。
- 沒有台灣「低價入口 → 維護訂閱」轉換率的數據；tripwire「10 倍」說法來源不明。
- 沒找到這篇或類似貼文的留言實況（Threads 頁面無法讀取）。

---

## 5. 原貼文與發文者公開方案的查找結果（「299 起」包含什麼？價格階梯？）

### Takeaway
用多組關鍵字搜尋，都沒找到原貼文，也沒找到發文者公開的方案頁，所以「299 起」包含什麼、有哪些價格階梯都無法確認。搜尋只找到相鄰證據：2026 年 Threads 上至少還有「199 元做網站」的低價方案被 YouTube 創作者拿出來討論，以及網頁設計業者在 Threads 用「LINE 開店幫手一年三萬多」來推自建官網。

### Cited Findings
- 用「別人報價5萬 我收299 網站 Threads 創業 Day」搜尋：沒有完全對應的貼文 — [搜尋結果中的 Threads 變現相關文章，例如 vocus](https://vocus.cc/article/6a41f378fd89780001eddfa9)（相關但非目標）
- 用「299起 做網站 LINE 團購 海鮮 Threads 一週 改了73次」搜尋：沒有符合內容；結果是 LINE 開店幫手成本討論、團購系統比較等相關內容 — [Threads 公開貼文（設計工作室）](https://www.threads.com/@mo__design.studio/post/DadRmacE7eR)；[巴哈姆特](https://home.gamer.com.tw/artwork.php?sn=6093751)
- 用「"不是因為廉價" 網站 便宜 因應市場變化 先找我比價」、「接案戰報 脆 Threads 本月進帳 客戶數 公開」、「創業第30天 Threads 每日紀錄 營收公開」搜尋：都沒有目標貼文（結果是比價網站、Threads 帳號數爭議、30 天經營實測等）— [vocus 30 天實測](https://vocus.cc/article/69b81df3fd89780001474308)；[自由時報](https://news.ltn.com.tw/news/life/breakingnews/5427331)
- 相鄰證據：YouTube 創作者提到在 Threads 看到有人用 199 元接做網站，代表 2026 年 Threads 上有多個「三位數價格」的網站方案 — [YouTube](https://www.youtube.com/watch?v=6M0TBCIyzR4)

### Inferences
- 貼文的「客戶 19、進帳 29,280」推出平均約 1,541 元，可見多數成交並非 299 本身。合理推測（僅是推測）「299」可能對應最陽春的單頁或模板版本，功能（例如訂單、金額計算、團購表單）另外計價；但也可能是某種月費或按次計價，無法排除。
- 「199 元」「299 元」同時出現，代表 Threads 上已經有一個「超低價 AI 建站」的小型價格戰，標題的數字錨點本身就是競爭手段。

### Gaps
- 原貼文、發文者帳號的方案說明、價目表、作品集都沒找到。主因是 Threads 貼文只部分被搜尋引擎索引，而且 threads.com 頁面在這次環境無法直接讀取。
- 依指示沒有嘗試辨識或記錄發文者身分等個人資訊。
- 建議（給報告撰寫者）：如果使用者能提供原貼文連結，可以補查方案頁與價格階梯。

---

## 6. 台灣開發者／設計師社群對超低價 AI 網站的反應（正反論點）

### Takeaway
反方（破壞行情派）認為：報價買的是時程、風險、策略與後續維護，不只是畫面；AI 低價讓客戶用「我自己叫 AI 就好」砍價，把風險轉給客戶，也拉低整體價格預期。正方（市場已變派）認為：AI 確實讓簡單網站的成本結構崩跌，原本付不起 5 萬的微型賣家現在被服務到了。這次沒能讀到 Threads／Dcard 上針對這篇貼文的直接留言，社群反應證據主要來自部落格、YouTube 與 PTT 的一般性討論。

### Cited Findings
**反方：削價／破壞行情、品質與風險**
- 設計師部落格（2026-06-02）：客戶砍價最常說「我都能自己叫 AI 做了」；AI 降低入門門檻，也直接拉低整個市場對設計的價格預期；設計師的價值在生成之前，也就是釐清使用者與問題 — [嫁給 RD 的 UI Designer](https://blog.akanelee.me/2026/06/02/ai-design-value-gap/)
- 台中網頁公司：報價依時程、人力、營運成本與風險計算，模組會互相牽動，AI 能幫忙但需要有經驗的人判斷 — [益盛科技 FAQ](https://des13.com/faq/ai.html)；自己用 AI 做網站，主機、版面、行動版、SEO、速度等細節可能耗掉幾百小時 — [益盛科技](https://des13.com/news/notes/notes/402-ai.html)
- 技術顧問：簡單的活動頁可以直接用 AI 做，但要長期承載 SEO 流量、串接 CRM 或多人維護，就需要專業架構、資安和後續維護；「AI 架站工具改變的是簡單網站的成本結構」— [CTK](https://ctkpro.com/ai-vs-enterprise-website-development/)
- 整理 PTT／Dcard 經驗的業者文章：低價不是不行，但風險很大，例如盜版佈景主題被律師函 — [GOT YOU DESIGN](https://hostswp.com/web-design-pricing-analysis/)
- YouTube〈AI 做網站 199 元起跳：接案新手最容易虧錢的四個地方〉：以 Threads 上 199 元做網站的貼文為引子，談低價接案的虧損點 — [YouTube](https://www.youtube.com/watch?v=6M0TBCIyzR4)
- 職涯文章引美國勞工統計局的看法：自動化設計工具可能減少企業外包給自由接案設計師的需求；風險最高的是需求明確、容易複製、「夠用就好」的任務 — [Worker360](https://www.worker360.com.tw/blog/ai-replace-designers-career-guide)
- 中國接案論壇：客戶以「都是 AI 寫的」為由要求降價，但接手的人發現 AI 產出的專案充滿 bug 和假資料，除錯返工的時間常被忽略 — [locdd](https://www.locdd.com/t/topic/83426)
- PTT Soft_Job：2025 年底討論擔心 AI 先壓縮初階、再壓縮中階工程師（「砍需求砍人力 junior 砍完砍 medium」）— [PTT Soft_Job](https://www.ptt.cc/bbs/Soft_Job/M.1763522645.A.A80.html)；也有討論批評接案公司把工程師當成本、薪資低於行情（歸屬未逐頁確認）— [PTT Soft_Job（2017）](https://www.ptt.cc/bbs/Soft_Job/M.1500887622.A.C34.html)；[PTT.BEST](https://www.ptt.best/bbs/Soft_Job/M.1703916102.A.D35.html)

**正方：市場確實變了、低價有正當性**
- 香港網頁工作室：「建站成本真係被打低咗」，中小型網站用 AI 加上少量人力往往就夠 — [TAN-studio](https://tan-studio.net/ai/since-the-emergence-of-ai-building-websites-really-isnt-as-expensive-as-it-used-to-be/)
- 2026 年網頁生成的邊際成本已接近零，任何人幾分鐘內就能生成「看起來不錯」的網站，價值重心轉向策略與使用者體驗 — [e7way](https://www.e7way.com.tw/article-info.asp?id=181)
- AI 建站工具月費約 US$5–50，專業設計公司約 HK$10,000–100,000 以上一次性；免費方案常有功能限制（顯示工具品牌、不能綁自訂網域）— [J Marketing](https://jmarketing.com.hk/ai-%E7%B6%B2%E9%A0%81%E8%A8%AD%E8%A8%88-%E5%BB%BA%E7%AB%99%E5%B7%A5%E5%85%B7-%E8%B6%A8%E5%8B%A2-2026/)
- PTT Soft_Job 2026 年討論：成本變得非常便宜後，終於能取得「能用、能打、真正有幫助」的模型 — [PTT Soft_Job](https://www.ptt.cc/bbs/Soft_Job/M.1771480523.A.B11.html)
- 上游 AI 模型本身也在價格戰：報導指出中國廠商的低成本攻勢引發 AI 大廠削價、AI 詞元價格跌到歷史新低 — [聯合新聞網](https://udn.com/news/story/6811/9730258)；[聯合新聞網](https://udn.com/news/story/6811/9692703)
- AI 接案者的觀點：AI 網站已經騙過人眼，是機會，也是價格戰訊號 — [vibecodingcoursemastery](https://vibecodingcoursemastery.com/blog/ai-website-slop-killed-freelance-pricing-2026)

### Inferences
- 這篇貼文第 8 句（「有些錢我真的不敢漫天喊價，因為實際真的沒做什麼」）正好戳中反方最在意的地方：把同業的報價說成「沒做什麼還收 5 萬」。可以預期會被同業引用或反駁。照 Threads 重視回覆的機制，這些反彈短期內反而可能增加觸及，但長期會讓發文者在同業和中高預算業主眼中被定位為「削價者」。
- 兩派其實在講不同市場：299–2,000 元服務的是原本付不起、也不會去找 5 萬方案的 LINE 團購微型賣家（原本沒在消費的那群人），5 萬方案服務的是要 SEO、品牌、整合、長期維護的企業。標題把兩者並列成同一場比價，是行銷框架，不是真正的同場競爭。
- 正方論點（AI 讓簡單網站成本崩跌）有公共認知支撐，這讓「我便宜是因應市場變化」聽起來合理；反方論點（風險、維護、範疇蔓延）則對應到第 4 節的算術：毛額約等於基本工資、一案改 73 次。兩邊都有證據，可持續性取決於能不能產品化，以及有沒有經常性收入。

### Gaps
- 沒能讀到 Threads 原貼文的留言串，也沒讀到 Dcard 原文討論串（Dcard 相關結果只有業者的二手整理）。
- PTT 結果多是對「AI 取代工程師」的一般討論，沒找到專門針對「299／199 元 AI 網站」的 PTT 討論串。
- YouTube 影片「四個最容易虧錢的地方」的具體內容沒取得。
- 沒有台灣中小店家對網站支付意願的問卷或量化資料。

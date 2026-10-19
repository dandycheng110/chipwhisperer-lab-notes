# 「299 元起」接案模式拆解：風險與合規（台灣，截至 2026-10-19）

> 研究範圍：(a) 低價替小店建置／維護線上點餐訂購系統的接案開發者；(b) 在 LINE 群組開團賣海鮮、月數百單、改用自有網站的小店（系統營運者）。
> 本筆記為研究摘要，**非法律意見**。
> **來源限制說明**：本研究環境的網路代理封鎖 law.moj.gov.tw、etax.nat.gov.tw、pdpc.gov.tw、tw.linebiz.com、leeandli.com 等網站（WebFetch DNS 失敗、curl CONNECT 403），無法直接開啟原文；以下資料主要透過搜尋引擎擷取的頁面內容與二手來源交叉確認。標示 **†** 者＝依全國法規資料庫條號引用、但未能在本環境直接開啟核對的條文內容（依既有知識＋二手來源），**請以全國法規資料庫現行條文覆核**。
> 嚴重度定義（用於第 9 節登錄表）：**高**＝可能刑責、百萬元級罰鍰／賠償或營運中斷；**中**＝數萬～數十萬元罰鍰或明顯消費爭議；**低**＝輕微或可快速補正。

---

## 1. 個人資料保護法：控制者 vs. 受託者、安全措施、外洩通報、2025 修法與個資會

### Takeaway
海鮮小店是蒐集會員個資（姓名、電話、地址、LINE ID）的「委託機關」（控制者）；開發者若代管這些資料即為「受託者」，依個資法第 4 條在受託範圍內「視同委託機關」，同受安全維護與損害賠償規範。網路零售賣家另受數位部 2023-10-12 施行之《數位經濟相關產業個人資料檔案安全維護管理辦法》拘束（**無規模門檻**、須訂安全維護計畫、重大事故 **72 小時內通報數位部**）。2025-11-11 公布的個資法修正（「知悉」即通知當事人、向個資會通報、未通報罰 2 萬–20 萬）**施行日期仍待行政院另定**——本次找到的最新資料（2026-03）仍寫「待定」。

### Cited Findings
**控制者／受託者（委託蒐集處理利用）**
- 個資法第 4 條：受委託蒐集、處理或利用個資者，於本法適用範圍內視同委託機關；法務部 102-07-05 法律字第 10203506220 號函重申受託者在委託機關的特定目的及受託範圍內視同委託機關 — [臺北市法規查詢系統（收錄法務部函釋）](https://laws.gov.taipei/Law/Interpretation/Content/FE253678)
- 法務部 101-11-21 函釋引施行細則第 8 條及立法理由：受託者雖實際執行蒐集處理，責任仍歸委託機關，故委託機關應對受託者為「適當之監督」 — [臺北市法規查詢系統（法務部函釋）](https://laws.gov.taipei/Law/Interpretation/Content/FE253678)
- 施行細則第 8 條† 監督事項：預定蒐集處理利用之範圍、類別、特定目的及期間；受託者採取之措施；複委託；受託者違反規定時應通知委託機關及補救措施；委託機關保留指示事項；委託關係終止時個資載體之返還及受託者儲存個資之刪除；委託機關應定期確認受託者執行狀況並記錄 — [全國法規資料庫 個資法施行細則 §8](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050022&flno=8)†
- 法務部另一函釋：受託之境外協力廠商若在委託機關原合法蒐集之特定目的與要件下處理，不必另取得當事人書面同意 — [臺北市法規查詢系統（法務部函釋）](https://laws.gov.taipei/Law/Interpretation/Content/FE253678)

**安全維護義務與罰則（2023 年修法，已施行）**
- 2023 年修法：違反安全維護義務改為「逕行處罰並同時命改正」，處 2 萬–200 萬元；情節重大者 15 萬–1,500 萬元；修法前須先命限期改正、屆期未改正才罰，最高僅 20 萬 — [國發會新聞稿](https://www.ndc.gov.tw/nc_27_36901)；[國發會](https://www.ndc.gov.tw/nc_14813_36902)

**數位部《數位經濟相關產業個人資料檔案安全維護管理辦法》（適用網路零售賣家）**
- 2023-10-12 發布施行，共 20 條，依個資法第 27 條第 3 項訂定；附表一涵蓋「電子購物及郵購業」中以網際網路零售商品之業者（自然人、私法人或團體），**未設資本額或資料筆數門檻** — [自由時報](https://ec.ltn.com.tw/article/breakingnews/4459610)；[工商時報](https://www.ctee.com.tw/news/20231226700106-439901)；[理律](https://www.leeandli.com/TW/NewslettersDetail/6757.htm)；[理律](https://www.leeandli.com/TW/NewslettersDetail/6955.htm)
- 業者須於施行後 3 個月內完成個資檔案安全維護計畫；未依期完成可按次處 2 萬–200 萬；情節重大或經限期改正仍未改正者按次處 15 萬–1,500 萬 — [自由時報](https://ec.ltn.com.tw/article/breakingnews/4459610)
- 個資事故危及營運或影響大量當事人權益時，應於發現後 **72 小時內通報數位部** — [自由時報](https://ec.ltn.com.tw/article/breakingnews/4459610)
- 須訂稽核機制；蒐集、處理、利用紀錄至少保存 **5 年**；資本額 1,000 萬以上或保有 5,000 筆以上個資者，每 12 個月至少對部分措施實施與檢討一次 — [工商時報](https://www.ctee.com.tw/news/20231226700106-439901)；[自由時報](https://ec.ltn.com.tw/article/breakingnews/4459610)
- 數位部另公布電商業者參考指引與計畫範本 — [數位部檔案](https://www-api.moda.gov.tw/File/Get/adi/zh-tw/ZoFEtDDQYJ1LHyd)；[數位部檔案](https://www-api.moda.gov.tw/File/Get/adi/zh-tw/sCr6PtbynHt914s)

**2025 年修法（已公布、未施行）**
- 立法院 2025-10-17 三讀、總統 2025-11-11 公布；修正第 1-1、12、18、21、22～26、41、47～49、52、53、55 條，增訂第 1-2、20-1、21-1～21-5、51-1、53-1 條；施行日期由行政院另定 — [全國法規資料庫 §48 頁面註記（搜尋擷取）](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=48)；[個資會籌備處](https://www.pdpc.gov.tw/News_Content/20/1001/)；[理律](https://www.leeandli.com/TW/NewslettersDetail/7532.htm)；[寰瀛](https://www.fblaw.com.tw/insights/legal-news-2025-11-25)；[中央社 2025-10-17](https://www.cna.com.tw/news/aipl/202510170211.aspx)
- 新第 12 條：公務或非公務機關一經「**知悉**」個資被竊取、竄改、毀損、滅失或洩漏，即應通知當事人（舊法以「違反本法」且「查明後」為前提）；非公務機關符合一定範圍者須向主管機關通報，內容、方式、時限及應變措施另以辦法定之 — [自由時報](https://news.ltn.com.tw/news/politics/paper/1728510)；[全國法規資料庫 §48（搜尋擷取）](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=48)
- 修法後由個資會統一受理事故通報；非公務機關違反通報規定處 **2 萬–20 萬**，屆期未改正按次處罰 — [自由時報](https://news.ltn.com.tw/news/politics/paper/1728510)
- 新第 48 條：違反第 20-1 條第 1 項（安全維護）等情形最高處 200 萬，屆期未改正按次處 15 萬–1,500 萬 — [全國法規資料庫 §48（搜尋擷取）](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=48)
- 公務機關須設個人資料保護長；非公務機關監督權限設 6 年過渡期分階段移轉至個資會 — [中央社 2025-10-17](https://www.cna.com.tw/news/aipl/202510170211.aspx)；[宏鑑](https://www.chenandlin.com/tc/blog_detail106.htm)
- 憲法法庭 111 年憲判字第 13 號要求設獨立監督機制，期限 2025-08-11 — [中央社 2025-02-02](https://www.cna.com.tw/news/aipl/202502020019.aspx)；行政院 2025-03-27 通過《個人資料保護委員會組織法》草案，定位為相當中央三級獨立機關、合議制 — [中央社 2025-03-26](https://www.cna.com.tw/news/aipl/202503260369.aspx)；[行政院簡報](https://www.ey.gov.tw/File/DF2DB787DCEC75FE?A=C)
- 籌備處已揭牌運作；個資會正式成立須俟組織法通過，行政院將配合組織法審議進度另定新法施行日期 — [理律（籌備處揭牌）](https://www.leeandli.com/TW/NewslettersDetail/7197.htm)；[個資會籌備處](https://www.pdpc.gov.tw/News_Content/20/1001/)
- 2026-03-13 日本律所電子報仍記載施行日期待定 — [Atsumi & Sakai TWN_005](https://www.aplawjapan.com/application/files/9217/7339/1552/TW_Newsletter_TWN_005.pdf)；另見 [理慈](https://www.leetsai.com/%E5%80%8B%E4%BA%BA%E8%B3%87%E6%96%99%E4%BF%9D%E8%AD%B7%E6%B3%95%E4%BF%AE%E6%AD%A3%E5%B0%8D%E7%A7%81%E9%83%A8%E9%96%80%E4%B9%8B%E5%BD%B1%E9%9F%BF%EF%BC%88%E8%87%BA%E7%81%A3%EF%BC%89?lang=zh-TW)、[廉貞](https://www.loyaltylaw.com.tw/%E5%B0%88%E6%AC%84%E6%96%87%E7%AB%A0/%E5%80%8B%E8%B3%87%E4%BF%9D%E8%AD%B7%E5%B0%88%E6%A1%88/key-points-of-the-2025-personal-data-protection-act-amendment-changes-in-the-personal-data-protection-commissions-authority-and-governance)、[山葵組（企業準備事項）](https://wasateam.com/blog/taiwan-pdpa-amendment-pdpc-enterprise-guide)

**損害賠償與蒐集利用（現行）**
- 第 29 條†：非公務機關違反本法致個資遭不法蒐集處理利用或侵害當事人權利者負損害賠償責任，但能證明無故意或過失者不在此限（舉證責任倒置）；準用第 28 條第 3–6 項†：被害人不易證明實際損害時，每人每一事件 500–20,000 元；同一原因事實多數當事人合計最高 2 億元（所涉利益超過 2 億者以該利益為限） — [全國法規資料庫 §28](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=28)†；[§29](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=29)†
- 第 8 條† 蒐集時告知義務（名稱、目的、類別、利用期間地區對象方式、當事人權利、不提供之影響）；第 19 條†（非公務機關蒐集須有特定目的並符合法定要件，如契約或類似契約關係、當事人同意）；第 20 條†（特定目的外利用之要件；當事人表示拒絕行銷時應即停止） — [全國法規資料庫 個資法全文](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021)†

### Inferences
- **多租戶託管的放大效應**：一個開發者托管多家小店的會員資料，單一破口（共用資料庫、共用後台密碼、IDOR）會讓所有客戶同時發生「事故」；每家店各自負通知當事人（未來＋通報個資會）義務，開發者依第 4 條同受規範。以第 28 條下限試算：1 萬名會員 × 500 元＝500 萬元的潛在請求曝險（若當事人求償），遠超 299 元方案的營收。
- 小店多數無資安能力，數位部辦法要求的「安全維護計畫」「72 小時通報」「5 年紀錄」實務上落在開發者身上；契約應寫明「發現事故 X 小時內通知賣家（建議 ≤24 小時，讓賣家趕得上 72 小時）」「協助通報與通知名單匯出」「每年提供安全確認紀錄」，否則賣家無法履行施行細則第 8 條的監督與定期確認。
- 「AI 把群組訂單整理成一張一張」若呼叫境外 LLM API，等於把含姓名、電話、地址的訊息交給第三方（複委託＋國際傳輸），須在隱私權政策揭露並選擇不保留／不訓練的 API 設定，或先遮罩再送。
- 新法雖未施行，方向明確（知悉即通知、統一通報、罰則加重）；現在設計系統就應預留事故偵測、受影響名單匯出、日誌留存。

### Gaps
- 未能確認行政院是否已在 2026-04～2026-10 間指定 2025 修正條文施行日，也未找到個資會組織法已三讀的資料；請查 pdpc.gov.tw／行政院公報。
- 新增第 20-1、21-1～21-5 條全文與未來「通報辦法」（時限是否 72 小時、門檻）未能取得原文。
- 未確認數位部辦法附表一是否也涵蓋開發者本身的行業（資訊服務、網站代管等）。
- 2025 修法是否對「受託者」新增直接義務（如受託者直接通報），未能查證。

---

## 2. 消費者保護法：通訊交易 7 日解除權與生鮮例外、必要揭露、購物金與訂金

### Takeaway
網路／LINE 接單賣海鮮屬「通訊交易」：須依消保法第 18 條以清楚易懂、可保存方式揭露業者資訊、價款、付款與交付方式、解除權與排除事由等。生鮮海鮮可依《通訊交易解除權合理例外情事適用準則》第 2 條第 1 款「易於腐敗、保存期限較短」排除 7 日解除權，但**前提是事先告知**；未告知則消費者仍可主張 7 日解除（且期間可延至最長 4 個月）。退款須在 15 日內返還，且**不得只給購物金**；消費者付費取得的「儲值型購物金」可能被視為禮券，須履約保障、不得設使用期限。

### Cited Findings
**揭露義務與 7 日解除權**
- 第 18 條第 1 項：以通訊交易訂約時，應將包括「依第 19 條解除契約之行使期限及方式」等資訊以清楚易懂文句記載於書面提供消費者 — [行政院消保處](https://www.ey.gov.tw/Page/8F51FEE53AB45EA9/36663b43-67df-4bdb-b8f7-d6a649b95223)
- 第 18 條† 各款：(1) 業者名稱、代表人、營業所及電話或電子郵件等聯絡資料；(2) 商品內容、對價、付款期日及方式、交付期日及方式；(3) 解除權行使期限及方式；(4) 依第 19 條第 2 項排除解除權之商品；(5) 消費申訴受理方式；經網際網路之通訊交易應以可供消費者完整查閱、儲存之電子方式提供 — [全國法規資料庫 消保法 §18](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=J0170001&flno=18)†
- 第 19 條第 1 項：收受商品後 7 日內得以退回商品或書面通知解除契約，無須說明理由及負擔任何費用或對價；但通訊交易有合理例外情事者不在此限 — [legis-pedia](https://www.legis-pedia.com/dictionary/53)；[消保處](https://www.ey.gov.tw/Page/8F51FEE53AB45EA9/008d4919-f21e-4caa-90be-82d745cdf63f)
- 準則第 2 條列 7 款例外，第 1 款為「易於腐敗、保存期限較短或解約時即將逾期」；適用前提為企業經營者告知消費者將排除解除權；準則第 3 條則規定已公告定型化契約應記載事項者適用其解除契約規定 — [消保處](https://www.ey.gov.tw/Page/8F51FEE53AB45EA9/008d4919-f21e-4caa-90be-82d745cdf63f)；[6laws 準則全文](https://6laws.net/6law/law3/通訊交易解除權合理例外情事適用準則.htm)；[legis-pedia](https://www.legis-pedia.com/dictionary/53)
- 準則適用採「例外從嚴」原則；行政院函釋：企業經營者未履行告知義務，消費者仍可主張 7 日解除權 — [消保處](https://www.ey.gov.tw/Page/8F51FEE53AB45EA9/36663b43-67df-4bdb-b8f7-d6a649b95223)
- 第 19 條第 3 項†：未提供解除權資訊者，7 日自提供之次日起算，但自原 7 日起算已逾 4 個月者解除權消滅；第 5 項†：違反本條之約定無效 — [全國法規資料庫 §19](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=J0170001&flno=19)†
- 退款時限：消費者以書面通知解除後，業者應於收到通知次日起 15 日內取回商品；並於取回商品或收到退回商品／通知次日起 15 日內返還已付對價（第 19-2 條†；回復原狀約定較民法第 259 條不利於消費者者無效†） — [臺北市法規查詢系統（條文擷取）](https://laws.gov.taipei/law/LawSearch/LawExport/FL012060?type=2)；[全國法規資料庫 §19-2](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=J0170001&flno=19-2)†；[legis-pedia QA](https://www.legis-pedia.com/QA/question/475)

**退款方式、購物金、禮券**
- 業者返還價金可提供退購物金、退現金等選項，但**不能強迫消費者只接受購物金**；約定「退貨只能換購物金」違反《零售業等網路交易定型化契約應記載及不得記載事項》第 10 點，可能被處 3 萬–30 萬（法律平台說法，除非屬無 7 日解除權之情形） — [legis-pedia QA 475](https://www.legis-pedia.com/QA/question/475)；[工商時報](https://www.ctee.com.tw/news/20250131700050-430104)
- 第 56-1 條†：使用定型化契約違反應記載／不得記載事項，經限期改正屆期不改正處 3 萬–30 萬；再次不改正 5 萬–50 萬並得按次處罰 — [全國法規資料庫 §56-1](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=J0170001&flno=56-1)†
- 禮券定義：發行人發行、記載或圈存一定金額之憑證，持有人可憑以請求交付商品或服務，**不包括發行人無償發行之抵用券、折扣券**；消保處函釋「買千送百」的「送百」屬無償抵用券，不受禮券規範、可限定使用期限，但須充分揭露 — [消保處](https://www.ey.gov.tw/Page/24C4B877E850ED4E/a61f2087-b7df-4658-a538-aacf24c2d27d)；[消保處](https://www.ey.gov.tw/Page/8F51FEE53AB45EA9/64c44490-ce73-407c-acd0-61c616b92227)
- 有償禮券**不得記載使用期限**；發行人須提供履約保障（金融機構足額履約保證、信託專戶專款專用、金融機構或電子支付機構價金保管、同業同級公司相互連帶擔保等）；消費者要求退還時手續費上限為返還金額 3%（108 年整併說明） — [消保處](https://www.ey.gov.tw/Page/8F51FEE53AB45EA9/64c44490-ce73-407c-acd0-61c616b92227)；[台中市政府宣導（禮券不可缺履保）](https://www.fire.taichung.gov.tw/df_ufiles/e/禮券不可缺履保少量購買盡快用10812.pdf)；[政大論文](https://thesis.lib.nccu.edu.tw/detail/91ea73189e05f69f12abb46e9fb44b72/)
- 購物金／點數期滿全數沒收可能被認定顯失公平而無效（法律平台意見，非官方） — [legis-pedia QA 6336](https://www.legis-pedia.com/QA/question/6336)

**訂金／預購**
- 預購規章即使寫明「不能退換」也可能無效，業者應事先說明排除 7 日解除權；實體店消費者自行反悔通常不能要求退定金，但網購預購是否適用 7 日解除權取決於是否屬例外且是否事先告知 — [legis-pedia QA 3724](https://www.legis-pedia.com/QA/question/3724)；[vocus](https://vocus.cc/article/606ba525fd897800011efc38)；[今周刊](https://www.businesstoday.com.tw/article/category/80401/post/201404100077/)
- 解除權須通知賣方始生效力，單純不取貨不等於行使解除權（法律平台問答） — [legis-pedia QA](https://www.legis-pedia.com/QA/5335/download)；[legis-pedia QA](https://www.legis-pedia.com/QA/5383/download)
- 民法第 249 條†（定金：因付定金者之事由致不能履行，不得請求返還；因受定金者之事由，應加倍返還）；第 259 條†（解除後回復原狀）；消保法第 12 條†（定型化條款違反誠信、對消費者顯失公平者無效） — [全國法規資料庫 民法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=B0000001)†；[消保法 §12](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=J0170001&flno=12)†

### Inferences
- **系統設計直接決定合規**：結帳頁顯示並要求勾選「生鮮易腐，依準則第 2 條第 1 款排除 7 日解除權」；訂單確認頁／訊息保存第 18 條資訊（可下載、可截存）；退款模組預設「原付款方式或現金」，購物金只能是消費者主動選項；系統有 15 日退款倒數提醒。
- 「退款退成購物金」要分清楚：消費者自願選擇＝可以；系統預設或只提供購物金＝違反第 10 點。貼文的「退款購物金有沒有還回去」屬另一層——消費者用購物金折抵後退貨，必須回補購物金＋退還現金部分，邏輯錯誤即形成「少退」爭議。
- 「購物金」若是消費者**付錢儲值**→ 禮券規範（履約保障、不得設期限），若可跨店使用還可能觸及電子支付「儲值」業務；若是**無償回饋**→ 可設期限但須揭露。建議開發者不要替小店提供「儲值」功能。
- 生鮮排除 7 日解除權**不等於**免除瑕疵責任：商品不新鮮、退冰、短少仍有民法物之瑕疵擔保（民法第 354、359 條†，[民法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=B0000001)），系統應保存出貨時間、物流單號、照片等證據。
- 「改單會不會吃掉訂金」：改單若導致訂金被沒收或未正確沖抵，可能被評為未依第 19-2 條返還對價或定型化條款顯失公平；訂金條款需事先、清楚、對等揭露。

### Gaps
- 未取得《零售業等網路交易定型化契約應記載及不得記載事項》第 10 點原文與最新修正日期（主管機關網站無法連線）。
- 未找到消保處針對「購物金」定性的專屬函釋，也未找到網購「訂金」的專門函釋或判決。
- 未查到 2025–2026 年消保法是否有新修正。

---

## 3. 食品安全：食品業者登錄、標示、冷鏈、平台義務

### Takeaway
具商業／公司／工廠登記之食品販售業者（**含純網路、無實體店面**）須辦「食品業者登錄」，網購業者並須在定型化契約／網頁揭露登錄字號（2015-09-30 起）；網路販售的包裝食品須符合食安法第 22 條標示；冷凍品須維持 -18°C 以下、冷藏 7°C 以下凍結點以上。純個人、未辦商業登記的小賣家是否須登錄，官方文字以「營業登記」為連結點；但月銷售額一旦達營業稅起徵點（貨物 10 萬）而須辦商業登記，就會觸發登錄義務。

### Cited Findings
- 自 2015-01-01 起，不論有無實體店面，具工廠、商業或公司登記之販售業者皆應依《食品業者登錄辦法》登錄；網購食品業者應具登錄字號並記載於定型化契約；未登錄經限期改正仍未改正可處 3 萬–300 萬 — [衛福部](https://mohw.gov.tw/cp-2704-20548-1.html)；[衛福部](https://mohw.gov.tw/cp-16-20548-1.html)
- 已公告須登錄者包括所有食品添加物業者，及具工廠／商業／公司登記之製造、加工、餐飲、輸入及販售業者；網購食品業者應記載登錄字號之規定自 2015-09-30 實施；食藥署開放消費者查詢登錄字號 — [衛福部](https://mohw.gov.tw/cp-2704-21300-1.html)；[衛福部](https://mohw.gov.tw/cp-16-21270-1.html)
- 2020 年台北市衛生局抽查 5 家直播拍賣業者、18 件食品：4 家定型化契約不符、4 家未揭露登錄字號、4 件外包裝標示不符 — [食力 foodNEXT](https://www.foodnext.net/news/newsnow/paper/5098431122)
- 食藥署：網路販售食品已屬擴大販賣範圍，須符合一般市售包裝食品標示規範（食安法第 22 條：添加物、營養標示、過敏原等）；食藥署認定只要有銷售行為即屬食品業者，不論數量多寡 — [食力](https://www.foodnext.net/news/newssafe/paper/4357922795)；[食力](https://www.foodnext.net/issue/paper/4357922795)
- 食安法第 22 條† 包裝食品應標示：品名、內容物名稱、淨重／容量／數量、食品添加物名稱、廠商名稱電話地址、原產地（國）、有效日期、營養標示、基因改造原料、其他經公告事項 — [全國法規資料庫 食安法 §22](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=L0040001&flno=22)†
- 進口食品作販售用途須申請輸入查驗並有完整中文標示；違反食安法第 30 條第 1 項可處販售者 3 萬–300 萬 — [食力](https://www.foodnext.net/news/newsnow/paper/5098431122)；[台南市衛生局](https://health.tainan.gov.tw/warehouse/AA06A696-3D9F-4B1A-AA13-1831AEC5423E/F_1677638693425e.pdf)
- 冷凍食品應保持 -18°C 以下、冷藏食品 7°C 以下凍結點以上，避免溫度劇烈變化；食藥署公布《低溫食品物流業者衛生安全宣導手冊》；2017 年查核 96 輛低溫車 94 輛合格，不合格原因含冷藏冷凍混放、車廂未達 -18°C；逾期未改正依食安法可處 6 萬–2 億 — [衛福部](https://mohw.gov.tw/cp-2621-9228-1.html)
- 理貨場所應在 15°C 以下並於 30 分鐘內完成，裝卸前應檢測並記錄品溫 — [食力](https://www.foodnext.net/news/newsnow/paper/4470357384)
- 商業登記法第 5 條†：每月銷售額未達營業稅起徵點之小規模商業得免辦商業登記 — [全國法規資料庫 商業登記法 §5](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=J0080001&flno=5)†

### Inferences
- 這家「月幾百單」的海鮮店，若客單價數百元以上，月營業額很可能超過 10 萬 → 須辦商業登記（或公司）＋稅籍登記 → **同時觸發**食品業者登錄與網頁揭露登錄字號。系統應內建「商號名稱／統編／食品業者登錄字號」頁尾欄位。
- 冷凍到店、宅配、面交的溫控責任都在賣家；面交與自行配送最難舉證溫度維持。系統可記錄出貨時間、物流單號、保冷方式，作為消費爭議與食安查核證據。
- 商品頁應有結構化欄位（原產地、淨重、保存方式、有效日期、是否曾解凍），讓網頁資訊與實物標示一致；網頁標示錯誤也可能構成消保／公平交易爭議。
- 從第三方 App 換成自有網站，等於脫離平台可能提供的部分把關（如代為檢核登錄字號、制式契約），所有揭露責任回到賣家自己。

### Gaps
- 未取得《散裝食品標示規定》中生鮮／冷凍水產品原產地標示的現行要求，亦未查到水產品專屬的網路販售規範。
- 未確認未辦商業登記之個人網路食品賣家是否另有登錄義務。
- 未查到 7-11／全家冷凍店到店的溫層規格、包裹限制與賠償上限之官方條款；賣貨便匯出是否使用官方介面亦未查證。
- 食安法下「電商平台業者」之配合義務未查證。

---

## 4. 稅務：賣家稅籍登記與發票門檻；接案者所得稅與二代健保

### Takeaway
**2025-01-01 起**，網路銷售**貨物**月銷售額達 **10 萬元**、銷售**勞務**達 **5 萬元**即應辦稅籍登記（所有平台／帳號合併計算）；月銷售額達 **20 萬元**須使用統一發票（5%），未達者多由國稅局查定課徵 1%。2023 年起網路營業人稅籍須登記網域與會員帳號，網頁須揭露營業人名稱與統編。接案開發者若以「程式設計師」身分提供專業勞務，屬執行業務所得、原則不屬營業稅課稅範圍；但若轉型為對多家商店收月費的標準化服務，可能被認定為「銷售勞務」之營業人。

### Cited Findings
**賣家（網路銷售）**
- 起徵點：自 2025-01-01 起，「銷售貨物」業別每月 10 萬、「銷售勞務」業別每月 5 萬（北區國稅局） — [聯合新聞網](https://udn.com/news/story/7243/8922512)；[工商時報 2024-10-19](https://www.ctee.com.tw/news/20241019700064-430104)；[NOWnews](https://www.nownews.com/news/6729525)
- 同一人經營多帳號、多平台、社群之銷售額須合併計算；國稅局以金流、物流資料交叉比對，以配偶、子女名義拆帳避稅被查獲須補稅並處罰 — [聯合新聞網](https://udn.com/news/story/7243/9528203)；[聯合新聞網](https://udn.com/news/story/7243/8922512)
- 月銷售額達 20 萬以上，國稅局核定使用統一發票、稅率 5%；未達者為小規模營業人 1%、免開統一發票（不同來源措辭有出入） — [PRO360](https://www.pro360.com.tw/guide/ecommerce_tax)；[PRO360](https://www.pro360.com.tw/guide/online_business_registration)；[財政部稅務入口網 Q&A](https://www.etax.nat.gov.tw/etwmain/tax-info/network-transaction-taxtation-area/q-and-a)
- 2023-01-01 起，透過網路平台或 APP 銷售之營業人，稅籍登記須新增「網域名稱及網路位址」「會員帳號」，並應於銷售網頁及 APP 清楚揭露「營業人名稱」及「統一編號」；已登記營業人新增網路銷售應申請變更登記 — [財政部稅務入口網](https://www.etax.nat.gov.tw/etwmain/tax-info/network-transaction-taxtation-area/press/gDqWW2g)；[KPMG 2022-11](https://kpmg.com/tw/zh/home/insights/2022/11/tax-news-update.html)
- 營業稅法第 32-1 條：以網際網路等電子方式開立電子發票者，應依時限傳輸至財政部電子發票整合服務平台存證（含載具識別資訊）；逾期或未據實傳輸處 1,500–15,000 元並得按次處罰 — [財政部稅務入口網](https://www.etax.nat.gov.tw/etwmain/tax-info/network-transaction-taxtation-area/press/66815oE)；[Deloitte 2024-11-22](https://www2.deloitte.com/content/dam/Deloitte/tw/Documents/tax/taxnews/tw-taxnews-20241122.pdf)
- 個人出售自用二手物品不課稅；收購再轉賣賺差價者須課稅 — [財政部 Q&A](https://www.etax.nat.gov.tw/etwmain/tax-info/network-transaction-taxtation-area/q-and-a)
- 網紅營業稅輔導期至 2026-06-30（已屆滿） — [聯合新聞網](https://udn.com/news/story/7243/9553340)；[工商時報 2026-06-08](https://www.ctee.com.tw/news/20260608701635-430104)

**開發者（個人接案）**
- 執行業務者提供專業性勞務及個人受僱提供勞務，原則不屬營業稅課稅範圍（營業稅法第 3 條第 2 項但書） — [工商時報 2024-02-19](https://www.ctee.com.tw/news/20240219701125-430103)
- 所得稅法第 11 條† 所稱執行業務者列有「程式設計師」 — [全國法規資料庫 所得稅法 §11](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=11)†
- 執行業務所得單次給付達 2 萬元，給付單位預扣 10%（未達 2 萬免扣）；預扣不含費用率，年度申報可能退稅 — [roo.cash](https://roo.cash/blog/freelance-tax-return)；[PRO360](https://www.pro360.com.tw/guide/freelancer_taxing)
- 二代健保：執行業務收入單筆給付達 2 萬元，扣取 2.11% 補充保費 — [健保署](https://www.nhi.gov.tw/ch/dl-85340-4e58804757e24feda5bf27f429fbbdbc-1.pdf)；[健保署](https://www.nhi.gov.tw/ch/dl-80097-39aa394983124e3880efd20a541d81d7-1.pdf)
- 程式設計師法定費用率 20%（**單一二手來源**） — [uptogo](https://uptogo.com.tw/?p=1789790)

### Inferences
- **海鮮小店**：「一個月幾百單」×假設客單價 600–1,000 元 ≈ 月營業額 18 萬–100 萬（假設值，貼文未揭露）→ 幾乎確定超過 10 萬起徵點；超過 20 萬須用統一發票，系統必須串接電子發票（透過金流商或加值中心），並在網頁揭露營業人名稱／統編。原本「末五碼轉帳」收進個人帳戶，正是國稅局金流比對的對象。
- **開發者**：貼文 30 天 19 客戶 29,280 元（平均每客戶約 1,541 元），低於勞務 5 萬起徵點；付款方多為未登記小店（非扣繳／扣費義務人），通常不會被扣 10% 或 2.11%，但所得仍須自行申報綜所稅。若業務長成「對多家商店收月費的 SaaS」，性質可能從執行業務轉為營業（銷售勞務），月收達 5 萬即須稅籍登記——建議諮詢會計師。
- 若客戶是已登記營業人且單筆付款 ≥2 萬（如一次性建置費），對方會扣 10% 稅款與 2.11% 補充保費，報價需含此現金流影響。

### Gaps
- 無法直接開啟財政部原文確認「20 萬」門檻細節，以及小規模營業人是否可免用電子發票。
- 個人以訂閱制銷售軟體服務屬「執行業務」或「營業」，未找到國稅局正式解釋。
- 程式設計師費用率 20% 僅一個二手來源，2025／2026 年度標準未核對。

---

## 5. 金流：代收代付、電子支付機構管理條例、持牌金流商、個人帳戶與警示帳戶

### Takeaway
開發者的系統一旦「先收消費者的錢、再轉給賣家」，就是「代理收付實質交易款項」——電子支付機構管理條例的許可業務（電子支付機構以股份有限公司為限，專營代理收付最低資本 1 億），並可能觸及銀行法第 29 條匯兌業務（刑責 3–10 年）。正確做法是款項直接進賣家自己的帳戶，或由賣家以自己名義向合規金流商（如綠界、藍新）申請特店，開發者只做串接。賣家用個人帳戶＋末五碼對帳，最大風險是被詐團利用為「三方詐騙」收款帳戶而遭列**警示帳戶**：存提款、匯款功能全停，解除須待偵查或審理結束。

### Cited Findings
- 「代理收付實質交易款項」：接受付款方基於實質交易所移轉之款項，經一定條件成就、一定期間屆至或付款方指示後，將款項移轉予收款方之業務 — [6laws 條例全文](https://www.6laws.net/6law/LAW/電子支付機構管理條例.htm)；[理律](https://www.leeandli.com/TW/Newsletters/5343.htm)
- 非電子支付機構原則上不得經營代理收付、儲值等業務，但有例外 — [6laws](https://6laws.net/6law/laws/電子支付機構管理條例.html)
- 電子支付機構以股份有限公司為限、採許可制，最低實收資本 5 億；僅辦理代理收付者 1 億 — [臺大李怡庭教授講義](https://homepage.ntu.edu.tw/~yitingli/file/Money%20and%20Banking/e_payment_2023.pdf)
- 收受儲值及代理收付款項應全部交付信託或取得銀行十足履約保證，並以專用存款帳戶保管 — [6laws](https://www.6laws.net/6law/LAW/電子支付機構管理條例.htm)；[6laws 專用存款帳戶管理辦法](https://6laws.net/6law/law3/電子支付機構專用存款帳戶管理辦法.htm)
- 金管會：第三方支付業者代收付全年日均餘額超過 20 億，須於 6 個月內申請電子支付許可，未申請有刑事罰則；2022 年有 6 家介於 10–20 億 — [TechNews 2024-02-07](https://finance.technews.tw/2024/02/07/third-party-payment-provider-daily-average-balance-check/)
- 銀行法第 29 條†：除法律另有規定外，非銀行不得經營收受存款、受託經理信託資金、公眾財產或辦理國內外匯兌業務；第 125 條†：違者處 3–10 年有期徒刑，得併科 1,000 萬–2 億元罰金 — [全國法規資料庫 銀行法 §29](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0380001&flno=29)†；[§125](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0380001&flno=125)†
- 警示帳戶：依《存款帳戶及其疑似不法或顯屬異常交易管理辦法》第 3 條，為司法機關偵辦刑事案件通知銀行列管之帳戶；列警示後提款、匯款、存款等功能暫停，匯入款項通常自動退回 — [legis-pedia](https://www.legis-pedia.com/dictionary/4863)；[legis-pedia](https://www.legis-pedia.com/dictionary/3837)
- 網路賣家是三方詐騙高風險族群：詐團假扮買家取得賣家帳戶，或利用賣家當金流工具 — [TVBS](https://news.tvbs.com.tw/money/3075354)
- 網銀、ATM、信用卡等服務也可能受限；解除通常須由通報機關啟動，並等案件偵查或審理結束 — [商業周刊](https://www.businessweekly.com.tw/career/blog/3018915)
- 交易糾紛類可在雙方和解後由警方協助解除；詐騙類須取得不起訴處分或無罪判決後申請解除 — [袋鼠金融](https://roo.cash/blog/?p=18570)；[PRO360](https://www.pro360.com.tw/guide/watch_listed_account)

### Inferences
- **末五碼對帳的具體風險**：(1) 同金額／末五碼撞號、分次匯款、代匯款人帳號不同 → 人工錯配；(2) 偽造轉帳截圖；(3) 三方詐騙讓被害人匯入賣家帳戶 → 帳戶警示，連同其他正常訂單款項全部卡住，整店現金流中斷；(4) 個人帳戶大量商業入帳，與稅務金流比對直接相關。改用金流商「每筆訂單唯一虛擬帳號」或信用卡／行動支付，可同時解決對帳與警示風險。
- **開發者紅線**：不要設計「消費者付款到開發者帳戶 → 定期撥款給小店」的模式（代收轉付）；改由每家小店以自己名義向合規金流商申請特店，開發者只負責 API 串接，不經手資金。也不要替小店做可跨店使用的「儲值」。
- 「取貨付款」由超商／物流代收貨款，是物流業者的合規管道，開發者系統只需記錄狀態與對帳。
- 金流 callback：只信任金流商伺服器對伺服器通知，並依各家官方技術文件驗證簽章／檢查碼，再以查詢 API 二次確認金額與狀態，處理需冪等（同一通知重送不重複入帳）。

### Gaps
- 未能取得電子支付機構管理條例現行（2021 年修正後）罰則條文原文（非電子支付機構經營代理收付之刑度），僅確認「超過門檻未申請有刑事罰則」的官員說法。
- 未查證綠界、藍新目前的許可類別（電子支付機構 vs. 第三方支付服務業）與費率。
- 未查證 2024 年《詐欺犯罪危害防制條例》對小型電商、金流業者的具體義務。

---

## 6. LINE 平台政策：群組中的官方帳號、bot 自動化、訊息計費、停權與依賴

### Takeaway
在群組中「打『菜單』自動跳商品」須用 **LINE 官方帳號＋Messaging API**，並開啟「允許加入群組」（預設關閉）；**一個群組同一時間只能有一個官方帳號**。回覆訊息（reply）不計入則數，但推播以「收件人數」計算——群組推播 1 則＝群組人數則。現行方案：輕用量免費 200 則、中用量 800 元／3,000 則、高用量 1,200 元／6,000 則；另有二手來源稱 **2026-11-01 起中／高用量調漲至 1,000／1,400 元**。LINE Notify 已於 2025-03-31 終止，說明平台功能可能單方面下架。

### Cited Findings
- 使用者在官方帳號所在群組發訊息時，LINE 平台會送 message event 給 bot server（source 含 groupId）；「Allow bot to join group chats」預設關閉；同一群組任一時間只能有一個 LINE 官方帳號；bot 在群組發的訊息所有成員可見；群組不支援 multicast — [LINE Developers：Group chats](https://developers.line.biz/en/docs/messaging-api/group-chats/)
- 官方建議驗證每個 webhook 請求的簽章；bot server 長時間無法接收 webhook 時，平台可能暫停傳送 — [LINE Developers：Receive messages](https://developers.line.biz/en/docs/messaging-api/receiving-messages/)；[Messaging API overview](https://developers.line.biz/en/docs/messaging-api/overview/)
- 計數方式：送出則數＝收件人數；例：一次請求含 4 個 message object 送到 5 人聊天室，計 5 則；封鎖者不計；reply 不計入方案則數；超過當月上限回傳錯誤、訊息不送出 — [LINE Developers：How message counts are calculated（2026-05-28）](https://developers.line.biz/en/tips/2026/05/28/how-to-count-messages/)；[Messaging API pricing](https://developers.line.biz/en/docs/messaging-api/pricing/)
- 台灣方案：輕用量免費 200 則、中用量 NT$800／3,000 則、高用量 NT$1,200／6,000 則 — [FirstLine 說明頁](https://help.firstline.cc/feature/channels/line/pricing)
- 2026-11-01 起中用量 800→1,000、高用量 1,200→1,400（未稅），輕用量維持 0 元（開發商部落格稱引官方公告、2026-09 查閱；**未能於官方頁面核實**） — [actgsys](https://actgsys.com/zh/blog/line-bot-development-cost-guide-2026)
- LINE Notify 已於 2025-03-31 終止，2025-04-01 起所有功能不可用，官方建議改用 Messaging API — [LINE Developers：end-of-life](https://developers.line.biz/en/news/tags/end-of-life)；[數位時代](https://www.bnext.com.tw/article/88845/)
- 官方方案費用 FAQ（本環境無法開啟） — [LINE Biz-Solutions FAQ](https://tw.linebiz.com/faq/oa-price/)

### Inferences
- **計費試算**：團購群組 300 人，推播一則開團公告＝300 則；輕用量（200 則）連一次都發不完；中用量 3,000 則≈每月 10 次群組推播。「菜單」指令以 reply 回覆不計費，是正確設計；但若訂單成立／出貨通知以 push 一對一發送，數百單 × 每單 2–3 則即可吃掉中用量額度，超額時訊息直接發送失敗（不是自動加價）。
- 原本「用別人的 App」若也是靠官方帳號在群組運作，換系統須先移除舊 OA（一群組僅能一個）。
- 群組內 bot 收到的是所有成員的訊息（含未加好友、未成為會員者）——這本身就是個資蒐集，應在群組記事本揭露用途，只保存與下單相關的訊息。
- **依賴風險**：LINE 帳號停權、政策或費率變動（Notify 下架、2026-11 調價）都會直接中斷接單。網站會員系統應另存可聯絡管道（電話／email）作為備援；官方帳號應以賣家名義申請，開發者只取得管理權限。
- 不要以非官方方式自動化個人 LINE 帳號（模擬點擊、逆向協定、外掛）——此類做法通常違反平台條款、有封號風險（條款原文未查到，見 Gaps）。

### Gaps
- 未取得 LINE 使用條款／LINE 官方帳號使用條款中關於個人帳號商業使用、外掛自動化、停權條件的原文（terms.line.me、tw.linebiz.com 無法連線）。
- 2026-11 調價僅一個二手來源；台灣方案超額加購單價未查證。

---

## 7. 開發者責任與契約條款

### Takeaway
接案建置屬民法「承攬」（後續維護多為委任或混合契約）：交付後 1 年內發見之瑕疵，定作人可請求修補、減少報酬、解約或損害賠償；契約不能預先免除故意或重大過失責任，定型化條款顯失公平者無效。著作權法第 12 條**預設程式著作權歸受聘的開發者**，客戶只有利用權——小店日後換人維護或要取回原始碼時，這是隱藏風險，必須在契約寫清楚。

### Cited Findings
- 民法第 490 條†（承攬定義）、第 492 條†（承攬人應保證工作具備約定品質，且無減少或滅失價值或不適於通常或約定使用之瑕疵）、第 493 條†（定作人得定相當期限請求修補，逾期得自行修補並請求償還費用）、第 494 條†（解除契約或請求減少報酬）、第 495 條†（可歸責於承攬人時得請求損害賠償）、第 498 條†（瑕疵發見期間為工作交付後 1 年）、第 514 條†（相關權利自瑕疵發見後 1 年間不行使而消滅） — [全國法規資料庫 民法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=B0000001)†
- 民法第 222 條†：故意或重大過失之責任，不得預先免除；第 247-1 條†：依定型化契約訂約，免除或減輕預定契約條款之當事人責任等按其情形顯失公平者，該部分約定無效 — [民法 §222](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=B0000001&flno=222)†；[民法 §247-1](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=B0000001&flno=247-1)†
- 著作權法第 12 條†：出資聘請他人完成之著作，除另有約定外以受聘人為著作人；未約定著作財產權歸屬者歸受聘人享有；出資人得利用該著作 — [全國法規資料庫 著作權法 §12](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=J0070017&flno=12)†
- 受託處理個資的開發者在受託範圍內視同委託機關（個資法第 4 條），委託終止時須返還載體、刪除持有之個資（施行細則第 8 條†） — [法務部函釋](https://laws.gov.taipei/Law/Interpretation/Content/FE253678)；[施行細則 §8](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050022&flno=8)†
- 非公務機關個資侵害採推定過失，每人每一事件 500–20,000 元推定賠償 — [個資法 §28](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=28)†；[§29](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=29)†

### Inferences — 建議契約條款清單（對 299 元起方案尤其重要）
1. **範圍（SOW）**：功能清單＋明列「不含」項目；變更以變更單計價（對照貼文「一週改了 73 次」）。
2. **驗收**：驗收標準（含金額計算測試案例清單，如貼文的 35 種金額情境）、驗收期限、逾期視為驗收。
3. **保固**：交付後 N 個月免費修正「瑕疵」（不含新需求）；民法 1 年發見期可依約調整，但不得顯失公平。
4. **維護費與 SLA**：月費涵蓋主機、備份、安全更新、回應時間（非 24/7）；停機定義、補償方式與上限。
5. **主機／網域／第三方帳號所有權**：網域、雲端、金流特店、LINE 官方帳號一律以賣家名義申請，開發者只取得管理權限。
6. **智財與原始碼**：著作財產權歸屬或授權範圍（可否轉由他人維護）；原始碼交付或第三方託管（escrow）的觸發條件（開發者停業、失聯、未續約）。
7. **資料**：資料歸賣家；可隨時匯出（CSV／JSON）；終止時返還與刪除（施行細則第 8 條）；備份頻率與保存期。
8. **個資委託條款**：處理目的範圍、安全措施、複委託清單（雲端、AI API）、事故通知時限（如 24 小時內通知賣家，讓賣家趕上數位部 72 小時通報／未來向個資會通報）、年度安全確認紀錄。
9. **責任限制**：例如以過去 12 個月已付費用為上限；但故意或重大過失不得預先免除（民法 222），定型化條款不得顯失公平（民法 247-1）；明定賣家自負的法遵事項（消保揭露、食品登錄、稅務、金流申請）。
10. **終止與移轉**：通知期、移轉協助的計價方式。

### Gaps
- 未查到台灣法院就「小型電商系統金額錯誤／資料遺失」判開發者賠償的案例。
- 未取得 2025–2026 年律所對軟體接案契約範本的評論。

---

## 8. 299 元起定價的商業可持續性與基本資安

### Takeaway
貼文數字（30 天 19 客戶、29,280 元；為單一客戶一週改 73 次、整天抓金額 bug）顯示：收入很低、單一客戶就吃掉大量工時，而且開發者成了多家小店的單點故障。OWASP Top 10:2025 仍以「存取控制失效」居首，並新增「軟體供應鏈失效」——正是多租戶、快速迭代、大量依賴套件的一人系統最常見的破口。

### Cited Findings
- 貼文自述：30 天 19 個客戶、營收 29,280 元；一週完成購物車、會員、優惠碼、購物金、超商冷凍到店、轉帳對末五碼、取貨付款、揀貨出貨單、賣貨便匯出、庫存毛利、群組「菜單」bot、AI 理單；一週改了 73 次；金額測了 35 種情況 — 使用者提供的 Threads 貼文內容（無 URL）
- OWASP Top 10:2025 已定案：A01 Broken Access Control 仍居首（併入 SSRF）；A03 為新的 Software Supply Chain Failures，取代 2021 年的 Vulnerable and Outdated Components — [The Register 2025-11-11](https://www.theregister.com/2025/11/11/new_owasp_top_ten_broken/)；[OWASP Top 10:2025](https://owasp.org/Top10/2025/ja/)；[Fastly](https://www.fastly.com/blog/new-2025-owasp-top-10-list-what-changed-what-you-need-to-know)
- 供應鏈類別範圍擴及建置管線完整性、dependency confusion、CI/CD 入侵、未維護套件與遭入侵的建置環境 — [FireCompass](https://firecompass.com/owasp-top-10/)；[Radware](https://www.radware.com/cyberpedia/application-security/owasp-top-10/)
- 各來源對 A01 盛行率說法不一（Radware 稱 100% 受測應用；The Register 引 3.73%） — [Radware](https://www.radware.com/cyberpedia/application-security/owasp-top-10/)；[The Register](https://www.theregister.com/2025/11/11/new_owasp_top_ten_broken/)
- LINE 官方建議 webhook 驗證簽章 — [LINE Developers](https://developers.line.biz/en/docs/messaging-api/receiving-messages/)

### Inferences
- **單位經濟**：29,280 ÷ 19 ≈ 每客戶 1,541 元；若 19 家都只付 299，月收僅 5,681 元，代表多數收入來自加購功能或一次性費用。以單一客戶一週 73 次修改、一整天專測金額估算，時薪極低；客戶數增加後支援量近乎線性成長，容易倦怠、品質下滑。
- **範圍蔓延**：「299 起」吸引預算極低的小店，但需求（冷凍到店、轉帳對帳、AI 理單、庫存毛利）已接近 5 萬元專案的規模；若沒有變更計價，成本全由開發者吸收。
- **關鍵人物風險**：開發者生病、轉職或失聯，多家小店的接單、會員、金流串接會同時停擺；小店手上沒有原始碼、主機權限或文件。
- **基本資安清單（多租戶）**：每個 API 在伺服器端以 tenant_id＋角色授權（防 IDOR，A01）；後台 MFA、登入速率限制；金流、物流、LINE callback 驗簽並做冪等；金鑰不進版控；相依套件鎖版並自動掃描弱點（A03）；備份＋還原演練；稽核日誌（同時滿足數位部 5 年紀錄要求）；電話、地址欄位加密／遮罩；送 AI 前去識別化。
- **金額邏輯**：用不可變的交易分錄（ledger：訂金、付款、購物金發放／使用／回補、退款），不直接覆寫訂單金額；改單＝沖銷＋新分錄，可從結構上避免「改單吃掉訂金」「退款購物金沒回補」；35 種情境應寫成自動化回歸測試，而非每次手測。
- **變更管理**：一週 73 次部署且無 staging，回歸錯誤直接影響真實訂單與金額；至少要有 staging、自動測試與可回滾部署。

### Gaps
- 無原貼文後續資訊（客戶留存、是否簽書面契約、主機架構、資料存放地）。
- 未查到台灣小型接案者定價與支援工時的統計資料。
- OWASP 2025 其餘類別（A02、A04–A10）未逐條核對，請以 owasp.org/Top10/2025 為準。

---

## 9. 綜合風險登錄表（Risk Register）

### Takeaway
最高風險集中在四處：(1) **開發者經手資金**（代收轉付→刑責）；(2) **多租戶個資外洩**（雙方都有罰鍰＋集體求償曝險）；(3) **賣家個人帳戶收款**（警示帳戶凍結＋稅務曝光）；(4) **金額邏輯錯誤加上沒有書面契約**（消保違規＋開發者賠償責任＋客戶失去原始碼）。多數風險可用「系統預設合規設計＋一份像樣的契約＋持牌金流」大幅降低。

### Cited Findings（登錄表；每列依據見對應來源）

| # | 風險 | 承擔者 | 嚴重度 | 說明（依據） | 緩解措施 |
|---|---|---|---|---|---|
| 1 | 開發者帳戶代收消費者款項再撥給小店（代收轉付） | 開發者（刑事）、賣家（款項風險） | 高 | 代理收付屬電子支付許可業務，電子支付機構須為股份有限公司、資本 1 億起（[臺大講義](https://homepage.ntu.edu.tw/~yitingli/file/Money%20and%20Banking/e_payment_2023.pdf)；[6laws](https://6laws.net/6law/laws/電子支付機構管理條例.html)）；可能觸及銀行法第 29、125 條†匯兌，3–10 年（[銀行法](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0380001&flno=125)†） | 永不經手資金；由賣家以自己名義申請合規金流特店，開發者只串接 |
| 2 | 多租戶系統個資外洩（姓名、電話、地址、LINE ID） | 兩者（對外以賣家為主；開發者依第 4 條視同委託機關） | 高 | 安全維護違反 2 萬–200 萬，重大 15 萬–1,500 萬（[國發會](https://www.ndc.gov.tw/nc_27_36901)）；推定賠償每人每事件 500–20,000 元、上限 2 億（[個資法 §28](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=28)†） | 租戶隔離、伺服器端授權、MFA、加密、備份、日誌；書面委託條款 |
| 3 | 外洩通報不及（數位部 72 小時；新法知悉即通知＋通報個資會） | 賣家（義務人）；開發者（實際執行） | 高 | 數位部辦法 72 小時通報（[自由時報](https://ec.ltn.com.tw/article/breakingnews/4459610)）；新法未通報 2 萬–20 萬（[自由時報](https://news.ltn.com.tw/news/politics/paper/1728510)），施行日待定（[個資會籌備處](https://www.pdpc.gov.tw/News_Content/20/1001/)） | 契約約定 ≤24 小時通知賣家；事故 SOP、通知範本、受影響名單匯出 |
| 4 | 網路零售賣家未訂個資安全維護計畫 | 賣家 | 中 | 數位部辦法無門檻適用網路零售，未依期完成按次 2 萬–200 萬（[自由時報](https://ec.ltn.com.tw/article/breakingnews/4459610)；[工商時報](https://www.ctee.com.tw/news/20231226700106-439901)） | 開發者以數位部範本提供計畫草稿（[數位部範本](https://www-api.moda.gov.tw/File/Get/adi/zh-tw/ZoFEtDDQYJ1LHyd)），列為加值服務 |
| 5 | 未盡告知義務／行銷利用不當（會員、LINE 推播） | 賣家 | 中 | 個資法第 8、19、20 條†（[個資法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021)†） | 註冊頁隱私告知、行銷同意與退訂機制 |
| 6 | LINE 群組訊息經 bot 送境外 AI 解析（處理非會員個資、複委託、跨境） | 兩者 | 中 | bot 會收到群組成員訊息事件（[LINE Developers](https://developers.line.biz/en/docs/messaging-api/group-chats/)）；受託／複委託規範（[法務部函釋](https://laws.gov.taipei/Law/Interpretation/Content/FE253678)） | 群組公告用途、只存下單訊息、送 AI 前遮罩、選不保留資料的 API |
| 7 | 個資會成立與新法施行時程不確定、主管機關轉換 | 兩者 | 低 | 6 年過渡期、施行日待定（[中央社](https://www.cna.com.tw/news/aipl/202510170211.aspx)；[Atsumi & Sakai](https://www.aplawjapan.com/application/files/9217/7339/1552/TW_Newsletter_TWN_005.pdf)） | 以「數位部辦法＋新法」較嚴者為設計基準 |
| 8 | 未事先告知生鮮排除 7 日解除權、未依第 18 條揭露 | 賣家 | 高 | 未告知→消費者仍可解除（[消保處](https://www.ey.gov.tw/Page/8F51FEE53AB45EA9/36663b43-67df-4bdb-b8f7-d6a649b95223)）；期間最長延至 4 個月（[消保法 §19](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=J0170001&flno=19)†） | 結帳頁勾選告知、訂單頁保存可下載的揭露資訊 |
| 9 | 退款只給購物金或逾 15 日退款 | 賣家（開發者設計責任） | 中 | 違反網路交易定型化契約第 10 點，3 萬–30 萬（[legis-pedia](https://www.legis-pedia.com/QA/question/475)）；15 日返還（[臺北市法規](https://laws.gov.taipei/law/LawSearch/LawExport/FL012060?type=2)） | 預設原路／現金退款，購物金僅為選項；退款倒數提醒 |
| 10 | 儲值型購物金被認定為禮券 | 賣家 | 中 | 有償禮券須履約保障、不得設期限；無償抵用券除外（[消保處](https://www.ey.gov.tw/Page/24C4B877E850ED4E/a61f2087-b7df-4658-a538-aacf24c2d27d)；[消保處](https://www.ey.gov.tw/Page/8F51FEE53AB45EA9/64c44490-ce73-407c-acd0-61c616b92227)） | 不提供儲值；只發無償購物金並揭露期限與規則 |
| 11 | 訂金／預購條款（「訂金不退」）被認定無效或顯失公平 | 賣家 | 中 | 預購「不能退換」可能無效（[legis-pedia](https://www.legis-pedia.com/QA/question/3724)；[vocus](https://vocus.cc/article/606ba525fd897800011efc38)）；消保法 §12†、民法 §249† | 訂金規則事先明示、對等；與生鮮例外告知一併呈現 |
| 12 | 金額邏輯錯誤（改單吃掉訂金、退款購物金未回補、多退少退） | 兩者（對消費者：賣家；對賣家：開發者承攬瑕疵責任） | 高 | 承攬瑕疵：修補、減價、解約、賠償，1 年發見期（[民法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=B0000001)†）；少退構成未返還對價（[臺北市法規](https://laws.gov.taipei/law/LawSearch/LawExport/FL012060?type=2)） | 不可變交易分錄、冪等、自動化回歸測試（35 種情境）、每日對帳報表 |
| 13 | 達起徵點後未辦食品業者登錄、網頁未揭露登錄字號 | 賣家 | 中 | 3 萬–300 萬；網購須揭露登錄字號（[衛福部](https://mohw.gov.tw/cp-2704-20548-1.html)） | 辦商業登記時同步登錄；系統頁尾登錄字號欄位 |
| 14 | 網頁／包裝標示不符（原產地、淨重、有效日期等） | 賣家 | 中 | 網路販售須符合包裝食品標示（[食力](https://www.foodnext.net/news/newssafe/paper/4357922795)；[食安法 §22](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=L0040001&flno=22)†） | 商品頁結構化標示欄位，與實物標籤一致 |
| 15 | 冷鏈斷鏈（冷凍到店、宅配、面交） | 賣家 | 高 | 冷凍 -18°C 以下、冷藏 7°C 以下（[衛福部](https://mohw.gov.tw/cp-2621-9228-1.html)）；理貨 15°C、30 分鐘（[食力](https://www.foodnext.net/news/newsnow/paper/4470357384)） | 合格低溫物流、保冷包裝、出貨時間與單號紀錄、面交時限 |
| 16 | 販售進口水產未辦輸入查驗 | 賣家 | 中（視貨源） | 食安法第 30 條，3 萬–300 萬（[食力](https://www.foodnext.net/news/newsnow/paper/5098431122)） | 向進口商索取查驗與中文標示文件 |
| 17 | 月銷售達 10 萬未辦稅籍登記（多帳號合併計） | 賣家 | 高 | 2025-01-01 起門檻 10 萬／5 萬（[聯合新聞網](https://udn.com/news/story/7243/8922512)）；國稅局金流物流比對（[聯合新聞網](https://udn.com/news/story/7243/9528203)） | 依門檻辦登記；≥20 萬用統一發票；網頁揭露名稱、統編（[財政部](https://www.etax.nat.gov.tw/etwmain/tax-info/network-transaction-taxtation-area/press/gDqWW2g)） |
| 18 | 電子發票未依時限傳輸存證 | 賣家（系統串接：開發者） | 低–中 | 1,500–15,000 元，按次處罰（[財政部](https://www.etax.nat.gov.tw/etwmain/tax-info/network-transaction-taxtation-area/press/66815oE)） | 由金流商或加值中心開票並自動上傳 |
| 19 | 開發者稅務定性不清（執行業務 vs. 營業）、漏報所得 | 開發者 | 中 | 執行業務專業勞務不課營業稅（[工商時報](https://www.ctee.com.tw/news/20240219701125-430103)）；勞務起徵點 5 萬（[聯合新聞網](https://udn.com/news/story/7243/8922512)）；單筆 ≥2 萬扣 10%／2.11%（[roo.cash](https://roo.cash/blog/freelance-tax-return)；[健保署](https://www.nhi.gov.tw/ch/dl-85340-4e58804757e24feda5bf27f429fbbdbc-1.pdf)） | 記帳留憑證；SaaS 化前諮詢會計師是否設行號 |
| 20 | 個人帳戶收款被列警示帳戶（三方詐騙） | 賣家 | 高 | 所有交易功能暫停，解除須待偵查或審理結束（[legis-pedia](https://www.legis-pedia.com/dictionary/4863)；[商業周刊](https://www.businessweekly.com.tw/career/blog/3018915)；[TVBS](https://news.tvbs.com.tw/money/3075354)） | 改用金流商虛擬帳號／信用卡；營業用與個人帳戶分離 |
| 21 | 末五碼人工對帳錯配、偽造截圖 | 賣家 | 中 | 由貼文流程推論（使用者提供貼文） | 每筆唯一虛擬帳號自動銷帳；未入帳不出貨 |
| 22 | 金流／物流 callback 偽造或重放（未付款出貨、重複入帳） | 兩者 | 高 | 屬存取控制／資料完整性類風險，存取控制失效為 OWASP 2025 第一名（[The Register](https://www.theregister.com/2025/11/11/new_owasp_top_ten_broken/)）；LINE 亦建議驗簽（[LINE Developers](https://developers.line.biz/en/docs/messaging-api/receiving-messages/)） | 驗章＋伺服器查詢 API 二次確認＋冪等鍵 |
| 23 | LINE 群組推播按人數計費、額度用完訊息直接失敗 | 賣家 | 中 | 推播以收件人數計、reply 不計、超額回錯誤（[LINE Developers](https://developers.line.biz/en/tips/2026/05/28/how-to-count-messages/)）；方案 0／800／1,200 元（[FirstLine](https://help.firstline.cc/feature/channels/line/pricing)），2026-11 或調為 1,000／1,400（[actgsys](https://actgsys.com/zh/blog/line-bot-development-cost-guide-2026)） | 指令一律用 reply；通知改由網站訂單頁、email；按群組人數試算方案 |
| 24 | LINE 平台依賴（停權、功能下架、調價、webhook 暫停） | 兩者 | 中 | LINE Notify 2025-03-31 終止（[LINE Developers](https://developers.line.biz/en/news/tags/end-of-life)）；webhook 長期失敗可能被暫停（[LINE Developers](https://developers.line.biz/en/docs/messaging-api/receiving-messages/)） | OA 以賣家名義申請；會員另存電話／email；網站可獨立接單 |
| 25 | 以非官方方式自動化個人 LINE 帳號或第三方後台（如賣貨便） | 兩者 | 中–高 | 條款原文未取得（見 Gaps）；一群組僅能有一個 OA（[LINE Developers](https://developers.line.biz/en/docs/messaging-api/group-chats/)） | 只用官方 Messaging API 與官方匯出／API |
| 26 | 無書面契約：範圍、驗收、保固、維護費、責任上限不明 | 兩者 | 高 | 承攬瑕疵責任依民法（[民法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=B0000001)†）；故意重過失不得預免、定型化條款顯失公平無效（[民法 §222](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=B0000001&flno=222)†；[§247-1](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=B0000001&flno=247-1)†） | 採用第 7 節 10 項條款清單 |
| 27 | 原始碼／著作權預設歸開發者，賣家無法換人維護 | 賣家 | 中–高 | 著作權法第 12 條†預設歸受聘人（[著作權法 §12](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=J0070017&flno=12)†） | 約定授權範圍或移轉；原始碼託管（escrow）及觸發條件 |
| 28 | 關鍵人物風險：一人開發者失聯，多家店同時停擺 | 賣家 | 高 | 推論（使用者提供貼文：一人一週完成、19 客戶） | 帳號歸賣家、文件、資料匯出、交接條款、備援維護者 |
| 29 | 資料遺失／停機（無備份、無還原演練） | 兩者 | 中–高 | 數位部辦法須保存紀錄 5 年、定期稽核（[工商時報](https://www.ctee.com.tw/news/20231226700106-439901)） | 每日備份＋異地＋還原演練；約定 RPO／RTO |
| 30 | 低價造成支援過載、範圍蔓延、倦怠 | 開發者（最終轉嫁賣家） | 高 | 推論：29,280÷19≈1,541 元／客戶；一週改 73 次（使用者提供貼文） | 方案分級、變更單計價、支援時段、產品標準化 |
| 31 | 多租戶存取控制與套件供應鏈漏洞 | 兩者 | 高 | OWASP 2025：A01 存取控制失效居首、A03 供應鏈失效（[The Register](https://www.theregister.com/2025/11/11/new_owasp_top_ten_broken/)；[FireCompass](https://firecompass.com/owasp-top-10/)） | 伺服器端 tenant 授權、後台 MFA、相依鎖版與弱點掃描 |
| 32 | 高頻部署無 staging、無自動測試（一週 73 次） | 兩者 | 中 | 推論（使用者提供貼文） | staging、CI 測試、可回滾部署、變更紀錄 |

### Inferences
- **優先序建議**：先處理 #1（不碰資金）、#20／#21（換掉個人帳戶＋末五碼）、#12（ledger＋測試）、#26～#28（契約＋帳號所有權＋原始碼）、#2／#3（資安＋事故通知）；其次是消保揭露（#8、#9）與稅籍／食品登錄（#17、#13）。
- 很多賣家端的合規義務（消保揭露、退款方式、登錄字號、統編揭露、電子發票）其實是「系統功能」；開發者若把它們做成預設值，就能變成高單價方案的賣點，而不只是成本。
- 對「別人報價 5 萬、我收 299」的比較：5 萬報價通常包含（或應包含）契約、驗收、保固、資安與文件；299 元若不含這些，風險只是從帳面移到了賣家與開發者的未來。

### Gaps
- 嚴重度為依法定罰則與營運影響做的定性判斷，非量化機率模型。
- 登錄表中標 † 的條文與「推論」列，須以全國法規資料庫原文與實際系統架構覆核。

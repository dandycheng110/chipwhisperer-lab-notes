# 技術拆解：一人一週做出「LINE 群組開團賣海鮮」店家系統（截至 2026-10-19）

> 研究方法說明（給報告撰寫者）：本次 WebFetch 對多數網域（developers.line.biz、tw.linebiz.com、metr.org、developer.mozilla.org、dev.to、techblog.lycorp.co.jp、chatbotta.com 等）都回報 DNS 解析失敗，只有 github.com 能直接讀取。因此以下大部分「Cited Findings」是根據搜尋引擎對該頁面的摘要內容整理，而不是逐頁讀完全文。價格、上限等數字請以「據某頁面摘要」的語氣呈現，上線前務必回官方頁面核對。來源彼此矛盾的地方都已標註。
>
> 貼文原文的功能清單（拆解對象）：購物車、會員、優惠碼、購物金；7-11 冷凍到店、全家、宅配、面交；轉帳對末五碼、取貨付款；揀貨單、出貨單、賣貨便一鍵匯出；掃條碼進貨、庫存、毛利報表；群組打「菜單」自動跳商品；AI 把群組訂單整理成一張一張；金額 bug 測 35 種情況；一週改 73 次，每次都測過才上。

---

## Q1. AI 輔助開發流程：2025–2026 年獨立開發者怎麼用 AI coding agent 快速交付 CRUD／電商系統？證據顯示生產力與品質如何？

### Takeaway
2025–2026 年常見做法是：拿自己熟悉的全端模板（Next.js／React + Postgres/Supabase + Vercel/Cloudflare），讓代理式 AI（Claude Code、Cursor、Codex 等）大量產出程式碼，再用自動測試把關。生產力證據並不一致：METR 2025 年的 RCT 發現，資深工程師在大型、成熟的 codebase 上用 AI 反而慢了 19%；2026 年的追蹤研究傾向「有加速」，但統計上不顯著。DORA 2025 發現 AI 提高了吞吐量，同時也伴隨更高的不穩定性。品質風險（安全漏洞、「差一點對」的程式碼）有具體數據佐證，這也說明了為什麼貼文要強調「金額測 35 種情況、每次都測過才上」。

### Cited Findings
- **METR 2025 RCT**：16 位資深開源開發者、246 個真實任務，多數使用 Cursor。允許用 AI 時完成時間反而多了約 19%。開發者事前預估會快 24%，做完後仍自認快了 20% — [CO/AI](https://getcoai.com/news/study-ai-coding-tools-slow-down-experienced-developers-by-19/)；[IT Brew](https://www.itbrew.com/stories/2025/08/04/ai-coding-tools-might-actually-be-slowing-you-down)（原始報告在 https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ，本次無法直接讀取）
- METR 本身並未主張「AI 全面無效」。研究期間是 2025 年 2 月，之後工具已有進步，結論也有場域特殊性 — [Implicator](https://www.implicator.ai/ai-coding-tools-make-experts-slower-not-faster-new-study-finds/)；[CO/AI](https://getcoai.com/news/study-ai-coding-tools-slow-down-experienced-developers-by-19/)
- **METR 2026-02 更新**：新實驗從 2025-08 開始，共 57 位開發者、143 個 repo、800 多個任務。回流的開發者任務時間 −18%，新招募者 −4%，但兩者的 95% 信賴區間都跨過 0。有 30–50% 的開發者表示，因為不想在沒有 AI 的情況下做，所以沒提交某些任務。METR 認為加速幅度可能被低估，但現有資料無法證明 — [devs-group](https://devs-group.ch/en/blog/ai-productivity-studies-2026/)；[Matthew Wong](https://www.matthewswong.com/en/blog/metr-developer-productivity-2026-uplift-update/)；[DEV（Gabriel Anhaia）](https://dev.to/gabrielanhaia/metrs-ai-coding-speed-study-broke-too-many-developers-wouldnt-work-without-ai-5afm)
  - ⚠️ 二手報導的正負號不一致：有報導把它寫成「仍慢 18%」。引用時應以 METR 原文為準 — [Ingenire](https://ingenire.com/blog/metr-2026-developer-productivity-study)；[valueaddvc](https://valueaddvc.com/blog/ai-coding-productivity-study-data-what-metr-mckinsey-and-github-actually-found-in-2026)
- METR 2026-05 調查了 349 位技術工作者（2026 年 2–4 月）。中位數受訪者自評速度提升 3 倍、工作價值提升 1.4–2 倍。這是自評，不是量測值；來源為二手整理 — [devs-group](https://devs-group.ch/en/blog/ai-productivity-studies-2026/)；[Matthew Wong](https://www.matthewswong.com/en/blog/metr-developer-productivity-2026-uplift-update/)
- **DORA 2025**：
  - 90% 的技術人員在工作中使用 AI，超過 80% 認為生產力有提升。
  - AI 採用與吞吐量的關係轉為正相關（2024 年是負相關），但與不穩定性上升有關。
  - DORA 的解釋是：如果缺乏強健的自動化測試、成熟的版本控制和快速回饋迴路，變更量增加就會造成不穩定。
  - 研究結果是相關性，不是因果。
  
  — [DORA 2025 報告 PDF](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf)；[DORA: Balancing AI tensions](https://dora.dev/insights/balancing-ai-tensions/)；[RedMonk](https://redmonk.com/rstephens/2025/12/18/dora2025/)；[Faros](https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025)
- **Stack Overflow 2025 開發者調查**：
  - 84% 已在使用或計畫使用 AI（2024 年是 76%）。
  - 信任 AI 準確度的只有約 29–33%（各來源數字不同），46% 表示不信任。
  - 最大的挫折是「差一點對」（45%）；66% 表示花更多時間修「差一點對」的程式碼。
  
  — [Stack Overflow Blog](https://stackoverflow.blog/2025/07/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/)；[ADTmag](https://adtmag.com/blogs/watersworks/2026/01/stack-overflow-survey.aspx)；[tech.co](https://tech.co/news/survey-developers-using-ai-more-trust-less)
- **Veracode 2025 GenAI Code Security Report**：測了 100 多個 LLM、80 個任務，約 45% 的產出樣本沒通過 OWASP Top 10 安全測試。Java 失敗率 72%，XSS（CWE-79）失敗率 86%。較新、較大的模型並沒有明顯更安全。測試用的是合成任務，不是線上 app — [Veracode](https://www.veracode.com/blog/genai-code-security-report/)；[CSA Research Note](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-codegen-vulnerability-debt-20260406-csa/)
- **Lovable CVE-2025-48757**：研究者掃描 1,645 個 Lovable 專案，發現 170 個的 Supabase RLS 設定不足，暴露 303 個端點。外洩資料包含 email、電話、付款狀態、API keys。MITRE 評分 9.3，Lovable 對此有異議。Lovable 之後改為發佈時自動掃描，但掃描只檢查 policy 是否存在，不檢查是否真的擋得住 — [Wolfgangsol](https://wolfgangsol.com/blog/lovable-cve-2025-48757-vibe-coding-security)
- **AI app builder 常見技術棧**：
  - Lovable：React 前端 + Supabase 後端，內建 auth、DB、檔案上傳、Stripe。
  - Bolt.new：在瀏覽器內的 Node 環境執行，框架選擇最彈性。
  - v0：最貼近 Next.js／Vercel；2026-01 從 v0.dev 改名為 v0.app，改用 token 計費。
  
  — [Rework](https://resources.rework.com/tools/ai-coding/lovable-vs-bolt-new-vs-v0)；[Superframeworks](https://superframeworks.com/compare/lovable-vs-bolt-vs-v0)；[aiagentrank](https://aiagentrank.io/blog/lovable-vs-bolt-vs-v0-2026)
- **Claude Code 用法**：Anthropic 官方 best practices 把 Claude Code 定位成低階、不強制特定工作流程的代理式工具 — [Anthropic Engineering](https://www.anthropic.com/engineering/claude-code-best-practices)（本次只讀到開頭摘要）。第三方整理的常見循環是 explore → plan → code → commit，由 agent 自己跑測試；專案指令、測試方式寫在 CLAUDE.md — [OpenHands](https://www.openhands.dev/blog/claude-code-best-practices-agentic-coding)；[Medium（Habib Mrad）](https://medium.com/@habib.mrad.83/claude-code-practical-best-practices-for-agentic-coding-2be1b62cfeff)
- **Claude Code 訂閱費**：
  - Pro US$20/月，含 Claude Code，但有用量上限。
  - Max 5x US$100/月，Max 20x US$200/月。
  - 用量以 5 小時和每週兩種視窗重置；2026 年調整過好幾次。
  
  — [Superblocks](https://www.superblocks.com/blog/claude-code-pricing)；[heyuan110](https://www.heyuan110.com/posts/ai/2026-02-25-claude-code-pricing/)
- **「別人的 App」可能是哪一類**：台灣已有多款「LINE 群組 +1 收單」SaaS，包括飛比 +1、Buy+1、OrderPally、樂樂BUY、LINE+1、CYBERBIZ LINE 團購、LiveShop。飛比專業版 NT$1,099/月（含稅）；樂樂BUY 免費版限 1 個群組、200 個商品 — [飛比 +1](https://one.feebee.com.tw/)；[樂樂BUY](https://leletobuy.com/)；[OrderPally](https://orderpally.com/linegroup/)；[Buy+1](https://buyplus1.com.tw/web/)；[LINE+1](https://www.lineplus.com.tw/)；[CYBERBIZ](https://help.cyberbiz.io/ec/integrations/line/group-buy/line-group-buy-shopping/)；[LiveShop](https://tw.line-oa-marketplace.com/list/chatisfy-groupbuying/)

### Inferences
- **貼文數字**：30 天 19 個客戶、營收 29,280，平均每客約 NT$1,541。搭配「299 起」的報價，可以推測多數客戶是小型、模板化的案子，海鮮團購這種完整系統屬於少數大案。一週做完的前提，幾乎一定是手上已有可重用的電商核心（商品、購物車、訂單、會員、優惠碼、後台、權限）。AI agent 主要負責兩件事：把模板改成這家店的流程，以及大量寫測試。
- **最可能的技術棧**（推測）：
  - Next.js（App Router）或 React + API server
  - Postgres（Supabase／Neon）或 Firebase
  - 部署在 Vercel 或 Cloudflare
  - LINE Bot 用官方 SDK，LLM 走雲端 API
  - Claude Code／Cursor 負責寫程式和測試
- **「一週改 73 次，每次都測過才上」**：約等於每天 10 次部署。這正是 DORA 說的「AI 讓變更量變大，就必須有自動測試和快速回饋，否則會不穩定」。它也呼應 Stack Overflow 調查裡「差一點對」的問題：金額邏輯是最容易「差一點對」、也最不能錯的地方。
- **METR 結論的適用範圍**：METR「變慢」的結果來自大型、成熟、開發者本人非常熟悉的 OSS codebase。這次這種 greenfield、以 CRUD 為主、規格明確的小型電商系統，正是 AI agent 最能發揮的場景。這是推論，不是任何研究的結論。
- **「模板 + 客製」模式的技術形態**（推測）：
  - 單一程式碼庫，多租戶（每家店一個 tenant），或每家店一個部署。
  - 功能用 feature flag／設定檔開關，例如有沒有冷凍物流、有沒有購物金、有沒有 LINE bot。
  - 真正需要客製的是 LINE 群組流程、物流選項、報表欄位和匯出格式。
- **最需要人工審查的高風險點**：AI 生成的 RLS／權限規則（參照 Lovable 事件），以及多租戶隔離。「A 店看到 B 店訂單」是這類系統最嚴重的事故類型。

### Gaps
- 貼文作者實際用了哪些工具、哪套技術棧，貼文沒有說明，無法驗證。
- Cursor、OpenAI Codex、Windsurf、Replit Agent 在 2026 年的價格與能力沒有深入查證。
- 找不到「台灣接案者用 AI 一週交付電商系統」的實證案例或量測資料。
- METR 原文和 Anthropic 官方文章全文無法直接讀取（DNS 失敗），只能依賴二手摘要。

---

## Q2. LINE Messaging API：官方帳號 bot 能否加入群組並收到群組訊息？Reply 與 Push 規則、台灣方案與費用、「菜單」關鍵字回 Flex 商品輪播、LIFF 與政策限制

### Takeaway
可以。LINE 官方帳號（OA）只要在 Developers Console 開啟「Allow bot to join group chats」，就能被邀進群組，透過 webhook 收到群組訊息事件（含 groupId、userId），並能在群組內用 Reply API 免費回覆。所以「打『菜單』跳商品」做得到，而且不花訊息費。

有兩個要特別注意的地方：
- **成本**：push 到群組會「按群組人數計費」。
- **導入**：一個群組只能有一個 OA，換系統前必須先把舊 App 的 bot 移出群組。

台灣方案從 2026-11-01 起調整：中用量 NT$1,000、高用量 NT$1,400。

### Cited Findings
- **加入群組**：
  - 要在 LINE Developers Console 的 Messaging API 分頁開啟「Allow bot to join group chats」，預設是關閉的。
  - bot 被加入時會收到 join event，可以回覆。
  - 群組訊息事件的 `source` 帶有 groupId／roomId，也可當成 push 的 `to`。
  - 一個群組或多人聊天室同時只能有一個 LINE OA。
  - 有 memberJoined／memberLeft 事件。
  - 收到 webhook 必須驗證簽章。
  
  — [LINE Developers: Group chats](https://developers.line.biz/en/docs/messaging-api/group-chats/)；[LINE Developers: Receive messages](https://developers.line.biz/en/docs/messaging-api/receiving-messages/)
- **取得群組成員資料**：可以用 `GET /v2/bot/group/{groupId}/member/{userId}` 取得群組成員 profile，對方沒加好友、甚至封鎖都拿得到；一般的 get-profile 只能查好友。userId 只在 message event 裡出現 — [iT 邦幫忙 Day16](https://ithelp.ithome.com.tw/articles/10229773)；[Ruby SDK doc](https://rubydoc.info/github/line/line-bot-sdk-ruby/Line/Bot/V2/MessagingApi/ApiClient:get_group_member_profile)
- 2020 年 LINE 新增了取得群組資訊、群組成員總數的 API — [LINE Engineering 2020-06](https://engineering.linecorp.com/zh-hant/blog/2020-june-update/)
- 取得群組「全部成員 ID 清單」限認證／付費（verified/premium）帳號。這是第三方 Make 文件的說法 — [Make: LINE](https://www.make.com/en/help/app/line)
- **webhook 重送與去重**：
  - 同一事件可能送達不只一次，官方建議用 `webhookEventId` 去重。
  - 開啟 redelivery 後，事件抵達順序可能和發生順序差很多，要用 `timestamp` 排序。
  - `deliveryContext.isRedelivery` 標示重送事件。
  
  — [LINE Developers: Receive messages](https://developers.line.biz/en/docs/messaging-api/receiving-messages/)
- **Edit／Unsend 事件**：
  - Edit event（使用者編輯訊息）目前只在群組觸發，可以回覆。
  - Unsend event 在 1:1、群組、多人聊天都會觸發。
  - 編輯功能目前在 LINE Labs 試用：需要 LINE 26.12.0 以上並手動開啟「訊息編輯」，送出後 15 分鐘內可編輯。
  - Unsend 沒有 reply token，要通知就只能 push，會計費。
  - 文章作者觀察到 Edit 事件的 message ID 與原訊息相同，可以當成訂單的鍵值。
  
  — [LINE Developers: Receive messages](https://developers.line.biz/en/docs/messaging-api/receiving-messages/)；[LY Corp Tech Blog（繁中）：用 Edit 與 Unsend Webhook 打造 LINE 團購 Bot](https://techblog.lycorp.co.jp/zh-hant/linebot-msg-edit-unsend)；[DEV（英文版）](https://dev.to/gde/ai-in-practice-building-a-dynamic-line-group-buying-bot-with-edit-and-unsend-webhooks-1clh)
- **計費規則**：
  - 訊息通數以「發送對象人數」計算。例：一次 push 4 個 message object 到 5 人的聊天室 = 5 通。
  - 泡泡（message object）數量不影響通數，計法是「送信請求數 × 對象人數」；一次請求最多 5 個 message object。
  - 發給封鎖者或不存在的 userId 不計費。
  - 群組人數 API 會把未加好友、已封鎖的成員也算進去。
  
  — [LINE Developers（ja）: Messaging API 料金](https://developers.line.biz/ja/docs/messaging-api/pricing/)；[LINE Developers Tips 2026-05-28：通數カウント方法](https://developers.line.biz/ja/tips/2026/05/28/how-to-count-messages/)
- 開發者實測：對 40 人的群組 push 15 次，被計為 600 通 — [taupe.site](https://taupe.site/entry/line-messaging-api-push-count/)；[kumadayo](https://blog.kumadayo.com/blog/line-messaging-api-limit-200/)
- **哪些訊息計費**：Reply API 不計入；Push／Multicast／Broadcast 計入 — [LINE for Business Help（ja）](https://help.linebiz.com/lineadshelp/s/article/L000001124?language=ja)；[LINE Help（en）](https://help2.line.me/official_account/android/pc?lang=en&contentId=20013992)。台灣說明也是：只有官方帳號主動發送的訊息計入，使用者主動互動觸發的（加好友歡迎訊息、一對一聊天、自動回應）不計 — [iT 邦幫忙](https://ithelp.ithome.com.tw/articles/10292653)
- **Reply 的限制**：一次 reply 最多 5 個 message object（官方）。reply token 只能用一次；有效時間沒能從官方摘要確認（Bottender 文件說 30 秒內） — [LINE Developers: Send messages](https://developers.line.biz/en/docs/messaging-api/sending-messages)；[Bottender](https://bottender.js.org/docs/channel-line-sending-messages)；[SMS-Magic](https://www.sms-magic.com/docs/salesforce/knowledge-base/understanding-line-messaging/)
- **台灣方案（2026-11 以前）**：
  - 輕用量 NT$0／免費 200 則
  - 中用量 NT$800／3,000 則
  - 高用量 NT$1,200／6,000 則
  - 低、中用量不能加購；高用量加購每則 NT$0.2 遞減到 0.11（2023-09 起）
  
  — [Omnichat](https://blog.omnichat.ai/tw/line-2-0-official-account-pricing/)；[FirstLine](https://help.firstline.cc/feature/channels/line/pricing)
- **台灣方案（2026-11-01 起，官方 2026-09-01 公告）**：
  - 中用量 NT$800 → NT$1,000，免費 3,000 則不變，不能加購。
  - 高用量 NT$1,200 → NT$1,400，免費 6,000 則不變。
  - 輕用量月費與免費則數不變。
  - 高用量加購改為階梯價：第 1–50,000 則 NT$0.2／則，第 50,001 則起 NT$0.15／則（chatbotta 整理，以官方為準）。
  - 10/27 前要決定降級或續用；10/28–11/2 後台暫停新購、升降級。
  - 以上皆未稅。
  
  — [LINE Biz-Solutions 官方專欄](https://tw.linebiz.com/column/LINEOA-2026-Price-Plan/)；[chatbotta](https://chatbotta.com/guides/line-oa-pricing/)；[蕃新聞](https://n.yam.com/Article/20261013326597)；[賴管家](https://lineoa.batmobile.com.tw/blogs/lineoa_message_counting)；[SAYA](https://www.saya.com.tw/insight-detail/Line_oa/)
- 最早查到 2026-11 調價說法的是一篇開發商文章；之後在官方專欄和其他多個來源得到印證 — [actgsys](https://actgsys.com/zh/blog/line-bot-development-cost-guide-2026)
- **Flex Message**：
  - carousel 最多 12 個 bubble，尺寸要一致。
  - 第三方整理：單一 bubble JSON 上限 30 KB，carousel 上限 50 KB。
  - 有 JSX 轉 Flex JSON 的開源套件。
  
  — [LINE Developers: Flex Messages](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/)；[Conferbot（413 錯誤）](https://www.conferbot.com/errors/line/413-payload-too-large)；[Mars Tseng（Medium）](https://medium.com/@marstseng/line-flex-message-b83b33483f9d)；[react-line-flex](https://github.com/chaiwattsw/react-line-flex)
- **LIFF → LINE MINI App**：LY Corp 在 2025-02-12 宣布 LIFF 與 LINE MINI App 將進行品牌整合，建議新的 LIFF app 直接建成 LINE MINI App。整合時間未定，既有的 LIFF app 可以繼續使用 — [LINE Developers News](https://developers.line.biz/ja/news/2025/02/12/line-mini-app/)；[LY Tech（X）](https://x.com/lycorptech_jp/status/1889538306335187248)；[Qiita](https://qiita.com/Hiroto_Aso/items/a3dcf80332e30c7b1991)
- LINE Notify 已於 2025 年終止，通知類需求要改用 Messaging API — [ke2b](https://ke2b.com/en/line-notify-closing-alt/)
- 官方 Node.js SDK 是 `@line/bot-sdk`（line/line-bot-sdk-nodejs，Apache-2.0），需要 Node.js 22 以上 — [GitHub: line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs)
- **現成 +1 群組 bot 的限制**：只支援「LINE 群組」和「多人聊天室」，LINE 社群（OpenChat）不能用；群組裡如果已有其他 bot，就無法加入 — [CYBERBIZ](https://help.cyberbiz.io/ec/integrations/line/group-buy/line-group-buy-shopping/)；[飛比 +1](https://one.feebee.com.tw/article/line-group)
- LINE Engineering 官方部落格有用 ChatGPT 做「LINE Bot 群組聊天摘要生成器」的教學，也就是 bot 讀取群組訊息後交給 LLM 處理 — [LINE Engineering](https://engineering.linecorp.com/zh-hant/blog/linebot-chatgpt)
- LINE 可以匯出聊天記錄：手機版「傳送聊天記錄」、電腦版「儲存聊天」，都是 .txt 純文字，不含圖片／貼圖 — [AirDroid](https://www.airdroid.com/zh-tw/app-tips/export-line-chat-history/)

### Inferences
- **「群組打菜單自動跳商品」的做法**：
  1. webhook 收到 `source.type=group` 的 text message。
  2. 比對關鍵字「菜單」（或「今日」「開團」）。
  3. 用該事件的 replyToken 回覆 1–5 個 Flex carousel，每個最多 12 項，所以一次最多 60 項商品。
  4. 每個 bubble 放「+1」postback 按鈕，或連到 LIFF／網站的商品頁。
  
  整個流程只用 Reply API，不計訊息費。商品更多時，就回一張「完整菜單」連結。
- **群組 push 很快就會燒光額度**（試算）：
  - 300 人群組，push 一次約 300 通。輕用量每月 200 通，連一次都不夠；中用量 3,000 通，大約只夠 10 次群組推播。
  - 設計原則：只在有人說話時用 reply；訂單確認、出貨通知改成 1:1 push（對方須是好友），或乾脆不推、讓客人到網頁／LIFF 查。
  - 每月幾百單、每單 1:1 push 2 則（成立＋出貨），約數百到一千多則，需要中用量（2026-11 起 NT$1,000／月）；不然就改成 reply 或網頁通知。
- **換系統的導入步驟**：一個群組只能有一個 OA，所以要先把舊 App 的 bot 移出群組。要另外準備 bot 不在場時的備案：店家匯出聊天 .txt → 後台貼上 → AI 解析。這很可能就是「AI 直接把群組訂單整理成一張一張」的其中一種實作。
- **改單與取消**：Edit／Unsend 事件很適合用來偵測改單和取消，但 Edit 目前還在 LINE Labs 試用、只有部分使用者能用，不能當成唯一依據。仍需要文字指令（「取消」「改 3 盒」）加上後台人工確認。
- **會員**：最自然的做法是用 LINE Login／LIFF 取得 userId，對應到群組 webhook 裡的 userId，這樣「群組 +1 的人」就能直接對上「網站會員」。

### Gaps
- developers.line.biz 的全文讀不到，以下幾點沒有找到官方明文：
  - bot 是否收到群組內「所有」訊息（不需 @ 標記）。不過多款 +1 SaaS 都依賴這個行為（例如 OrderPally 說明「消費者於 LINE 群組內留言『商品關鍵字+1』，系統會自動分析並成立訂單」— [OrderPally](https://orderpally.com/linegroup/)），強烈暗示答案是「會」。
  - reply token 的有效時間。
  - 群組人數上限（一般認知是 500 人，未查證）。
  - 群組 push 是否把封鎖 OA 的成員也算進通數。
- 同一 provider 底下 userId 跨 channel（LINE Login 與 Messaging API）是否一致，沒有找到官方說明。
- 搜尋摘要提到「2022/12/27 之後 LIFF 無法取得 Group ID」，但無法確認原始出處。
- 台灣 LINE MINI App 的上架審查要求沒有查。

---

## Q3. 用 LLM 把群組自由文字訂單（「+1」「蝦 2 盒」、暱稱、改單／取消）轉成結構化訂單：structured outputs、準確度陷阱、人工確認流程、每 1,000 則的成本

### Takeaway
技術上已經成熟，也很便宜。用 structured outputs 或 strict tool use，可以讓模型輸出一定符合 JSON schema 的訂單草稿。以 2026 年的小型模型估算，每 1,000 則群組訊息的 API 成本約 US$0.1–0.6（Claude Haiku 4.5 約 US$2），對單一店家來說月成本可以忽略。

真正的難點是語意正確性：暱稱、「+1」到底指哪個商品、改單／取消、幫別人訂。因此設計上要「規則先行 → LLM 補位 → 低信心進人工確認佇列」。

### Cited Findings
- **OpenAI Structured Outputs（2024-08）**：
  - 用 constrained decoding，限制模型只能產生符合 schema 的 token。
  - 官方 eval 中，gpt-4o-2024-08-06 在複雜 schema 達到 100% 符合，gpt-4-0613 不到 40%；JSON mode 不保證符合 schema。
  - 只支援 JSON Schema 的子集；新 schema 的第一次請求會有額外延遲；碰到 token 上限時輸出可能被截斷。
  - 論壇有使用者回報 strict 模式沒有完全強制（個案）。
  
  — [OpenAI](https://openai.com/index/introducing-structured-outputs-in-the-api/)；[Maginative](https://www.maginative.com/article/openai-launches-structured-outputs-slashes-prices-for-gpt-4o/)；[Gigazine](https://gigazine.net/gsc_news/en/20240807-openai-structured-outputs)；[OpenAI Community](https://community.openai.com/t/strict-mode-does-not-enforce-the-json-schema/1104630)
- **Claude**：
  - 用 `output_config.format` 做 structured outputs；工具定義加上 `strict: true`，可保證 tool input 符合 schema。
  - Batch API 費用是 50%。
  - 價格（每百萬 tokens，input／output）：
    - Claude Haiku 5.5：US$0.10／0.50（prompt ≤100K tokens；超過則 0.50／2.50）
    - Claude Haiku 4.5：US$1／5
    - Claude Sonnet 5.5：US$2／10
  
  — [Claude Docs: Pricing](https://platform.claude.com/docs/en/about-claude/pricing)；[Claude Docs: Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)；[Claude Docs: Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)（數字取自 Anthropic 官方 claude-api 參考資料中 2026-10-06 的快取模型表；Haiku 4.5 的 US$1／5 與第三方 [getdeploying](https://getdeploying.com/llms/claude-haiku-4.5) 一致）
- **OpenAI 價格（多為第三方彙整站）**：
  - GPT-5 nano：US$0.05／0.40；有一站寫 0.025／0.20。
  - GPT-5 mini：US$0.25／2.00；有一站寫 GPT-5 mini 將於 2026-12-11 停用。
  - 較新的 GPT-5.4 nano：US$0.20／1.25；GPT-5.4 mini：US$0.75／4.50。
  
  — [usagepricing](https://www.usagepricing.com/ai-token-pricing/openai)；[pricepertoken](https://pricepertoken.com/pricing-page/model/openai-gpt-5-nano)；[Spur](https://www.spurnow.com/en/tools/openai-chatgpt-api-pricing-calculator)；[writeworks](https://www.writeworks.ai/ai-updates/openai/pricing)
- **Gemini 價格**：
  - Gemini 2.5 Flash-Lite：多數來源 US$0.10／0.40，有一站寫 0.05／0.20。
  - 3.1 Flash-Lite：US$0.25／1.50；batch 輸出 US$0.75。
  - 3.5 Flash-Lite：US$0.30／2.50。
  - thinking tokens 以輸出價計費，會推高結構化輸出類工作的成本。
  
  — [benchlm](https://benchlm.ai/google/api-pricing)；[morphllm](https://www.morphllm.com/gemini-api-pricing)；[pricepertoken](https://pricepertoken.com/pricing-page/model/google-gemini-2.5-flash-lite)；[CloudZero](https://www.cloudzero.com/blog/gemini-pricing/)
- **台灣現有 +1 系統多半是規則式**：「商品關鍵字 +1」自動成立訂單 — [OrderPally](https://orderpally.com/linegroup/)；「+1 留言自動轉訂單、批次對帳與催款」 — [飛比 +1](https://one.feebee.com.tw/)
- LY Corp 的團購 bot 範例用 Edit／Unsend webhook 處理「反悔」：編輯後 message ID 不變，可以當訂單鍵值 — [LY Corp Tech Blog](https://techblog.lycorp.co.jp/zh-hant/linebot-msg-edit-unsend)

### Inferences
- **建議 pipeline**：
  1. **規則層**：用 regex 處理「+1」「品名＋數字＋單位」「取消」這類高頻固定句型，不需要叫 LLM。
  2. **上下文**：組合最近一則開團文（商品、規格、價格、截止時間）、商品別名表（「蝦蝦」「白蝦」「草蝦」）、該使用者近期的訊息。
  3. **LLM**：用 strict schema 輸出，例如 `{line_user_id, display_name, action: new|modify|cancel, items:[{sku, qty, unit}], for_whom?, confidence, needs_review_reason}`。
  4. **寫入訂單草稿**：`confidence` 低、`modify`、`cancel`、找不到 SKU 的，都進人工佇列。
  5. **店家確認**：在後台一鍵確認，成立正式訂單並扣庫存。
  6. **回饋客人**：有 replyToken 時用 reply 回覆解析結果（免費），否則讓客人到網頁／LIFF 確認。
- **準確度陷阱清單**（推論）：
  - 暱稱或俗名（「蝦蝦」「大隻的」）
  - 單位混用（盒／斤／包／尾，中文數字「兩盒、半斤」）
  - 指涉前文（「同上」「我也要」「+1」指的是哪則開團文）
  - 代訂（「幫我媽 +2」）
  - 一則訊息多品項
  - 改單（「改成 3 盒」「剛剛那個取消」）
  - 跨日或多團同時進行
  - 貼圖、圖片訂單
  - 同品項多規格價格不同
  
  Schema 合法不等於內容正確。
- **成本試算**（假設：每次呼叫 = 系統提示＋菜單 1,500 tokens、訊息 50 tokens、輸出 100 tokens；1,000 則逐則呼叫 → 約 1.55M input + 0.1M output tokens）：

  | 模型 | 每 1,000 則成本（未用快取／batch） |
  |---|---|
  | GPT-5 nano | 約 US$0.12 |
  | Gemini 2.5 Flash-Lite | 約 US$0.20 |
  | Claude Haiku 5.5 | 約 US$0.21 |
  | GPT-5 mini | 約 US$0.59 |
  | Claude Haiku 4.5 | 約 US$2.05 |
  | Claude Sonnet 5.5 | 約 US$4.10 |

  - 每 20 則合併成一次呼叫，input 會降到約 0.13M tokens；以 Haiku 5.5 計約 US$0.06／1,000 則。再加上 prompt caching 或 batch 的 50% 折扣會更低。
  - 結論：就算每月 1 萬則群組訊息，LLM 成本也只有幾美元以內。要注意 reasoning／thinking tokens 以輸出價計費，應把推理強度調到最低。
  - 中文 token 數依 tokenizer 不同，以上只是量級估計。
- **為什麼要人工確認**：「AI 把群組訂單整理成一張一張」最務實的定位是「產生草稿，店家確認」，不是全自動成單。原因是錯單直接牽涉金額和冷凍品備貨，錯了很難挽回。

### Gaps
- 沒有找到針對「中文 LINE 團購訊息解析」的公開準確率基準或論文。
- 各家 LLM 價格多來自第三方彙整站，OpenAI／Google 官方價格頁沒有直接讀到；GPT-5 mini 的停用日期只有單一來源。
- 把顧客聊天內容送到境外 LLM API 的個資法（告知、境外傳輸）要求沒有研究，應交給合規面的研究者。

---

## Q4. 台灣金流物流整合：綠界 ECPay、藍新 NewebPay、PAYUNi 統一金流的超商取貨付款、冷凍店到店（7-11／全家）、宅配（黑貓／新竹）支援度與費用；需要直接串 API 嗎，還是 CSV 匯出就夠？

### Takeaway
各家支援度：
- **7-11 冷凍店取**：有 API 可串。綠界的 B2C 物流子類型有 `UNIMARTFREEZE`；PAYUNi 統一金流支援 7-11 冷凍的大宗寄倉和店到店。
- **全家冷凍**：在綠界的子類型裡找不到；PayNow 有全家冷凍 C2C 的 API。
- **宅配**：可以透過綠界串黑貓。

但直接串 API 要先開通特約商店，B2C 物流還要通過實體「測標」，一週內很難全部上線。比較可能的一週版本是：結帳時收集物流方式和門市資訊，再匯出 CSV／Excel 給店家既有的平台（賣貨便、綠界後台）出貨，之後再升級成 API。

### Cited Findings
- **綠界物流子類型**：
  - B2C 只能帶 FAMI（全家）、UNIMART（7-ELEVEN）、HILIFE（萊爾富）、UNIMARTFREEZE（7-ELEVEN 冷凍店取）其中之一；C2C 有 FAMIC2C 等。
  - 每個子類型都要分別通過「測標」：用雷射印表機列印標籤，寄到指定物流中心驗收，通過後才能建單。
  - 物流對帳檔的溫層代碼：0001 常溫、0002 冷藏、0003 冷凍。
  - 門市清單 API 的 CvsType `UNIMARTFREEZE` 標示為「7-ELEVEN 超商（冷鏈）」。
  - 搜尋結果中沒有看到全家冷凍的子類型。
  
  — [ECPay：門市訂單建立](https://developers.ecpay.com.tw/8809/)；[ECPay：一段標測試資料產生（B2C）](https://developers.ecpay.com.tw/10102/)；[ECPay：測試標籤資料產生](https://developers.ecpay.com.tw/7402/)；[ECPay：下載物流對帳檔](https://developers.ecpay.com.tw/50594/)；[ECPay：取得門市清單](https://developers.ecpay.com.tw/47496/)；[ECPay：門市電子地圖](https://developers.ecpay.com.tw/8795/)
- **綠界費用**：
  - 超商店到店（C2C）取貨付款運費 65 元（7-ELEVEN、全家）。
  - 代收手續費原價 1%，優惠 0.75%，每筆最低 3 元。
  - 純取貨只收運費；最終結算另加 5% 營業稅。
  - B2C 大宗寄倉運費 55 元起。
  - 第三方說超商取貨付款代收款每週二撥款。
  
  — [ECPay 服務費率表](https://www.ecpay.com.tw/Business/payment_fees)；[ECPay 物流寄件服務費用說明](https://support.ecpay.com.tw/15275/)；[ECPay 物流費用總覽](https://www.ecpay.com.tw/IntroTransport/Service_Fee)；[BVSHOP](https://bvshop.tw/article/22)。⚠️ 有教學文寫 0.5%，和官方的 0.75% 不同，可能是特約費率或舊資料。
- **綠界黑貓宅配規範**：總重 ≤20 公斤；低溫包裹長＋寬＋高 ≤120 公分，常溫 ≤150 公分；今天寄、明天到；可用 12 碼託運單號查件 — [ECPay 黑貓規範手冊 PDF](https://www.ecpay.com.tw/Content/files/ecpay_029.pdf)
- 全家從 2026-04-28 起導入黑貓，提供常溫、冷藏、冷凍多種溫層的寄件 — [自由時報](https://ec.ltn.com.tw/article/breakingnews/5418218)
- **PAYUNi 統一金流**：
  - 物流 API 涵蓋 7-ELEVEN 大宗寄倉和店到店（C2C）的冷凍與常溫，可取貨付款。
  - 官方費用頁：7-ELEVEN 大宗寄倉冷凍每件 125 元；取貨付款代收費每筆 0.5%，不足 1 元以 1 元計。
  - 如果沒在後台設定「限定 API 之 IP」，幕後交易會被拒絕。
  - 7-11 超商取貨的撥款天數是付款日後 7 天。
  - WP 外掛提醒要用固定 IP 的主機。
  
  — [PAYUNi 開發專區](https://docs.payuni.com.tw/web/)；[PAYUNi 費用](https://www.payuni.com.tw/fee)；[ShopStore 金流設定](https://shopstore.tw/teachinfo/643)；[ShopStore 物流設定](https://shopstore.tw/teachinfo/649)；[WPBrewer](https://wpbrewer.com/product/wpbr-payuni-shipping/)；[BV SHOP](https://bvshop.tw/teachInfo/176)
- PayNow 的 API 文件涵蓋「全家冷凍 C2C」：電子地圖、建立、查詢、取消物流單、貨態回傳 — [PayNow API](https://owlting.github.io/paynow-guideline/docs/api-reference/)
- 全家冷凍店到店有地區限制，只開放本島寄本島、本島寄離島、離島寄本島 — [FamiPort 寄件店到店說明](https://fmec.famiport.com.tw/FP_Entrance/Notice)
- **7-11 冷凍交貨便**（多為部落格與消費資訊網站，非官方）：
  - 單件約 5 公斤以內。
  - 2025-04-01 起可以用自備紙箱。
  - 取件期限通常 7 天。
  - 運費說法互相矛盾：一說 90–130 元，另一份 2026 年整理則是本島 200 元、離島 335 元。
  
  — [roo.cash](https://roo.cash/blog/convenience-store-frozen-delivery/)；[StockFeel](https://stockfeel.com.tw/7-11-%e5%ba%97%e5%88%b0%e5%ba%97-%e4%ba%a4%e8%b2%a8%e4%be%bf%e9%81%8b%e8%b2%bb)；[NOWnews](https://www.nownews.com/news/6121773)
- 藍新 NewebPay：沒有找到物流（超商取貨／冷凍）的規格與費用；官方 API 文件下載點是 https://www.newebpay.com/website/Page/content/download_api（由 Laravel 套件說明指出）— [Packagist laravel-newebpay](https://packagist.org/packages/datomon/laravel-newebpay)

### Inferences
- **一週版本最可能的做法**：
  1. 結帳時讓客人選 7-11 冷凍、全家、宅配或面交，並記下門市店號。
  2. 依物流方式套用運費規則和免運門檻。
  3. 後台把訂單按物流方式分組，匯出到店家原本就在用的出貨管道：7-11 走賣貨便／交貨便批次匯入（見 Q5）；宅配走黑貓或綠界後台的大量匯入，或手寫託運單。
  
  直接串 API 要先申請特店、B2C 每個子類型都要寄實體標籤測標、還有正式和測試兩套金鑰，前置作業可能要好幾天到好幾週，不太可能塞進一週的開發期。
- **冷凍品的實際選擇**：
  - 7-11 冷凍：綠界 UNIMARTFREEZE（B2C），或 PAYUNi（B2C 和 C2C 都有）。
  - 全家冷凍：PayNow，或全家自己的寄件服務。
  - 宅配冷凍：黑貓（可透過綠界），或直接和物流商簽約。
  
  PAYUNi 和 7-11 同屬統一集團，冷鏈選項看起來最完整。
- **Serverless 部署的坑**：
  - PAYUNi 要求 API 呼叫來源 IP 白名單，但 Vercel／Cloudflare 這類 serverless 預設沒有固定出口 IP，需要固定 IP 的代理或 VPS。
  - 綠界提醒 ReturnURL 不要設在國外 CDN 網址上，而 Vercel／Cloudflare 本身就是 CDN 架構。可能需要獨立的回呼端點；實際影響沒有驗證。
- **其他細節**：
  - 簽章驗證（CheckMacValue／Hash）
  - 撥款時程不同（每週二、7 天）
  - 手續費另加 5% 稅
  - 冷凍包裹尺寸和重量上限
  - 取件期限 7 天，逾期退回後要回補庫存和退款
- **取貨付款（COD）不一定要串金流**：如果店家用賣貨便的取貨付款，系統只要把訂單標記為 COD 並記錄應收金額，等賣貨便撥款後再人工或匯入對帳就好。

### Gaps
- 藍新的物流能力（冷凍、全家、萊爾富）沒查到。
- 新竹物流、黑貓直接簽約的 API 沒查到。
- 綠界有沒有全家冷凍子類型無法確認，只看到 FAMI 和 FAMIC2C。
- 7-11 冷凍交貨便的現行官方運費沒查到，來源互相矛盾。
- 各家特店申請、測標實際需要幾天，沒有官方數字。

---

## Q5. 7-11 賣貨便有 API 或批次匯入（批次建立／批次出貨）嗎？「賣貨便一鍵匯出」技術上可能是什麼？

### Takeaway
沒有找到賣貨便的公開 API。不過賣貨便（交貨便）有官方的「批次匯入」功能：下載範例 Excel、照格式填好上傳，每次最多 100 筆，而且只支援 Windows 版 Excel。之後可以把多筆交貨便代碼一次送到 OPEN POINT App，到 ibon 一次印完。

所以「賣貨便一鍵匯出」最可能是：系統把訂單轉成官方範例檔格式的 .xlsx（每個檔 ≤100 筆），店家再拿去上傳。

### Cited Findings
- **官方批次匯入頁**：要使用範例檔填寫；目前只支援 Windows 系統的 Microsoft Excel；批次匯入單次上限 100 筆 — [7-ELEVEN 交貨便：批次匯入](https://myship2.7-11.com.tw/C2C/Import)
- 賣貨便說明中心：匯入功能適合在外部接單、代客下單的賣家；大量訂單匯入和合併訂單不能使用折價券／折扣碼 — [7-ELEVEN 賣貨便說明中心](https://myship.7-11.com.tw/Home/HelpCenter)
- **一次列印多張**：在賣貨便勾選多筆訂單，把交貨便代碼傳到「OPEN POINT」App，再到 ibon 掃 QR Code 一次列印 — [傑昇通信](https://www.jyes.com.tw/news.php?act=view&id=9357)。有使用者分享，上傳範例檔後還要在 OPEN POINT App 的「寄件 → 我的包裹」完成匯入，才能到 ibon 列印（個人經驗，非官方）— [Threads 使用者分享](https://www.threads.com/@yang.badminton.diary/post/DDO_nFzyqus?hl=zh-tw)
- 賣家後台可以勾選待出貨訂單批次列印交貨便服務單（快收便）— [ShixiNote](https://shixinote.com/%E8%B3%A3%E8%B2%A8%E4%BE%BF%E6%95%99%E5%AD%B8/)

### Inferences
- **「一鍵匯出」的實作**（推測）：
  1. 把待出貨、物流選「7-11」的訂單，依官方範例檔欄位對應：收件人、電話、取件門市、品名、金額、是否取貨付款等。
  2. 用 SheetJS／exceljs 產生 .xlsx。因為官方只支援 Windows Excel，應產生真正的 xlsx，不要用 CSV。
  3. 超過 100 筆就自動切成多個檔案；冷凍和常溫是否要分開，視範本而定。
  4. 店家上傳後，再到 OPEN POINT／ibon 批次列印。
- **實作細節**：
  - 結帳時就要拿到正確的 7-11 門市店號：可以用金流商的電子地圖 API，或請客人自己填。
  - 電話前導 0、門市代碼要以文字格式寫入。
  - 範本欄位如果被官方改掉，匯出就會悄悄失效，所以要做欄位驗證，再測一次「上傳 1–2 筆」。
- **跟優惠碼的關係**：官方說批次匯入不能套折價券。這對店家的影響不大，因為優惠碼是在店家自己的網站上折抵，不是在賣貨便上。

### Gaps
- 官方範例檔的實際欄位和格式沒有讀到（頁面無法直接抓取）。
- 批次匯入是否支援冷凍交貨便、是否支援取貨付款欄位，沒有確認。
- 賣貨便是否禁止自動化操作（爬蟲／RPA）的條款沒有查到。

---

## Q6. 轉帳對末五碼：常見實作與失敗模式；以及用金流商的虛擬帳號替代

### Takeaway
「對末五碼」本質上是人工或半自動比對銀行明細：客人回報帳號末五碼、金額和時間，店家再對照網銀明細。已知的失敗模式包括：網路轉帳的明細少一碼、卡號和帳號搞混、客人不願提供末五碼、同金額撞單、合併付款、短付或溢付。

替代方案是虛擬帳號（例如綠界 ATM）：每筆訂單配一組專屬帳號，付款完成後自動回呼 ReturnURL。費用依第三方資料約 1%，最低 NT$15。

### Cited Findings
- **末五碼對不上的原因**：網路轉帳（例如 e 動郵局）的明細常會少掉「末一碼」，或只顯示「網路轉帳」；金融卡上印的不一定是帳號；團購主分享過對帳教學 — [Jill 部落格：後五碼對帳教學](https://jillpunk.pixnet.net/blog/posts/13210958651)；[PTT Bank_Service](https://www.ptt.cc/bbs/Bank_Service/M.1400146823.A.D3D.html)；[PTT Chat82gether](https://www.ptt.cc/bbs/Chat82gether/M.1417708486.A.538.html)
- 有店家因為要求客人提供末五碼而起爭議，客人擔心帳號被盜用 — [ETtoday](https://house.ettoday.net/news/2215796)
- **綠界 ATM 虛擬帳號**：
  - ExpireDate 可設 1–60 天，預設 3 天，以到期日當天 23:59 為限。
  - 虛擬帳號資訊回傳到 PaymentInfoURL；銀行確認入帳後，付款結果才回傳到 ReturnURL。
  - 收到通知要回應 `1|OK`，這只代表「收到」，不會改變付款狀態。
  - 過期才繳款不會有通知；短繳、溢繳、重複繳會回傳交易失敗通知。
  - 後台可用「模擬付款」測試。
  - ReturnURL 要能對外連線、不要設在國外 CDN 網址；摘要稱只支援 https（443 埠）。
  
  — [ECPay：ATM 虛擬帳號付款](https://developers.ecpay.com.tw/2872/)；[ECPay：付款結果通知](https://developers.ecpay.com.tw/28010/)；[ECPay：ReturnURL](https://developers.ecpay.com.tw/9058/)；[ECPay Support：WebATM 與 ATM 虛擬帳號常見問題](https://support.ecpay.com.tw/16452/)；[iT 邦幫忙：PaymentInfoURL 與 ClientRedirectURL](https://ithelp.ithome.com.tw/articles/10349127)
- 綠界 ATM 虛擬帳號費率 1%，最低 15 元，未稅（結算加收 5% 營業稅）。這是第三方資料，以合約為準 — [site-now](https://site-now.app/ecpay-review/)
- 虛擬帳號轉帳失敗常見原因是金額或帳號輸入錯誤、超過繳費時效 — [citiesocial 說明](https://citiesocial.zendesk.com/hc/zh-tw/articles/205016280--%E8%BD%89%E5%B8%B3%E5%A4%B1%E6%95%97%E7%9A%84%E5%8E%9F%E5%9B%A0)

### Inferences
- **「對末五碼」的典型實作**（推測）：
  1. 訂單頁顯示店家帳號和應付金額。
  2. 客人在網站或 LIFF 回報「末五碼＋轉帳金額＋轉帳時間」。
  3. 後台匯入網銀 CSV 明細，或店家手動對照。
  4. 系統用 (末五碼, 金額, 日期 ±1–2 天) 比對，候選唯一就自動標記「已付款」，否則列入人工佇列。
  
  付款狀態要寫進「付款紀錄表」，而不是只改訂單上的一個欄位，才能處理部分付款和溢付。
- **失敗模式與對策**：

  | 情況 | 對策 |
  |---|---|
  | 同末五碼、同金額撞單 | 加時間窗；請客人附備註 |
  | 用家人帳號轉帳 | 允許人工綁定 |
  | 一筆轉帳付兩張訂單 | 支援一筆付款對多張訂單 |
  | 短付或溢付 | 溢付轉購物金，短付要求補差額 |
  | 跨行、假日入帳延遲 | 延後自動取消訂單的期限 |
  | 網路轉帳少一碼 | 支援模糊比對（後 4 碼）＋人工確認 |
  | 客人打錯 | 允許客人修改回報資料 |

- **何時改用虛擬帳號**：一張 NT$1,000 的訂單用虛擬帳號，手續費約 NT$15（1.5%）。對毛利薄的海鮮團購來說不便宜，所以小店繼續「末五碼＋人工」很合理。等月單量變大、對帳人力成本高過手續費時，再改虛擬帳號。

### Gaps
- 沒有研究台灣各銀行是否提供入帳通知 API 或 webhook（例如企業網銀 API）。
- 藍新、PAYUNi 虛擬帳號的費率沒有查證。
- 綠界 ATM 費率只有第三方來源。

---

## Q7. Web app 掃條碼（BarcodeDetector API 支援度、ZXing／html5-qrcode）、庫存異動、毛利報表基礎

### Takeaway
Web 端可以做到，但 iOS Safari 至今仍不支援 BarcodeDetector（預設停用），必須準備 ZXing／ZBar-WASM 這類 fallback。後台進貨最簡單可靠的做法，是用 USB 或藍牙的「鍵盤模擬」掃描槍：不需要驅動，掃到的內容直接輸入到目前聚焦的欄位。

庫存應該用「異動流水帳」記錄；毛利報表就是銷售額減掉成本。

### Cited Findings
- **BarcodeDetector 支援度**：
  - Safari iOS 3.2–16.7 不支援；17.0–26.6 為「預設停用」；27.0 仍是預設停用。
  - Chrome 標示為部分支援。有 DEV 文章說 Chrome 134 已預設開啟，與 caniuse 的「部分支援」說法不完全一致。
  
  — [caniuse: BarcodeDetector](https://caniuse.com/mdn-api_barcodedetector)；[DEV（jamiepark）](https://dev.to/jamiepark-design/building-a-zero-dependency-barcode-scanner-with-the-web-barcode-detection-api-246k)
- 在有支援的瀏覽器上，可以設定偵測 QR Code、EAN-13、Code 128 — [Scanbot 教學](https://scanbot.io/techblog/barcode-detection-api-tutorial/)；規格文件 — [WICG Shape Detection API](https://wicg.github.io/shape-detection-api/)；PWA 能力示範 — [What PWA Can Do Today](https://whatpwacando.today/barcode/)
- iOS 常見的替代做法是把 ZBar 等解碼器編譯成 WASM。DEV 文章引用 WebKit bug #254573 — [DEV（ilhannegis）](https://dev.to/ilhannegis/barcode-scanning-on-ios-the-missing-web-api-and-a-webassembly-solution-2in2)；也有專案在 issue 中討論 iOS Safari 的 fallback 需求 — [GitHub issue](https://github.com/jasonkryst/BookWheel/issues/187)
- **鍵盤模擬（HID wedge）掃描槍**：
  - 行為就像鍵盤，不需要 COM port 或驅動，掃描結果直接輸入到聚焦的文字框。
  - Web app 要自己管理 focus。
  - 建議把掃描槍設定成結尾送 Enter 自動送出，並加前綴以區分掃描和人工打字。
  - 要開啟 EAN-13；app 端應驗證檢查碼（前 12 碼以 1、3 交替加權）。
  
  — [iMerchant: Wedge scanners](https://imrchnt.screenstepslive.com/s/17626/a/835522-wedge-scanners)；[IDAutomation 整合指南](https://www.idautomation.com/barcode-scanners/integration-guide/)；[Zebra 開發者討論](https://developer.zebra.com/thread/36876)；[IronSoftware（EAN-13 檢查碼範例）](https://ironsoftware.com/zh/barcode/csharp/blog/using-ironbarcode/csharp-usb-barcode-scanner/)

### Inferences
- **「掃條碼進貨」最可能的實作**：後台「進貨單」頁放一個常駐 focus 的輸入框，搭配幾百元的 USB 掃描槍。每掃一次就 +1 數量，或掃完再輸入數量。手機掃描只是加分功能：Android Chrome 用 BarcodeDetector，iOS 用 WASM／ZXing fallback。
- **海鮮的特殊性**：
  - 很多冷凍海鮮是秤重、分裝的，原包裝不一定有條碼。店家可能需要自印內部條碼（Code 128，或店內碼）。
  - 秤重商品的「數量」最好以 g 或份記錄。
- **資料模型**（推測）：
  - `products / variants`：SKU、條碼、規格（盒／斤）、售價。
  - `stock_movements`：type = purchase_in / sale_out / adjust / return / waste，記錄 qty、unit_cost、ref_id、created_by。
  - 庫存 = Σ movements，或另存快照並定期核對。
  - 冷凍海鮮的損耗、報廢一定要有獨立的異動類型，否則毛利會被高估。
- **毛利報表**：
  - 營收 = Σ 已完成訂單的實收金額（扣掉折扣、購物金折抵，運費另計）。
  - 銷貨成本（COGS）用移動加權平均成本，或 FIFO 批次成本。
  - 毛利 = 營收 − COGS；毛利率 = 毛利 ÷ 營收。
  - 依商品、團次（開團日）、物流方式分組。
  - 要事先決定購物金在報表上算「折扣」還是「付款方式」，否則報表會不一致。

### Gaps
- html5-qrcode、@zxing/browser 在 2026 年的維護狀態和 iOS 表現沒有查證（搜尋沒有拿到相關資料）。
- 沒有官方 MDN 頁面全文，因為 DNS 失敗。

---

## Q8. 金額邏輯正確性：「35 種情況」大概涵蓋什麼？最佳實務（整數金額、購物金帳本、金流回呼冪等、表格驅動與性質測試）

### Takeaway
貼文舉的兩個例子是「改單會不會吃掉訂金」和「退款購物金有沒有還回去」，正好是「訂金 × 改單」和「購物金 × 退款」的交叉案例。

可靠的做法有：
- 金額一律用整數（新台幣元）。
- 購物金用只能新增、不能修改的帳本（餘額由分錄加總而來），修正一律用沖銷分錄。
- 所有金流和 LINE 回呼都按事件 ID 去重（冪等）。
- 用表格驅動測試窮舉組合，再加上性質測試（例如 fast-check）驗證不變式。

### Cited Findings
- **Stripe 冪等鍵**：同一個 idempotency key 的第一次請求結果（狀態碼和內容，包括失敗）會被保存，之後重送都回傳相同結果；建議用 V4 UUID；連線錯誤時可以安全重試，不會重複建立或更新 — [Stripe Docs: Idempotent requests](https://docs.stripe.com/api/idempotent_requests)
- **Webhook 去重**：用「已處理事件表」，以事件 ID 為主鍵、`INSERT … ON CONFLICT DO NOTHING` 一次原子寫入，避免兩次並行重送都通過檢查；第三方引述 Stripe 文件說 webhook 不保證 exactly-once，也不保證順序 — [Inquir](https://inquir.org/blog/idempotency-making-webhooks-and-jobs-safe-to-retry)；[Axonbuild](https://axonbuild.com/blog/how-to-make-a-webhook-handler-idempotent/)；[Peerlist（Yoann Jaspar）](https://peerlist.io/yjaspar/articles/idempotent-stripe-webhooks-in-nodejs-typescript-patterns-tha)
- LINE webhook 也會重送，官方建議用 `webhookEventId` 去重 — [LINE Developers: Receive messages](https://developers.line.biz/en/docs/messaging-api/receiving-messages/)。綠界：重複繳款會回傳交易失敗通知；收到通知要回 `1|OK` — [ECPay：ATM 虛擬帳號付款](https://developers.ecpay.com.tw/2872/)
- **帳本設計**：
  - 餘額由不可變分錄加總得出，不另存可直接改寫的餘額欄位。
  - 每筆交易的借貸要能平衡（總和為 0）。
  - 錯誤用「沖銷分錄」修正，不修改原分錄；可以在 DB 層禁止 UPDATE／DELETE。
  - 金額用 BIGINT 存最小單位。
  - 用列鎖或 serializable 交易處理並行；用冪等鍵防止重試時重複扣款。
  - 每晚對帳。
  
  — [GitHub: double-entry-wallet-ledger](https://github.com/Vrinda-Vijay5/double-entry-wallet-ledger)；[DEV：Designing a Digital Wallet With a Double-Entry Ledger](https://dev.to/roni_das_b1b76c5ee6583027/designing-a-digital-wallet-with-a-double-entry-ledger-dik)；[Modern Treasury ebook](https://www.moderntreasury.com/ebooks/building-a-digital-wallet-from-ledger-to-launch)；[GitHub: WalletLedger](https://github.com/KunMonanz/WalletLedger)；[ScaleDojo](https://scaledojo.dev/blogs/double-entry-ledger-design-the-500-year-old-system-that-powers-banking)
- **性質測試**：fast-check 是 JS／TS 的 property-based testing 函式庫，會自動產生輸入、跑數百個案例，失敗時縮小（shrink）到最小反例；可整合 Vitest、Jest、Node test runner — [fast-check 官方介紹](https://fast-check.dev/docs/introduction/)；[PkgPulse](https://www.pkgpulse.com/guides/property-based-testing-fast-check-javascript-2026)
- 綠界超商取貨付款的代收手續費是 0.75%，最低 3 元（「應收金額」和「實際撥款」會有差額，要列入對帳）— [ECPay 服務費率表](https://www.ecpay.com.tw/Business/payment_fees)

### Inferences
- **「35 種情況」可能的測試矩陣**（推測，依貼文提到的功能組合拼出來）：

  | 類別 | 案例 |
  |---|---|
  | A 基本計價 | 1 未達免運加運費；2 剛好等於免運門檻；3 差 1 元；4 各物流運費不同（7-11 冷凍／全家／宅配／面交 0 元）；5 多規格單價×數量；6 商品調價後舊訂單維持價格快照 |
  | B 優惠碼 | 7 固定金額折抵；8 百分比折扣的整數進位規則；9 最低消費門檻與免運誰先算；10 過期、用量用完、每人限用一次（含並發）；11 折扣大於商品金額時不得為負；12 只適用特定商品 |
  | C 購物金 | 13 部分折抵；14 全額折抵（應付 0，不產生轉帳或 COD）；15 與優惠碼疊加的順序；16 可否折抵運費；17 兩個分頁同時使用（不得超扣）；18 到期 |
  | D 訂金／改單 | 19 付訂金後加品項，尾款增加；20 減品項，若低於訂金，差額退購物金或現金；21 整單取消時訂金的處理；22 改單時訂金不能被當成折扣「吃掉」；23 訂金＋取貨付款：代收額 = 總額 − 訂金 − 購物金；24 改物流方式造成運費變動 |
  | E 退款 | 25 部分退款（缺貨一項），退回該品項分攤折扣後的實付；26 全額退款：購物金退回購物金、現金退回現金；27 退款後優惠碼是否恢復；28 重複點退款（冪等）；29 退款後不再滿足免運，運費是否追回；30 出貨後退貨的運費負擔 |
  | F 付款對帳 | 31 轉帳短付；32 溢付轉購物金；33 一筆轉帳付兩張訂單；34 取貨付款未取件退回（狀態、庫存、購物金回補）；35 金流回呼重送不得重複入帳 |

- **建議的不變式**（給 fast-check 或表格測試用）：
  - 應付金額 ≥ 0。
  - Σ付款 − Σ退款 = 訂單淨額。
  - 購物金餘額 = Σ分錄，且永遠 ≥ 0。
  - 單筆退款 ≤ 該筆已付金額。
  - 各品項分攤後的實付加總 = 小計 − 折扣。
  - 改單前後，已付訂金總額不變；改單只會改變尾款，或產生退款／購物金分錄。
  - 同一個冪等鍵重放，結果完全相同。
- **實作要點**：
  - 新台幣一律用整數「元」。百分比折扣的進位規則（四捨五入、無條件捨去）只在一個函式裡定義，所有地方共用。
  - 訂單明細要存價格快照。
  - 付款、退款、購物金分錄都分別成表，訂單上的「已付」「餘額」由這些表推導。
  - 改單用「調整紀錄」，不要直接覆寫訂單金額。
  - 金流、LINE 回呼表以 (provider, event_id) 設 unique。
- **AI 寫金額邏輯的風險**：這正是 Stack Overflow 調查裡「差一點對」最危險的地方。比較好的流程是：先讓 AI 依上表產生測試案例（table-driven），人工逐案核對預期值，再讓 AI 改實作直到全部通過。這也是「一週改 73 次、每次都測過才上」的合理解讀。

### Gaps
- 貼文的 35 個案例實際內容不公開，上表是推測。
- 沒有找到台灣小型電商針對「訂金＋購物金＋取貨付款」的公開事故案例或規範。
- 電子發票（折讓、作廢）與金額的連動不在本題範圍，沒有研究。

---

## Q9. 讓獨立開發者一天安全部署約 10 次的實務（CI 測試、preview 部署、資料庫 migration、回滾）

### Takeaway
要一天安全部署 10 次，需要這幾件事：每次 push 都自動跑測試（尤其是金額矩陣）、每個 PR 都有 preview 部署（含 DB preview branch）、正式環境出問題可以一鍵回滾，而且 migration 必須向後相容。要注意：回滾 app 不會回滾資料庫。

DORA 2025 明確指出，沒有這些控制機制時，AI 帶來的高變更量會轉成不穩定。

### Cited Findings
- DORA 2025：缺乏強健的自動化測試、成熟的版本控制、快速回饋迴路時，變更量增加會導致不穩定 — [DORA: Balancing AI tensions](https://dora.dev/insights/balancing-ai-tensions/)；[DORA 2025 報告 PDF](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf)
- **Supabase Branching**：
  - 開 PR 時，GitHub app 會建立 Preview Branch，並執行 `./supabase/migrations` 裡的 migration；錯誤會顯示在該 commit 的 Check Run。
  - 之後新增的 migration 檔會增量執行。
  - merge 到主分支時，會對正式資料庫執行 migration。
  - 搭配 Vercel 整合時，Supabase 會自動把 preview branch 的環境變數寫入 Vercel 對應的 preview。
  - 兩邊可能有 race condition，所以 Supabase 會自動重新部署該 PR 最新的 deployment。
  - Branching 2.0（public alpha）不需要 GitHub 也能用。
  
  — [Supabase Docs: Branching integrations](https://supabase.com/docs/guides/deployment/branching/integrations)；[Supabase Branching](https://supabase.com/features/branching)；[Supabase Blog](https://supabase.com/blog/supabase-branching)
- **Vercel 方案**：
  - Hobby 方案禁止商業用途；商業用途定義很廣，包括收款、廣告、接受捐款等。
  - Pro 約 US$20／月。有來源說是平台費含 1 個部署席位和 US$20 用量額度，也有來源說是每位開發者 US$20，計價方式說法不一。
  - Pro 含 1 TB 傳輸，超過每 GB US$0.15；Hobby 上限 100 GB。
  
  — [MakerKit](https://makerkit.dev/blog/saas/vercel-cost)；[Costbench](https://costbench.com/software/developer-tools/vercel/)；[Supadrop](https://supadrop.host/blog/vercel-pricing-free-tier-limits/)；[temps.sh](https://temps.sh/blog/vercel-pricing-complete-guide-2026)
- Vercel 回滾（Instant Rollback）的官方說明在 https://vercel.com/docs/deployments/rollbacks（第三方頁面指出，本次未能讀取驗證）— [Smithery skill 頁](https://smithery.ai/skills/sgcarstrends/deployment-rollback)
- Next.js + Supabase 用 GitHub Actions 做 CI/CD 的教學 — [iloveblogs](https://www.iloveblogs.blog/guides/nextjs-supabase-cicd-github-actions-production)

### Inferences
- **一人每天 ~10 次部署的流程**（推測）：
  1. 主幹開發，每個變更都很小（agent 一次只改一件事）。
  2. push 後由 GitHub Actions 跑：型別檢查、lint、單元測試（含 Q8 的金額矩陣和性質測試）、少量 Playwright 冒煙測試（下單→付款→出貨匯出）。
  3. 產生 preview URL，搭配 Supabase preview branch 和測試資料。
  4. 用另一個 LINE channel（staging bot）加入測試群組，在 preview 上驗收。
  5. merge 後自動部署正式環境。
  6. 出錯時一鍵回滾到上一版。
- **Migration 原則**：
  - 採「擴充 → 遷移 → 收斂」（expand／contract）：先加欄位或資料表、讓新舊程式都能跑，之後再移除舊欄位。
  - 金額相關的 migration 要附資料修補腳本和對帳查詢。
  - 因為 app 回滾不會回滾 DB，破壞性的 migration 不能和功能變更放在同一次部署。
- **多租戶時**：用 feature flag 逐店開啟新功能，避免一次部署影響全部客戶。
- **AI agent 的角色**：讓 agent 在每次提交前「先跑測試再 commit」（寫在 CLAUDE.md 等專案說明裡），是「每次都測過才上」最低成本的落實方式。

### Gaps
- Vercel 官方回滾文件、Vercel 正式價格頁沒能直接讀到。
- Cloudflare Workers／Pages 的 preview 和 rollback 機制沒有查證。
- 「73 次」指的是 commit、部署還是 PR，貼文沒有說明。

---

## Q10. 每位客戶的每月營運成本估算（主機、DB、LINE OA 方案、LLM API、網域）與工時估算（從零開發 vs 既有模板）

### Takeaway
如果是多租戶共用一套部署，每家店的邊際基礎設施成本大約是每月 NT$150–250，再加上 LINE OA 方案：只用 reply 可以停在輕用量 NT$0；要 1:1 推播通常需要中用量，2026-11 起 NT$1,000／月。LLM 費用通常每月不到 US$2。

如果每家店都獨立一套（Supabase Pro + Vercel Pro），光基礎設施就約 US$45／月（約 NT$1,400，假設 1 USD ≈ 30–33 TWD）。所以「299 起」的價格只有在共用基礎設施、LINE 盡量只用 reply 的前提下才合理。

工時方面，以 AI 輔助、一人開發的推估：從零做約 70–130 小時，從自有模板改約 25–50 小時。一週做完，代表作者大概率已有模板。

### Cited Findings
- **Supabase**：
  - Free：一週沒活動就暫停、最多 2 個 active 專案、DB 500 MB。
  - Pro：US$25／月，含 US$10 compute 額度（約等於一個 Micro 專案）；另計 compute、超過 8 GB 的儲存、超過 250 GB 的 egress。付費方案不會因為沒活動而暫停。
  - Team：US$599／月。
  
  — [Supabase Pricing](https://supabase.com/pricing)；[MakerKit](https://makerkit.dev/blog/saas/supabase-pricing)；[Jetadmin](https://www.jetadmin.io/blog/supabase-pricing-2026-guide-to-plans-limits-and-real-world-costs/)；[omidsaffari](https://omidsaffari.com/blog/supabase-pricing)
- Vercel：Hobby 禁止商用；Pro 約 US$20／月（計價方式說法不一，見 Q9）— [MakerKit](https://makerkit.dev/blog/saas/vercel-cost)；[Costbench](https://costbench.com/software/developer-tools/vercel/)
- **Cloudflare Workers Paid**：
  - 每帳號每月最低 US$5，含 Workers、Pages Functions、KV、Hyperdrive、Durable Objects 用量；egress 不另收費。
  - 官方表格寫每月含 2,000 萬次請求，超過每百萬次 US$0.60；第三方計算器寫 1,000 萬次，兩者矛盾。
  - Free：每日 10 萬次請求、每次呼叫 10 ms CPU。
  - D1 價格只有第三方說法，彼此矛盾。
  
  — [Cloudflare Workers Pricing](https://developers.cloudflare.com/workers/about/pricing)；[MakerKit 計算器](https://makerkit.dev/pricing-calculator/cloudflare)
- LINE OA 台灣方案：輕用量 NT$0（200 則）；中用量 NT$1,000（3,000 則，2026-11-01 起）；高用量 NT$1,400（6,000 則）；未稅 — [LINE Biz-Solutions](https://tw.linebiz.com/column/LINEOA-2026-Price-Plan/)；[chatbotta](https://chatbotta.com/guides/line-oa-pricing/)
- LLM 價格見 Q3：Claude Haiku 5.5 US$0.10／0.50、GPT-5 nano US$0.05／0.40、Gemini 2.5 Flash-Lite US$0.10／0.40（每百萬 tokens）— [Claude Docs: Pricing](https://platform.claude.com/docs/en/about-claude/pricing)；[usagepricing](https://www.usagepricing.com/ai-token-pricing/openai)；[benchlm](https://benchlm.ai/google/api-pricing)
- **網域**：Gandi 的 .tw 原價 NT$744／年（2025-08 至 10 月促銷 NT$262）；.com.tw 只限已登記的公司註冊 — [Gandi .tw](https://www.gandi.net/zh-hant/domain/tld/tw)
- Claude Code 開發工具費：Pro US$20、Max US$100／200（每月）— [Superblocks](https://www.superblocks.com/blog/claude-code-pricing)
- 金流物流按筆計費（例：綠界 C2C 運費 65 元、COD 0.75%；PAYUNi 冷凍大宗 125 元、COD 0.5%；虛擬帳號約 1%，最低 15 元）— [ECPay 服務費率表](https://www.ecpay.com.tw/Business/payment_fees)；[PAYUNi 費用](https://www.payuni.com.tw/fee)；[site-now](https://site-now.app/ecpay-review/)

### Inferences
- **每月成本試算**（假設 1 USD ≈ NT$32；匯率是假設值，未查當日匯率）：

  | 項目 | A. 多租戶共用（約 20 家店分攤） | B. 每店獨立一套 | 備註 |
  |---|---|---|---|
  | 前端／API 主機 | Vercel Pro US$20 ÷ 20 ≈ NT$32 | Vercel Pro 共用帳號，或 Cloudflare US$5 起 ≈ NT$32–160 | Hobby 禁止商用 |
  | 資料庫 | Supabase Pro US$25（加 compute 升級約 US$25–55）÷ 20 ≈ NT$40–90 | 每店一個專案，約 US$10 compute ≈ NT$320（第一個專案含在 Pro 的 US$25 內） | Free 會暫停，不適合正式營運 |
  | LLM | 約 NT$3–60 | 同左 | 1–10 萬則訊息／月的量級 |
  | 網域 | .tw 約 NT$62／月（NT$744／年） | 同左 | 可讓店家自己持有網域 |
  | LINE OA | NT$0（只用 reply）／NT$1,000（中用量） | 同左 | 通常由店家自己的 OA 付費 |
  | 小計（不含 LINE） | **約 NT$150–250／店／月** | **約 NT$400–600／店／月**（若每店再各買一個 Vercel Pro 席位，會升到 NT$1,400+） | |

  解讀：
  - 「299 起」的月費如果包含主機，只有方案 A 能賺錢；LINE OA 的方案費最好讓店家自己付。
  - 按筆計費的金流物流手續費（COD 0.5–0.75%、虛擬帳號 1%）是轉嫁給店家的成本，不屬於系統營運成本。
- **元件別技術拆解與工時**（AI 輔助、一人開發的推估，不含店家溝通和特店申請等待）：

  | 元件 | 可行性 | 可能實作 | 服務／API | 月成本 | 主要坑 | 從零（h） | 用模板（h） |
  |---|---|---|---|---|---|---|---|
  | 購物車＋會員 | 高 | Next.js 頁面＋Postgres；會員用 LINE Login／LIFF 或手機號 | LINE Login、Supabase Auth | 含在主機 | 多租戶隔離、RLS | 12–20 | 3–6 |
  | 優惠碼 | 高 | coupons 表＋規則引擎（門檻、適用商品、次數） | — | — | 並發超用、進位規則 | 4–6 | 1–2 |
  | 購物金 | 高 | 只新增的帳本（ledger） | — | — | 退款回補、並發超扣 | 6–10 | 2–3 |
  | 物流選項（7-11 冷凍／全家／宅配／面交） | 高（不串 API）；中（串 API） | 運費規則＋門市店號欄位＋分組匯出 | 綠界／PAYUNi／PayNow（日後串接） | 按件 | 測標、IP 白名單、CDN 回呼限制 | 6–10（不串 API）／＋8–16（串 API） | 2–4 |
  | 轉帳對末五碼＋取貨付款 | 高 | 付款回報表單＋明細比對＋人工佇列；COD 記應收 | （選配）虛擬帳號 | 選配約 1% | 撞單、短付溢付、少一碼 | 4–8 | 2–3 |
  | 揀貨單／出貨單 | 高 | 列印用 CSS（A4、標籤）；揀貨單按商品彙總，出貨單按訂單 | — | — | 冷凍、常溫分開揀 | 4–6 | 1–2 |
  | 賣貨便一鍵匯出 | 高 | 依官方範例檔產生 xlsx，每檔 ≤100 筆 | 交貨便批次匯入頁 | — | 範本變動、只支援 Windows Excel | 2–4 | 0.5–1 |
  | 掃條碼進貨、庫存、毛利 | 高 | HID 掃描槍＋異動流水帳＋報表 | （手機掃描）ZXing／WASM | — | iOS 不支援 BarcodeDetector、秤重品、損耗 | 8–14 | 3–5 |
  | 群組「菜單」回 Flex | 高 | webhook 關鍵字 → reply carousel | Messaging API | 免費（reply） | 一群一 OA、每個 carousel ≤12 項 | 4–8 | 1–2 |
  | AI 群組訂單整理 | 中高 | 規則＋LLM structured output＋人工確認佇列；也支援貼上聊天 .txt | LLM API | <US$2 | 語意誤判、改單取消、個資 | 8–16 | 3–6 |
  | 金額測試（35 案例）與修 bug | 必要 | 表格驅動＋fast-check | Vitest／Jest | — | AI「差一點對」 | 6–12 | 4–8 |
  | 後台、權限、CI／CD、資料搬遷 | 高 | 管理後台、GitHub Actions、preview、從舊 App 匯入商品與客戶 | Vercel／Supabase | 含在主機 | 舊系統的購物金餘額搬遷 | 8–16 | 3–6 |
  | **合計** | | | | | | **約 72–130** | **約 25–48** |

  - 一週如果投入 70–85 小時（每天 10–12 小時），從零做完全部功能非常吃緊；從模板改就在合理範圍內，還能留時間給「35 種金額情況」和 73 次迭代。
  - 不靠 AI 的話，以上工時可能要乘以 2–3 倍。這是主觀推估，沒有來源。
- 非程式時間也要算進去：需求訪談、舊 App 資料匯出與搬遷、LINE OA 開通 Messaging API 並把 bot 加進群組、金流物流特店申請與測標（可能要幾天到幾週）、教店家操作。

### Gaps
- 所有工時都是推論，沒有可引用的實證資料。
- 匯率、Vercel 的確切席位計價、Supabase compute 各級的價格沒有從官方頁直接核對。
- .com 等其他網域的價格沒有查。
- 沒有查 Firebase、Neon、VPS（例如在台灣機房）等其他方案的價格。如果要符合「固定 IP」或「不要用國外 CDN 當回呼」的要求，VPS 方案可能比較合適，但沒有研究。

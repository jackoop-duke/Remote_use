# ライフネット生命保険（Lifenet Insurance, TSE 7157）AI／生成式 AI 導入進展（截至 2026 年 11 月）

> 研究方法說明：本次雲端環境無法直接連線 prtimes.jp、voix.jp、ir.lifenet-seimei.co.jp、www.lifenet-seimei.co.jp（DNS 被網路政策擋下），因此以下事實來自搜尋引擎對各頁面內容的擷取摘要，而非逐頁全文閱讀。數字已盡量以兩個以上來源交叉核對；只有單一來源的數字會特別標示。
>
> 時間軸速覽（依時間排序）：
> - 2022-02：官網加入「AI サイト内検索」
> - 2023-03：與 JMDC 啟動「引受リスク予測AI」實證
> - 2023-07：成立生成式 AI 推進專案小組
> - 2024-07-01：自建「社内用LLM」上線
> - 2024-07-04：LINE 生成式 AI 個性診斷內容上線
> - 2024-08 起：分階段全員導入 Google Workspace with Gemini
> - 2025-01：社內 LLM 利用率 87%
> - 2025-06：社長由森亮介交棒橫澤淳平
> - 2025-11-07：客服中心導入對話型 AI 與 AI ボイスボット
> - 2026-03-31：生成式 AI 利用率 100%
> - 2026-05-27：獲選「財界 BEST AI 100」
> - 2026-07 末：自建 AI Agent 導入全部門（2026-08-25 適時開示）
> - 2026-09-14：Lifenet InsurTech Meetup #03

## 1. 具體 AI 應用（客服、核保、理賠、行銷、內部生成式 AI、AI Agent 等）

### Takeaway
Lifenet 的 AI 應用以「內部生產力」與「客服中心」兩條主線最成熟，皆已上線：
- 內部生產力：2024 年 7 月自建社內 LLM，再加上 Google Workspace with Gemini；2026 年 7 月底進一步把自建 AI Agent 導入全部門。
- 客服中心：2025 年 11 月以對話型 AI 與 AI ボイスボット取代 IVR。

AI 核保（引受査定）目前仍只停留在 2023 年與 JMDC 的實證階段。理賠「最短當日支付」的提速主要來自 API 即時匯款，並不是 AI。

### Cited Findings

**A. 內部生成式 AI（已上線）**
- 推進組織：2023 年 7 月成立生成式 AI 推進專案小組，先從文章生成 AI 的社內利用起步 — [IT Leaders](https://it.impress.co.jp/articles/-/27735)；[新日本保険新聞（2026-08-25 引述）](https://www.shinnihon-ins.co.jp/industry-news/industry-news-20260825-15/)
- 導入前的狀況：2023 年底時，因資安考量，社內幾乎沒有在用生成式 AI — [日經クロストレンド](https://xtrend.nikkei.com/atcl/contents/18/01254/00003/)（日期未確認，依內容推估為 2025–2026 年）
- 社內 LLM 上線：2024 年 7 月 1 日導入「社内用LLM」，定位為中期經營計畫「Tech & Services」領域的活動之一。
  - 開發方式：未委託外部 vendor，由データサイエンス推進室的社員（橋詰）在自家雲端基盤上一人實作。
  - 來源：[ライフネット生命 公式 note](https://note.lifenet-seimei.co.jp/n/nb15c67a7d450?gs=519a8d5bfac6)；[PR TIMES 2025-04 新聞稿](https://prtimes.jp/main/html/rd/p/000000145.000069919.html)
- 外部支援：ハーベスト（Harvest）以「共創パートナー」身分協助建置生成 AI／LLM 開發基盤 — [Harvest 新聞頁](https://harvest-w.com/news/news03)
- 工具分工：除自建 LLM 外，另導入 Google「Gemini」，處理資安上沒有疑慮的任務，依用途分開使用 — [日經クロストレンド](https://xtrend.nikkei.com/atcl/contents/18/01254/00003/)
- Gemini 導入時程：2024 年 8 月起分階段推廣到全體員工 — [財界 BEST AI 100 新聞稿 2026-05-27（IR PDF）](https://ir.lifenet-seimei.co.jp/ja/news/index/auto_20260527549739/pdfFile.pdf)；[PR TIMES](https://prtimes.jp/main/html/rd/p/000000218.000069919.html)
- 技術棧：無論自建 LLM 是否以 Google Cloud Vertex AI 為底層，公開資料都沒有明確寫出 — 見 Gaps。

**B. AI Agent 全部門導入（已上線，2026 年）**
- 時程：2026 年 7 月底完成，將自建 AI Agent 導入「全部門」；2026 年 8 月 25 日以適時開示公告 — [日經会社情報DIGITAL 適時開示](https://www.nikkei.com/nkd/disclosure/tdnr/20260825525504/)；[ほけデジ 2026-08](https://hokedigi.tmj.jp/information/2026/08/23373/)；[新日本保険新聞 2026-08-25](https://www.shinnihon-ins.co.jp/industry-news/industry-news-20260825-15/)
- 技術與目標：以「Google の先端技術」為基礎，加上自家客製化，目標是讓牽涉多系統、多條件分歧的複雜保險業務能「自動且自律地完結」 — [ほけデジ](https://hokedigi.tmj.jp/information/2026/08/23373/)
- 導入背景：既有 chat 型 AI 每次都要人下指令，難以把定型業務自動化，因此從「個人の業務補助」轉向「業務プロセス自体の自動化」 — [新日本保険新聞](https://www.shinnihon-ins.co.jp/industry-news/industry-news-20260825-15/)
- 配套研修：2026 年 7 月起開辦全部門實踐研修，建立由各部門主導推動業務自動化的體制 — [ほけデジ](https://hokedigi.tmj.jp/information/2026/08/23373/)
- 社內教育：另有 AI Agent 勉強會 — [公式 note「ゆるっと始めて、着実に。AIエージェント勉強会レポート」](https://note.lifenet-seimei.co.jp/n/nd909d5868d8d?gs=5a78308b0650)
- 對外技術分享：2026 年 9 月 14 日舉辦「Lifenet InsurTech Meetup #03」，分享 AI Agent 用於廣告分析與業務效率化的做法，以及安全設計等實作 — [PR TIMES](https://prtimes.jp/main/html/rd/p/000000249.000069919.html)

**C. 客服中心：對話型 AI 與 AI ボイスボット（已上線，2025-11-07 發布）**
- 舊制問題：IVR 每道問題都要顧客自己操作畫面，接通真人客服前的等待時間太長 — [IT Leaders](https://it.impress.co.jp/articles/-/28587)；[PR TIMES](https://prtimes.jp/main/html/rd/p/000000179.000069919.html)
- 新做法：改由對話型 AI 透過自然對話判斷來電目的並自動分流，必要時轉接真人 — [AIdiver](https://aidiver.jp/news/detail/206)
- 服務延伸：「控除証明書」補發改為 24 小時受理，以前只限營業時間 — [AIdiver](https://aidiver.jp/news/detail/206)；[時事ドットコム（PR TIMES 轉載）](https://www.jiji.com/jc/article?k=000000179.000069919&g=prt)
- 定位：官方稱這是「人と AI が協働する次世代コンタクトセンター」的「第一歩」 — [PR TIMES](https://prtimes.jp/main/html/rd/p/000000179.000069919.html)；[公式 note 次世代型コンタクトセンター](https://note.lifenet-seimei.co.jp/n/n4ca7dccd1073?gs=44f7ceb64672)

**D. AI 核保（引受査定）（仍在實證，未確認正式上線）**
- 實證啟動：2023 年 3 月 29 日與 JMDC 宣布開始。使用 JMDC 的匿名加工醫療資料，加上模擬マイナポータル欄位的「仮想マイナポータルデータ」，驗證能預測未來傷病發生的「引受リスク予測AI」 — [JMDC 新聞稿 PDF 2023-03-29](https://www.jmdc.co.jp/wp-content/uploads/2023/03/news20230329.pdf)；[マイナビ TECH+ 2023-03-30](https://news.mynavi.jp/techplus/article/20230330-2640036/)；[日本経済新聞](https://www.nikkei.com/article/DGXZRSP652100_Z20C23A3000000/)
- 目標：把 AI 嵌入核保流程，擴大可承保範圍並優化核保基準；將來目標是串接真正的マイナポータル — [atpress](https://www.atpress.ne.jp/news/350744)；[ほけデジ 2023-03](https://hokedigi.tmj.jp/information/2023/03/22993/)
- 實證結果：據引述 2026 年版統合報告書的報導，實證「有効性が証明」，若能展開到實際運用，可望提升核保效率與投保便利。只有公司自述，沒有公開精度數字 — 來源為搜尋摘要（[新日本保険新聞 2026-08-24](https://www.shinnihon-ins.co.jp/industry-news/industry-news-20260824-8/)，原頁未能直接開啟確認）
- 招募訊號：データ・AI推進部的職缺把「AI 査定」列為面向顧客的應用範例 — [HRMOS 職缺](https://hrmos.co/pages/lifenet-seimei/jobs/5-1-1)

**E. 理賠支付提速（已上線，但不是 AI）**
- 平均支付日數：2024 年度 1.91 日 → 2025 年度 1.08 日 → 2026 年度 Q1（4–6 月）0.58 日（定義為平均營業日數） — [IR 新聞稿 2026-08-21](https://ir.lifenet-seimei.co.jp/ja/news/index/auto_20260821524238.html)；[官網新聞稿](https://www.lifenet-seimei.co.jp/newsrelease/1190896_1707.html)；[新日本保険新聞 2026-08-24](https://www.shinnihon-ins.co.jp/industry-news/industry-news-20260824-8/)
- 提速原因：用 API 串接，把匯款基盤即時化，讓收到請求文件當天就能入帳。公開說明中並沒有把這歸功於 AI — 同上

**F. 行銷與廣告**
- LINE 生成式 AI 內容：2024 年 7 月 4 日，與インティメート・マージャー、ディグラム・ラボ合作，在 Lifenet 的 LINE 公式帳號推出以生成式 AI 製作的「ディグラム診断」（個性診斷）內容，目標是個人化溝通與持續的顧客互動 — [インティメート・マージャー 新聞](https://corp.intimatemerger.com/news/20240704_digramlabolifenet/)；[PR TIMES](https://prtimes.jp/main/html/rd/p/000000132.000084943.html)
- 廣告內製化與品質防護：Lifenet 推動廣告運用內製化，並採用 Momentum 的「HYTRA」系列，防範ブランドセーフティ問題與アドフラウド，以確保 AI 分析所用的配信資料可信；Momentum 於 2026-05-19 公開此導入案例 — [Momentum 導入事例](https://www.m0mentum.co.jp/news/2026-lifenet-seimei)；[Momentum 訪談](https://www.m0mentum.co.jp/column/interview2026_lifenet-seimei)；[RBB TODAY 2026-05-19](https://www.rbbtoday.com/release/prtimes2-today/20260519/1273438.html)（屬廠商自家發布，具宣傳性質）
- 廣告效果分析：另有以 Ledge 協助可視化生命保險廣告效果、優化預算分配的案例 — [Ledge 案例](https://ledge-eg.com/cases/lifenet/)（日期與是否使用 AI 未確認）

**G. 較早期的應用（2022 年）**
- 2022 年 2 月，官網新增「AI サイト内検索」功能，以 AI 讓顧客更容易找到站內資訊，屬森亮介社長任內的發布 — [IR PDF 2022-02-03（依 URL 推定日期）](https://ir.lifenet-seimei.co.jp/ja/news/index/auto_20220203579263/pdfFile.pdf)

### Inferences
- Lifenet 的路線偏「內製」，先後是自建 LLM、自建 AI Agent，搭配 Google 生態系（Gemini、Google 技術做 Agent 底層），並沒有大量外包給 SIer。這與其約 200 名總合職正社員的小規模組織相符。
- 「全部門導入 AI Agent」表示已部署到所有部門，但在公開資料中還沒看到量化成效。實際自動化了多少流程、有多深，仍待觀察。
- AI 核保從 2023 年實證到 2026 年統合報告書都只寫「有效」，沒有宣布上線，判斷仍停在實證或等待マイナポータル實際串接的階段。

### Gaps
- 沒有找到 AI 詐欺偵測、理賠 AI 審查、OCR、語音辨識（客服通話轉文字或摘要）的公開導入資訊。
- 自建 LLM 用哪個基礎模型或雲端（Vertex AI、Azure OpenAI 等），公開資料沒有明確寫出。
- AI Agent 的具體 use case 數量、自動化了哪些流程，公開資料沒有揭露。
- 2022 年 AI サイト内検索的供應商與成效未確認。

## 2. 各應用的成效數字與上線時間

### Takeaway
目前能確認的量化成效集中在四組數字：
- 社內 LLM 利用率 87%（2025 年 1 月）
- 導入兩個月共省下 152 小時（2024 年 8 月調查）
- 生成式 AI 利用率 100%（2026 年 3 月 31 日）
- 客服等待時間由 95 秒縮短到 65 秒，約 -30%

AI Agent 尚無公開成效數字。

### Cited Findings
- **社內 LLM 利用率**
  - 2025 年 1 月底，總合職正社員（203 人）中 87% 使用過社內 LLM（官方 2025 年 4 月發布） — [PR TIMES](https://prtimes.jp/main/html/rd/p/000000145.000069919.html)；[IT Leaders](https://it.impress.co.jp/articles/-/27735)；[minkabu 轉載](https://minkabu.jp/news/4196895)
- **工時削減**
  - 2024 年 8 月社內調查：導入兩個月內，56 名使用者合計省下 152 小時業務時間 — [IT Leaders](https://it.impress.co.jp/articles/-/27735)；[PR TIMES](https://prtimes.jp/main/html/rd/p/000000145.000069919.html)
  - 注意：152 小時是導入兩個月、56 人的累計，不是每月數字。部分媒體標題寫成「月 152 時間」，屬誤讀。
- **活躍率與利用率（不同時點、不同口徑）**
  - 社內 LLM 加 Gemini 的員工活躍率「90% 以上」 — [日經クロストレンド](https://xtrend.nikkei.com/atcl/contents/18/01254/00003/)
  - 2026 年 3 月 31 日，生成式 AI 社內利用率 100%（對象為總合職正社員，不含休職者；自建 LLM 與 Google Workspace with Gemini 合計） — [財界 BEST AI 100 新聞稿 2026-05-27](https://prtimes.jp/main/html/rd/p/000000218.000069919.html)；[新日本保険新聞 2026-05-28](https://www.shinnihon-ins.co.jp/industry-news/industry-news-20260528-4/)
  - 「利用率 100%」也被用在推手橋詰登壇「CX Circle Tokyo 2026」的宣傳 — [moneyzone](https://moneyzone.jp/169482/)
- **客服中心**
  - 2025 年 11 月導入後，接通真人客服前的等待時間由 95 秒縮短到 65 秒 — [財界 BEST AI 100 新聞稿](https://prtimes.jp/main/html/rd/p/000000218.000069919.html)
  - 公式 note 的說法是約 1 分 35 秒縮短到約 1 分 5 秒 — [公式 note](https://note.lifenet-seimei.co.jp/n/n4ca7dccd1073?gs=44f7ceb64672)
  - ダイヤモンド的報導稱縮短約 30% — [diamondv](https://www.diamondv.jp/article/cFqdDtXcXU3rZ8akcJLWLy)
  - 控除証明書補發：由營業時間內受理改為 24 小時、365 日受理 — [AIdiver](https://aidiver.jp/news/detail/206)
- **AI Agent**
  - 2026 年 7 月底完成全部門導入，但公開資料中沒有工時削減等成效數字 — [ほけデジ](https://hokedigi.tmj.jp/information/2026/08/23373/)
- **理賠（非 AI，僅供對照）**
  - 平均支付日數 1.91 日（FY2024）→ 1.08 日（FY2025）→ 0.58 日（FY2026 Q1） — [IR 新聞稿 2026-08-21](https://ir.lifenet-seimei.co.jp/ja/news/index/auto_20260821524238.html)

### Inferences
- 利用率的分母是「總合職正社員」，約 200 人，絕對規模小。和大型金控比較時，應改看滲透率與自動化深度，不宜比較絕對人數或節省總時數。
- 152 小時除以 56 人除以約兩個月，大約是每人每月省 1.4 小時。這是推算，原始資料沒有這個數字。

### Gaps
- 沒有找到成本削減金額（日圓）、客服 AI 自助完結率、應答率、AI Agent 處理件數等數字。
- 日經クロストレンド報導的確切刊出日期未確認。

## 3. 合作夥伴

### Takeaway
核心技術夥伴是 Google，提供 Gemini 與 AI Agent 的技術底層。核保 AI 的夥伴是 JMDC；生成式 AI 開發基盤由 Harvest 協助；行銷端則有インティメート・マージャー／ディグラム・ラボ與 Momentum。沒有找到與 KDDI、ELYZA、Microsoft（Azure OpenAI）合作的證據。

### Cited Findings
- **Google**
  - Google Workspace with Gemini 全員導入（2024 年 8 月起） — [PR TIMES 2026-05-27](https://prtimes.jp/main/html/rd/p/000000218.000069919.html)
  - AI Agent 以「Google の先端技術」為底層（2026 年 7 月） — [ほけデジ](https://hokedigi.tmj.jp/information/2026/08/23373/)
- **JMDC**：2023 年 3 月起合作「引受リスク予測AI」實證，使用醫療大數據 — [JMDC PDF](https://www.jmdc.co.jp/wp-content/uploads/2023/03/news20230329.pdf)
- **ハーベスト（Harvest）**：社內 LLM 利活用的開發基盤建置夥伴 — [Harvest](https://harvest-w.com/news/news03)
- **インティメート・マージャー、ディグラム・ラボ**：2024 年 7 月在 LINE 推出生成式 AI 內容 — [インティメート・マージャー](https://corp.intimatemerger.com/news/20240704_digramlabolifenet/)
- **Momentum（HYTRA）**：廣告品質與詐欺防護，2026 年 5 月公開案例 — [Momentum](https://www.m0mentum.co.jp/news/2026-lifenet-seimei)
- **客服 AI 供應商**：客服對話型 AI 與 AI ボイスボット由哪家供應，搜尋摘要中沒有確認 — [IT Leaders](https://it.impress.co.jp/articles/-/28587)

### Inferences
- 以 Google 為中心的架構（Gemini 搭配 Google 技術的 Agent）很明確。實作則堅持自建，外部廠商只做基盤支援或特定領域服務。

### Gaps
- 客服 AI ボイスボット的供應商名稱。
- 自建 LLM 使用的基礎模型（Gemini API、OpenAI 或其他），公開資料沒有寫出。
- 查無 KDDI、ELYZA、Microsoft 或日本 AI 新創的合作資訊。

## 4. AI 治理與方針

### Takeaway
沒有找到 Lifenet 對外公開的「AI 利用ポリシー」或 AI 治理方針全文。目前能確認的治理措施有三項：
- 已訂定社內生成式 AI 指引
- 依資安等級把工具分流：機密資料用自建 LLM，非機密任務用 Gemini
- 設有專責組織「データ・AI推進部」與擔當役員

### Cited Findings
- 社內規範與素養活動：除訂定「生成 AI に関する社内ガイドライン」外，也辦社內勉強會、「AI 短歌コンテスト」等，帶動全公司 AI 素養 — [Infoseek（PR TIMES 轉載，CX Circle 登壇新聞）](https://news.infoseek.co.jp/article/prtimes_000000227_000069919/)；[AdverTimes：生成AI短歌コンテスト](https://www.advertimes.com/?p=520252)
- 以資安為出發點：2023 年底因資安考量幾乎沒有使用；2024 年自建 LLM，Gemini 只用於資安上沒問題的任務 — [日經クロストレンド](https://xtrend.nikkei.com/atcl/contents/18/01254/00003/)
- 組織與職責：金杉貴仁為「データ・AI推進部、事業開発部、商品開発部」的擔當役員，曾出席財界 BEST AI 100 頒獎典禮 — [PR TIMES 2026-05-27](https://prtimes.jp/main/html/rd/p/000000218.000069919.html)；[橫澤社長 X 貼文](https://x.com/Junpei_Yokozawa/status/2059600841531924543)
- 演進脈絡：自建 LLM 時期的推動單位是「データサイエンス推進室」，2026 年資料已改稱「データ・AI推進部」 — [公式 note 社員インタビュー](https://note.lifenet-seimei.co.jp/n/n7bc4f1a997f4?gs=6befd9f2c1f5df92b250888d3238eb05)；[HRMOS](https://hrmos.co/pages/lifenet-seimei/jobs/5-1-1)
- 外部合作的倫理立場：在生成式 AI 的外部合作上，表明「技術的・倫理的な課題の解決にも取り組んでまいります」（2024 年 LINE 生成式 AI 內容新聞稿） — [PR TIMES](https://prtimes.jp/main/html/rd/p/000000132.000084943.html)
- AI Agent 的資安：2026 年 9 月 Meetup #03 分享了 AI Agent 的「セキュリティ設計」 — [PR TIMES](https://prtimes.jp/main/html/rd/p/000000249.000069919.html)

### Inferences
- 推進組織由「室」升格為「部」，並有專責役員，顯示 AI 已提升到經營層級的優先事項。
- 治理重點目前放在社內利用與資料保護，偏實務。和大型金融集團相比，Lifenet 沒有公開 AI 倫理原則或 AI 治理委員會。

### Gaps
- 對外公開的 AI 原則或 AI 利用政策、AI 治理委員會、模型風險管理（model risk management）框架，均未找到。
- 社內生成式 AI 指引的具體內容。

## 5. 2023–2026 最新動態與管理層公開發言

### Takeaway
最新的重大動態有兩項：
- 2026 年 7 月底完成全部門自建 AI Agent 導入（2026-08-25 適時開示）
- 2026 年 5 月 27 日成為保險業第一家獲選「財界 BEST AI 100」的公司

管理層方面要注意：森亮介已於 2025 年 6 月卸任社長，現任社長是橫澤淳平。橫澤把「AI 加上マイナンバー」打造的「全自動の保険」列為中期計畫「Tech & Services」的核心。

### Cited Findings
- **財界 BEST AI 100**：2026 年 5 月 27 日獲選，為保險業第一家。該獎表彰透過 AI 實現業務流程變革的 100 家企業。評價對象包括：
  - 客服中心的對話型 AI 與 AI ボイスボット
  - 自建社內 LLM
  - Google Workspace with Gemini 全員導入
  - 來源：[PR TIMES](https://prtimes.jp/main/html/rd/p/000000218.000069919.html)；[ほけデジ 2026-06](https://hokedigi.tmj.jp/information/2026/06/23348/)；[新日本保険新聞 2026-05-28](https://www.shinnihon-ins.co.jp/industry-news/industry-news-20260528-4/)
- **AI Agent 全部門導入**：2026 年 7 月底完成，2026 年 8 月 25 日適時開示 — [日經会社情報DIGITAL](https://www.nikkei.com/nkd/disclosure/tdnr/20260825525504/)
- **社長交棒**
  - 2025 年 3 月 17 日適時開示宣布人事異動 — [IR PDF](https://ir.lifenet-seimei.co.jp/ja/news/index/auto_20250317594736/pdfFile.pdf)；[新日本保険新聞 2025-03-18](https://www.shinnihon-ins.co.jp/industry-news/industry-news-20250318-9/)
  - 橫澤淳平 2025 年 6 月就任社長。經歷：2003 年進入 NTT データネッツ，2008 年加入 Lifenet，2024 年任上級執行役員 — [財界 訪談](https://www.zaikai.jp/articles/detail/5774)；[ニッキン](https://www.nikkinonline.com/article/258889)
- **中期計畫**：2024 年 5 月發布，把「Tech & Services」列為成長戰略重點領域之一。目標是運用 AI 與マイナンバー制度，把從投保到領取保險金或給付金的流程自動化，實現「全自動の保険」 — [財界 橫澤訪談](https://www.zaikai.jp/articles/detail/5774)；[IR 社長メッセージ](https://ir.lifenet-seimei.co.jp/ja/company/message.html)
- **橫澤的公開發言與活動**
  - 財界訪談標題：「テクノロジーの力でお客さまの利便性を高めていく」 — [財界](https://www.zaikai.jp/articles/detail/5774)
  - 2025 年 12 月於中央大學商學部「AI・データサイエンスの基礎」講座，講題為「AI・データサイエンスが生命保険の仕事をどう変えているのか」 — [中央大學](https://www.chuo-u.ac.jp/academics/faculties/commerce/news/2025/12/83466/)
  - 另有日經ヴェリタス「トップに聞く」與週刊エコノミスト編集長訪談 — [日經ヴェリタス](https://www.nikkei.com/prime/veritas/article/DGXZQOKC081TF0Y5A001C2000000)；[エコノミスト](https://www.weekly-economist.com/interview/yokozawa_junpei/)（AI 相關段落內容未能確認）
- **森亮介（前社長，2018–2025 年 6 月）的發言**：2022 年受訪時表示，金融機關需要的是「枯れた」（成熟、穩定）的技術，先從智慧型手機上理所當然能做到的事做起。這不是針對 AI 的發言 — [ITmedia エグゼクティブ 2022-01](https://mag.executive.itmedia.co.jp/executive/article/2201/18/1220118052/)；[ITmedia エグゼクティブ 2022-04](https://mag.executive.itmedia.co.jp/executive/article/2204/25/1220425023/)
- **對外輸出**
  - 橋詰（社內 LLM 開發者）於「CX Circle Tokyo 2026」登壇 — [moneyzone](https://moneyzone.jp/169482/)
  - 2026 年 9 月 14 日舉辦 Lifenet InsurTech Meetup #03（主題為 AI 與數位行銷） — [PR TIMES](https://prtimes.jp/main/html/rd/p/000000249.000069919.html)
- **語音 AI Agent 銷售實驗（未確認）**：NewsPicks 有一篇「AIエージェントで生命保険を売ろう！～音声エージェント実証実験から見えた可能性と課題～」，但無法確認是否為 Lifenet 的案例 — [NewsPicks](https://newspicks.com/news/15265623/body/)。因此不列為事實。

### Inferences
- 2024 到 2026 年的軌跡很清楚：先自建 LLM（工具），再普及到利用率 100%，再到 AI Agent 自動化業務流程，同時把 AI 擴到客服端。下一步依中期計畫，很可能是讓 AI 核保與マイナポータル串接，邁向「全自動の保険」。這是推論，官方沒有公布時程。
- 新社長橫澤出身 IT（NTT データ系），AI 的推動力道在他任內明顯加速：100% 利用率、AI Agent、財界獎都發生在他就任後。

### Gaps
- 沒有找到森亮介針對生成式 AI 的具體發言。
- 橫澤社長對 AI Agent 的直接引言（例如新聞稿中的社長コメント），本次無法讀取原文確認。
- 決算說明資料或統合報告書裡的 AI 相關 KPI 或投資金額未能確認，因為 IR 網站無法連線。

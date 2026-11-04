# 國泰金融控股（Cathay FHC）AI／生成式 AI 導入進展（截至 2026 年 11 月）

> 研究方法說明：本次 session 的 WebFetch 無法連線至 ithome.com.tw、techorange.com、taiwannews.com.tw 等外部網站（DNS 被網路設定封鎖），因此以下內容全部來自 WebSearch（extended）回傳的搜尋摘要與段落，沒有逐篇讀完原文。數字已盡量對應到具體報導 URL，但仍建議撰稿者在引用關鍵數字前回原文核對。很多數字出自國泰新聞稿或業配／廣編內容（如數位時代 BusinessNext 專題、ETtoday【廣編】），屬公司自述，並非第三方查核。

---

## Q1. 各子公司具體 AI 應用案例與成效數字

### Takeaway
國泰把 AI 用在客服（阿發）、壽險理賠／核保、產險車險風險預測、銀行防詐、企金徵信、HR 知識助理、RPA 等場景。公開的量化成效多是「比率」或單一應用的數字，例如理賠自動化比率上升 20%、HR 助手準確度 95%、產險事故率降低五成。集團層級的整體節省工時或 ROI 目前沒有公開。

### Cited Findings

**智能客服「阿發」（國泰世華、國泰人壽，後擴及產險、證券、投信）— 已上線**
- 阿發自 2018 年推出。2025 年國泰金控技術年會（2025-10-20）首度展示「升級版阿發」；國泰稱阿發近三年累積的互動人次，約等於與全台每位民眾深度對話兩次 — [工商時報 2025-11-10](https://www.chinatimes.com/newspapers/20251110000356-260208)
- 升級版阿發與 Google Cloud 合作，以 Dialogflow CX 建構，加上 RAG 架構（回覆前先檢索相關內容以提升準確性），並用 GKE 部署評測與監控程式持續追蹤 LLM 回覆品質。這是三階段進化路徑的第二階段，第三階段規劃走向 Agentic AI；報導只說成效「明顯提升」，沒有給百分比 — [天下雜誌 cw.com.tw/article/5139151](https://www.cw.com.tw/article/5139151)
- 國泰世華官網說明：升級版阿發採用生成式 AI，以國泰世華官網資訊作為資料庫 — [CUBE 官網 阿發介紹](https://www.cathay-cube.com.tw/cathaybk/personal/digital-service/intro/chatbot)
- 較舊的數據（年份未明，應為 2020 年前後，屬生成式 AI 之前）：近五成客戶直接透過智能客服解決疑問，月均功能使用量逾 90 萬次，使用滿意度 97%。另有報導指阿發「二年成長 10 倍、已打敗傳統語音客服」 — [經濟日報 money.udn.com/money/story/5613/4831766](https://money.udn.com/money/story/5613/4831766)；[國泰金控新聞稿](https://www.cathayholdings.com/holdings/information-centre/intro/latest-news/detail?news=UJPnd4qZ8UqHAbzo9k1gUw)
- 阿發曾升級為「智能雙腦」，擴展上線產險、證券、投信（年份未明，較早期）— [風傳媒](https://www.storm.mg/article/3008217)；[MoneyDJ](https://www.moneydj.com/KMDJ/News/NewsViewer.aspx?a=%7B92fad792-22d9-4ec6-9f8b-383933a221a9%7D)
- 2025 年技術年會的宣傳標題提到「CUBE 智能客服」為生成式 AI 兩大升級之一 — [國泰 YouTube Shorts](https://www.youtube.com/shorts/j-dcSaXf00E)

**客戶意圖辨識小型語言模型（SLM）— 研究／技術驗證**
- 2026 年 6 月在 NVIDIA GTC Taipei 2026 發表：微調開源 SLM 做客戶意圖分類，評估了 Meta、TAIDE、TAME、NVIDIA、OpenAI 的開源模型。使用 NVIDIA NeMo Customizer、NeMo Curator、TensorRT-LLM 和 Hopper 架構算力；訓練資料全部是合成資料，不使用真實客戶資料。結果自稱「接近主流閉源 LLM」，但沒有公開具體準確率 — [PR Newswire APAC 2026-06](https://www.prnewswire.com/apac/news-releases/cathay-financial-holdings-leverages-open-source-small-language-models-to-identify-customer-intent-302798631.html)；[Open Source For You 2026-06](https://www.opensourceforu.com/2026/06/cathay-fhc-uses-open-source-slms-to-power-customer-understanding/)

**國泰人壽：理賠、核保、精準行銷 — 已上線**
- 獲 2026-01-22 商周「AI 創新百強」白金獎：AI 輔助下，理賠作業自動化比率上升 20%（另一版本寫作「理賠作業效率提升 20%」，指標名稱不一致），保障型商品成交率成長 5.7 倍，整體 NPS 提升 5.9% — [國泰產險新聞稿 2026-01-22](https://www.cathay-ins.com.tw/cathayins/news/20260122/)；[鉅亨網](https://news.cnyes.com/news/id/6319245)
- 獲 IIC Asia Awards 2025 數位轉型先鋒獎（台灣金融業唯一）：理賠案件審理時間縮短 10%，核保財務指標評估效率提升 80% — [國泰人壽新聞 2025-03-28](https://www.cathaylife.com.tw/cathaylife/news/hotnews/20250328_iic-asia-awards-2025)
- 天下雜誌專訪（約 2024 年）：理賠流程已導入 4–5 個 AI 模型，包括自動核賠；管理層「預估」未來自動核賠率可提升到五成、等待時間可從一週縮短到兩三天（屬規劃目標，非已達成）— [天下雜誌 5132643](https://www.cw.com.tw/article/5132643)
- 2025-09：國泰金試辦投保時用人臉辨識簡化流程，AI 導入核保、理賠等四大面向（試辦）— [壹蘋新聞網 2025-09-24](https://news.nextapple.com/finance/20250924/252CE4F98D9F1DDDB4B26E8E7E53C9CD)
- 2025-10：國泰人壽以 AI Agent 重塑理賠等核心流程（業配專題，無件數）— [數位時代 2025-10](https://www.bnext.com.tw/article/84726/cathayholdings202510)

**國泰產險 — 已上線**
- CarTech 智能車險加值服務：結合駕駛行為數據與 AI 預測行車風險，風險辨識能力提升三倍，事故率降低五成（商周 AI 創新百強優選獎，2026-01）— [國泰產險新聞稿 2026-01-22](https://www.cathay-ins.com.tw/cathayins/news/20260122/)
- 理賠導入衛星影像、雷擊專利辨識結合自動通知，以及 AI 防詐，打造「主動關懷」理賠 — [聯合報](https://udn.com/news/story/121591/9851651)；[Yahoo 股市](https://tw.stock.yahoo.com/news/%E5%9C%8B%E6%B3%B0%E7%94%A2%E9%9A%AA%E5%B0%8E%E5%85%A5%E8%A1%9B%E6%98%9F%E5%BD%B1%E5%83%8F-%E9%9B%B7%E6%93%8A%E5%B0%88%E5%88%A9%E8%88%87ai%E9%98%B2%E8%A9%90-%E6%89%93%E9%80%A0-%E4%B8%BB%E5%8B%95%E9%97%9C%E6%87%B7-%E7%90%86%E8%B3%A0%E6%96%B0%E9%AB%94%E9%A9%97-070655001.html)

**國泰世華：詐騙偵測／洗錢防制**
- 2025 年臨櫃攔阻約 2,200 多件、金額逾新台幣 17.6 億元（警政署統計），獲行政院防詐獎項。這是臨櫃攔阻總數，不全是 AI 的成果 — [工商時報 2026-09-01](https://www.ctee.com.tw/news/20260901700175-439901)；[聯合報](https://udn.com/news/story/7239/9725534)
- 「金融盾」專案：用聯合學習在不交換個資的前提下，與其他金融機構共同訓練防詐 AI 模型（已上線）— [工商時報 2026-09-01](https://www.ctee.com.tw/news/20260901700175-439901)
- 參與「金融阻詐聯防平台」先導，導入生成式 AI 歸納警示帳戶共通樣態；上半年（應為 2026 上半年）臨櫃阻詐逾 6.7 億元 — [自由財經](https://ec.ltn.com.tw/article/paper/1772759)
- 2026 年與刑事局合作導入「被害者樣態」行為分析模型，「預估」每年可攔阻約 9,000 萬元財損（預估值）— [經濟日報](https://money.udn.com/money/story/5612/9516646)；[經濟日報](https://money.udn.com/money/story/5612/9518675)
- ATM 導入情境式選擇題，即時提醒並攔阻疑似詐欺交易 — [工商時報 2026-09-01](https://www.ctee.com.tw/news/20260901700175-439901)
- AML：AI Agent 可自動調查可疑交易並整合外部新聞，把可疑活動報告（SAR）撰寫時間從數小時縮短到數分鐘（國泰金控數數發中心經理謝昌宏於 TechOrange「AI Ready 數據治理論壇」分享，2026-03-31／報導 2026-04-13；是否全面上線未說明）— [科技報橘 2026-04-13](https://techorange.com/2026/04/13/cathayholdings-ai-ready-forum/)

**國泰世華：企金、HR、員工應用（GAIA STUDIO 上的應用）— 已上線**
- 「企業金融助手」用 AI 輔助撰寫徵信報告與財務分析，減少約 20% 工時 — [自由財經](https://ec.ltn.com.tw/article/paper/1735055)；[經濟日報](https://money.udn.com/money/story/122376/9188108)
- HR 知識助手每月處理逾 600 次詢問，回覆時間縮短到 1 分鐘內，準確度 95%，每月省下約 7.3 人天 — [國泰產險新聞稿 2026-01-22](https://www.cathay-ins.com.tw/cathayins/news/20260122/)；[商業周刊](https://www.businessweekly.com.tw/business/blog/3020485)
- RPA（非生成式 AI，另一套系統）：一百餘條 RPA 流程，每年替行員節省逾 20 萬小時作業時數 — [ETtoday 財經](https://finance.ettoday.net/news/2983282)

### Inferences
- 國泰公開的成效指標多是「單點應用的比率改善」，沒有集團層級的 AI 財務效益（成本節省金額、ROI）。和同業比較時，應比較同類指標，例如理賠自動化比率、客服解決率。
- 阿發的量化數據（90 萬次／月、97% 滿意度、近五成自助解決）多是生成式 AI 之前的數字。生成式 AI 版阿發上線後的新指標尚未公開。
- 防詐 17.6 億元是臨櫃攔阻總數（含行員人工判斷），不應直接歸功於 AI。

### Gaps
- 沒有找到國泰人壽「秒賠／自動核賠」的實際件數或比例（只有 2024 年前後「預估提升到五成」的目標）。
- 沒有找到信用評分 AI 模型（如 AI 信貸審核）的具體成效數字。
- 沒有找到國泰證券、國泰投信的投資／理財機器人（robo-advisor）最新 AI 數字，本次搜尋未涵蓋。
- 生成式 AI 版阿發的解決率、轉真人率、處理量都沒有公開數字。

---

## Q2. 生成式 AI 策略：自建平台、科技夥伴、員工使用規模

### Takeaway
國泰自建集團級生成式 AI 框架 GAIA：2024-09 發表 1.0，2025-10 升級 2.0 並轉向 AI Agent。採多模型、多雲策略：Model Hub 有 50 多種模型（含 Gemini、OpenAI），2026-04-07 再與 OpenAI 簽長期策略合作，全集團部署 ChatGPT Enterprise。NVIDIA 是開源 SLM 微調的技術夥伴，Google Cloud 支撐阿發。公開的員工使用規模數字很零散：GAIA STUDIO 支援 25 個單位、35～50 項應用、每月 2.4 萬次對話；ChatGPT Enterprise 的授權席次未公開。

### Cited Findings

**GAIA 1.0（2024）— 已上線**
- 2024-09-26「2024 國泰金控技術年會」由資深副總姚旭杰首度公開「國泰生成式 AI 技術發展框架 GAIA」。同時宣布 AIaaS（AI 即服務）三大策略：整合共識（AI Ready）、智能驅動（AI Native）、賦能革新（AI Empower）— [國泰金控新聞稿](https://www.cathayholdings.com/holdings/lastest_news/news_archive/newsarticle?newsID=-2ySBnTzeEe6Dpd-rlTZHg)；[iThome 165210](https://www.ithome.com.tw/news/165210)；[CIO Taiwan](https://www.cio.com.tw/first-publicly-generated-ai-framework-gaia-cathay-pacific-announces-the-three-strategies-of-aiaas/)
- GAIA 核心元件：金融領域知識庫、企業級 Model Hub、自研複合層級 AI 護欄、推動「AI 公民化」 — [國泰金控 GAIA 介紹頁](https://www.cathayholdings.com/holdings/brand/fintech/ctc/trends/2024cathay_gaia)；[數位時代 2024-11](https://www.bnext.com.tw/article/81192/cathaybk202411_01)
- 全集團統一 GAI 戰略與技術框架，子公司在框架上各自開發應用 — [iThome 165557](https://www.ithome.com.tw/news/165557)

**GAIA 2.0（2025-10-20 技術年會）— 框架已發表，Agent 應用逐步落地**
- GAIA 2.0 導入 AI Agent 概念，四大核心：Agent Core（核心框架）、Agent Workspace（可控環境）、Agent Protocol（串接協定）、Agent Marketplace（整合市集）。同時宣告進入「雲端優先（Cloud First）」階段 — [工商時報 2025-10-02](https://www.ctee.com.tw/news/20251002700870-430201)；[iThome 172381](https://www.ithome.com.tw/news/172381)；[iThome 172382](https://www.ithome.com.tw/news/172382)；[經濟日報](https://money.udn.com/money/story/5613/9082615)
- 規模數字（公司自述）：知識庫超過 200 種資料類別；Model Hub 匯集 50 多種模型，累計運算量 18 億 Token；自建 AI 護欄有 70 道安全檢查點 — [數位時代 2025-12（業配）](https://www.bnext.com.tw/article/85468/cathay1209)；[台視財經](https://www.ttv.com.tw/finance/view/1020252109347FF07719B5ED46F4AA6B09FC02B9EF235393/587)
- 2025 年技術年會逾 5 千人報名 — [國泰金控新聞稿](https://www.cathayholdings.com/holdings/lastest_news/news_archive/newsarticle?newsID=8-0C1qzaP0aGC2qHopqJCg)
- 多代理架構案例「Smart Archie」：以生成式 AI 加多 AI 代理打造「AI 雲端架構師團隊」，支援多雲治理（內部 IT 應用）— [iThome 172490](https://www.ithome.com.tw/news/172490)
- AI 護欄效能提升 4 倍，檢核時間從 28 秒縮短到 7 秒 — [商業周刊](https://www.businessweekly.com.tw/business/blog/3020485)；[鉅亨網](https://news.cnyes.com/news/id/6319245)

**GAIA STUDIO（國泰世華員工 AI 自助平台，低程式碼／無程式碼）— 已上線**
- 國泰世華稱之為「AI 民主化」，用視覺化、低程式碼／無程式碼介面，讓非技術員工自行設計 AI 工具。模型控制中心提供 Gemini、OpenAI 等多種 LLM，串接專屬知識庫（RAG）與自研 AI 護欄 — [經濟日報 2025](https://money.udn.com/money/story/122376/9188108)；[聯合報](https://udn.com/news/story/7239/9184120)；[ETtoday 廣編](https://finance.ettoday.net/news/3079123)
- 使用規模（各報導時間點不同，數字不一致）：
  - 上線三個月內，28 個部門自助開發超過 40 支內部 AI 服務 — [自由財經](https://ec.ltn.com.tw/article/paper/1735055)
  - 開放銀行 25 個種子單位使用，累計 35 款 AI 對話助手，每月平均對話逾 2.4 萬次 — [經理人](https://www.managertoday.com.tw/articles/view/72159)；[商業周刊](https://www.businessweekly.com.tw/business/blog/3020485)
  - 「已催生近 50 項 AI 應用」，涵蓋文書處理、知識檢索、資料整合 — [經濟日報](https://money.udn.com/money/story/122376/9188108)
  - 2026-01 商周 AI 百強新聞稿：GAIA 支援 25 個內部單位、開發逾 35 項 AI 助手工具 — [國泰產險新聞稿 2026-01-22](https://www.cathay-ins.com.tw/cathayins/news/20260122/)
- 商業周刊標題稱國泰「整合 5 萬員工、破解技術孤島」打造集團 AI 防護網。5 萬應是集團員工總數，不是 GAI 實際使用人數 — [商業周刊](https://www.businessweekly.com.tw/business/blog/3020485)

**OpenAI 策略合作（2026-04-07）— 已簽約、部署中**
- 國泰金控宣布與 OpenAI 長期策略合作，涵蓋 AI 研究、部署與治理；媒體稱這是台灣金融業首家、「金融業唯一」 — [中央社 2026-04-07](https://www.cna.com.tw/news/afe/202604070151.aspx)；[經濟日報](https://money.udn.com/money/story/5612/9426627)；[Taiwan News](https://www.taiwannews.com.tw/news/6335805)
- 內容：在旗下各子公司全面部署 ChatGPT Enterprise；打造「企業級 AI 工作站」，整合 OpenAI LLM、國泰內部知識庫與專屬 Agents，支援文件摘要、資料彙整、簡報製作、用自然語言生成程式碼，並在安全機制下串接既有系統 — [經濟日報](https://money.udn.com/money/story/123828/9427578)；[TechNews 2026-04-07](https://finance.technews.tw/2026/04/07/agentic-ai/)；[DIGITIMES](https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?cnlid=13&cat=100&id=0000751465_V4A3FQMP7T3BKG4OAUB7L)
- 同時使用 OpenAI API 開發新應用；首波兩項計畫是企業金融（corporate banking）與保險的 Agentic AI 系統（規劃／開發中）— [Frontier Enterprise](https://www.frontier-enterprise.com/cathay-fhc-taps-openai-to-push-group-wide-ai-adoption/)；[FutureCIO](https://futurecio.tech/cathay-fhc-to-advance-ai-adoption-with-openai/)
- 雙方將規劃專業培訓計畫，提升員工 AI 能力（規劃中）— [經濟日報](https://money.udn.com/money/story/123828/9427578)

**其他夥伴**
- Google Cloud：升級版阿發（Dialogflow CX、RAG、GKE、Gemini）；Google Cloud 台灣技術總經理林書平在 2026 技術年會講 Multi-Agent 架構 — [天下雜誌](https://www.cw.com.tw/article/5139151)；[經濟日報 2026-09](https://money.udn.com/money/story/123828/9815127)
- NVIDIA：2025 年合作研究生成式 AI 在金融場景落地；2026-06 GTC Taipei 發表 SLM 微調成果 — [PR Newswire 2026-06](https://www.prnewswire.com/apac/news-releases/cathay-financial-holdings-leverages-open-source-small-language-models-to-identify-customer-intent-302798631.html)
- 台灣本地模型：SLM 研究評估了 TAIDE、TAME 等本地開源模型 — [PR Newswire 2026-06](https://en.prnasia.com/releases/apac/cathay-financial-holdings-leverages-open-source-small-language-models-to-identify-customer-intent-536906.shtml)
- 雲端：2024 年獲主管機關核准，成為全台第一家全面推動資料上雲的金融業者 — [科技報橘 2026-04-13](https://techorange.com/2026/04/13/cathayholdings-ai-ready-forum/)

### Inferences
- 國泰採「自建平台＋多模型」路線：GAIA 是統一的治理與工具層，底層模型來源多元（OpenAI、Gemini、開源 SLM）。2026 年的 OpenAI 合作是在 GAIA 之上加入一套全員可用的商用 GenAI 工具，沒有取代 GAIA。
- 時間軸：2023 成立 AI CoE → 2024-01 治理委員會 → 2024-09 GAIA 1.0 → 2025-10 GAIA 2.0／Cloud First → 2026-04 OpenAI／ChatGPT Enterprise → 2026-09 Agent First／AI 數位同事。

### Gaps
- 沒有找到 ChatGPT Enterprise 的授權席次或實際使用人數；Taiwan News 等英文版也沒有提到席次。
- 沒有找到國泰與 Microsoft Azure OpenAI 或 AWS 的直接合作證據（搜尋無結果，不代表沒有合作）。
- GAIA 平台整體的員工活躍用戶數、整體節省工時都沒有公開數字。
- 部分英文報導的 CTO 英文名不一致（Marcus Yao／Marcus Lopez），中文報導是資深副總「姚旭杰」，以中文為準。

---

## Q3. AI 治理：倫理原則、委員會、對應金管會 AI 指引

### Takeaway
國泰在 2024-01 成立金控層級「資料暨 AI 治理委員會」，下設 AI 卓越中心（AI CoE，2023 年成立），以「負責任 AI」為原則。治理架構分六大面向，金控訂一階 AI 政策並對齊金管會 2024-06-20《金融業運用人工智慧(AI)指引》，子公司再訂二階辦法。另設「國泰 AI 評測中心」做上線前評測，技術面用 70 道檢查點的自研護欄把關。

### Cited Findings
- 2024 年 1 月成立金控級「資料暨 AI 治理委員會」，訂定集團 AI 治理規範，以負責任 AI 為發展原則；委員會下設 AI CoE，成員來自金控、銀行、人壽、產險等子公司，負責 AI 策略、技術治理與專案審查 — [網管人 NetAdmin](https://www.netadmin.com.tw/netadmin/zh-tw/trend/E36A75FB827D4DE9B413D81F4CE189FF)
- AI CoE 成立於 2023 年 — [科技報橘 2026-04-13](https://techorange.com/2026/04/13/cathayholdings-ai-ready-forum/)
- 負責任 AI 治理架構有六大面向：策略、法制、流程、組織、技術、應用；流程面包含風險評估框架與 AI 審核流程 — [網管人](https://www.netadmin.com.tw/netadmin/zh-tw/trend/E36A75FB827D4DE9B413D81F4CE189FF)
- 分級：金控的委員會與 AI CoE 制定集團「一階 AI 政策」（對齊金管會 AI 指引），各子公司依此訂「二階管理辦法」 — [網管人](https://www.netadmin.com.tw/netadmin/zh-tw/trend/E36A75FB827D4DE9B413D81F4CE189FF)
- 「國泰 AI 評測中心」：提供 AI 系統上線前的評測標準與工具，依據是金管會 AI 指引六大原則加上數位發展部 AI 評測中心的十大評測項目 — [網管人](https://www.netadmin.com.tw/netadmin/zh-tw/trend/E36A75FB827D4DE9B413D81F4CE189FF)；[科技報橘 2026-04-13](https://techorange.com/2026/04/13/cathayholdings-ai-ready-forum/)
- 金管會 2024-06-20 發布《金融業運用人工智慧(AI)指引》，性質是行政指導 — [金管會新聞稿](https://www.fsc.gov.tw/ch/home.jsp?id=96&parentpath=0%2C2&mcustomize=news_view.jsp&dataserno=202406200001&dtable=News)；[理律法律事務所](https://www.leeandli.com/TW/Newsletters/7287.htm)
- 技術治理：自建 AI 護欄有 70 道檢查點，防止機敏資訊外洩與不當內容；GAIA STUDIO 內建護欄 — [數位時代](https://www.bnext.com.tw/article/85468/cathay1209)；[經濟日報](https://money.udn.com/money/story/122376/9188108)
- AI 數位同事的治理：具身分與權限控管、資安監控、稽核追蹤；重大決策、規則確認、例外情境由真人做最終決策（human-in-the-loop）— [yipee 2026-09](https://3c.yipee.cc/355994/)；[鏡週刊 2026-09-15](https://www.mirrormedia.mg/story/20260915mkt002)
- 2026 技術年會把「負責任 AI」列為主軸之一 — [經濟日報 2026-09](https://money.udn.com/money/story/123828/9815127)
- 相關資安：國泰推動零信任強化計畫，目標三年內各子公司重要風險場景達到進階水準 — [iThome 168864](https://www.ithome.com.tw/news/168864)

### Inferences
- 國泰的治理是「委員會＋CoE＋評測中心＋技術護欄」四層結構，並明確對齊金管會 AI 指引六大原則。在台灣金融業中，這是公開揭露較完整的一家。

### Gaps
- 沒有取得國泰金控最新永續報告書（2025 年版）的 AI 治理章節原文，無法確認是否有書面 AI 倫理原則條列、委員會開會次數、AI 模型盤點數量等揭露。
- 沒有找到 AI 風險事件或外部 AI 稽核／認證（如 ISO/IEC 42001）的資訊。

---

## Q4. AI 人才與投資

### Takeaway
國泰負責 AI 的集團單位是金控「數數發中心（DDT，數據暨數位發展中心）」，下設數據暨人工智慧發展部。2025 年集團徵才 7,500 人，其中數位科技人才逾 800 名，較前一年增加 60%。2026 年數位科技職缺再創新高，連續第 4 年成長。資料科學家的實際人數和 AI 投資金額沒有公開。

### Cited Findings
- 2025 年集團招募 7,500 個職缺，重點招募逾 800 名數位科技人才（AI 資料科學分析師、雲端數據管理師、區塊鏈架構師、商業數據分析師等），較前一年大增 60%，創歷年新高 — [中央社 2025-01-02](https://www.cna.com.tw/news/afe/202501020204.aspx)；[鉅亨網](https://news.cnyes.com/news/id/5889829)；[DIGITIMES](https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=0000711460_MUP5S9MH5HHFV31IW4PUT)
- 2026 年：「國泰金擁抱 AI 人才，數位科技職缺逾 800 名創高、連續 4 年成長」 — [經濟日報](https://money.udn.com/money/story/5612/9365536)
- DDT 有「資料科學分析師 Data Scientist — 人工智慧科技」和「AI 資料科學家 Data&AI Scientist」等集團職缺 — [104 人力銀行](https://www.104.com.tw/job/87kgr)
- 主要 AI 主管：國泰金控副總經理暨國泰世華數據長梁明喬（Joe Liang）；數數發中心數據暨人工智慧發展部副總經理劉浩翔（Jeremy Liu）；國泰金控／國泰世華數位長陳冠學；資深副總姚旭杰（GAIA 發表人）；副總經理施君蘭 — [2026 國泰金控技術年會官網](https://www.cathaytechcon.com.tw/2026CTC/)；[天下 Podcast](https://podcasts.apple.com/sg/podcast/id1486227803?i=1000747294035)
- 員工 AI 培訓：國泰人壽「董總領頭全員學 AI」 — [天下雜誌 5132643](https://www.cw.com.tw/article/5132643)
- 前線部署工程師（FDE）：一篇搜尋摘要提到國泰設 FDE 協助前線員工導入 AI，但第二次搜尋沒有找到可證實的原文段落，可信度低 — [科技報橘 2026-04-13](https://techorange.com/2026/04/13/cathayholdings-ai-ready-forum/)（未證實）

### Inferences
- 800 名是「招募需求」，不是在職數位人才存量。合理推估國泰的數位／數據人才規模在千人級，但沒有公開數字可以證實，撰稿時應標為推估。

### Gaps
- 資料科學家／AI 工程師的在職人數、AI 研發預算或 IT 投資金額、AI 專責實驗室名稱和規模，都沒有找到公開數字（年報／永續報告書可能有，但本次無法直接讀取原文）。

---

## Q5. 2023–2026 最新動態（AI Agent、多代理系統）

### Takeaway
2026-09-15 第 7 屆國泰金控技術年會宣告從「Cloud First」進入「Agent First」，首度公開三位以 AI Agent 打造的「AI 數位同事」：Vanessa.ai（專案管理）、Sherlock.ai（科技治理審查）、Lawrence.ai（法務合約初審）。目前仍在專案測試／試驗階段，沒有公開成效數字。

### Cited Findings
- 2026-09-15 國泰金控技術年會（連續第 7 年舉辦）：近 7,000 人報名，線上加現場同時觀看逾 3,500 人；主題是 Agentic AI 與數位同事、AI 驅動 IT 現代化、數位資產與 Web3／穩定幣、負責任 AI — [經濟日報 2026-09](https://money.udn.com/money/story/123828/9815127)；[聯合報](https://udn.com/news/story/7239/9756265)；[工商時報 2026-09-16](https://www.ctee.com.tw/news/20260916700674-430201)
- 三位 AI 數位同事：Vanessa.ai（專案管理助手）、Sherlock.ai（科技治理審查專員）、Lawrence.ai（法務合約初審專員），「已實際投入專案測試」，仍是探索與實驗階段 — [CIO Taiwan](https://www.cio.com.tw/119970/)；[鉅亨網](https://news.cnyes.com/news/id/6607667)；[壹蘋 2026-09-15](https://news.nextapple.com/finance/20260915/EC46D92373626E31145B10254709B24B)
- 數位同事能依任務自行調用企業知識庫與工具，具長期記憶、跨工作階段記憶，能主動喚醒並持續推進長期任務 — [iThome 179000](https://www.ithome.com.tw/news/179000)（只看到標題與摘要）
- 國泰稱已從 Cloud First 走向 Agent First，以可治理的 AI Workflow 與 Agent Platform 建立「數位勞動力」，把 AI 實驗轉成可規模化的集團級 IT 能力；國泰世華以 AI Scrum、AI SDLC team 參與需求整理、開發測試與文件製作 — [CIO Taiwan](https://www.cio.com.tw/119970/)；[聯合報](https://udn.com/news/story/7239/9756265)
- 年會外部講者：OpenAI 國際業務主管謝家豪、Google Cloud 台灣技術總經理林書平（Multi-Agent 架構）— [工商時報 2026-09-08](https://www.ctee.com.tw/news/20260908700616-430201)
- 梁明喬預測 2026 年是金融業「AI Agent 元年」，從被動助理轉向自主代理 — [未來城市＠天下](https://futurecity.cw.com.tw/article/3930)
- 2026-04 OpenAI 合作的首波 Agentic AI 計畫：企業金融與保險（開發中）— [Frontier Enterprise](https://www.frontier-enterprise.com/cathay-fhc-taps-openai-to-push-group-wide-ai-adoption/)
- 2025-10 GAIA 2.0 的 Agent 架構，以及多代理「AI 雲端架構師團隊」Smart Archie — [iThome 172490](https://www.ithome.com.tw/news/172490)
- 2026-01-22 國泰金控 GAIA 獲商周 AI 創新百強銀質獎，國泰人壽獲白金獎，國泰產險獲優選獎 — [國泰產險新聞稿](https://www.cathay-ins.com.tw/cathayins/news/20260122/)

**已上線 vs 試辦／規劃（整理）**
| 項目 | 狀態 | 時間 |
|---|---|---|
| 阿發智能客服（含生成式 AI 升級版） | 已上線 | 2018 起；GenAI 版 2025 |
| GAIA 1.0（Model Hub、知識庫、護欄） | 已上線 | 2024-09 |
| GAIA STUDIO（國泰世華員工自助平台） | 已上線 | 2025 |
| GAIA 2.0 Agent 框架 | 已發表，應用逐步落地 | 2025-10 |
| 人壽理賠／核保 AI 模型 | 已上線 | 2024–2025 |
| 人臉辨識投保 | 試辦 | 2025-09 |
| 產險 CarTech 車險 AI | 已上線 | 至 2026-01 |
| 金融盾聯合學習防詐 | 已上線 | 至 2026 |
| 被害者樣態模型（與刑事局） | 2026 導入，成效為預估 | 2026 |
| ChatGPT Enterprise 全集團部署 | 部署中 | 2026-04 起 |
| 企金／保險 Agentic AI（OpenAI） | 開發中 | 2026 |
| 開源 SLM 客戶意圖辨識 | 研究驗證 | 2026-06 |
| AI 數位同事 Vanessa／Sherlock／Lawrence | 試驗（專案測試） | 2026-09 |
| AML SAR 撰寫 AI Agent | 已有案例，是否全面上線不明 | 2026-04 揭露 |

### Inferences
- 國泰 2026 年的 AI 主軸已從「員工知識助理」轉向「受治理的自主 Agent」，但對外仍標示為試驗，沒有給 KPI。可以判斷大規模、可量化的 Agent 成效最快要到 2027 年才會揭露。

### Gaps
- AI 數位同事的任務完成率、節省工時、錯誤率等試驗成效沒有公開。
- 沒有找到 2026 年 Q3 法說會簡報中的 AI KPI（本次無法讀取 cathayholdings.com 原文）。
- 沒有找到 AI Agent 支付、穩定幣與 AI 結合的具體上線內容，只有年會主題層級的描述。

# 專案交接 Prompt：日本壽險業認知症商品盤點

> 用法：開新對話時，把「---」以下全文貼上即可接續此專案。

---

你是我的 AI 指揮官（Claude Code）。請接手以下已完成第一階段的專案，先讀取指定檔案掌握現況，再等我下一步指示。

## 專案概要
- 專案名稱：日本壽險業「認知症（失智症）」相關商品全面盤點
- 目標：對生命保険協会 41 家會員公司地毯式盤查，主契約與特約分開表列、每項商品附簡介、另有熱銷與特殊商品專章，報告同時產出 Word 與 Markdown，所有事實需附參考來源。
- 第一階段已完成（2026-09-01），成果已 commit 並 push。

## 檔案位置（我的電腦）
- 工作資料夾（git 倉庫）：`C:\ai-work-local\Remote_use`，分支 `claude/japan-dementia-insurance-products-xk7ijh`，遠端 `https://github.com/jackoop-duke/Remote_use.git`
- 成果資料夾（OneDrive 同步）：`C:\Users\Jack\OneDrive\ai-work\dementia_insurance`
- 專案子目錄 `dementia_insurance\` 內容：
  - `research_plan.md`：研究計畫、分類碼、派工表
  - `report.md`／`report.docx`：最終報告（979 行，260 筆參考文獻）
  - `report_draft.md`：報告原稿，引用以 `[W1-R5]`、`[V-R3]` 等代碼標記，重建報告時修改此檔
  - `findings\WP-0 ~ WP-5、WP-2b`：各工單原始調查結果，每份檔尾有自己的來源清單
  - `findings\V_verification.md`：主筆複核紀錄與補查來源（27 筆）
  - `tools\build_report.py`：把 `report_draft.md` 的引用代碼解析成全域編號並產生參考文獻 → `report.md`
  - `tools\md2docx.py`：Markdown 轉 Word
  - `tools\sync_to_pc.ps1`：從 GitHub 拉取並複製成果到 OneDrive
- 重建流程：`python tools\build_report.py report_draft.md report.md` → `python tools\md2docx.py report.md report.docx`（需 `pip install python-docx`）

## 分類碼（全報告統一使用）
A 認知症專屬主契約／B 認知症專屬特約／C 介護保障型含認知症要件／D MCI・預防型／E 保費豁免・契約管理型（契約者代理特約、指定代理請求、家族登錄）／F 附帶服務

## 主要結論（摘要）
- 41 社中：A 類 12 社、B 類（不含 A）7 社、僅 C 類 8 社＋C 類要件未確認 4 社、D 類 14 社、僅 E/F 類 5 社、未見任何商品 4 社（FWD、カーディフ、明治安田トラスト、SBI 未確認）。
- 熱銷：太陽生命認知症系列累計 100 萬件（2025/4）；朝日生命あんしん介護シリーズ 100 萬件（2023/11）且 2026 オリコン專家評價第 1；加入率 2024 年度 7.6%。
- 趨勢：MCI 給付成標配；預防給付金（太陽）、認知症年金、Vitality 連動（住友）、歯数割引（第一ネオ）、外幣一時払內嵌（銀行窗販系）、契約者代理特約普及。
- 公司名異動已反映：ネオファースト→第一ネオ生命（2026/4）；アリアンツ→イオン・アリアンツ→明治安田トラスト生命（2025/10）；アクサダイレクト併入アクサ（2025/4）。

## 已知限制與待辦
- 第一階段執行環境無法開啟任何外部網頁全文，所有事實僅靠搜尋引擎摘要交叉確認；報告第十部列有 10 項待複核清單，最優先是取得生命保険協会 2021 年「別紙 生命保険各社の認知症保険および認知症に関するサービス」PDF（https://www.seiho.or.jp/activity/kourei/pdf/ninchi1.pdf）全文做一次性交叉驗證。
- 其他待複核：SBI 生命是否有認知症特約；FWD・カーディフ官網確認；ソニー・マニュライフ・クレディ・アグリコル・チューリッヒ的介護保障約款是否明示認知症；住友生命認知症PLUS 金額分級；太陽生命治療年金金額區間；各表「未確認」之發售年月與加入年齡。
- Word 版第四部 41 社總覽表為 10 欄，尚未肉眼檢視版面，可能需改橫向頁面。

## 工作方式（沿用）
- 我不是工程師，回報用白話中文。
- 派工原則：計畫擬定、review、彙整由你（主代理）負責；低階搜尋與資料蒐集派給較低成本的模型或外援（Codex CLI 主力、Gemini CLI 備援），派工規則見 `C:\ai-work-local` 內的 CLAUDE.md（若尚未放入，請先提醒我）。
- 修改報告一律改 `report_draft.md` 後重建，不要直接改 `report.md`；新來源加進對應 findings 檔尾的來源清單或 `V_verification.md`，並用代碼引用。
- 每個階段完成後 commit、push 到同一分支，並執行 `tools\sync_to_pc.ps1` 同步成果到 OneDrive。

請先讀 `research_plan.md`、`report.md` 第一部與第十部、`findings\V_verification.md`，用 10 行以內告訴我你掌握的現況，然後等我的指示。

# 專案交接 Prompt：日本壽險業認知症商品盤點

> 用法：開新對話時，把「---」以下全文貼上即可接續此專案。

---

你是我的 AI 指揮官（Claude Code）。請接手以下已完成第一階段的專案，先讀取指定檔案掌握現況，再等我下一步指示。

## 專案概要
- 專案名稱：日本壽險業「認知症（失智症）」相關商品全面盤點
- 目標：對生命保険協会 41 家會員公司地毯式盤查，主契約與特約分開表列、每項商品附簡介、另有熱銷與特殊商品專章，報告同時產出 Word 與 Markdown，所有事實需附參考來源。
- 第一階段已完成（2026-09-01）；第二階段複核（2026-09-03，本機環境開啟協會 PDF 與各社官網全文）已完成，成果已 commit 並 push。

## 檔案位置（我的電腦）
- 工作資料夾（git 倉庫）：`C:\ai-work-local\Remote_use`，分支 `claude/japan-dementia-insurance-products-xk7ijh`，遠端 `https://github.com/jackoop-duke/Remote_use.git`
- 成果資料夾（OneDrive 同步）：`C:\Users\Jack\OneDrive\ai-work\dementia_insurance`
- 專案子目錄 `dementia_insurance\` 內容：
  - `research_plan.md`：研究計畫、分類碼、派工表
  - `report.md`／`report.docx`：最終報告（1,014 行，278 筆參考文獻；Word 版 10 欄總覽表已置於橫向頁）
  - `report_draft.md`：報告原稿，引用以 `[W1-R5]`、`[V-R3]` 等代碼標記，重建報告時修改此檔
  - `findings\WP-0 ~ WP-5、WP-2b`：各工單原始調查結果，每份檔尾有自己的來源清單
  - `findings\V_verification.md`：主筆複核紀錄與補查來源（第一階段 R1～R27、第二階段 R28～R47）
  - `findingsef_seiho2021_ninchi1_extracted.txt`：生命保険協会 2021 年「別紙」PDF 全文抽出（29 社，2021/4 時點）
  - `tools\build_report.py`：把 `report_draft.md` 的引用代碼解析成全域編號並產生參考文獻 → `report.md`
  - `tools\md2docx.py`：Markdown 轉 Word
  - `tools\sync_to_pc.ps1`：從 GitHub 拉取並複製成果到 OneDrive
- 重建流程：`python tools\build_report.py report_draft.md report.md` → `python tools\md2docx.py report.md report.docx`（需 `pip install python-docx`）

## 分類碼（全報告統一使用）
A 認知症專屬主契約／B 認知症專屬特約／C 介護保障型含認知症要件／D MCI・預防型／E 保費豁免・契約管理型（契約者代理特約、指定代理請求、家族登錄）／F 附帶服務

## 主要結論（摘要）
- 41 社中（第二階段複核後）：A 類 12 社、B 類（不含 A）7 社＋部分 B 類 1 社（はなさく）、僅 C 類 8 社、D 類 13 社、僅 E/F 類 9 社（含 FWD 僅 2021 年協会資料所載服務；ソニー・マニュライフ・チューリッヒ介護保障未明示認知症故不計 C）、未見任何商品 4 社（カーディフ、明治安田トラスト、SBI、クレディ・アグリコル）。
- 熱銷：太陽生命認知症系列累計 100 萬件（2025/4）；朝日生命あんしん介護シリーズ 100 萬件（2023/11）且 2026 オリコン專家評價第 1；加入率 2024 年度 7.6%。
- 趨勢：MCI 給付成標配；預防給付金（太陽）、認知症年金、Vitality 連動（住友）、歯数割引（第一ネオ）、外幣一時払內嵌（銀行窗販系）、契約者代理特約普及。
- 公司名異動已反映：ネオファースト→第一ネオ生命（2026/4）；アリアンツ→イオン・アリアンツ→明治安田トラスト生命（2025/10）；アクサダイレクト併入アクサ（2025/4）。

## 已知限制與待辦
- 第一階段執行環境無法開啟網頁全文；第二階段（2026-09-03）已取得協会 2021 年「別紙」PDF 全文並開啟各社官網，第十部 10 項待複核事項全數覆核，結果見 `report.md` 第十部與 `V_verification.md` 第二階段章節。
- 殘餘待辦：大樹生命「特定認知症保障特約」初版年（僅能定為 2021/4 之後）；マニュライフ官網原文（回應 403，現用次級來源）；FWD「認知度チェックテスト」現行提供狀況；各表仍標「未確認」之發售年月與加入年齡。
- 協会「別紙」為 2021/4 時點資料，其後新商品（東京海上認知症一時金特約、第一ネオ、ライフネット be、大樹ケアα 等）以各社官網為準。

## 工作方式（沿用）
- 我不是工程師，回報用白話中文。
- 派工原則：計畫擬定、review、彙整由你（主代理）負責；低階搜尋與資料蒐集派給較低成本的模型或外援（Codex CLI 主力、Gemini CLI 備援），派工規則見 `C:\ai-work-local` 內的 CLAUDE.md（若尚未放入，請先提醒我）。
- 修改報告一律改 `report_draft.md` 後重建，不要直接改 `report.md`；新來源加進對應 findings 檔尾的來源清單或 `V_verification.md`，並用代碼引用。
- 每個階段完成後 commit、push 到同一分支，並執行 `tools\sync_to_pc.ps1` 同步成果到 OneDrive。

請先讀 `research_plan.md`、`report.md` 第一部與第十部、`findings\V_verification.md`，用 10 行以內告訴我你掌握的現況，然後等我的指示。

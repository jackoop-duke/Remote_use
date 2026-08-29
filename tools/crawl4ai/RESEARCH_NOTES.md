# Crawl4AI 研究紀錄

- **紀錄日期**:2026-08-29
- **來源**:Threads 貼文(@ai_triallab)推薦的 GitHub 專案
- **專案**:[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) — Open-source LLM Friendly Web Crawler & Scraper
- **存檔**:`crawl4ai-v0.9.2-7e80152.tar.gz`(本目錄,8.9MB,1056 個檔案)
  - 版本:v0.9.2(2026-07-15 發布)
  - Commit:`7e801521428ee12509994d39151006f64055ebe3`
  - 打包方式:`git archive`(不含 .git 歷史),解壓即為完整原始碼

## 這是什麼

Crawl4AI 是開源的 Python 網頁爬蟲/抓取框架,核心賣點是「專為 LLM 打造」:
把任意網頁轉成乾淨、規範的 Markdown 或結構化 JSON,直接餵給 LLM 做 RAG、
AI agent 或資料流水線。

- 授權:Apache 2.0(建議標註出處)
- 完全免費、不用註冊、不需要 API Key
- GitHub 星標最高的爬蟲類專案(截圖時約 80k stars / 8k forks / 87 contributors)
- 需求:Python >= 3.10,底層用 Playwright 驅動瀏覽器
- 官方另有 Cloud API(closed beta 中,尚未公開)

## 核心功能

| 面向 | 說明 |
|------|------|
| Markdown 生成 | 帶引用/參考連結的結構化輸出;`fit_markdown` 自動剝掉導覽列、廣告等雜訊,降低 token 成本 |
| 結構化擷取 | CSS selector、XPath;也可用 LLM 依 schema 抽取欄位 |
| 瀏覽器控制 | Playwright:session 管理、代理、stealth 模式、虛擬捲動(無限捲動頁面) |
| 深度爬取 | BFS/DFS 策略、crash recovery、prefetch 模式(官方稱大型任務快 5–10 倍) |
| 部署 | Docker + FastAPI API server、JWT 驗證、監控儀表板、GPU 容器支援 |

## 快速上手

```bash
pip install -U crawl4ai
crawl4ai-setup    # 安裝 Playwright 瀏覽器
crawl4ai-doctor   # 檢查環境
```

```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://example.com")
        print(result.markdown)

asyncio.run(main())
```

## 版本近況

- **v0.9.2**(2026-07,本存檔版本):維護版;修 MemoryAdaptiveDispatcher
  串流任務洩漏、Docker Playground 驗證、Playwright headless-shell 打包、GPU Docker build
- **v0.9.0**:重要安全性版本,Docker API server 預設啟用驗證(secure-by-default)

## 限制與評估

1. **反爬蟲能力有限**:遇到 Cloudflare、驗證碼等強防護站點需自備代理池或其他工具;
   這是與付費服務(Firecrawl、Bright Data 等)最大差距
2. **基礎設施自己扛**:程式庫免費,但規模化時瀏覽器程序吃記憶體、
   任務佇列需要背壓與監控;伺服器/代理/LLM 費用加總可能超過託管方案
3. **適用定位**:Python 團隊的研究、原型、內部工具、RAG 資料管線最合適;
   想「買基礎設施」省事選託管 API(Firecrawl 約 $83/月起),
   想「擁有並客製爬取邏輯」選 Crawl4AI

## Threads 貼文查核

- 「GitHub 上星標最高的爬蟲工具」:屬實
- 「免費、不用註冊、不需要 API Key」:屬實(程式庫本身)
- 「最新版優化記憶體調度跟 GPU 容器部署」:屬實(對應 v0.9.x)
- 「作者被 $16/月付費爬蟲惹毛而手搓」:起源故事與官方 README 一致
  (被要求付費才能取回自己的資料),金額細節為社群轉述

## 參考來源

- [Crawl4AI on PyPI](https://pypi.org/project/Crawl4AI/)
- [官方文件](https://docs.crawl4ai.com/)
- [ScrapingBee: Crawl4AI guide](https://www.scrapingbee.com/blog/crawl4ai/)
- [Apify: Crawl4AI vs. Firecrawl](https://blog.apify.com/crawl4ai-vs-firecrawl/)
- [WebcrawlerAPI: Best open source crawlers 2026](https://webcrawlerapi.com/blog/best-open-source-web-crawlers)

## 還原方式

```bash
tar -xzf crawl4ai-v0.9.2-7e80152.tar.gz -C crawl4ai-src
# 或直接從上游取得同一版本:
git clone --branch v0.9.2 https://github.com/unclecode/crawl4ai
```

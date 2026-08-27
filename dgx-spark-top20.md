# 地端 DGX Spark 有趣及有用程式/App/Skill 20 選

> 地毯式調查報告 · 2026-08-27
> 調查範圍:NVIDIA 官方 DGX Spark Playbooks(47+ 份)、GitHub、Hugging Face、NVIDIA 開發者論壇、社群實測評測
> 方法:4 路並行研究(LLM 推論/媒體生成/Agent 與 RAG 工具/微調與科學應用),ARM64 Docker 映像逐一對 Docker Hub / GHCR manifest 驗證

---

## 先懂硬體,才會選對軟體

DGX Spark(GB10 Grace Blackwell)的三個關鍵事實,決定了什麼軟體「在它上面特別有價值」:

| 特性 | 數值 | 意義 |
|---|---|---|
| 統一記憶體 | 128GB LPDDR5x(實際可用約 110GB) | **能跑消費級顯卡(24–32GB)完全塞不下的模型** —— 這是 Spark 的核心價值 |
| 記憶體頻寬 | ~273 GB/s | 天花板所在:解碼速度比 RTX 5090 慢 2–4 倍,「容量取勝、速度不取勝」 |
| CPU / GPU | 20 核 ARM(aarch64)+ Blackwell sm_121,CUDA 13 | x86 二進位檔不能跑;預編譯 wheel 常缺 sm_121 kernel,**優先用 NGC 容器與官方 playbook 容器** |

最甜蜜點是 **MoE 模型**(總參數大、啟用參數小):gpt-oss-120b、GLM-4.5-Air、Qwen3-80B/235B 級。單機可舒適容納 gpt-oss-120b MXFP4(約 60GB,解碼 ~60 t/s)。

官方資源總入口:[build.nvidia.com/spark](https://build.nvidia.com/spark) 與 [NVIDIA/dgx-spark-playbooks](https://github.com/NVIDIA/dgx-spark-playbooks)(47+ 份 playbook)。社群整理:[awesome-dgx-spark](https://github.com/bidual/awesome-dgx-spark)、[natolambert/dgx-spark-setup](https://github.com/natolambert/dgx-spark-setup)。

---

## 20 選總覽

| # | 名稱 | 類別 | Spark 相容狀態 |
|---|---|---|---|
| 1 | Ollama + Open WebUI | 私人 ChatGPT | ✅ 官方 playbook |
| 2 | llama.cpp | 推論引擎(單人最快上手) | ✅ 官方 playbook + 作者親測 |
| 3 | vLLM / SGLang | 多人併發 API 服務 | ✅ 官方 playbook |
| 4 | TensorRT-LLM + NVFP4 量化 | Blackwell 原生推論 | ✅ 官方 playbook |
| 5 | LM Studio | 桌面 GUI | ✅ 官方 playbook(以 Spark 為 ARM64 Linux 首發機) |
| 6 | EXO 雙機叢集 | 跑 >128GB 巨型模型 | ⚠️ 社群驗證(alpha) |
| 7 | ComfyUI | 影像/影片/音訊生成中樞 | ✅ 官方 playbook + NVFP4 原生支援 |
| 8 | FLUX.1/FLUX.2 + DreamBooth LoRA | 影像生成與微調 | ✅ 官方 playbook |
| 9 | Wan2GP(DGX-Spark fork) | 影片生成超級 App | ⚠️ 社群驗證(專用 fork) |
| 10 | faster-whisper / whisper.cpp | 語音轉文字 | ✅ Arm 官方教程 + 社群驗證 |
| 11 | Kokoro / Chatterbox / F5-TTS | 語音合成與聲音克隆 | ✅ 社群驗證 |
| 12 | ACE-Step 1.5 | 本地音樂生成 | ⚠️ 社群驗證 |
| 13 | Unsloth | 微調 gpt-oss-120b 級模型 | ✅ 官方 playbook + 官方部落格 |
| 14 | LLaMA-Factory | 圖形化微調 WebUI | ✅ 官方 playbook |
| 15 | Continue.dev / Cline / Aider | 本地 AI 編程助手 | ✅ 官方 Vibe Coding playbook |
| 16 | OpenHands | 自主軟體工程 Agent | ✅ ARM64 Docker 已驗證 |
| 17 | n8n + Self-hosted AI Starter Kit | 私有自動化工作流 | ✅ ARM64 Docker 已驗證 |
| 18 | AnythingLLM / LightRAG | 私有知識庫 RAG | ✅ NVIDIA 背書 + ARM64 已驗證 |
| 19 | Home Assistant × Spark 語音管家 | 智慧家庭 AI 大腦 | ✅ 標準架構(Wyoming 協定) |
| 20 | Isaac Lab + GR00T / LeRobot | 機器人模擬與訓練 | ✅ 官方 playbook + 社群驗證 |

---

## 一、LLM 推論與服務(#1–6)

### 1. Ollama + Open WebUI —— 十分鐘擁有私人 ChatGPT

- **連結:** [ollama/ollama](https://github.com/ollama/ollama)(~180k ⭐)· [open-webui/open-webui](https://github.com/open-webui/open-webui)(~150k ⭐)
- **是什麼:** Ollama 是最易用的模型管理 + 推論引擎(OpenAI 相容 API);Open WebUI 是事實標準的自架 ChatGPT 介面(多用戶、RAG、網頁搜尋、MCP)。
- **Spark 狀態:** 兩者皆有**官方 playbook**([Open WebUI with Ollama](https://build.nvidia.com/spark/open-webui));Ollama 與 NVIDIA 在上市前即合作,原生出 ARM64+CUDA 版並發表[官方效能文章](https://ollama.com/blog/nvidia-spark-performance)。
- **為什麼有趣:** 這是整台機器的「前門」——之後所有端點(vLLM、NIM、LightRAG)都能註冊進同一個 UI 給全家/全團隊用。128GB 讓你能同時常駐一個 120B 對話模型 + 一個 coding 模型 + embedding 模型。
- **注意:** Ollama 在統一記憶體上偶爾誤判可用量而悄悄把模型切到 CPU——用 `ollama ps` 確認全在 GPU。

### 2. llama.cpp —— 驗證最充分、單人最快

- **連結:** [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)(~126k ⭐)
- **Spark 狀態:** **官方 playbook**,且作者 Georgi Gerganov 親自在 Spark 上發表[官方 benchmark 討論串](https://github.com/ggml-org/llama.cpp/discussions/16578)。
- **實測數據:** gpt-oss-120b MXFP4:prefill ~1,900 t/s、**解碼 ~60 t/s**;gpt-oss-20b:prefill ~3,600 t/s。Blackwell 原生 MXFP4 kernel 已實驗性合入。
- **為什麼有趣:** 60GB 的 120B 級模型 + 超長 KV cache 全放統一記憶體;`GGML_CUDA_ENABLE_UNIFIED_MEMORY=1` 可選。單人互動延遲最佳。
- **注意:** 需 NVIDIA 6.17+ 核心(載入時間 104s→22s、恢復應有速度);無官方 aarch64+CUDA 預編譯檔,需 `-DGGML_CUDA=ON` 自建(HF 上有社群 sm_121a 預編譯:[merve/llama.cpp-dgx-spark-gb10-sm121a](https://huggingface.co/merve/llama.cpp-dgx-spark-gb10-sm121a))。

### 3. vLLM / SGLang —— 把 Spark 變成小型生產級 API 伺服器

- **連結:** [vllm-project/vllm](https://github.com/vllm-project/vllm)(~90k ⭐)· [sgl-project/sglang](https://github.com/sgl-project/sglang)(~32.5k ⭐)
- **Spark 狀態:** 各有**官方 playbook**;vLLM 官方發表 [DGX Spark 專文](https://vllm.ai/blog/2026-06-01-vllm-dgx-spark),sm_121 支援已合入(用 `vllm/vllm-openai:cu130-nightly` 或 playbook 容器)。
- **實測數據:** SGLang 在 gpt-oss-120b 解碼 **~52 t/s**(單機最快回報);vLLM 在併發場景比 Ollama 快 2–3 倍。
- **為什麼有趣:** 給團隊/多 Agent 併發用的 OpenAI 相容伺服器——continuous batching + prefix caching 是 Ollama 沒有的。所有後面的 coding/Agent 工具都吃這個端點。
- **注意:** 務必用 CUDA 13 容器版本;pip 安裝的舊 wheel 在 GB10 上會炸(sm_120 kernel 問題已修,但版本要對)。

### 4. TensorRT-LLM + NVFP4 量化 —— 真正吃到 Blackwell FP4 算力

- **連結:** [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)(~14.5k ⭐)· [TensorRT Model Optimizer](https://github.com/NVIDIA/TensorRT-Model-Optimizer)
- **Spark 狀態:** **三份官方 playbook**(TRT-LLM 推論、NVFP4 量化、投機解碼)。
- **為什麼有趣:** 「1 PFLOP FP4」這個數字就活在這裡。NVFP4 讓模型體積約砍半(如 Nemotron-30B:60GB→18GB),CES 2026 更新實測 FP8→NVFP4 + Eagle3 投機解碼**吞吐量翻倍以上**。也是**唯一官方支援的多台 Spark 張量平行**方案(2–3 台跑 Qwen3-235B 級)。
- **注意:** 對版本極敏感(GB10 上 RC 版常有 `sm_121a` ptxas 錯誤),嚴格照 playbook 指定的容器 tag。

### 5. LM Studio —— 桌面級 GUI,Spark 是它的 ARM64 Linux 首發機

- **連結:** [lmstudio.ai](https://lmstudio.ai)([官方 DGX Spark 文章](https://lmstudio.ai/blog/dgx-spark))
- **Spark 狀態:** **官方 playbook**;LM Studio 專為 DGX Spark 推出 Linux ARM64 版(此前只有 macOS/Windows/x86)。
- **為什麼有趣:** 最無痛的圖形化模型下載/試玩/比較體驗;headless 伺服器模式 + 「LM Link」可把 Spark 上的模型透過加密通道分享給你的筆電用。
- **注意:** 閉源;重度服務場景仍建議 vLLM/SGLang。

### 6. EXO 雙機叢集 —— 兩台 Spark 跑 Llama-405B

- **連結:** [exo-explore/exo](https://github.com/exo-explore/exo)(~47k ⭐)· 完整雙機指南:[ArgentAIOS/dgx-spark-cluster](https://github.com/ArgentAIOS/dgx-spark-cluster)
- **Spark 狀態:** 社群驗證(alpha,tinygrad CUDA 後端);官方另有 Connect Two/Three Sparks、NCCL 等叢集 playbook。
- **為什麼有趣:** 兩台 Spark 用機背 ConnectX-7 200GbE 直連(免交換器)= 256GB 統一記憶體池,可跑 Llama-405B 4-bit(~200GB)。EXO Labs 更示範過 2 台 Spark(prefill)+ M3 Ultra Mac Studio(decode)的異構分工,快 2.8 倍([Tom's Hardware 報導](https://www.tomshardware.com/software/two-nvidia-dgx-spark-systems-combined-with-m3-ultra-mac-studio-to-create-blistering-llm-system-exo-labs-demonstrates-disaggregated-ai-inference-and-achieves-a-2-8-benchmark-boost))。
- **注意:** alpha 成熟度;叢集是「借容量、不借速度」。務實路線是 TRT-LLM 多節點 playbook。

---

## 二、影像/影片/語音/音樂生成(#7–12)

### 7. ComfyUI —— 一切生成式媒體的中樞

- **連結:** [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)(~90k ⭐)
- **Spark 狀態:** **官方 playbook**(10 分鐘出圖);NVIDIA 2026 年 1 月更新為 Spark 加入**原生 NVFP4/FP8** 支援——最高 3 倍速、省 60% 記憶體。
- **為什麼有趣:** 節點式工作流一次驅動 FLUX、SD3.5、Qwen-Image(20B!)、Wan、LTX、ACE-Step 全部模型。128GB 讓 transformer + T5 文字編碼器 + VAE 全精度同時常駐,不用像 24GB 卡那樣拆來拆去。
- **實測:** FLUX.1-dev 約 82s/張;FLUX.2 Klein 9B 約 60s(Tom's Hardware)。
- **注意:** 早期韌體在重負載影片工作流有電源尖峰當機問題,社群已有修正(功耗限制 patch);Spark 專用優化包:[comfyui-aeon-spark](https://github.com/AEON-7/comfyui-aeon-spark)(CUDA 13 + SageAttention sm_121a + NVFP4)。

### 8. FLUX.1 / FLUX.2 + DreamBooth LoRA 微調 —— 在桌上訓練自己的影像模型

- **連結:** [black-forest-labs/flux](https://github.com/black-forest-labs/flux)(~13k ⭐)· [官方微調 playbook](https://build.nvidia.com/spark/flux-finetuning)
- **Spark 狀態:** 推論(ComfyUI playbook)與**微調(專屬 playbook)**皆官方支援;FLUX.2 有 Spark 最佳化 NVFP4 checkpoint。
- **為什麼有趣:** 對 12B 擴散模型做 DreamBooth LoRA 訓練,在 24GB 消費卡上幾乎不可能——這是 Spark 的招牌「別處辦不到」工作負載。訓練完的 LoRA 直接丟回 ComfyUI 用。

### 9. Wan2GP(DGX-Spark fork)—— 開源影片生成超級 App

- **連結:** [deepbeepmeep/Wan2GP](https://github.com/deepbeepmeep/Wan2GP)(~10k ⭐)· Spark 專用 fork:[rongxike/Wan2GP-DGX-SPARK](https://github.com/rongxike/Wan2GP-DGX-SPARK)
- **是什麼:** 一個 Gradio 介面整合 Wan 2.1/2.2、LTX-2、HunyuanVideo 1/1.5、Qwen-Image、FLUX、TTS/音樂模型,含佇列、LoRA、量化格式。
- **為什麼有趣:** Wan 2.2 A14B 未優化需 ~80GB VRAM、HunyuanVideo 720p 需 60–80GB——都是「只有 Spark 級記憶體跑得動」的經典。**務實建議:影片首選 LTX-2**(NVIDIA day-0 支援,720p 短片約 3 分鐘);Wan 2.2 用 4-step 蒸餾 LoRA + fp8,否則 5 秒 720p 要 30+ 分鐘。
- **注意:** 上游以 x86 為主,用 fork 或 Docker。

### 10. faster-whisper / whisper.cpp —— 快於即時的本地語音轉文字

- **連結:** [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)(~18k ⭐)· [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)(~45k ⭐)· [WhisperX Blackwell 移植](https://github.com/Mekopa/whisperx-blackwell)
- **Spark 狀態:** **Arm 官方 Learning Path** 用 faster-whisper + vLLM 在 Spark 上建整套離線語音聊天機器人(互動延遲 ~70–90ms);whisper.cpp 有社群 CUDA 13 ARM64 Docker 建置指南。
- **為什麼有趣:** Whisper 本身不吃記憶體(large-v3 約 3GB),重點是**能和 120B LLM + TTS 同機共存**——統一記憶體、零 PCIe 拷貝,湊成完整語音管線。
- **注意:** CTranslate2 的 aarch64+CUDA13 wheel 需用社群版或自建。

### 11. Kokoro / Chatterbox / F5-TTS —— 語音合成與聲音克隆三件套

- **連結:** [hexgrad/kokoro](https://github.com/hexgrad/kokoro)(~5k ⭐,82M 參數,超快,Apache-2.0)· [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox)(~12k ⭐,5 秒樣本零樣本克隆,MIT)· [SWivid/F5-TTS](https://github.com/SWivid/F5-TTS)(~14k ⭐,克隆自然度最佳)
- **Spark 狀態:** Kokoro 有 [Spark ARM64 實測](https://forums.developer.nvidia.com/t/running-kokoro-tts-on-nvidia-dgx-spark-arm64-gb10/368846);Chatterbox 隨 Wan2GP 驗證;另有 Spark 專用語音管線 [VibeVoice 實測 766ms 首音延遲](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B/discussions/23)。
- **為什麼有趣:** 全部 <3GB,在 Spark 上是「順便跑」的等級——搭配 #10 和 #19 組成完全離線的語音助理。
- **注意:** torchaudio 在 ARM64 安裝有坑,照論壇指南裝。

### 12. ACE-Step 1.5 —— 本地版 Suno

- **連結:** [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5)(新版快速竄紅;v1 約 3k ⭐)
- **是什麼:** 3.5B 開源音樂基礎模型——含人聲的完整歌曲、歌詞控制、LoRA 個人化;v1.5 宣稱商用級品質。
- **Spark 狀態:** 社群驗證——已預載於 Spark 專用 ComfyUI 包(comfyui-aeon-spark)與 Wan2GP。
- **為什麼有趣:** 音樂生成是目前本地 AI 最被低估的玩法;128GB 讓你邊生音樂邊跑其他模型,還能 LoRA 訓練自己的風格。

---

## 三、微調訓練(#13–14)

### 13. Unsloth —— 在桌上 QLoRA 微調 gpt-oss-120b

- **連結:** [unslothai/unsloth](https://github.com/unslothai/unsloth)(~50k ⭐)
- **Spark 狀態:** **官方 playbook** + [NVIDIA 官方部落格](https://developer.nvidia.com/blog/train-an-llm-on-an-nvidia-blackwell-desktop-with-unsloth-and-scale-it/) + Unsloth 官方 Spark 文件。
- **為什麼有趣:** 這是全份清單最「只有 Spark 辦得到」的一項:**QLoRA 微調 120B 級模型**(4-bit 權重 60–70GB + 最佳化器/激活值)只因 CPU/GPU 共用一池記憶體才裝得下。官方示範含 RL(GRPO)訓練 gpt-oss-20b 玩 2048。
- **注意:** 用 playbook 指定的 NGC `pytorch:25.11-py3` 容器;上市初期需 transformers patch(已修)。社群還有宣稱 7.7x 加速的 sm_121a Triton kernel 專案。

### 14. LLaMA-Factory —— 點滑鼠就能微調 100+ 模型

- **連結:** [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)(~60k ⭐)
- **Spark 狀態:** **官方 playbook**(SFT/LoRA/QLoRA/DPO,附 WebUI)。
- **實用尺寸表(官方 PyTorch 微調 playbook):** 全參數微調 Llama-3.2-3B;LoRA 到 70B;QLoRA 到 Llama-3.3-70B——70B LoRA 是 HF 技術棧在 128GB 內的現實天花板。
- **注意:** UMA 記憶體壓力大時官方建議手動清 buffer cache;訓練任務用 cgroup 限制在 ~100GB 以免「swap 死亡螺旋」(統一記憶體沒有乾淨的 OOM)。

---

## 四、AI 編程(#15–16)

### 15. Continue.dev / Cline / Aider —— 零 API 費的本地 Copilot

- **連結:** [continuedev/continue](https://github.com/continuedev/continue)(~35.6k ⭐)· [cline/cline](https://github.com/cline/cline)(~66.9k ⭐)· [Aider-AI/aider](https://github.com/Aider-AI/aider)(~48.5k ⭐)
- **Spark 狀態:** NVIDIA 有**官方「Vibe Coding in VS Code」playbook**(Ollama + Continue.dev)與「CLI Coding Agent」playbook;Cline 有 vLLM on Spark 詳細教學。
- **為什麼有趣:** Cline 這類 Agent 極度吃 token(長系統提示 + 大量工具呼叫)——正是「無按量計費的 128GB 私有機」的完美用途。Continue.dev 獨有本地 **Tab 自動補全(FIM)**:小模型(qwen2.5-coder 1.5b/7b)補全 + 大模型(gpt-oss-120b / Qwen3-Coder-30B)對話,兩者同時常駐。
- **注意:** 記得拉高 `OLLAMA_CONTEXT_LENGTH`(≥64k),否則 Agent 迴圈悄悄劣化;實測心得:Aider 對指令明確的修改最穩,Agent 模式對本地模型的工具呼叫仍不如雲端頂級模型。

### 16. OpenHands —— 自主軟體工程 Agent 整套跑在 Spark 上

- **連結:** [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)(~85.2k ⭐,MIT)
- **Spark 狀態:** Docker 多架構映像(**arm64 已驗證**),整個沙箱化 SWE Agent(終端 + 瀏覽器 + 執行環境)可直接在 Spark 上跑;官方文件有本地模型指南(Devstral、Qwen3-Coder、gpt-oss)。
- **為什麼有趣:** 一次長程 SWE 任務燒數百萬 token,在 Spark 上免費且私有——丟一張 issue 給它,晚上回來看 PR。
- **注意:** 本地模型的解題率仍明顯低於雲端頂級模型;沙箱容器會和模型伺服器搶記憶體。

---

## 五、Agent 工作流與知識庫(#17–18)

### 17. n8n + Self-hosted AI Starter Kit —— 私有自動化的黏著劑

- **連結:** [n8n-io/n8n](https://github.com/n8n-io/n8n)(~202.5k ⭐)· [Starter Kit](https://github.com/n8n-io/self-hosted-ai-starter-kit)(n8n + Ollama + Qdrant + Postgres 一鍵 compose)
- **Spark 狀態:** ARM64 Docker **已驗證**,Starter Kit 幾乎是為 Spark 量身打造——把它的 Ollama 指向 Spark 的 GPU 端點即可。
- **為什麼有趣:** 400+ 整合 + 原生 AI Agent 節點 + MCP:郵件摘要、Slack 機器人、RAG 排程、資料管線,全部不出內網。範本生態巨大(n8n-workflows 集合 ~56k ⭐)。進階版:[coleam00/local-ai-packaged](https://github.com/coleam00/local-ai-packaged)(再加 Open WebUI、Supabase、SearXNG、Langfuse)。
- **注意:** fair-code 授權(非 OSI);Agent 節點要配工具呼叫可靠的模型(gpt-oss、Qwen3)。

### 18. AnythingLLM / LightRAG —— NVIDIA 背書的私有知識庫

- **連結:** [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)(~65.3k ⭐)· [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)(~39.2k ⭐,EMNLP'25)
- **Spark 狀態:** AnythingLLM 是 **NVIDIA 官方宣傳的 Spark 夥伴**(「runs seamlessly on DGX Spark」),ARM64 Docker 已驗證;LightRAG 的 GHCR arm64 映像已驗證,且能偽裝成 Ollama 模型掛進 Open WebUI。
- **為什麼有趣:** AnythingLLM 是最低門檻的「餵文件、問問題」全包 App(等於 Chat with RTX 的正統後繼);LightRAG 用知識圖譜 + 向量做多跳推理,索引期的大量 LLM 呼叫由本地 128GB 伺服器免費吸收。
- **注意:** 要頂級 PDF/掃描件解析選 [RAGFlow](https://github.com/infiniflow/ragflow)(~89.3k ⭐)——官方映像只有 amd64,但 NVIDIA 論壇已有 [Spark 原生 ARM64 建置成功案例](https://forums.developer.nvidia.com/t/ragflow-v0-24-0-on-dgx-spark-working-native-arm64-build-with-gpu-accelerated-ocr/366321)(GPU 加速 OCR)。

---

## 六、特色應用(#19–20)

### 19. Home Assistant × Spark —— 70B 級的本地語音管家

- **連結:** [home-assistant/core](https://github.com/home-assistant/core)(~90.1k ⭐)
- **架構:** HA 留在原本的小主機,**Spark 當 AI 大腦**:HA 原生 Ollama 整合(對話)+ Wyoming 協定掛 faster-whisper(STT)+ Piper(TTS),全部 GPU 加速在 Spark 上。
- **為什麼有趣:** 一般家庭因硬體限制只能跑 llama3.2:3b 當語音助理;Spark 讓管家直接升級成 70B–120B 帶工具呼叫的模型,同時 whisper-large 即時聽寫——體驗是質變,而且語音永遠不出家門。
- **注意:** 語音延遲預算緊:模型設 `keep_alive=-1` 常駐、開串流;暴露太多 HA 實體會把 prompt 撐爆,要圈定 Agent 能控制的範圍。

### 20. Isaac Lab + GR00T N1.5 / LeRobot —— 桌上型機器人實驗室

- **連結:** [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab)(~5k ⭐)· [NVIDIA/Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T)(~5k ⭐)· [huggingface/lerobot](https://github.com/huggingface/lerobot)(~18k ⭐)
- **Spark 狀態:** Isaac Sim/Lab 有**官方 playbook**(aarch64 原始碼建置,示範 Unitree H1 人形機器人步態 RL);GR00T 微調有[完整社群驗證指南](https://github.com/NVIDIA/Isaac-GR00T/issues/474);LeRobot 走 NVIDIA 官方 sim-to-real SO-101 課程,社群實測 ACT 策略訓練僅用 ~18GB。
- **為什麼有趣:** GR00T 機器人 VLA 基礎模型微調需 ~48GB VRAM——消費卡不可能、Spark 很舒適,**可說是最強的「只有 Spark 辦得到」桌面工作負載**。搭配一隻 SO-101 機械臂(~百美元級)就是完整的模仿學習→微調→部署管線。官方 playbook 還有 Reachy Mini 拍貼機示範。
- **注意:** Isaac 需原始碼建置(10–15 分鐘,GCC 11);大規模平行 RL 環境數量比不上 5090。

---

## 遺珠之憾(值得知道的 10+ 個)

| 名稱 | 一句話 | 狀態 |
|---|---|---|
| [Dify](https://github.com/langgenius/dify)(~153.6k ⭐)/ [Langflow](https://github.com/langflow-ai/langflow)(~153.7k ⭐) | 團隊級 LLM App/Agent 視覺化平台,ARM64 映像皆已驗證 | 與 n8n 擇一即可 |
| [local-deep-research](https://github.com/LearningCircuit/local-deep-research)(~9k ⭐) | 「本地優先」深度研究:本地模型 + SearXNG + 私有文件,ARM64 已驗證 | 最像為 Spark 而生的研究工具 |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher)(~29.2k ⭐) | 自動產出附引用的長篇研究報告 | 單篇報告燒數十萬 token → 本地免費 |
| [Boltz-2](https://github.com/jwohlwend/boltz) / [OpenFold3 Spark 移植](https://github.com/adrian-greenneuron/openfold3-DGX-Spark) | AlphaFold3 級蛋白質結構預測,GB10 實測(泛素 55 秒) | 大複合體只有 128GB 跑得動 |
| RAPIDS / CUDA-X 資料科學(官方 playbook) | `cudf.pandas` 零改碼加速 pandas;~100GB 資料集整份進記憶體 | 另有投資組合最佳化、單細胞 RNA-Seq playbook |
| [Ultralytics YOLO](https://docs.ultralytics.com/guides/nvidia-dgx-spark)(~50k ⭐) | 官方出 Spark 專頁 + ARM64 映像,訓練/微調/TensorRT 匯出 | 電腦視覺入口 |
| [browser-use](https://github.com/browser-use/browser-use)(~111k ⭐)/ [Skyvern](https://github.com/Skyvern-AI/skyvern) | 本地 VLM 驅動瀏覽器自動化(私有憑證不出網) | 簡單流程 OK,複雜 SPA 仍吃力 |
| [Khoj](https://github.com/khoj-ai/khoj) / [Onyx](https://github.com/onyx-dot-app/onyx) | 個人第二大腦 / 企業級私有搜尋(40+ 連接器) | ARM64 皆已驗證 |
| [Qwen-Image](https://github.com/QwenLM/Qwen-Image)(20B) | 文字渲染最強的影像模型,BF16 ~40GB 只有 Spark 級跑得動 | NVIDIA 為 Spark 出 NVFP4 版 |
| 官方 Multi-Agent Chatbot playbook | gpt-oss-120b 當主管路由到 coding/RAG/視覺子 Agent | 這台機器的參考架構 |

## 地雷區(調查中確認要避開的)

- **Flowise**:2026/8/31 EOL(被 Workday 收購後停止維護)→ 改用 Langflow/Dify/n8n
- **Void 編輯器**:2026/6 封存 → 用 VS Code + Continue/Cline
- **AutoGen**:維護模式 → 用 AG2 或 Microsoft Agent Framework
- **Axolotl**:無 GB10 移植跡象 → 微調用 Unsloth / LLaMA-Factory
- **Evo2 基因體模型**:依賴 H100 調校的 TransformerEngine,GB10 未驗證

## 共通避坑守則

1. **一切優先用容器**:NGC PyTorch 容器或 playbook 指定容器是最穩路線;任何連到 CUDA 12 的東西直接失敗(`libcudart.so.12`)。
2. **PyTorch 裝法**:`pip install torch --index-url https://download.pytorch.org/whl/cu130`(aarch64 cu130 wheel,sm_120 kernel 與 sm_121 二進位相容)。flash-attn 無官方 ARM64 wheel——在 Blackwell 上 SDPA 反而更快,直接用它。
3. **升級到 NVIDIA 6.17+ 核心**:llama.cpp 級引擎的載入速度與生成速度差數倍。
4. **統一記憶體沒有乾淨的 OOM**:關 swap、訓練任務用 cgroup 壓在 ~100GB、「明明有記憶體卻 OOM」時清 page cache(`echo 3 > drop_caches`)。
5. **正確的期望值**:頻寬 273GB/s 是天花板——同樣塞得下的模型,5090 比它快;Spark 贏在**塞得下別人塞不下的**(120B 推論、70B LoRA、12B 影像模型訓練、48GB 機器人模型微調)與**高併發吞吐**。

---

## 主要資料來源

- [NVIDIA DGX Spark Playbooks(官方,47+ 份)](https://github.com/NVIDIA/dgx-spark-playbooks) / [build.nvidia.com/spark](https://build.nvidia.com/spark)
- [llama.cpp 官方 Spark benchmark 討論串](https://github.com/ggml-org/llama.cpp/discussions/16578) · [vLLM DGX Spark 官方部落格](https://vllm.ai/blog/2026-06-01-vllm-dgx-spark) · [Ollama Spark 效能文](https://ollama.com/blog/nvidia-spark-performance) · [LM Studio Spark 發表文](https://lmstudio.ai/blog/dgx-spark)
- [NVIDIA × Unsloth 官方微調部落格](https://developer.nvidia.com/blog/train-an-llm-on-an-nvidia-blackwell-desktop-with-unsloth-and-scale-it/) · [NVIDIA 2026/1 軟體更新(NVFP4/ComfyUI)](https://developer.nvidia.com/blog/new-software-and-model-optimizations-supercharge-nvidia-dgx-spark)
- [Arm Learning Path:Spark 離線語音聊天機器人](https://learn.arm.com/learning-paths/laptops-and-desktops/dgx_spark_voicechatbot/) · [Arm Learning Path:Isaac 機器人](https://learn.arm.com/learning-paths/laptops-and-desktops/dgx_spark_isaac_robotics/)
- [Tom's Hardware Spark 評測](https://www.tomshardware.com/pc-components/gpus/nvidia-dgx-spark-review/3) · [Simon Willison Spark 評測](https://simonwillison.net/2025/Oct/14/nvidia-dgx-spark/) · [StorageReview 叢集評測](https://www.storagereview.com/review/nvidia-dgx-spark-cluster-review-distributed-inference-on-dell-gigabyte-and-hp)
- [awesome-dgx-spark](https://github.com/bidual/awesome-dgx-spark) · [natolambert/dgx-spark-setup](https://github.com/natolambert/dgx-spark-setup) · NVIDIA 開發者論壇多篇實測討論串(內文已逐一附連結)

*星數為 2026-08-27 近似值;ARM64 Docker 可用性於同日對 Docker Hub / GHCR manifest 驗證。*

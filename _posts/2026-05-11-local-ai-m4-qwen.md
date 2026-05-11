---
layout: post
title: 本地 AI 的實踐：在 M4 MacBook 上運行 Qwen 3.5-9B 的完整實驗
date:   2026-05-11 15:00:00 +0800
categories: [AI, 本地運算, 硬體]
tags: [M4, Local AI, Qwen, LM Studio]
---

# 本地 AI 的實踐：在 M4 MacBook 上運行 Qwen 3.5-9B 的完整實驗

**資料來源**：jola.dev
**原文連結**：https://jola.dev/posts/running-local-models-on-m4
**文章發布時間**：2026-05-10
**市場訊息發布時間**：2026-05-10
**Hacker News 熱度**：251 點，79 條留言

## 引言：為何要本地運行 AI？

軟體工程師 Johanna Larsson 在標題為「Running local models on an M4 with 24GB memory」的文章中，詳細記錄了她在 Apple M4 MacBook Pro 上嘗試運行本地大型語言模型的實驗過程。這篇文章在 Hacker News 上引起廣泛討論，點亮了開發者社群對於本地 AI 可行性的深刻省思。

作者開篇就點明了本地運行 AI 的多重優勢：不需要網路連接、可以在飛機上使用、成本只考量電費而非訂閱費用、可以減少對大型科技公司的依賴、並且有減少數據中心使用的環境效益。她開玩笑地說：「雖然訓練這些模型會造成嚴重的環境成本，但開源模型公司在環境影響排名裡還沒有到頂，使用自己的硬體意味著更少的數據中心。」

更賞心悅目的是，這項實驗充滿了探索的樂趣，即使模型犯錯也很有趣。這種解開讓人學習的工具使用方式，遠比單純依賴 SOTA（State-of-the-Art）雲端模型更為健康和有意義。

## 本地 AI 的設置挑戰

作者指出，讓本地模​​運作起來並不容易。首先要選擇運行模型的方式：Ollama、llama.cpp 或 LM Studio。每個都有各自的怪癖和限制，不會提供完全相同的模型選項。其次還要選擇模型，要找適合記憶體容量、仍留有足夠空間運行常規 Electron 應用程式的模型、至少要有 64K 的上下文窗口、最好 128K 或更多的模型。

最近，作者嘗試了 Qwen 3.6 Q3、GPT-OSS 20B、Devstral Small 24B，它在技術上都能放入記憶體但實際上無法使用；以及 Gemma 4B，它可以正常運行但難以進行工具使用。

除了工具和模型選擇，還有許多配置選項需要調整，從眾所周知的溫度，到更神祕的「K Cache Quantization Type」。雖然許多工具提供了基本的建議設置，但適當的設置取決於是否啟用 thinking 模式等因素。

## Qwen 3.5-9B (Q4 量化) 的勝出

經過多方對比，作者終於找到可行的設置：`qwen3.5-9b@q4_k_s`（來自 HuggingFace 的 GGUF 版本），這是目前為止作者最成功的工作方案，在 LM Studio 上以合理的約 40 tokens/秒運行，啟用 thinking、工具使用成功，擁有 128K 上下文窗口。

相較於 SOTA 模型，Qwen 3.5 9B (Q4) 更容易分心、有時會卡在循環中、會誤解需求。但對於一款能在 24GB Macbook Pro 上運行、同時為其他大量應用程式騰出空間的模型來說，其表現已經令人驚訝地好。

### 推薦設置

作者提出了適用於 thinking 模式和編碼任務的推薦基本設置：

```
Thinking mode for precise coding tasks (e.g., WebDev):
temperature=0.6, top_p=0.95, top_k=20,
min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0
```

為了啟用 thinking，作者還必須選擇模型、進入配置、滾動到 Inference 選項卡的底部，並將 `&lt;%- set enable_thinking = true %&gt;` 添加到 Prompt Template 中。

## 整合到開發工具流程

作者試著通過 Pi 和 OpenCode 兩個工具使用 Qwen 模型，目前尚未決定哪一個比較偏好。Pi 感覺更靈快一些，雖然作者很欣賞 idea of the harness building itself 以及所有客製化的構想，但她不免希望 Pi 能有一些合理的預設值。她覺得最終可能會花更多時間調整 Pi 的設定要完美，而不是花在自己的專案上。

### Pi 設置

以下是作者的 `~/.pi/agent/models.json`：

```json
{
  "providers": {
    "lmstudio": {
      "baseUrl": "http://localhost:1234/v1",
      "api": "openai-completions",
      "apiKey": "lm-studio",
      "models": [
        {
          "id": "qwen3.5-9b@q4_k_s",
          "reasoning": true,
          "compat": { "thinkingFormat": "qwen-chat-template" }
        }
      ]
    }
  }
}
```

為了隱藏令人分心的思考過程，作者還在 `~/.pi/agent/settings.json` 中添加 `"hideThinkingBlock": true`。

### OpenCode 設置

以下是 `~/.config/opencode/opencode.json`：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "lmstudio": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "LM Studio (local)",
      "options": {
        "baseURL": "http://127.0.0.1:1234/v1"
      },
      "models": {
        "qwen3.5-9b@q4_k_s": {
          "name": "Qwen 3.5 9B Q4_K_S",
          "tools": true,
          "context_length": 131072,
          "max_tokens": 32768
        }
      }
    }
  },
  "model": "lmstudio/qwen3.5-9b@q4_k_s"
}
```

## 本地 AI vs SOTA 模型的對比

作者強調，Qwen 3.5 9B (Q4) 根本沒有像 SOTA 模型那樣在較長時間內獨立解決複雜問題的能力。要求它一次性建構整個應用根本沒有意義，只會讓大腿發燙而得不到任何東西。

真正有效的是更互動的工作流程，你逐步清楚地向模型溝通，並給它 많指導。對許多人來說，這聽起來毫無意義：為什麼要使用一個必須當保姆才能工作的模型？但作者發現，這反而鼓勵她更投入其中。

使用 SOTA 模型的缺點是讓你太容易地將所有認知努力都卸載出去，即使你在努力防止這種情況發生。使用本地模型使作者必須承擔更多的思考和規劃任務，必須更加具體指導，但它仍充當研究助理、橡膠鴨題解法，以及能即時回憶大量程式語言細節和命​​令行呼叫的專家。

它不會像大型 AI 公司宣稱的 10 倍生產力提升，但確實有些效果，而且很有趣。

## 實際應用案例

為了給讀者更具體的印象，作者分享了兩個簡單的實際案例。

### 案例 1：Credo 警告修復

作者想要將 Elixir linter `credo` 更新到最新版本，並收到了一些代碼警告。作為實驗，她問 Qwen 看看。

Qwen 建議：在 Elixir 語言中，目前已使用 `length/1` 檢查列表是否非空的編碼風格不夠地道的。Credo 建議使用與空列表比較的方式。作者要求 Qwen 進行了 4 次並行編輯，並非常高效。整體來說這是一個作者自己就可以透過反覆切換終端機和編輯器來取得行號進行修改的簡單任務。差異不大，但很方便、很愉快。

### 案例 2：Git 衝突解決

在一些依賴庁升級後，作者有一個 dependabot PR 存在 Git 衝突，而 dependabot 不知何故拒絕進行 rebase。作者將它下來、rebase，並要求 Qwen 看看。這是一個非常簡單的衝突，只需採取每個較新版本即可，模型識別了這一點。

然而，當要求進行更改時，Qwen 忘記進行編輯，反而嘗試添加更改並繼續 rebase，但衝突標記仍然存在。此外，它沒有認識到 `git rebase --continue` 會打開編輯器，導致 OpenCode 掛起來，雖然這可能只是一次性問題。

## 企業級應用場景

作者的實驗揭示了本地 AI 在企業環境中的幾個關鍵應用場景：

### 1. 隱私保護

對於處理敏感數據的企業，本地 AI 提供了零數據外流的解決方案。金融服務、醫療保健、政府部門等行業可以專注於法規要求，而不會將客戶數據發送到第三方雲端服務。

### 2. 離線工作能力

飛機、偏遠地區、內網限制的環境，本地 AI 能夠確保開發者不會因為網路連接中斷而停滯。

### 3. 成本效益

24GB 記憶體的 MacBook Pro 價格約為 2000-3000 美元（視配置而定），而 SOTA 雲端 API 調用成本按量計費。對於高頻率、長時間的使用場景，一次性硬體投資可能更加划算。

### 4. 減少供應商鎖定

作者提到本地 AI 有助於減少對大型科技公司的依賴。對於希望保持技術自主權的企業來說，這是一個重要考量。

## 技術實現細節

### 硬體需求

M4 MacBook Pro 的 24GB 統一記憶體提供了足夠的空間在運行 Q4 量化的 9 萬億參數模型的同時，還有足夠空間給作業系統和其他應用程式。對比 16GB 記憶體的版本，難以在運行模型時同時進行多任務處理。

作者提到的 M4 記憶體配置是 Apple 在 2026 年推出的新規格，超過了先前 M3 系列的 18GB 最大值。這使更多開發者能在本地運行更大的模型而不犧牲日常開發工作。

### 模型量化

Qwen 3.5-9B 使用 Q4_K_S 量化，這意味著模型參數以 4-bit 整數存儲，而非 16-bit 浮點數。這使模型大小從大約 18GB（FP16）減少到約 5GB（Q4_K_S），僅絲毫損失準確性，同時使推理速度達到約 40 tokens/秒。

上下文窗口為 131,072 tokens（128K），足以處理大部分程式碼專案和長篇文檔，接近平日 GPT-4 的 128K 上限。

### 工具使用

LM Studio 支持 OpenAI 兼容 API 格式，使它能夠輕鬆整合到 Pi 和 OpenCode 等 AI IDE 延伸工具中。`tools: true` 選項啟用了模型進行函數調用的能力，使其能夠執行 Git 操作、檔案編輯、終端指令等。

### Thinking 模式

Thinking 模式，即 reasoning 模式，使模型能在生成最終答案之前先內部思考過程。啟用後，模型會先輸出一個 thinking 區塊，然後再提供答案。這對複雜問題解決、程式碼生成和除錯特別有用。通過 Qwen 提供的專屬 thinking 模板格式（`qwen-chat-template`），模型能夠有效利用這種能力。

## 市場趨勢與產業影響

### 1. 硬體升級循環

Apple M4 推出 24GB 記憶體版本的策略與提升本地 AI 能力的需求同步。預期未來硬體市場將出現企業級筆記型電腦對更多記憶體的競爭，因為開發者需要本地執行大規模模型。

### 2. 開源模型成熟度

Qwen（通義千問）是阿里巴巴開發的開源語言模型系列，其 3.5 版本在本地執行場景中表現優異，顯示開源模型在實際應用環境已達到高實用性。這持續填補了 SOTA 雲端模型與硬體限制之間的差距。

### 3. AI IDE 工具演化

Pi 和 OpenCode 等工具代表 AI 整合到 IDE 的持續演進。本地模型的可及性意味著這些工具不必完全依賴雲端 API，能夠提供更隱私、更低延遲的體驗。

### 4. 開發者工作模式轉變

作者的觀察顯示，使用本地 AI 模型改變了開發者的思考方式。不同於完全卸載思考給 SOTA 模型，本地模型要求開發者保持主動，將 AI 視為合作夥伴而非替代者。這種工作模式可能會在開發者社群中持續傳播。

## 未來展望

作者認為本地 AI 的實現路徑雖然有嚴重權衡，但伴隨著相當引人注目的優勢。 LLM 提供了無限的可能性，即使本地模型也能做很多事情。想像力是唯一的限制。本地模型有嚴重的折衷，但它們也有一些相當吸引人的優勢：

- 不需要網路連接，你可以在飛機上工作！
- 成本限制在你所使用的電力，假設你無論如何都打算購買一台電腦。不需要訂閱。
- 訓練這些模型仍然會有嚴重的環境成本，但開源模型公司遠未在環境影響排名中名列前茅，使用自己的硬體意味著更少的數據中心。
- 它很有趣。

隨著硬體的持續升級、開源模型的持續改進、以及工具生態系統的持續成長，本地 AI 很有可能在未來幾年內從利基愛好者轉變為主流開發者的標配。

---

**原始文章**：https://jola.dev/posts/running-local-models-on-m4
**Hacker News 討論**：https://news.ycombinator.com/item?id=48089091
**Qwen 3.5-9B GGUF**：https://huggingface.co/unsloth/Qwen3.5-9B-GGUF
**LM Studio**：https://lmstudio.ai/
**Pi**：https://pi.dev/
**OpenCode**：https://opencode.ai/

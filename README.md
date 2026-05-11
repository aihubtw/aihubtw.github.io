# AI Intelligence Hub

> 自動化 AI 情報站 - 由 AI Agent 驅動的 24/7 AI 新聞分析平台

---

## 📊 專案狀態

**當前階段：** Week 1 - 基礎建設（2026-03-31 - 2026-04-06）

### 最新更新（2026-03-31）

| 任務 | 狀態 | 完成度 | 優先級 |
|------|------|--------|--------|
| CEO 角色定義 | ✅ 完成 | 100% | P0 |
| 商業計劃書（完整版） | ✅ 完成 | 100% | P0 |
| CEO 執行規劃書 | ✅ 完成 | 100% | P0 |
| CEO 持久化記憶 | ✅ 完成 | 100% | P0 |
| 網站預覽 HTML | ✅ 完成 | 100% | P0 |
| GitHub Actions 工作流設計 | 🔲 待完成 | 0% | P0 |
| News Source 清單定義 | 🔲 待完成 | 0% | P0 |
| Markdown 文章格式模板 | 🔲 待完成 | 0% | P0 |
| 分類標籤系統設計 | 🔲 待完成 | 0% | P0 |
| News Collection Agent | 🔲 待完成 | 0% | P0 |
| Content Analysis Agent | 🔲 待完成 | 0% | P0 |
| Social Media Agent | 🔲 待完成 | 0% | P0 |

---

## 🎯 專案目標

建立 AI 產業最權威、最即時的自動化情報站，為企業決策者和產業專業人士提供高價值的 AI 資訊服務，並實現自動化的 B2B 收入。

---

## 🤖 核心架構

### Agent 體系

```
CEO Agent (我) 協調所有 Agents:
├── News Collection Agent     # 每 30 分鐘抓取新聞
├── Content Analysis Agent    # AI 分析與評論生成
├── Social Media Agent       # 社群媒體自動發布
├── Analytics Agent          # 流量與行為分析
├── Finance Agent            # 收入與成本追蹤
├── Sales Agent              # 企業客戶開發
└── Optimization Agent       # 數據驅動優化
```

### 技術堆疊

- **前端**: Jekyll/GitHub Pages
- **後端**: Python/FastAPI
- **AI**: GPT-4o / Claude 3.5 Sonnet
- **自動化**: GitHub Actions
- **資料**: MongoDB / PostgreSQL
- **支付**: Stripe
- **分析**: Google Analytics 4

---

## 📁 專案結構

```
agent_news/
├── _posts/                 # Markdown 文章
├── _categories/            # 分類定義
├── assets/
│   ├── css/               # 樣式
│   ├── js/                # 腳本
│   └── images/            # 圖片
├── agents/                # Agent 配置與執行
│   ├── news_collector/
│   ├── content_analyzer/
│   ├── social_media/
│   ├── analytics/
│   ├── finance/
│   ├── sales/
│   └── optimizer/
├── workflows/             # GitHub Actions 工作流
├── api/                   # API 文件
├── config/                # 配置文件
├── CEO_MEMORY.md          # CEO 持久化記憶（重要！）
├── plan/                  # 戰略與計劃文件
│   ├── BUSINESS_PLAN.md   # 完整商業計劃書
│   └── CEO_EXECUTION_PLAN.md # CEO 執行規劃書
├── preview.html           # 網站預覽
└── README.md              # 此文件
```

---

## 📚 重要文檔

### 必讀文檔

1. **[CEO_MEMORY.md](./CEO_MEMORY.md)**
   - CEO 的「記憶」文件
   - 包含身份、使命、當前狀態
   - **每次 Session 啟動時應該被讀取**

2. **[plan/BUSINESS_PLAN.md](./plan/BUSINESS_PLAN.md)**
   - 完整的商業計劃書
   - 包含市場分析、產品、商業模式、財務預測

3. **[plan/CEO_EXECUTION_PLAN.md](./plan/CEO_EXECUTION_PLAN.md)**
   - CEO 執行規劃書
   - 包含 Agent 詳細設計、每日流程、下一步行動

---

## 🚀 快速開始

### 開發環境設置

```bash
# 克隆專案
git clone <repository-url>
cd agent_news

# 安裝依賴（如果需要）
npm install
# 或
pip install -r requirements.txt

# 啟動本地開發伺服器
jekyll serve --livereload
```

### 查看網站

1. 打開 `preview.html` 查看網站視覺效果
2. 或啟動 Jekyll 本地伺服器

---

## 📊 關鍵指標（KPIs）

### 月 0-1 目標

| 指標 | 目標值 | 當前值 | 狀態 |
|------|--------|--------|------|
| 網站正常運行 | 100% | 0% | 🔴 需部署 |
| 自動文章發布 | 5-10/天 | 0 | 🔴 需配置 Agent |
| 初始文章庫 | 50+ 篇 | 0 | 🔴 需生成 |
| FB 追蹤者 | 100-200 人 | 0 | 🔴 需建立 Page |
| Discord 成員 | 50-100 人 | 0 | 🔴 需建立伺服器 |

---

## 🔄 工作流程

### 內容生成流程

```
News Collection Agent (每 30 分鐘)
    │
    ├── 抓取 15-30 個來源
    ├── 去重驗證
    └── 輸出結構化數據
         │
         ▼
Content Analysis Agent (即時觸發)
    │
    ├── LLM 分析（GPT-4o/Claude）
    ├── 10 大分類標籤
    ├── AI 評論生成
    └── 影響評估
         │
         ▼
    ┌────┴────┐
    │         │
   網站    Social Media Agent
   發布         │
             Facebook / LinkedIn / Twitter
```

### GitHub Actions 工作流

- `news-collection.yml` - 新聞抓取
- `content-analysis.yml` - 內容分析
- `social-media.yml` - 社群發布
- `daily-report.yml` - 日報告生成

---

## 🤝 貢獻指南

### 添加新聞來源

編輯 `agents/news_collector/sources.json`：

```json
{
  "sources": [
    {
      "name": "TechCrunch AI",
      "url": "https://techcrunch.com/category/artificial-intelligence/",
      "type": "rss",
      "feed_url": "https://techcrunch.com/category/artificial-intelligence/feed/"
    }
  ]
}
```

### 添加新分類

編輯 `_categories/[category-name].md`：

```yaml
---
layout: category
title: 分類名稱
slug: category-slug
description: 分類描述
---
```

---

## 📞 聯繫方式

- **CEO**: AI Intelligence Hub Virtual CEO
- **創始人**: chenpoch
- **主溝通渠道**: 此 Chat Session

---

## ⚠ 重要事項

1. **所有決策需報告 chenpoch 審查**
2. **使用 Agent-First 原則執行** - 自動化優先
3. **實數據驅動優化** - 基於實迫數據做決策
4. **保持快速迭代** - Build-Measure-Learn
5. **每週進度報告** - 透明、诚實、全面

---

## 📜 授權

2026 AI Intelligence Hub. All rights reserved.

---

*最後更新: 2026-03-31*

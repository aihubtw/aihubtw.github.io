# AI News Hub - 部署指南

## 📋 專案概述

AI News Hub 是一個自動化的 AI 新聞聚合平台，透過 GitHub Actions 定時執行 Python 腳本來爬取最新 AI 新聞，並將其轉換為 Markdown 文章發布到 GitHub Pages。

## 🚀 快速開始

### 1. 創建 GitHub Repository

```bash
# 1. 在 GitHub 上創建新 repository
# Repository 名稱建議：agent_news
# 設為 Public（公開）才能使用 GitHub Pages

# 2. 複製專案到local
cd your-workspace
git clone https://github.com/your-username/agent_news.git
cd agent_news

# 3. 將創建的檔案複製到專案目錄
```

### 2. 本地開發設置

#### 安裝 Ruby 和 Jekyll

**Windows:**
```bash
# 使用 RubyInstaller 下載並安裝 Ruby
# https://rubyinstaller.org/

# 安裝 Jekyll 和依賴
gem install jekyll bundler
cd agent_news
bundler install

# 本地運行
bundle exec jekyll serve
```

**macOS:**
```bash
# 安裝 Homebrew（如果還沒有）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安裝 Ruby
brew install ruby

# 安裝 Jekyll
gem install jekyll bundler
cd agent_news
bundler install

# 本地運行
bundle exec jekyll serve
```

**Linux (Ubuntu/Debian):**
```bash
# 安裝系統依賴
sudo apt-get update
sudo apt-get install ruby-full build-essential zlib1g-dev

# 安裝 Jekyll
gem install jekyll bundler
cd agent_news
bundler install

# 本地運行
bundle exec jekyll serve
```

### 3. 配置 GitHub Pages

1. 進入 GitHub 上的 repository
2. 點擊 **Settings** > **Pages**
3. 在 **Build and deployment** 中：
   - Source: 選擇 **GitHub Actions**
4. 保存設置

### 4. 設置 GitHub Secrets

在 GitHub repository 中設置以下 secrets：

**路徑:** Settings > Secrets and variables > Actions > New repository secret

| 名稱 | 說明 |
|------|------|
| `GITHUB_TOKEN` | 自動生成，無需手動設置 |
| `OPENAI_API_KEY` | （可選）用於 AI 摘要生成 |
| `NEWS_API_KEY` | （可選）用於 News API |

### 5. 測試 GitHub Actions

1. 提交並推送代碼到 GitHub：
```bash
git add .
git commit -m "Initial commit: Set up AI News Hub"
git push origin main
```

2. 在 GitHub 上進入 **Actions** 頁籤
3. 選擇 **Update AI News** workflow
4. 點擊 **Run workflow** > **Run workflow** 進行手動測試

### 6. 查看網站

等待 GitHub Actions 完成後，網站將在以下 URL 可用：
```
https://your-username.github.io/agent_news/
```

## ⚙️ 自訂配置

### 修改 Jekyll 配置

編輯 `_config.yml` 文件：

```yaml
# 修改網站標題和描述
title: "你的網站標題"
description: "你的網站描述"

# 修改作者信息
author:
  name: "你的名字"
  email: "your-email@example.com"

# 修改社媒連結
social:
  github: "https://github.com/your-username"
  twitter: "https://twitter.com/your-twitter"
```

### 自訂配色方案

在 `assets/css/main.css` 中修改 CSS 變量：

```css
:root {
    --primary-color: #2563EB;      /* 主色 */
    --secondary-color: #7C3AED;    /* 次要色 */
    --accent-color: #10B981;       /* 強調色 */
    --dark-bg: #0F172A;            /* 背景色 */
    --card-bg: #1E293B;            /* 卡片背景 */
}
```

### 修改定時排程

在 `.github/workflows/update-news.yml` 中修改 cron 表達式：

```yaml
schedule:
  # 每天早上 9 點 (台北時間 = UTC+8)
  - cron: '0 1 * * *'  # 1:00 AM UTC = 9:00 AM Taipei time
  
  # 其他常用時間：
  # '0 */6 * * *'    # 每 6 小時
  # '0 0 * * *'      # 每天午夜
  # '0 0 * * 1'      # 每週一午夜
```

## 🐛 故障排除

### 常見問題

**1. GitHub Actions 失敗**
- 檢查 Secrets 是否正確設置
- 查看 Actions 日誌中的錯誤訊息
- 確認 Python 腳本的語法沒有錯誤

**2. 網站未更新**
- 確認 GitHub Actions 成功完成
- 檢查 `_posts` 目錄是否有新文件
- 等待 GitHub Pages 部署完成（通常需要幾分鐘）

**3. 本地 Jekyll 服務器無法啟動**
- 確認 Ruby 版本 >= 2.7
- 運行 `bundle install` 更新依賴
- 檢查端口 4000 是否被占用

**4. 樣式異常**
- 清除瀏覽器快取
- 檢查 CSS 文件路徑是否正確
- 確認 CSS 變量在 `:root` 中定義

## 📚 擴展功能

### 添加新聞來源

在 `scripts/scrape_ai_news.py` 中添加新的來源：

```python
NEWS_SOURCES = [
    # 現有來源...
    {
        "name": "你的新聞來源",
        "url": "https://example.com/ai/",
        "base_url": "https://example.com",
        "category": "Industry"
    }
]
```

### 添加新的爬蟲方法

```python
def scrape_your_source(self):
    """爬取自定義新聞來源"""
    articles = []
    # 實現你的爬蟲邏輯
    return articles
```

### 修改文章格式

在 `generate_markdown_post` 方法中修改 frontmatter 和內容格式。

## 📝 文件結構

```
agent_news/
├── .github/
│   └── workflows/
│       └── update-news.yml      # GitHub Actions 配置
├── _includes/
│   ├── navigation.html          # 導航欄
│   ├── hero.html                # 主視覺
│   └── footer.html              # 頁尾
├── _layouts/
│   ├── default.html             # 預設佈局
│   ├── home.html                # 首頁佈局
│   └── post.html                # 文章頁佈局
├── _posts/                      # 新聞文章（自動生成）
├── assets/
│   ├── css/
│   │   ├── main.css             # 主要樣式
│   │   └── responsive.css       # 響應式樣式
│   └── js/
│       └── main.js              # 主要 JavaScript
├── scripts/
│   └── scrape_ai_news.py        # Python 爬蟲腳本
├── _config.yml                  # Jekyll 配置
├── Gemfile                      # Ruby 依賴
├── index.md                     # 首頁
├── about.md                     # 關於頁面
└── README.md                    # 專案說明
```

## 🎨 設計原則

本網站設計遵循以下原則：

1. **深色科技風格**：使用深藍與紫色漸層營造科技感
2. **響應式設計**：支援各種裝置尺寸
3. **可訪問性**：遵循 WCAG 2.1 規範
4. **性能優化**：最小化資源載入
5. **SEO 友善**：適當的 meta 標籤和結構化數據

## 📄 授權

本專案採用 MIT 授權，歡迎自由使用與修改。

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request 來改進這個專案！

---

*Made with ❤️ by AI Agent*

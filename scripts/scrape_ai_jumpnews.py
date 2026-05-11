#!/usr/bin/env python3
"""
AI Intelligence Hub - News Scraper & Analyst
自動化收集 AI 領域相關新聞，並生成專業分析和評論
"""

import os
import sys
import json
import re
from datetime import datetime, timezone
from pathlib import Path
import argparse

# 嘗試導入依賴項
try:
    import requests
    from bs4 import BeautifulSoup
    from openai import OpenAI
    import yaml
except ImportError as e:
    print(f"缺少必要依賴: {e}")
    print("請執行: pip install requests beautifulsoup4 openai pyyaml")
    sys.exit(1)

# 配置
POSTS_DIR = Path("_posts")
OUTPUT_DIR = Path(POSTS_DIR)

# 分類映射
CATEGORY_MAPPING = {
    "llm": "大語言模型",
    "gpt": "大語言模型",
    "claude": "大語言模型",
    "llama": "大語言模型",
    "語言模型": "大語言模型",
    "生成式": "生成式AI",
    "生成": "生成式AI",
    "圖像": "生成式AI",
    "影像": "生成式AI",
    "音訊": "生成式AI",
    "深度學習": "深度學習",
    "神經網絡": "深度學習",
    "transformer": "深度學習",
    "產業": "產業動態",
    "融資": "產業動態",
    "薪資": "產業動態",
    "就業": "產業動態",
    "應用": "AI應用",
    "專案": "AI應用",
    "工具": "AI應用",
    "醫療": "AI應用",
    "教育": "教育與學習",
    "學習": "教育與學習",
    "監管": "責任與治理",
    "法規": "責任與治理",
    "安全": "責任與治理",
    "倫理": "責任與治理",
    "治理": "責任與治理",
    "gpu": "硬體與基礎設施",
    "晶片": "硬體與基礎設施",
    "硬體": "硬體與基礎設施",
    "hw": "硬體與基礎設施",
    "觀點": "觀點與分析",
    "分析": "觀點與分析",
    "洞察": "觀點與分析",
    "看法": "觀點與分析",
    "競賽": "活動與社群",
    "開源": "活動與社群",
    "社群": "活動與社群",
    "研討會": "活動與社群",
}

# AI 新聞來源配置
NEWS_SOURCES = {
    "techcrunch": {
        "name": "TechCrunch AI",
        "url": "https://techcrunch.com/category/artificial-intelligence/",
        "article_selector": "div.post-block",
        "title_selector": "a.post-block__title__link",
        "link_selector": "a.post-block__title__link",
        "excerpt_selector": "div.post-block__content",
    },
    "venturebeat": {
        "name": "VentureBeat AI",
        "url": "https://venturebeat.com/category/ai/",
        "article_selector": "div.article-feed-top-stories-wrapper div",
        "title_selector": "h3.title",
        "link_selector": "h3.title a",
        "excerpt_selector": "p.excerpt",
    },
}

class AIIntelligenceScraper:
    def __init__(self, openai_api_key=None):
        """初始化爬蟲和 AI 分析器"""
        self.openai_client = None
        if openai_api_key:
            self.openai_client = OpenAI(api_key=openai_api_key)
        
        # 確保輸出目錄存在
        OUTPUT_DIR.mkdir(exist_ok=True)

    def fetch_articles(self, source_key, limit=5):
        """從指定來源獲取文章列表"""
        if source_key not in NEWS_SOURCES:
            print(f"未知的新聞來源: {source_key}")
            return []
        
        source = NEWS_SOURCES[source_key]
        articles = []
        
        try:
            print(f"正在從 {source['name']} 獲取文章...")
            response = requests.get(source["url"], timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            
            article_elements = soup.select(source["article_selector"])[:limit]
            
            for element in article_elements:
                try:
                    title_elem = element.select_one(source["title_selector"])
                    link_elem = element.select_one(source["link_selector"])
                    excerpt_elem = element.select_one(source["excerpt_selector"])
                    
                    if title_elem and link_elem:
                        title = title_elem.get_text(strip=True)
                        link = link_elem.get("href")
                        excerpt = excerpt_elem.get_text(strip=True) if excerpt_elem else ""
                        
                        articles.append({
                            "title": title,
                            "link": link if link.startswith("http") else f"https://{source_key}.com{link}",
                            "excerpt": excerpt,
                            "source": source["name"],
                        })
                except Exception as e:
                    print(f"解析文章元素時出錯: {e}")
                    continue
            
            print(f"成功獲取 {len(articles)} 篇文章")
            return articles
            
        except Exception as e:
            print(f"獲取 {source['name']} 文章時出錯: {e}")
            return []

    def categorize_article(self, title, excerpt):
        """根據標題和摘要為文章分類"""
        content = f"{title} {excerpt}".lower()
        
        best_category = "產業動態"  # 預設分類
        best_score = 0
        
        for keyword, category in CATEGORY_MAPPING.items():
            if keyword in content:
                best_category = category
                best_score = max(best_score, 1)
        
        return best_category

    def generate_ai_insights(self, article, category):
        """使用 OpenAI API 生成 AI 觀點和分析"""
        if not self.openai_client:
            print("未提供 OpenAI API Key，跳過 AI 分析生成")
            return None
        
        try:
            print(f"正在為文章生成 AI 分析: {article['title'][:50]}...")
            
            prompt = f"""
作為 AI Intelligence Hub 的高級分析師，請為以下 AI 新聞文章生成專業的觀點和分析。

文章標題: {article['title']}
文章摘要: {article['excerpt']}
文章分類: {category}

請生成以下四個部分的分析：

1. 核心觀點 (ai_insight):
- 提供獨特的技術視角
- 分析事件在 AI 行業的意義
- 關注商業或戰略層面的影響

2. 深度分析 (ai_analysis):
- 技術實現或架構突破
- 產業影響評估
- 數據或基準測試分析

3. 未來展望 (ai_implication):
- 技術趨勢預測
- 市場競爭格局變化
- 相關領域發展方向

4. 建議與提醒 (ai_recommendation):
- 對開發者的建議
- 對企業的建議
- 對用戶或投資者的建議

請以 JSON 格式返回，包含以上四個字段，每個字段都是完整的 markdown 文本。
"""

            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "你是 AI Intelligence Hub 的高級分析師，專業、客觀、前瞻。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            # 嘗試解析 JSON 響應
            content = response.choices[0].message.content
            
            # 提取 JSON 部分
            json_match = re.search(r'\{[\s\S]*\}', content)
            if json_match:
                insights = json.loads(json_match.group())
                return insights
            else:
                # 如果無法解析，返回 None
                print("AI 生成內容無法解析為 JSON")
                return None
                
        except Exception as e:
            print(f"生成 AI 分析時出錯: {e}")
            return None

    def create_article_file(self, article, category, insights=None):
        """創建 Markdown 文章文件"""
        # 生成文件名 (使用當前日期)
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        slug = re.sub(r'[^\w-]', '-', article['title'][:50]).lower().strip('-')
        filename = f"{date_str}-{slug}.md"
        
        # 確定文章類型
        if insights:
            post_type = "深度分析"
        else:
            post_type = "熱點新聞"
        
        # 產生標籤
        content_lower = f"{article['title']} {article['excerpt']}".lower()
        tags = []
        for keyword, cat in CATEGORY_MAPPING.items():
            if keyword in content_lower and cat == category:
                tags.append(keyword)
        
        if len(tags) > 5:
            tags = tags[:5]
        elif len(tags) == 0:
            tags = ["AI", "新聞"]
        
        # 準備 frontmatter
        frontmatter_lines = [
            "---",
            f"layout: post",
            f'title: "{article["title"]}"',
            f"date: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %z')}",
            f"category: {category}",
            f"type: {post_type}",
            f"tags: {json.dumps(tags, ensure_ascii=False)}",
            f"""excerpt: {article['excerpt'][:150]}...""",
        ]
        
        # 添加 AI 分析
        if insights:
            for key in ["ai_insight", "ai_analysis", "ai_implication", "ai_recommendation"]:
                if key in insights and insights[key]:
                    frontmatter_lines.append(f'\n{key}: |')
                    for line in insights[key].split('\n'):
                        frontmatter_lines.append(f"  {line}")
        
        frontmatter_lines.append("---")
        
        # 準備文章主體
        body_lines = [
            "",
            f"## {article['title']}",
            "",
            f"### 文章來源",
            f"- **標題**: {article['title']}",
            f"- **來源**: {article['source']}",
            f"- **連結**: {article['link']}",
            "",
            f"### 摘要",
            article['excerpt'],
            "",
            "---",
            "",
            f"*本文由 AI Intelligence Hub 自動生成與分析*",
        ]
        
        # 寫入文件
        filepath = OUTPUT_DIR / filename
        
        # 檢查文件是否已存在
        if filepath.exists():
            print(f"文章已存在，跳過: {filename}")
            return None
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(frontmatter_lines + body_lines))
        
        print(f"成功創建文章: {filename}")
        return str(filename)

    def run(self, sources=None, limit=5, use_ai=False):
        """運行主程序"""
        if sources is None:
            sources = list(NEWS_SOURCES.keys())
        
        created_articles = []
        
        for source in sources:
            articles = self.fetch_articles(source, limit)
            
            for article in articles:
                category = self.categorize_article(article['title'], article['excerpt'])
                
                insights = None
                if use_ai:
                    insights = self.generate_ai_insights(article, category)
                
                result_path = self.create_article_file(article, category, insights)
                if result_path:
                    created_articles.append(result_path)
        
        return {
            "total": len(created_articles),
            "articles": created_articles,
        }


def main():
    parser = argparse.ArgumentParser(description="AI Intelligence Hub - 新聞爬蟲與分析")
    parser.add_argument("--source", "-s", action="append", 
                        help="指定新聞來源 (可多選)，選項: techcrunch, venturebeat")
    parser.add_argument("--limit", "-l", type=int, default=3,
                        help="每個來源最多獲取的文章數 (默認: 3)")
    parser.add_argument("--use-ai", "-a", action="store_true",
                        help="使用 OpenAI API 生成 AI 分析")
    parser.add_argument("--api-key", "-k",
                        help="OpenAI API Key (或通過 OPENAI_API_KEY 環境變量)")
    
    args = parser.parse_args()
    
    # 獲取 API key
    api_key = args.api_key or os.environ.get("OPENAI_API_KEY")
    
    if args.use_ai and not api_key:
        print("警告: 啟用了 AI 分析但未提供 API Key，將跳過 AI 分析生成")
    
    # 初始化爬蟲
    scraper = AIIntelligenceScraper(openai_api_key=api_key)
    
    # 運行
    results = scraper.run(sources=args.source, limit=args.limit, use_ai=args.use_ai)
    
    print(f"\n完成！共創建 {results['total']} 篇文章")
    for article in results['articles']:
        print(f"  - {article}")


if __name__ == "__main__":
    main()

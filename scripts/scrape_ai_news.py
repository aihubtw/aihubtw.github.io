#!/usr/bin/env python3
"""
AI News Scraper
自動化收集 AI 領域相關新聞並生成 Markdown 文章
"""

import os
import sys
import json
import re
from datetime import datetime, timedelta
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from dateutil import parser

# 配置
POSTS_DIR = Path("_posts")
CATEGORIES = [
    "AI News",
    "Deep Learning",
    "Machine Learning",
    "LLM",
    "Computer Vision",
    "NLP",
    "Robotics",
    "Industry"
]

# 新聞來源
NEWS_SOURCES = [
    {
        "name": "TechCrunch AI",
        "url": "https://techcrunch.com/category/artificial-intelligence/",
        "base_url": "https://techcrunch.com",
        "category": "Industry"
    },
    {
        "name": "VentureBeat AI",
        "url": "https://venturebeat.com/ai/",
        "base_url": "https://venturebeat.com",
        "category": "Industry"
    },
    {
        "name": "The Verge AI",
        "url": "https://www.theverge.com/ai-artificial-intelligence",
        "base_url": "https://www.theverge.com",
        "category": "AI News"
    }
]

# 搜索查詢（用於 Google News 或其他聚合站點）
SEARCH_QUERIES = [
    "OpenAI GPT",
    "Google DeepMind",
    "NVIDIA AI",
    "Claude AI",
    "machine learning news",
    "AI breakthrough"
]


class NewsScraper:
    """新聞爬蟲類別"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def fetch_url(self, url):
        """獲取 URL 內容"""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def scrape_techcrunch(self):
        """爬取 TechCrunch AI 新聞"""
        articles = []
        source = NEWS_SOURCES[0]
        
        response = self.fetch_url(source["url"])
        if not response:
            return articles
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 尋找文章列表
        post_blocks = soup.find_all('div', class_='post-block')[:5]  # 限制為最新的 5 篇
        
        for block in post_blocks:
            try:
                title_elem = block.find('h2', class_='post-block__title')
                if not title_elem:
                    title_elem = block.find('a', class_='post-block__title__link')
                
                if not title_elem:
                    continue
                
                title = title_elem.get_text(strip=True)
                link_elem = title_elem.find('a') if title_elem.name != 'a' else title_elem
                link = link_elem.get('href') if link_elem else None
                
                if link and not link.startswith('http'):
                    link = source["base_url"] + link
                
                excerpt_elem = block.find('div', class_='post-block__excerpt')
                excerpt = excerpt_elem.get_text(strip=True) if excerpt_elem else ""
                
                date_elem = block.find('time')
                date_str = date_elem.get('datetime') if date_elem else ""
                
                article = {
                    "title": title,
                    "url": link,
                    "excerpt": excerpt,
                    "date": date_str,
                    "category": source["category"],
                    "source": source["name"],
                    "tags": ["OpenAI", "AI", "Tech"]  # 簡單標籤生成
                }
                articles.append(article)
            except Exception as e:
                print(f"Error parsing article: {e}")
                continue
        
        return articles
    
    def generate_markdown_post(self, article):
        """生成 Markdown 文章格式"""
        # 處理日期
        try:
            if article.get("date"):
                date_obj = parser.parse(article["date"])
            else:
                date_obj = datetime.now()
        except:
            date_obj = datetime.now()
        
        # 生成文件名
        slug = self.slugify(article["title"])
        filename = date_obj.strftime("%Y-%m-%d-%s.md") % (date_obj.strftime("%H-%M-%S"), slug)
        filepath = POSTS_DIR / filename
        
        # 生成 Markdown 內容
        frontmatter = f"""---
layout: post
title: "{article['title']}"
date: {date_obj.strftime("%Y-%m-%d %H:%M:%S +0800")}
category: "{article['category']}"
excerpt: "{article['excerpt'][:100]}..."
tags:
{chr(10).join(f'  - {tag}' for tag in article.get('tags', []))}

---

{article['excerpt']}

[繼續閱讀全文]({article['url']})

---
*資料來源：{article['source']} | AI Agent 自動收集*"""
        
        return filepath, frontmatter
    
    def slugify(self, text):
        """將標題轉換為 URL 友善的格式"""
        text = text.lower()
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '-', text)
        text = text.strip('-')
        return text[:100]  # 限制長度
    
    def save_post(self, filepath, content):
        """保存文章到文件"""
        try:
            # 檢查文章是否已存在
            if filepath.exists():
                print(f"Post already exists: {filepath}")
                return False
            
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Created post: {filepath}")
            return True
        except Exception as e:
            print(f"Error saving post: {e}")
            return False


def main():
    """主函數"""
    print("🤖 AI News Scraper Started")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    scraper = NewsScraper()
    new_posts = 0
    
    # 爬取各個來源
    for source in NEWS_SOURCES:
        print(f"\n📰 Scraping {source['name']}...")
        
        # 根據不同來源使用不同的爬取方法
        if "techcrunch" in source["name"].lower():
            articles = scraper.scrape_techcrunch()
        
        print(f"Found {len(articles)} articles")
        
        # 為每篇文章創建 Markdown 文件
        for article in articles:
            if not article.get("url"):
                continue
            
            try:
                filepath, content = scraper.generate_markdown_post(article)
                if scraper.save_post(filepath, content):
                    new_posts += 1
            except Exception as e:
                print(f"Error processing article: {e}")
                continue
    
    print("-" * 50)
    print(f"✅ Finished! Created {new_posts} new posts")
    print(f"Total posts in directory: {len(list(POSTS_DIR.glob('*.md')))}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

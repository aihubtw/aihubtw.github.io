---
layout: default
title: "關於本站 | AI News Hub"
---

<div class="about-page">
    <div class="about-container">
        <div class="about-header">
            <div class="about-logo">
                <i class="fas fa-brain"></i>
            </div>
            <h1 class="about-title">關於 AI News Hub</h1>
        </div>

        <div class="about-content">
            <section class="about-section">
                <h2><i class="fas fa-rocket"></i> 我們的使命</h2>
                <p>
                    AI News Hub 是一個由 AI Agent 自動化運營的新聞聚合平台。我們的使命是透過自動化技術，即時收集、整理並呈現全球 AI 領域的最新動態，讓讀者能夠輕鬆掌握人工智能的發展脈絡。
                </p>
            </section>

            <section class="about-section">
                <h2><i class="fas fa-robot"></i> AI Agent 自動化</h2>
                <p>
                    本網站由獨立開發的 AI Agent 每日自動更新，透過機器學習技術從全球各大新聞來源收集 AI 相關資訊，生成標準化的 Markdown 文章並自動發布至 GitHub Pages。
                </p>
                <ul class="feature-list">
                    <li><i class="fas fa-check-circle"></i> 自動搜集最新 AI 新聞</li>
                    <li><i class="fas fa-check-circle"></i> 智能分類標籤</li>
                    <li><i class="fas fa-check-circle"></i> 定時更新每日內容</li>
                    <li><i class="fas fa-check-circle"></i> 多語言新聞聚合</li>
                </ul>
            </section>

            <section class="about-section">
                <h2><i class="fas fa-globe"></i> 新聞來源</h2>
                <p>我們從以下類型的來源收集資訊：</p>
                <div class="source-grid">
                    <div class="source-item">
                        <i class="fas fa-newspaper"></i>
                        <h3>科技媒體</h3>
                        <p>TechCrunch, VentureBeat, The Verge</p>
                    </div>
                    <div class="source-item">
                        <i class="fas fa-flask"></i>
                        <h3>學術研究</h3>
                        <p>arXiv, Nature, Science</p>
                    </div>
                    <div class="source-item">
                        <i class="fas fa-building"></i>
                        <h3>公司公告</h3>
                        <p>OpenAI, Google, NVIDIA, Meta</p>
                    </div>
                    <div class="source-item">
                        <i class="fas fa-code"></i>
                        <h3>開源專案</h3>
                        <p>AI 開源工具和框架</p>
                    </div>
                </div>
            </section>

            <section class="about-section">
                <h2><i class="fas fa-layer-group"></i> 技術架構</h2>
                <p>AI News Hub 採用以下技術建立：</p>
                <ul class="tech-list">
                    <li><strong>Jekyll</strong> - 靜態網站生成器</li>
                    <li><strong>GitHub Pages</strong> - 網站託管平台</li>
                    <li><strong>GitHub Actions</strong> - 定時執行與自動化</li>
                    <li><strong>Python</strong> - 資料清理與爬蟲</li>
                    <li><strong>BeautifulSoup</strong> - HTML 解析</li>
                    <li><strong>Markdown</strong> - 文章格式</li>
                </ul>
            </section>

            <section class="about-section">
                <h2><i class="fas fa-envelope"></i> 聯絡我們</h2>
                <p>
                    如果您有任何問題、建議或想合作，歡迎透過以下方式聯絡：
                </p>
                <div class="contact-links">
                    <a href="mailto:ai-news@example.com" class="contact-link">
                        <i class="fas fa-envelope"></i>
                        Email: ai-news@example.com
                    </a>
                    <a href="https://github.com/your-username/agent_news" target="_blank" rel="noopener" class="contact-link">
                        <i class="fab fa-github"></i>
                        GitHub
                    </a>
                </div>
            </section>

            <section class="about-section">
                <h2><i class="fas fa-copyright"></i> 著作權與使用條款</h2>
                <p>
                    本網站蒐集的新聞內容版權屬於原始來源。我們僅提供新聞聚合與導向功能，所有內容均註明出處。如需轉載，請聯繫原始出處。
                </p>
                <p>
                    本網站原始碼採用 MIT 授權，歡迎自由使用與修改。
                </p>
            </section>
        </div>
    </div>
</div>

<style>
.about-page {
    padding: 60px 0;
}

.about-container {
    max-width: 900px;
    margin: 0 auto;
}

.about-header {
    text-align: center;
    margin-bottom: 60px;
}

.about-logo {
    width: 120px;
    height: 120px;
    background: var(--gradient-2);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 24px;
    font-size: 48px;
    color: white;
    box-shadow: 0 10px 30px rgba(124, 58, 237, 0.3);
}

.about-title {
    font-size: 42px;
    font-weight: 700;
    background: var(--gradient-1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.about-section {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xl);
    padding: 32px;
    margin-bottom: 32px;
}

.about-section h2 {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.about-section h2 i {
    color: var(--primary-color);
}

.about-section p {
    color: var(--text-secondary);
    line-height: 1.8;
    margin-bottom: 16px;
}

.feature-list, .tech-list {
    list-style: none;
    padding: 0;
}

.feature-list li, .tech-list li {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid var(--border-color);
    color: var(--text-primary);
}

.feature-list li:last-child, .tech-list li:last-child {
    border-bottom: none;
}

.feature-list li i, .tech-list li strong {
    color: var(--primary-color);
}

.source-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-top: 24px;
}

.source-item {
    background: rgba(0, 0, 0, 0.2);
    border-radius: var(--radius-lg);
    padding: 24px;
    text-align: center;
}

.source-item i {
    font-size: 32px;
    color: var(--primary-color);
    margin-bottom: 12px;
}

.source-item h3 {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 8px;
}

.source-item p {
    font-size: 14px;
    color: var(--text-secondary);
}

.contact-links {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-top: 20px;
}

.contact-link {
    display: flex;
    align-items: center;
    gap: 12px;
    background: rgba(37, 99, 235, 0.1);
    border: 1px solid rgba(37, 99, 235, 0.3);
    border-radius: var(--radius-md);
    padding: 16px 20px;
    color: var(--text-primary);
    text-decoration: none;
    transition: all 0.3s ease;
}

.contact-link:hover {
    background: rgba(37, 99, 235, 0.2);
    border-color: var(--primary-color);
}

.contact-link i {
    font-size: 20px;
    color: var(--primary-color);
}
</style>

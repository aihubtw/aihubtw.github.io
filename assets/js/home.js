// ========================================
// AI Intelligence Hub - Homepage JavaScript
// 首頁專用功能
// ========================================

/**
 * Homepage initialization
 */
function onPageLoad() {
    // Initialize category cards hover effects
    initCategoryHover();
    
    // Initialize article cards animations
    initArticleAnimations();
    
    // Initialize stats counter animation
    if (shouldAnimateStats()) {
        animateStats();
    }
    
    // Initialize subscribe form
    initSubscribeForm();
}

/**
 * Category card hover effects
 */
function initCategoryHover() {
    const categoryCards = document.querySelectorAll('.category-card');
    
    categoryCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            if (this.__observer__) {
                clearTimeout(this.__observer__);
            }
        });
    });
}

/**
 * Article card scroll animations
 */
function initArticleAnimations() {
    const articleCards = document.querySelectorAll('.article-card, .insight-card');
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    articleCards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
}

/**
 * Check if stats should be animated
 */
function shouldAnimateStats() {
    return window.matchMedia('(min-width: 768px)').matches;
}

/**
 * Animate stats counter
 */
function animateStats() {
    const statNumbers = document.querySelectorAll('.stat-number');
    
    statNumbers.forEach(stat => {
        const text = stat.textContent.trim();
        
        // Skip non-numeric stats
        if (!/^\d+$/.test(text)) return;
        
        const target = parseInt(text);
        const duration = 1500;
        const steps = 30;
        const increment = target / steps;
        let current = 0;
        
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                stat.textContent = target;
                clearInterval(timer);
            } else {
                stat.textContent = Math.floor(current);
            }
        }, duration / steps);
    });
}

/**
 * Initialize subscribe form
 */
function initSubscribeForm() {
    const form = document.querySelector('.subscribe-form');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const emailInput = this.querySelector('input[type="email"]');
            const email = emailInput.value.trim();
            
            if (email && isValidEmail(email)) {
                // Show success message
                showToast('訂閱成功！感謝您的支持。');
                emailInput.value = '';
                
                // In production, you would send this to your backend
                console.log('Subscribe email:', email);
            } else {
                showToast('請輸入有效的電子郵件地址', 'error');
            }
        });
    }
}

/**
 * Validate email format
 */
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Show toast notification
 */
function showToast(message, type = 'success') {
    // Check if main.js already has a showToast function
    if (window.AIHub && window.AIHub.showToast) {
        window.AIHub.showToast(message);
        return;
    }
    
    // Fallback implementation
    const toast = document.createElement('div');
    toast.className = 'toast-notification';
    toast.textContent = message;
    
    const bgColor = type === 'error' 
        ? 'linear-gradient(135deg, #f5576c 0%, #f093fb 100%)'
        : 'linear-gradient(135deg, #4fd1c5 0%, #38b2ac 100%)';
    
    toast.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: ${bgColor};
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        z-index: 10000;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            document.body.removeChild(toast);
        }, 300);
    }, 3000);
}

// Add animation styles if not already present
if (!document.querySelector('#toast-animations')) {
    const style = document.createElement('style');
    style.id = 'toast-animations';
    style.textContent = `
        @keyframes slideIn {
            from {
                transform: translateY(100%);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }
        
        @keyframes slideOut {
            from {
                transform: translateY(0);
                opacity: 1;
            }
            to {
                transform: translateY(100%);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', onPageLoad);
} else {
    onPageLoad();
}

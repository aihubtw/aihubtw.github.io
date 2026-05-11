// ========================================
// AI News Hub - Main JavaScript
// 主要 JavaScript 功能
// ========================================

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all features
    initNavigation();
    initSmoothScroll();
    initScrollEffects();
    initDarkMode();
});

/**
 * Navigation toggle for mobile
 */
function initNavigation() {
    const navMenu = document.getElementById('navMenu');
    const navToggle = document.querySelector('.nav-menu-toggle');
    
    // Close menu when clicking on a link
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                navToggle.innerHTML = '<i class="fas fa-bars"></i>';
            }
        });
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.nav-container') && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
            navToggle.innerHTML = '<i class="fas fa-bars"></i>';
        }
    });
}

/**
 * Toggle mobile navigation menu
 */
function toggleMenu() {
    const navMenu = document.getElementById('navMenu');
    const navToggle = document.querySelector('.nav-menu-toggle');
    
    navMenu.classList.toggle('active');
    
    if (navMenu.classList.contains('active')) {
        navToggle.innerHTML = '<i class="fas fa-times"></i>';
    } else {
        navToggle.innerHTML = '<i class="fas fa-bars"></i>';
    }
}

/**
 * Smooth scroll for anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                
                if (target) {
                    const navHeight = document.querySelector('.navigation').offsetHeight;
                    const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navHeight;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
}

/**
 * Scroll effects (navbar, animations)
 */
function initScrollEffects() {
    const navigation = document.querySelector('.navigation');
    let lastScroll = 0;
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        // Add shadow to navbar on scroll
        if (currentScroll > 50) {
            navigation.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        } else {
            navigation.style.boxShadow = 'none';
        }
        
        // Hide/show navbar on scroll down/up
        if (currentScroll > 100 && currentScroll > lastScroll) {
            navigation.style.transform = 'translateY(-100%)';
        } else {
            navigation.style.transform = 'translateY(0)';
        }
        
        lastScroll = currentScroll;
    });
    
    // Animate elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.post-card, .stat-card, .sidebar-widget').forEach(el => {
        observer.observe(el);
    });
}

/**
 * Dark mode toggle
 */
function initDarkMode() {
    // Check system preference
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const storedTheme = localStorage.getItem('theme');
    
    if (storedTheme) {
        document.documentElement.setAttribute('data-theme', storedTheme);
    } else if (prefersDark) {
        document.documentElement.setAttribute('data-theme', 'dark');
    }
    
    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        if (!localStorage.getItem('theme')) {
            document.documentElement.setAttribute('data-theme', e.matches ? 'dark' : 'light');
        }
    });
}

/**
 * Search articles
 */
function searchArticles() {
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');
    const query = searchInput.value.toLowerCase().trim();
    
    if (query.length < 2) {
        searchResults.innerHTML = '';
        return;
    }
    
    // In a real implementation, this would search through posts
    // For now, we'll show a placeholder
    searchResults.innerHTML = '<p class="text-muted">搜尋功能開發中...</p>';
    
    // Example implementation:
    /*
    const posts = document.querySelectorAll('.post-card');
    const results = [];
    
    posts.forEach(post => {
        const title = post.querySelector('.post-card-title').textContent.toLowerCase();
        const excerpt = post.querySelector('.post-card-excerpt').textContent.toLowerCase();
        
        if (title.includes(query) || excerpt.includes(query)) {
            results.push(post.cloneNode(true));
        }
    });
    
    if (results.length > 0) {
        searchResults.innerHTML = '<h4>搜尋結果</h4>';
        results.forEach(result => {
            searchResults.appendChild(result);
        });
    } else {
        searchResults.innerHTML = '<p class="text-muted">沒有找到符合的文章</p>';
    }
    */
}

/**
 * Share functions
 */
function shareToTwitter(url, title) {
    window.open(
        `https://twitter.com/intent/tweet?text=${encodeURIComponent(title)}&url=${encodeURIComponent(url)}`,
        '_blank'
    );
}

function shareToFacebook(url) {
    window.open(
        `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`,
        '_blank'
    );
}

function shareToLinkedIn(url, title) {
    window.open(
        `https://www.linkedin.com/shareArticle?mini=true&url=${encodeURIComponent(url)}&title=${encodeURIComponent(title)}`,
        '_blank'
    );
}

function copyLink(url) {
    navigator.clipboard.writeText(url).then(() => {
        showToast('連結已複製到剪貼簿！');
    }).catch(() => {
        showToast('複製失敗，請手動複製');
    });
}

/**
 * Toast notification
 */
function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'toast-notification';
    toast.textContent = message;
    toast.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: var(--gradient-2);
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

// Add styles for toast animation
const style = document.createElement('style');
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

/**
 * Initialize other page-specific functions if they exist
 */
if (typeof onPageLoad === 'function') {
    onPageLoad();
}

/**
 * Debounce function
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Throttle function
 */
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Export functions for use in other files
window.AIHub = {
    toggleMenu,
    searchArticles,
    shareToTwitter,
    shareToFacebook,
    shareToLinkedIn,
    copyLink,
    showToast,
    debounce,
    throttle
};

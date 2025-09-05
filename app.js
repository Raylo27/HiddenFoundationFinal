// PVAMU Bridge Substructure Monitoring Research - Interactive Features

class BridgeMonitoringApp {
    constructor() {
        this.currentSection = 'overview';
        this.currentCase = 'delaware';
        this.isInitialized = false;
        this.init();
    }

    init() {
        // Ensure DOM is fully loaded before initialization
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.initializeApp());
        } else {
            this.initializeApp();
        }
    }

    initializeApp() {
        console.log('Initializing PVAMU Bridge Monitoring App...');
        
        this.setupInitialState();
        this.setupNavigation();
        this.setupOverviewCards();
        this.setupCaseStudyTabs();
        this.setupDownloadButtons();
        this.setupAccessibility();
        this.setupSmoothScrolling();
        this.setupKeyboardNavigation();
        this.handleInitialHash();
        
        this.isInitialized = true;
        console.log('PVAMU Bridge Monitoring Research Application Initialized Successfully');
        
        // Debug info
        this.logDebugInfo();
    }

    setupInitialState() {
        console.log('Setting up initial state...');
        
        // Ensure all sections exist and are properly configured
        const sections = document.querySelectorAll('.content-section');
        console.log('Found sections:', sections.length);
        
        sections.forEach((section, index) => {
            console.log(`Section ${index}: ${section.id}`);
            section.classList.remove('active');
            section.setAttribute('aria-hidden', 'true');
            section.style.display = 'none';
        });

        // Show overview section by default
        const overviewSection = document.getElementById('overview');
        if (overviewSection) {
            console.log('Showing overview section');
            overviewSection.classList.add('active');
            overviewSection.setAttribute('aria-hidden', 'false');
            overviewSection.style.display = 'block';
        } else {
            console.error('Overview section not found!');
        }

        // Set overview nav button as active
        const overviewButton = document.querySelector('[data-section="overview"]');
        if (overviewButton) {
            this.updateActiveButton(overviewButton);
        }

        // Setup case study initial state
        this.setupCaseStudyInitialState();
    }

    setupCaseStudyInitialState() {
        console.log('Setting up case study initial state...');
        
        // Hide all case study content
        const caseContents = document.querySelectorAll('.case-study-content');
        console.log('Found case study contents:', caseContents.length);
        
        caseContents.forEach(content => {
            content.classList.remove('active');
            content.style.display = 'none';
        });

        // Show Delaware case study by default
        const delawareCase = document.getElementById('delaware-case');
        if (delawareCase) {
            console.log('Showing Delaware case study');
            delawareCase.classList.add('active');
            delawareCase.style.display = 'block';
        }

        // Set Delaware tab as active
        const delawareTab = document.querySelector('[data-case="delaware"]');
        if (delawareTab) {
            this.updateActiveCaseTab(delawareTab);
        }
    }

    setupNavigation() {
        console.log('Setting up navigation...');
        const navButtons = document.querySelectorAll('.nav-btn');
        console.log('Found nav buttons:', navButtons.length);
        
        navButtons.forEach((button, index) => {
            const targetSection = button.getAttribute('data-section');
            console.log(`Nav button ${index}: targets ${targetSection}`);
            
            // Remove any existing event listeners
            button.replaceWith(button.cloneNode(true));
            const newButton = document.querySelectorAll('.nav-btn')[index];
            
            newButton.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                const target = e.target.getAttribute('data-section');
                console.log('Navigation clicked:', target);
                
                if (target) {
                    this.showSection(target);
                    this.updateActiveButton(e.target);
                }
            });

            // Add keyboard support
            newButton.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    newButton.click();
                }
            });
        });
    }

    setupOverviewCards() {
        console.log('Setting up overview cards...');
        const overviewCards = document.querySelectorAll('.overview-card');
        console.log('Found overview cards:', overviewCards.length);
        
        overviewCards.forEach((card, index) => {
            const targetSection = card.getAttribute('data-goto');
            console.log(`Overview card ${index}: targets ${targetSection}`);
            
            // Remove existing listeners
            card.replaceWith(card.cloneNode(true));
            const newCard = document.querySelectorAll('.overview-card')[index];
            
            // Add click handler
            newCard.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                const target = e.currentTarget.getAttribute('data-goto') || 'case-studies';
                console.log('Overview card clicked:', target);
                
                this.showSection(target);
                const navButton = document.querySelector(`[data-section="${target}"]`);
                if (navButton) {
                    this.updateActiveButton(navButton);
                }
            });

            // Add keyboard support
            newCard.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    newCard.click();
                }
            });

            // Make cards focusable
            newCard.setAttribute('tabindex', '0');
            newCard.setAttribute('role', 'button');
            
            // Add aria-labels
            const title = newCard.querySelector('h3');
            if (title) {
                newCard.setAttribute('aria-label', `Navigate to case studies section to learn about ${title.textContent}`);
            }
        });
    }

    setupCaseStudyTabs() {
        console.log('Setting up case study tabs...');
        const tabButtons = document.querySelectorAll('.tab-btn');
        console.log('Found tab buttons:', tabButtons.length);
        
        tabButtons.forEach((button, index) => {
            const targetCase = button.getAttribute('data-case');
            console.log(`Tab button ${index}: targets ${targetCase}`);
            
            // Remove existing listeners
            button.replaceWith(button.cloneNode(true));
            const newButton = document.querySelectorAll('.tab-btn')[index];
            
            newButton.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                const target = e.target.getAttribute('data-case');
                console.log('Case study tab clicked:', target);
                
                if (target) {
                    this.showCaseStudy(target);
                    this.updateActiveCaseTab(e.target);
                }
            });

            // Add keyboard support
            newButton.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    newButton.click();
                }
            });
        });
    }

    setupDownloadButtons() {
        console.log('Setting up download buttons...');
        const downloadButtons = document.querySelectorAll('.download-btn');
        console.log('Found download buttons:', downloadButtons.length);
        
        downloadButtons.forEach((button, index) => {
            const fileType = button.getAttribute('data-file');
            console.log(`Download button ${index}: file type ${fileType}`);
            
            button.addEventListener('click', (e) => {
                e.preventDefault();
                const type = e.target.getAttribute('data-file');
                this.handleDownload(type, e.target);
            });
        });
    }

    showSection(sectionId) {
        console.log('Attempting to show section:', sectionId);
        
        if (!sectionId) {
            console.error('No section ID provided');
            return;
        }
        
        // Hide all sections first
        const sections = document.querySelectorAll('.content-section');
        console.log('Hiding all sections, found:', sections.length);
        
        sections.forEach(section => {
            section.classList.remove('active');
            section.setAttribute('aria-hidden', 'true');
            section.style.display = 'none';
        });

        // Show target section
        const targetSection = document.getElementById(sectionId);
        console.log('Target section found:', targetSection ? 'YES' : 'NO', targetSection?.id);
        
        if (targetSection) {
            // Force display and then add active class
            targetSection.style.display = 'block';
            targetSection.style.opacity = '0';
            
            // Use requestAnimationFrame for smooth transition
            requestAnimationFrame(() => {
                targetSection.classList.add('active');
                targetSection.setAttribute('aria-hidden', 'false');
                targetSection.style.opacity = '1';
                
                // Scroll to top
                window.scrollTo({ top: 0, behavior: 'smooth' });
                
                console.log('Section displayed:', sectionId);
            });
            
            this.currentSection = sectionId;
            this.updatePageTitle(sectionId);
            this.updateUrlHash(sectionId);
            
            // Focus management
            setTimeout(() => {
                const firstHeading = targetSection.querySelector('h1, h2');
                if (firstHeading) {
                    firstHeading.setAttribute('tabindex', '-1');
                    firstHeading.focus();
                }
            }, 100);
            
        } else {
            console.error('Section not found:', sectionId);
            console.log('Available sections:', Array.from(document.querySelectorAll('.content-section')).map(s => s.id));
        }
    }

    showCaseStudy(caseId) {
        console.log('Attempting to show case study:', caseId);
        
        // Hide all case study content
        const caseContents = document.querySelectorAll('.case-study-content');
        caseContents.forEach(content => {
            content.classList.remove('active');
            content.style.display = 'none';
        });

        // Show target case study
        const targetCase = document.getElementById(`${caseId}-case`);
        
        if (targetCase) {
            targetCase.style.display = 'block';
            setTimeout(() => {
                targetCase.classList.add('active');
            }, 10);
            
            this.currentCase = caseId;
            console.log('Case study shown successfully:', caseId);
        } else {
            console.error('Case study not found:', caseId);
        }
    }

    updateActiveButton(activeButton) {
        // Remove active class from all nav buttons
        const buttons = document.querySelectorAll('.nav-btn');
        buttons.forEach(btn => {
            btn.classList.remove('active');
            btn.setAttribute('aria-pressed', 'false');
        });

        // Add active class to clicked button
        if (activeButton) {
            activeButton.classList.add('active');
            activeButton.setAttribute('aria-pressed', 'true');
        }
    }

    updateActiveCaseTab(activeTab) {
        // Remove active class from all case tabs
        const tabs = document.querySelectorAll('.tab-btn');
        tabs.forEach(tab => {
            tab.classList.remove('active');
            tab.setAttribute('aria-selected', 'false');
        });

        // Add active class to clicked tab
        if (activeTab) {
            activeTab.classList.add('active');
            activeTab.setAttribute('aria-selected', 'true');
        }
    }

    updatePageTitle(sectionId) {
        const titles = {
            'overview': 'Overview - Advanced Bridge Substructure Monitoring Technologies',
            'technologies': 'Technologies - Bridge Monitoring Systems',
            'case-studies': 'Case Studies - Real-World Implementations',
            'cost-analysis': 'Cost Analysis - ROI Assessment',
            'implementation': 'Implementation - Guidelines & Best Practices',
            'references': 'References - Research Citations',
            'downloads': 'Downloads - Resources & Reports'
        };

        document.title = titles[sectionId] || 'PVAMU Bridge Substructure Monitoring Research';
    }

    updateUrlHash(sectionId) {
        if (history.pushState) {
            const newUrl = window.location.pathname + window.location.search + '#' + sectionId;
            history.pushState({ section: sectionId }, '', newUrl);
        }
    }

    handleInitialHash() {
        // Handle initial page load with hash
        if (window.location.hash) {
            const hash = window.location.hash.substring(1);
            console.log('Initial hash detected:', hash);
            if (document.getElementById(hash)) {
                setTimeout(() => {
                    this.showSection(hash);
                    const navButton = document.querySelector(`[data-section="${hash}"]`);
                    if (navButton) {
                        this.updateActiveButton(navButton);
                    }
                }, 200);
            }
        }
    }

    handlePopState() {
        // Handle browser back/forward buttons
        const hash = window.location.hash.substring(1);
        if (hash && document.getElementById(hash)) {
            this.showSection(hash);
            const navButton = document.querySelector(`[data-section="${hash}"]`);
            if (navButton) {
                this.updateActiveButton(navButton);
            }
        } else {
            this.showSection('overview');
            const overviewButton = document.querySelector('[data-section="overview"]');
            if (overviewButton) {
                this.updateActiveButton(overviewButton);
            }
        }
    }

    handleDownload(fileType, button) {
        console.log('Download requested:', fileType);
        
        if (!button) return;
        
        // Show loading state
        const originalText = button.textContent;
        button.textContent = 'Preparing Download...';
        button.disabled = true;
        button.style.opacity = '0.7';

        // Simulate download preparation
        setTimeout(() => {
            // Reset button state
            button.textContent = originalText;
            button.disabled = false;
            button.style.opacity = '1';

            // Show download notification
            this.showDownloadNotification(fileType);
            
            console.log(`Download simulation complete for: ${fileType}`);
        }, 1500);
    }

    showDownloadNotification(fileType) {
        // Create and show a temporary notification
        const notification = document.createElement('div');
        notification.className = 'download-notification';
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--pvamu-purple);
            color: white;
            padding: 16px 24px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 1000;
            font-size: 14px;
            transform: translateX(100%);
            transition: transform 0.3s ease;
            max-width: 300px;
        `;
        
        const fileNames = {
            'complete-report': 'Complete Research Report',
            'tech-specs': 'Technology Specifications',
            'implementation': 'Implementation Checklist',
            'cost-analysis': 'Cost Analysis Spreadsheet',
            'case-studies': 'Case Study Summaries',
            'presentation': 'Presentation Slides'
        };

        notification.innerHTML = `
            <div style="display: flex; align-items: center; gap: 12px;">
                <span>📥</span>
                <div>
                    <div style="font-weight: 600;">Download Ready</div>
                    <div style="font-size: 12px; opacity: 0.9;">${fileNames[fileType] || 'File'}</div>
                </div>
            </div>
        `;

        document.body.appendChild(notification);

        // Animate in
        setTimeout(() => {
            notification.style.transform = 'translateX(0)';
        }, 100);

        // Auto-remove after 4 seconds
        setTimeout(() => {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.parentNode.removeChild(notification);
                }
            }, 300);
        }, 4000);
    }

    setupAccessibility() {
        // Add skip link
        const skipLink = document.createElement('a');
        skipLink.href = '#main-content';
        skipLink.textContent = 'Skip to main content';
        skipLink.className = 'sr-only';
        skipLink.style.cssText = `
            position: absolute;
            top: -40px;
            left: 6px;
            background: var(--pvamu-purple);
            color: white;
            padding: 8px;
            text-decoration: none;
            border-radius: 4px;
            z-index: 1000;
            transition: top 0.3s;
        `;
        
        skipLink.addEventListener('focus', () => {
            skipLink.style.top = '6px';
        });
        
        skipLink.addEventListener('blur', () => {
            skipLink.style.top = '-40px';
        });

        document.body.insertBefore(skipLink, document.body.firstChild);

        // Add id to main content
        const mainContent = document.querySelector('.main-content');
        if (mainContent) {
            mainContent.id = 'main-content';
        }
    }

    setupSmoothScrolling() {
        // Handle smooth scrolling for internal links
        document.addEventListener('click', (e) => {
            if (e.target.matches('a[href^="#"]') && 
                !e.target.classList.contains('nav-btn') && 
                !e.target.classList.contains('tab-btn')) {
                e.preventDefault();
                const targetId = e.target.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    }

    setupKeyboardNavigation() {
        document.addEventListener('keydown', (e) => {
            // Alt + number keys for section navigation
            if (e.altKey && e.key >= '1' && e.key <= '7') {
                e.preventDefault();
                const sectionMap = {
                    '1': 'overview',
                    '2': 'technologies',
                    '3': 'case-studies',
                    '4': 'cost-analysis',
                    '5': 'implementation',
                    '6': 'references',
                    '7': 'downloads'
                };
                
                const targetSection = sectionMap[e.key];
                if (targetSection) {
                    this.showSection(targetSection);
                    const navButton = document.querySelector(`[data-section="${targetSection}"]`);
                    if (navButton) {
                        this.updateActiveButton(navButton);
                    }
                }
            }

            // Arrow keys for case study navigation when in case studies section
            if (this.currentSection === 'case-studies' && !e.ctrlKey && !e.altKey) {
                if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
                    const cases = ['delaware', 'minnesota', 'florida'];
                    const currentIndex = cases.indexOf(this.currentCase);
                    let newIndex;
                    
                    if (e.key === 'ArrowLeft') {
                        newIndex = currentIndex > 0 ? currentIndex - 1 : cases.length - 1;
                    } else {
                        newIndex = currentIndex < cases.length - 1 ? currentIndex + 1 : 0;
                    }
                    
                    const newCase = cases[newIndex];
                    this.showCaseStudy(newCase);
                    const tabButton = document.querySelector(`[data-case="${newCase}"]`);
                    if (tabButton) {
                        this.updateActiveCaseTab(tabButton);
                        tabButton.focus();
                    }
                }
            }
        });
    }

    logDebugInfo() {
        console.log('=== Debug Information ===');
        console.log('Available sections:');
        const sections = document.querySelectorAll('.content-section');
        sections.forEach(section => {
            console.log('- Section ID:', section.id);
        });

        console.log('Available nav buttons:');
        const navButtons = document.querySelectorAll('.nav-btn');
        navButtons.forEach(button => {
            console.log('- Nav button for:', button.getAttribute('data-section'));
        });

        console.log('Available case study tabs:');
        const tabButtons = document.querySelectorAll('.tab-btn');
        tabButtons.forEach(button => {
            console.log('- Tab button for:', button.getAttribute('data-case'));
        });

        console.log('Available download buttons:');
        const downloadButtons = document.querySelectorAll('.download-btn');
        downloadButtons.forEach(button => {
            console.log('- Download button for:', button.getAttribute('data-file'));
        });
    }

    // Public method for external testing
    testNavigation() {
        console.log('Testing navigation...');
        const sections = ['overview', 'technologies', 'case-studies', 'cost-analysis', 'implementation', 'references', 'downloads'];
        
        sections.forEach((sectionId, index) => {
            setTimeout(() => {
                console.log(`Testing section: ${sectionId}`);
                this.showSection(sectionId);
                const navButton = document.querySelector(`[data-section="${sectionId}"]`);
                if (navButton) {
                    this.updateActiveButton(navButton);
                }
            }, index * 2000);
        });
    }
}

// Initialize the application
let app;

// Ensure proper initialization
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeApp);
} else {
    initializeApp();
}

function initializeApp() {
    console.log('DOM Content Loaded - Initializing PVAMU Bridge Monitoring App');
    
    app = new BridgeMonitoringApp();
    
    // Make app globally accessible for debugging
    window.bridgeApp = app;
    
    // Handle browser back/forward buttons
    window.addEventListener('popstate', (e) => {
        if (app && app.isInitialized) {
            app.handlePopState();
        }
    });

    // Performance monitoring
    if ('performance' in window) {
        window.addEventListener('load', () => {
            const loadTime = performance.now();
            console.log(`Application loaded in ${loadTime.toFixed(2)}ms`);
        });
    }

    console.log('PVAMU Bridge Substructure Monitoring Research Application Ready');
}

// Error handling
window.addEventListener('error', (e) => {
    console.error('Application error:', e.error);
});

// Export for potential module use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = BridgeMonitoringApp;
}
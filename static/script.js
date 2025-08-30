document.addEventListener('DOMContentLoaded', () => {
    // Language Selector UI
    const langToggleButton = document.getElementById('lang-toggle');
    const langDropdown = document.getElementById('lang-dropdown');

    if (langToggleButton) {
        langToggleButton.addEventListener('click', () => {
            langDropdown.classList.toggle('active');
        });
    }

    // Close dropdown if clicked outside
    document.addEventListener('click', (e) => {
        if (langDropdown && !langToggleButton.contains(e.target) && !langDropdown.contains(e.target)) {
            langDropdown.classList.remove('active');
        }
    });

    // Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const mainNav = document.querySelector('.main-nav');

    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            mainNav.classList.toggle('active');
        });
    }

    // Close mobile menu when a link is clicked
    if (mainNav) {
        mainNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                if (mainNav.classList.contains('active')) {
                    mainNav.classList.remove('active');
                }
            });
        });
    }
});
"use strict";


const themeLight = "light",
    themeDark = "dark",
    themeSwitcher = "id-theme-switcher";

/**
 * Set theme.
 *
 * @param {String} theme. Theme name.
 */
function setTheme(theme: string) {
    const off: string = theme === themeLight ? themeDark : themeLight;

    document.documentElement.classList.add(theme);
    document.documentElement.classList.remove(off);
}


/**
 * Set up theme switcher.
 */
function setUpThemeSwitcher() {
    const $themeSwitcher: HTMLElement = document.getElementById(themeSwitcher);

    $themeSwitcher.dataset.theme = (window.matchMedia && window.matchMedia(`(prefers-color-scheme: ${themeDark})`).matches) ? themeDark : themeLight;
    $themeSwitcher.addEventListener("click", () => {
        const theme: string = $themeSwitcher.dataset.theme === themeLight ? themeDark : themeLight;

        setTheme(theme);
        $themeSwitcher.dataset.theme = theme;
    });
}


/**
 * Add theme switcher event listener on window load.
 */
window.onload = () => {
    setUpThemeSwitcher();
};

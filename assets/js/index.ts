"use strict";


const themeLight: string = "light",
    themeDark: string = "dark",
    themeSwitcher: string = "id-theme-switcher";

/**
 * Set theme.
 *
 * @param {String} theme. Theme name.
 */
function setTheme(theme: string) {
    let off: string = theme === themeLight ? themeDark : themeLight;

    document.documentElement.classList.add(theme);
    document.documentElement.classList.remove(off);
}


/**
 * Set up theme switcher.
 */
function setUpThemeSwitcher() {
    let $themeSwitcher: HTMLElement = document.getElementById(themeSwitcher);

    $themeSwitcher.dataset.theme = (window.matchMedia && window.matchMedia(`(prefers-color-scheme: ${themeDark})`).matches) ? themeDark : themeLight;
    $themeSwitcher.addEventListener("click", () => {
        let theme: string = $themeSwitcher.dataset.theme === themeLight ? themeDark : themeLight;

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

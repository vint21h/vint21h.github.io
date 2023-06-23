const themeLight = "light",
    themeDark = "dark",
    themeSwitcherSelector = "id-theme-switcher";

/**
 * Set theme.
 *
 * @param {String} theme. Theme name.
 */
function setTheme(theme) {

    "use strict";

    let off = theme === themeLight ? themeDark : themeLight;

    document.documentElement.classList.add(theme);
    document.documentElement.classList.remove(off);
}


/**
 * Set up theme switcher.
 */
function setUpThemeSwitcher() {

    "use strict";

    let $themeSwitcher = document.getElementById(themeSwitcherSelector);

    $themeSwitcher.dataset.theme = (window.matchMedia && window.matchMedia(`(prefers-color-scheme: ${themeDark})`).matches) ? themeDark : themeLight;
    $themeSwitcher.addEventListener("click", () => {
        let theme = $themeSwitcher.dataset.theme === themeLight ? themeDark : themeLight;

        setTheme(theme);
        $themeSwitcher.dataset.theme = theme;
    });
}


/**
 * Add theme switcher event listener on window load.
 */
window.onload = () => {

    "use strict";

    setUpThemeSwitcher();
};

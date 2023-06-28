"use strict";
var themeLight = "light", themeDark = "dark", themeSwitcher = "id-theme-switcher";
/**
 * Set theme.
 *
 * @param {String} theme. Theme name.
 */
function setTheme(theme) {
    var off = theme === themeLight ? themeDark : themeLight;
    document.documentElement.classList.add(theme);
    document.documentElement.classList.remove(off);
}
/**
 * Set up theme switcher.
 */
function setUpThemeSwitcher() {
    var $themeSwitcher = document.getElementById(themeSwitcher);
    $themeSwitcher.dataset.theme = (window.matchMedia && window.matchMedia("(prefers-color-scheme: ".concat(themeDark, ")")).matches) ? themeDark : themeLight;
    $themeSwitcher.addEventListener("click", function () {
        var theme = $themeSwitcher.dataset.theme === themeLight ? themeDark : themeLight;
        setTheme(theme);
        $themeSwitcher.dataset.theme = theme;
    });
}
/**
 * Add theme switcher event listener on window load.
 */
window.onload = function () {
    setUpThemeSwitcher();
};
//# sourceMappingURL=index.js.map

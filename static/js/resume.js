/**
 * Set theme.
 *
 * @param {String} theme. Theme name.
 */
function setTheme(theme) {

    "use strict";

    let off = theme === "light" ? "dark" : "light";

    document.documentElement.classList.add(theme);
    document.documentElement.classList.remove(off);
}


/**
 * Add theme switcher event listener on window load.
 */
window.onload = () => {

    "use strict";

    let $themeSwitcher = document.getElementById("id-theme-switcher");

    $themeSwitcher.dataset.theme = (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) ? "dark" : "light";
    $themeSwitcher.addEventListener("click", () => {
        let theme = $themeSwitcher.dataset.theme === "light" ? "dark" : "light";

        setTheme(theme);
        $themeSwitcher.dataset.theme = theme;
    });
};

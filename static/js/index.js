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
 * Set up theme switcher.
 */
function setUpThemeSwitcher() {

    "use strict";

    let $themeSwitcher = document.getElementById("id-theme-switcher");

    $themeSwitcher.dataset.theme = (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) ? "dark" : "light";
    $themeSwitcher.addEventListener("click", () => {
        let theme = $themeSwitcher.dataset.theme === "light" ? "dark" : "light";

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

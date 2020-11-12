// vint21h.github.io
// static/js/resume.js


/**
 * Set theme.
 *
 * @param {String} theme. Theme name.
 */
function setTheme(theme) {

    "use strict";

    var off = theme === "light" ? "dark" : "light";

    document.documentElement.classList.add(theme);
    document.documentElement.classList.remove(off);
}


/**
 * Add theme switcher event listener on window load.
 */
window.onload = function () {

    "use strict";

    var themeSwitcher = document.getElementById("id-theme-switcher");

    themeSwitcher.dataset.theme = (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) ? "dark" : "light";
    themeSwitcher.addEventListener("click", function () {
        var theme = themeSwitcher.dataset.theme === "light" ? "dark" : "light";

        setTheme(theme);
        themeSwitcher.dataset.theme = theme;
    });
};

// vint21h.github.io
// static/js/resume.js


/**
 * Set theme.
 *
 * @param {String} theme. Theme name.
 */
function setTheme(theme) {

    "use strict";

    var on = theme;
    var off = theme === "light" ? "dark" : "light";

    document.documentElement.classList.add(on);
    document.documentElement.classList.remove(off);
}


// TODO: make this work.
var avatar = document.querySelector(".avatar");
avatar.addEventListener("click", function() {

    "use strict";

    var theme = avatar.dataset.checked ? "light" : "dark";

    setTheme(theme);
    avatar.dataset.checked = !avatar.dataset.checked;
});

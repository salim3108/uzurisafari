document.addEventListener("DOMContentLoaded", function () {
    // Sidebar collapse toggle
    const body = document.body;
    const toggleBtn = document.querySelector("[data-widget='pushmenu']");
    if (toggleBtn) {
        toggleBtn.addEventListener("click", () => {
            body.classList.toggle("sidebar-collapse");
        });
    }

    // User profile hover
    const userMenu = document.querySelector(".user-menu");
    if (userMenu) {
        userMenu.addEventListener("mouseenter", () => {
            userMenu.classList.add("show");
        });
        userMenu.addEventListener("mouseleave", () => {
            userMenu.classList.remove("show");
        });
    }
});

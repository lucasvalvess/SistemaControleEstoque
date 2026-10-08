document.addEventListener("DOMContentLoaded", () => {
    const nav = document.querySelector(".main-nav");
    const toggle = document.querySelector(".nav-toggle");

    if (nav && toggle) {
        toggle.addEventListener("click", () => {
            const isOpen = nav.classList.toggle("is-open");
            toggle.setAttribute("aria-expanded", String(isOpen));
            toggle.setAttribute("aria-label", isOpen ? "Fechar menu" : "Abrir menu");
        });

        nav.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                nav.classList.remove("is-open");
                toggle.setAttribute("aria-expanded", "false");
                toggle.setAttribute("aria-label", "Abrir menu");
            });
        });
    }

    const path = window.location.pathname;
    document.querySelectorAll(".nav-link[data-nav]").forEach((link) => {
        const target = link.dataset.nav;
        const isActive =
            (target === "dashboard" && (path === "/" || path === "")) ||
            (target === "produtos" && path.startsWith("/produtos/")) ||
            (target === "categorias" && path.startsWith("/categorias/")) ||
            (target === "fornecedores" && path.startsWith("/fornecedores/"));

        link.classList.toggle("is-active", isActive);
        if (isActive) {
            link.setAttribute("aria-current", "page");
        } else {
            link.removeAttribute("aria-current");
        }
    });

    document.querySelectorAll(".message-close").forEach((button) => {
        button.addEventListener("click", () => {
            const message = button.closest(".message");
            if (message) {
                message.remove();
            }
        });
    });
});

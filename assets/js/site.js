(() => {
  const root = document.documentElement;
  const systemTheme = window.matchMedia?.("(prefers-color-scheme: dark)");
  let savedTheme = null;

  try {
    const stored = localStorage.getItem("site-theme");
    if (stored === "light" || stored === "dark") savedTheme = stored;
  } catch (error) {
    console.warn("Theme preference could not be read.", error);
  }

  const setTheme = (theme) => {
    root.dataset.theme = theme;
    const button = document.querySelector(".theme-toggle");
    if (button) {
      button.setAttribute("aria-pressed", String(theme === "dark"));
      button.textContent = "Dark theme";
    }
  };

  setTheme(savedTheme ?? (systemTheme?.matches ? "dark" : "light"));

  const siteHeader = document.querySelector(".site-header .nav");
  if (siteHeader) {
    const navigation = siteHeader.querySelector("nav");
    if (navigation) {
      navigation.classList.add("navlinks");
      navigation.setAttribute("aria-label", "Main navigation");
      navigation.id ||= "main-navigation";

      const controls = document.createElement("div");
      controls.className = "site-controls";

      const menuButton = document.createElement("button");
      menuButton.className = "site-menu-toggle";
      menuButton.type = "button";
      menuButton.textContent = "Menu";
      menuButton.setAttribute("aria-controls", navigation.id);
      menuButton.setAttribute("aria-expanded", "false");
      menuButton.addEventListener("click", () => {
        const isOpen = menuButton.getAttribute("aria-expanded") === "true";
        menuButton.setAttribute("aria-expanded", String(!isOpen));
        navigation.classList.toggle("is-open", !isOpen);
      });

      const themeButton = document.createElement("button");
      themeButton.className = "theme-toggle";
      themeButton.type = "button";
      themeButton.addEventListener("click", () => {
        const theme = root.dataset.theme === "dark" ? "light" : "dark";
        setTheme(theme);
        try {
          localStorage.setItem("site-theme", theme);
          savedTheme = theme;
        } catch (error) {
          console.warn("Theme preference could not be saved.", error);
        }
      });

      navigation.addEventListener("click", (event) => {
        if (event.target.closest("a")) {
          navigation.classList.remove("is-open");
          menuButton.setAttribute("aria-expanded", "false");
        }
      });
      navigation.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && navigation.classList.contains("is-open")) {
          navigation.classList.remove("is-open");
          menuButton.setAttribute("aria-expanded", "false");
          menuButton.focus();
        }
      });

      controls.append(menuButton, themeButton);
      siteHeader.append(controls);
      siteHeader.classList.add("js-enhanced");
      setTheme(root.dataset.theme);
    }
  }

  if (/(^|\/)services\.html$/.test(window.location.pathname)) {
    const grid = document.querySelector(".content .grid");
    const cards = grid ? [...grid.querySelectorAll(".card")] : [];

    if (grid && cards.length) {
      const search = document.createElement("div");
      search.className = "service-search";

      const label = document.createElement("label");
      label.htmlFor = "service-search";
      label.textContent = "Find a capability";

      const input = document.createElement("input");
      input.id = "service-search";
      input.type = "search";
      input.placeholder = "Try AI, data, strategy, or software";
      input.setAttribute("aria-describedby", "service-search-status");

      const status = document.createElement("p");
      status.id = "service-search-status";
      status.className = "search-status";
      status.setAttribute("role", "status");
      status.setAttribute("aria-live", "polite");

      const updateResults = () => {
        const query = input.value.trim().toLocaleLowerCase();
        let visibleCount = 0;
        for (const card of cards) {
          const matches = card.textContent.toLocaleLowerCase().includes(query);
          card.hidden = !matches;
          if (matches) visibleCount += 1;
        }
        status.textContent = query
          ? `${visibleCount} ${visibleCount === 1 ? "capability" : "capabilities"} found`
          : `${visibleCount} capabilities`;
      };

      input.addEventListener("input", updateResults);
      search.append(label, input, status);
      grid.before(search);
      updateResults();
    }
  }

  if (!savedTheme && systemTheme?.addEventListener) {
    systemTheme.addEventListener("change", (event) => {
      if (!savedTheme) setTheme(event.matches ? "dark" : "light");
    });
  }
})();

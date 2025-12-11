document.addEventListener("DOMContentLoaded", () => {
  const menuButton = document.getElementById("mobile-menu-button");
  const mobileMenu = document.getElementById("mobile-menu");
  const hamburgerIcon = document.getElementById("hamburger-icon");
  const closeIcon = document.getElementById("close-icon");

  // ✅ Mobile nav toggle + icon swap
  if (menuButton && mobileMenu && hamburgerIcon && closeIcon) {
    menuButton.addEventListener("click", () => {
      const isOpen = !mobileMenu.classList.contains("hidden");
      mobileMenu.classList.toggle("hidden");
      hamburgerIcon.classList.toggle("hidden");
      closeIcon.classList.toggle("hidden");
      menuButton.setAttribute("aria-expanded", String(!isOpen));
    });

    // ✅ Close menu when clicking a link (mobile)
    mobileMenu.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        mobileMenu.classList.add("hidden");
        hamburgerIcon.classList.remove("hidden");
        closeIcon.classList.add("hidden");
        menuButton.setAttribute("aria-expanded", "false");
      });
    });
  }

  // ✅ Hero slider
  const slides = document.querySelectorAll("#hero-slider video");
  let current = 0;

  if (slides.length > 0) {
    slides.forEach((s, i) => {
      s.classList.add(
        "transition-opacity",
        "duration-1000",
        "absolute",
        "inset-0",
        "w-full",
        "h-full",
        "object-cover"
      );
      if (i === 0) {
        s.classList.remove("opacity-0");
        s.classList.add("opacity-100");
      } else {
        s.classList.remove("opacity-100");
        s.classList.add("opacity-0");
      }
    });

    if (slides.length > 1) {
      setInterval(() => {
        slides[current].classList.remove("opacity-100");
        slides[current].classList.add("opacity-0");

        current = (current + 1) % slides.length;

        slides[current].classList.remove("opacity-0");
        slides[current].classList.add("opacity-100");
      }, 5000);
    }
  }

  // ✅ Social toggle
  const toggleBtn = document.getElementById("social-toggle");
  const toggleIcon = document.getElementById("toggle-icon");
  const socialIcons = document.getElementById("social-icons");

  if (toggleBtn && toggleIcon && socialIcons) {
    toggleBtn.addEventListener("click", () => {
      socialIcons.classList.toggle("hidden");
      if (socialIcons.classList.contains("hidden")) {
        toggleIcon.classList.remove("bx-x");
        toggleIcon.classList.add("bx-message-rounded-dots");
      } else {
        toggleIcon.classList.remove("bx-message-rounded-dots");
        toggleIcon.classList.add("bx-x");
      }
    });
  }
});

// 1. Mobile menu toggle (also closes when a link is tapped)
const navToggle = document.getElementById("navToggle");
const navLinks = document.getElementById("navLinks");
navToggle.addEventListener("click", () => {
  const open = navLinks.classList.toggle("open");
  navToggle.setAttribute("aria-expanded", open);
});
navLinks.querySelectorAll("a").forEach((link) =>
  link.addEventListener("click", () => {
    navLinks.classList.remove("open");
    navToggle.setAttribute("aria-expanded", "false");
  })
);

// 2. Add a shadow to the navbar when the page is scrolled
const navbar = document.getElementById("navbar");
window.addEventListener("scroll", () => {
  navbar.classList.toggle("scrolled", window.scrollY > 10);
});

// 3. Show the current year in the footer
document.getElementById("year").textContent = new Date().getFullYear();

// 4. Reveal elements as they scroll into view
const revealItems = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );
  revealItems.forEach((el) => observer.observe(el));
} else {
  revealItems.forEach((el) => el.classList.add("visible"));
}

// 5. Menu filter + search (only runs on the Menu page)
const filters = document.getElementById("filters");
if (filters) {
  const buttons = filters.querySelectorAll(".filter-btn");
  const items = document.querySelectorAll(".menu-item");
  const search = document.getElementById("menuSearch");
  const emptyMsg = document.getElementById("emptyMsg");
  let category = "all";

  function applyFilters() {
    const text = search.value.trim().toLowerCase();
    let visible = 0;
    items.forEach((item) => {
      const matchCategory = category === "all" || item.dataset.category === category;
      const matchText = item.dataset.name.includes(text);
      const show = matchCategory && matchText;
      item.classList.toggle("hidden", !show);
      if (show) visible++;
    });
    emptyMsg.classList.toggle("hidden", visible > 0);
  }

  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      buttons.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      category = btn.dataset.filter;
      applyFilters();
    });
  });
  search.addEventListener("input", applyFilters);
}

// 6. Contact form validation (only runs on the Contact page; nothing is sent anywhere)
const form = document.getElementById("contactForm");
if (form) {
  const msg = document.getElementById("formMsg");
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();
    const emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

    if (!name || !emailOk || !message) {
      msg.textContent = "Please fill all fields with a valid email.";
      msg.className = "form-msg error";
      return;
    }
    msg.textContent = "Thank you, " + name + "! We will get back to you soon.";
    msg.className = "form-msg success";
    form.reset();
  });
}

// 1. Mobile menu toggle
const navToggle = document.getElementById("navToggle");
const navLinks = document.getElementById("navLinks");
navToggle.addEventListener("click", () => navLinks.classList.toggle("open"));

// 2. Add a shadow to the navbar when the page is scrolled
const navbar = document.getElementById("navbar");
window.addEventListener("scroll", () => {
  navbar.classList.toggle("scrolled", window.scrollY > 10);
});

// 3. Show the current year in the footer
document.getElementById("year").textContent = new Date().getFullYear();

// 4. Menu category filter (only runs on the Menu page)
const filters = document.getElementById("filters");
if (filters) {
  const buttons = filters.querySelectorAll(".filter-btn");
  const items = document.querySelectorAll(".menu-item");
  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      buttons.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      const filter = btn.dataset.filter;
      items.forEach((item) => {
        const show = filter === "all" || item.dataset.category === filter;
        item.classList.toggle("hidden", !show);
      });
    });
  });
}

// 5. Contact form validation (only runs on the Contact page; nothing is sent anywhere)
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

# Restaurant Website: Flask + Docker + Jenkins + pytest + Git

Repository: https://github.com/OnkarYadav007/Restaurant_Project_Repo.git
Placeholders used: `[PROJECT_NAME]` = Restaurant_Project_Repo, `[GITHUB_REPO_URL]` = the URL above, `[DOCKER_IMAGE_NAME]` = restaurant-website.

## 1. PROJECT OVERVIEW
**Purpose:** a simple restaurant website ("Tasty Corner") with Home, About, Menu and Contact pages, served by Flask.
**Technologies:** Python, Flask, HTML, CSS, JavaScript, pytest, Git, GitHub, Docker, Jenkins.
**Features:** responsive navbar, illustrated hero section, menu cards with category filter and live search, testimonials, contact info and a validated form, scroll animations, footer, no database or login.
**Why it suits a college presentation:** it is small enough to explain in minutes, yet it touches the full workflow (code, tests, version control, containers, CI), so you can show how a real project is built and delivered.

## 2. FOLDER STRUCTURE
```
Restaurant_Project_Repo/
│
├── app.py
├── conftest.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── Jenkinsfile
├── Jenkinsfile.linux
├── README.md
├── PROJECT_GUIDE.md
├── create_git_history.sh
├── .gitignore
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── menu.html
│   └── contact.html
│
├── static/
│   ├── css/style.css
│   ├── js/script.js
│   └── images/        (SVG dish illustrations, storefront, favicon)
│
├── screenshots/
│
└── tests/
    ├── __init__.py
    └── test_app.py
```
| File | Purpose |
|---|---|
| `app.py` | Creates the Flask app, holds the menu list and defines the four routes |
| `conftest.py` | Empty file at the root so pytest can import `app.py` |
| `requirements.txt` | Python packages to install (Flask, pytest) |
| `Dockerfile` | Recipe to package the app into a Docker image |
| `.dockerignore` | Files Docker should not copy (venv, .git) |
| `Jenkinsfile` | CI pipeline for a Windows Jenkins agent: checkout, install, test, build image |
| `Jenkinsfile.linux` | The same pipeline using `sh` for Linux |
| `screenshots/` | Screenshots used in the README |
| `README.md` | Project documentation for GitHub |
| `PROJECT_GUIDE.md` | This guide |
| `create_git_history.sh` | Script that creates the 6 commits |
| `.gitignore` | Files Git should ignore |
| `templates/base.html` | Shared layout (navbar, footer) that other pages extend |
| `templates/index.html` | Home page: hero and favourites |
| `templates/about.html` | About page |
| `templates/menu.html` | Menu page with filter buttons and cards |
| `templates/contact.html` | Contact info and form |
| `static/css/style.css` | All styling and responsive rules |
| `static/js/script.js` | Mobile menu, filter, form validation |
| `static/images/*.svg` | Hand-made SVG illustrations: pizzas, burgers, lemonade, brownie, storefront, favicon (crisp at any size, no downloads needed) |
| `tests/test_app.py` | Automated tests |

## 3. COMPLETE SOURCE CODE
### `app.py`
````python
"""Restaurant website - a simple Flask app (no database, no login)."""
import os
from flask import Flask, render_template

app = Flask(__name__)

# Menu data lives in a plain Python list. No database is needed.
# To use a real photo instead of an illustration, drop the file in
# static/images/ and change the "image" value (for example "margherita.jpg").
MENU = [
    {"name": "Margherita Pizza", "category": "pizza", "price": 349, "veg": True,
     "badge": "Bestseller", "image": "pizza-margherita.svg",
     "desc": "San Marzano tomato, fresh mozzarella and basil on a wood-fired crust."},
    {"name": "Pepperoni Pizza", "category": "pizza", "price": 429, "veg": False,
     "badge": "Spicy", "image": "pizza-pepperoni.svg",
     "desc": "Crisp-edged pepperoni, mozzarella and a hint of chilli oil."},
    {"name": "Classic Burger", "category": "burger", "price": 299, "veg": False,
     "badge": "Chef's pick", "image": "burger-classic.svg",
     "desc": "Juicy beef patty, cheddar, lettuce, tomato and our house sauce."},
    {"name": "Veggie Burger", "category": "burger", "price": 279, "veg": True,
     "badge": "", "image": "burger-veggie.svg",
     "desc": "Crispy garden patty with avocado, cucumber and herb mayo."},
    {"name": "Fresh Lemonade", "category": "drinks", "price": 129, "veg": True,
     "badge": "Refreshing", "image": "lemonade.svg",
     "desc": "Hand-squeezed lemons, mint and ice. Sweet, sharp and cold."},
    {"name": "Chocolate Brownie", "category": "dessert", "price": 199, "veg": True,
     "badge": "Must try", "image": "brownie.svg",
     "desc": "Warm fudgy brownie topped with vanilla ice cream and chocolate sauce."},
]

CONTACT = {
    "address": "123 Food Street, Pune, Maharashtra",
    "phone": "+91 98765 43210",
    "email": "hello@restaurant.example",
    "hours": [("Monday - Friday", "11:00 AM - 11:00 PM"),
              ("Saturday - Sunday", "10:00 AM - 12:00 AM")],
}


@app.route("/")
def home():
    featured = [MENU[0], MENU[2], MENU[5]]
    return render_template("index.html", active="home", featured=featured)


@app.route("/about")
def about():
    return render_template("about.html", active="about")


@app.route("/menu")
def menu():
    return render_template("menu.html", active="menu", items=MENU)


@app.route("/contact")
def contact():
    return render_template("contact.html", active="contact", info=CONTACT)


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(host="0.0.0.0", port=5000, debug=debug)
````

### `requirements.txt`
````
Flask>=3.0.3
pytest>=8.4
````

### `.gitignore`
````
venv/
__pycache__/
*.pyc
.pytest_cache/
.env
.idea/
.vscode/
*.log
````

### `conftest.py`
````python
# Empty on purpose: its presence at the project root lets pytest find app.py.
````

### `templates/base.html`
````html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Tasty Corner - wood-fired pizza, burgers and desserts in Pune.">
  <title>{% block title %}Home{% endblock %} | Tasty Corner</title>
  <link rel="icon" type="image/svg+xml" href="{{ url_for('static', filename='images/favicon.svg') }}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
  <script>document.documentElement.classList.add('js');</script>
</head>
<body>
  <header class="navbar" id="navbar">
    <div class="container nav-inner">
      <a class="logo" href="{{ url_for('home') }}">
        <img src="{{ url_for('static', filename='images/favicon.svg') }}" alt="" width="34" height="34">
        <span>Tasty Corner</span>
      </a>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
      <nav class="nav-links" id="navLinks">
        <a href="{{ url_for('home') }}" class="{{ 'active' if active == 'home' }}">Home</a>
        <a href="{{ url_for('about') }}" class="{{ 'active' if active == 'about' }}">About</a>
        <a href="{{ url_for('menu') }}" class="{{ 'active' if active == 'menu' }}">Menu</a>
        <a href="{{ url_for('contact') }}" class="{{ 'active' if active == 'contact' }}">Contact</a>
        <a href="{{ url_for('contact') }}" class="btn btn-small nav-cta">Book a table</a>
      </nav>
    </div>
  </header>

  <main>{% block content %}{% endblock %}</main>

  <footer class="footer">
    <div class="container footer-grid">
      <div>
        <a class="logo logo-light" href="{{ url_for('home') }}">
          <img src="{{ url_for('static', filename='images/favicon.svg') }}" alt="" width="34" height="34">
          <span>Tasty Corner</span>
        </a>
        <p class="footer-text">Fresh, honest food cooked to order since 2015.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <a href="{{ url_for('home') }}">Home</a>
        <a href="{{ url_for('about') }}">About</a>
        <a href="{{ url_for('menu') }}">Menu</a>
        <a href="{{ url_for('contact') }}">Contact</a>
      </div>
      <div>
        <h4>Visit us</h4>
        <p>123 Food Street, Pune</p>
        <p>+91 98765 43210</p>
        <p>Open daily from 11 AM</p>
      </div>
    </div>
    <div class="container footer-bottom">© <span id="year">2026</span> Tasty Corner. All rights reserved.</div>
  </footer>

  <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
````

### `templates/index.html`
````html
{% extends "base.html" %}
{% block title %}Home{% endblock %}
{% block content %}
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-text">
      <span class="eyebrow">Wood-fired kitchen · Pune · Since 2015</span>
      <h1>Fresh food, cooked with <em>fire</em> and love.</h1>
      <p class="lead">Hand-stretched pizzas, juicy burgers and desserts worth saving room for. Made to order with ingredients from local farms.</p>
      <div class="hero-actions">
        <a class="btn" href="{{ url_for('menu') }}">Explore the menu</a>
        <a class="btn btn-ghost" href="{{ url_for('contact') }}">Book a table</a>
      </div>
      <ul class="hero-stats">
        <li><strong>4.8★</strong><span>Guest rating</span></li>
        <li><strong>10k+</strong><span>Happy diners</span></li>
        <li><strong>100%</strong><span>Made fresh</span></li>
      </ul>
    </div>
    <div class="hero-visual" aria-hidden="true">
      <div class="blob"></div>
      <img class="dish dish-main" src="{{ url_for('static', filename='images/pizza-margherita.svg') }}" alt="">
      <img class="dish dish-burger" src="{{ url_for('static', filename='images/burger-classic.svg') }}" alt="">
      <img class="dish dish-drink" src="{{ url_for('static', filename='images/lemonade.svg') }}" alt="">
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true">
  <div class="marquee-track">
    <span>Wood-fired pizza</span><span>Fresh daily</span><span>Locally sourced</span><span>Cooked to order</span><span>Family recipes</span>
    <span>Wood-fired pizza</span><span>Fresh daily</span><span>Locally sourced</span><span>Cooked to order</span><span>Family recipes</span>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Our favourites</span>
      <h2>Dishes our guests keep coming back for</h2>
    </div>
    <div class="cards">
      {% for item in featured %}
      <article class="dish-card reveal">
        <div class="dish-img">
          {% if item.badge %}<span class="badge">{{ item.badge }}</span>{% endif %}
          <img src="{{ url_for('static', filename='images/' + item.image) }}" alt="{{ item.name }}" loading="lazy">
        </div>
        <div class="dish-body">
          <h3><span class="veg-dot {{ 'veg' if item.veg else 'nonveg' }}" title="{{ 'Vegetarian' if item.veg else 'Non-vegetarian' }}"></span>{{ item.name }}</h3>
          <p>{{ item.desc }}</p>
          <div class="price-row"><span class="price">₹{{ item.price }}</span></div>
        </div>
      </article>
      {% endfor %}
    </div>
    <div class="center"><a class="btn btn-outline" href="{{ url_for('menu') }}">See the full menu</a></div>
  </div>
</section>

<section class="section section-sand">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Why Tasty Corner</span>
      <h2>Simple food, done properly</h2>
    </div>
    <div class="features">
      <div class="feature reveal"><div class="feature-icon">🌿</div><h3>Fresh ingredients</h3><p>Vegetables, herbs and cheese come from local suppliers every morning.</p></div>
      <div class="feature reveal"><div class="feature-icon">🔥</div><h3>Wood-fired oven</h3><p>Our oven runs at 400°C, so pizzas cook in about 90 seconds with a perfect crust.</p></div>
      <div class="feature reveal"><div class="feature-icon">👨‍🍳</div><h3>Made to order</h3><p>Nothing is pre-made. Every dish is cooked the moment you order it.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Kind words</span>
      <h2>What our guests say</h2>
    </div>
    <div class="quotes">
      <figure class="quote reveal"><blockquote>The best margherita in the city. The crust is light, crisp and smoky.</blockquote><figcaption><span class="avatar">AS</span>Aarav S.</figcaption></figure>
      <figure class="quote reveal"><blockquote>Friendly staff and fast service. The brownie with ice cream is a must.</blockquote><figcaption><span class="avatar">PK</span>Priya K.</figcaption></figure>
      <figure class="quote reveal"><blockquote>Our go-to spot for family dinners. Everyone finds something they love.</blockquote><figcaption><span class="avatar">RM</span>Rohan M.</figcaption></figure>
    </div>
  </div>
</section>

<section class="cta">
  <div class="container cta-inner reveal">
    <h2>Hungry yet? Let us save you a table.</h2>
    <a class="btn btn-light" href="{{ url_for('contact') }}">Book a table</a>
  </div>
</section>
{% endblock %}
````

### `templates/about.html`
````html
{% extends "base.html" %}
{% block title %}About{% endblock %}
{% block content %}
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">About us</span>
    <h1>A small kitchen with a big appetite</h1>
  </div>
</section>

<section class="section">
  <div class="container two-col">
    <img class="rounded reveal" src="{{ url_for('static', filename='images/storefront.svg') }}" alt="Illustration of the Tasty Corner restaurant front">
    <div class="reveal">
      <span class="eyebrow">Our story</span>
      <h2>From a family kitchen to your neighbourhood favourite</h2>
      <p>Tasty Corner started in 2015 as a tiny family kitchen with one oven and a handful of recipes passed down from our grandmother.</p>
      <p>Today we serve hundreds of guests every week, but the idea is the same: use fresh ingredients, cook every dish to order, and make everyone feel at home.</p>
    </div>
  </div>
</section>

<section class="stats-band">
  <div class="container stats">
    <div><strong>2015</strong><span>Year we opened</span></div>
    <div><strong>12</strong><span>Team members</span></div>
    <div><strong>50+</strong><span>Local suppliers</span></div>
    <div><strong>10k+</strong><span>Guests served</span></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">What we believe</span><h2>Our values</h2></div>
    <div class="features">
      <div class="feature reveal"><div class="feature-icon">🌿</div><h3>Fresh ingredients</h3><p>If it is not fresh, it does not go on the plate.</p></div>
      <div class="feature reveal"><div class="feature-icon">💛</div><h3>Warm service</h3><p>We treat every guest like a member of the family.</p></div>
      <div class="feature reveal"><div class="feature-icon">♻️</div><h3>Less waste</h3><p>We plan our prep carefully and compost what we cannot use.</p></div>
    </div>
  </div>
</section>

<section class="section section-sand">
  <div class="container narrow">
    <div class="section-head reveal"><span class="eyebrow">Our journey</span><h2>Milestones</h2></div>
    <ul class="timeline">
      <li class="reveal"><strong>2015</strong><p>Opened our doors with a 20-seat dining room.</p></li>
      <li class="reveal"><strong>2018</strong><p>Installed our wood-fired oven and launched the pizza menu.</p></li>
      <li class="reveal"><strong>2022</strong><p>Expanded the kitchen and added burgers and desserts.</p></li>
      <li class="reveal"><strong>Today</strong><p>Serving hundreds of happy guests every week.</p></li>
    </ul>
  </div>
</section>
{% endblock %}
````

### `templates/menu.html`
````html
{% extends "base.html" %}
{% block title %}Menu{% endblock %}
{% block content %}
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Our menu</span>
    <h1>Made fresh, served hot</h1>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="toolbar">
      <div class="filters" id="filters">
        <button class="filter-btn active" data-filter="all">All</button>
        <button class="filter-btn" data-filter="pizza">Pizza</button>
        <button class="filter-btn" data-filter="burger">Burgers</button>
        <button class="filter-btn" data-filter="drinks">Drinks</button>
        <button class="filter-btn" data-filter="dessert">Desserts</button>
      </div>
      <input type="search" id="menuSearch" class="search" placeholder="Search dishes..." aria-label="Search dishes">
    </div>
    <p class="legend"><span class="veg-dot veg"></span> Vegetarian <span class="veg-dot nonveg"></span> Non-vegetarian</p>

    <div class="cards">
      {% for item in items %}
      <article class="dish-card menu-item" data-category="{{ item.category }}" data-name="{{ item.name|lower }} {{ item.desc|lower }}">
        <div class="dish-img">
          {% if item.badge %}<span class="badge">{{ item.badge }}</span>{% endif %}
          <img src="{{ url_for('static', filename='images/' + item.image) }}" alt="{{ item.name }}" loading="lazy">
        </div>
        <div class="dish-body">
          <h3><span class="veg-dot {{ 'veg' if item.veg else 'nonveg' }}" title="{{ 'Vegetarian' if item.veg else 'Non-vegetarian' }}"></span>{{ item.name }}</h3>
          <p>{{ item.desc }}</p>
          <div class="price-row"><span class="price">₹{{ item.price }}</span></div>
        </div>
      </article>
      {% endfor %}
    </div>
    <p class="empty hidden" id="emptyMsg">No dishes match your search. Try another word.</p>
  </div>
</section>
{% endblock %}
````

### `templates/contact.html`
````html
{% extends "base.html" %}
{% block title %}Contact{% endblock %}
{% block content %}
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Contact</span>
    <h1>Come hungry. We will do the rest.</h1>
  </div>
</section>

<section class="section">
  <div class="container two-col top">
    <div class="info-stack">
      <div class="info-card reveal"><span class="info-icon">📍</span><div><h3>Address</h3><p>{{ info.address }}</p></div></div>
      <div class="info-card reveal"><span class="info-icon">📞</span><div><h3>Phone</h3><p>{{ info.phone }}</p></div></div>
      <div class="info-card reveal"><span class="info-icon">✉️</span><div><h3>Email</h3><p>{{ info.email }}</p></div></div>
      <div class="info-card reveal"><span class="info-icon">🕒</span><div><h3>Opening hours</h3>
        {% for days, time in info.hours %}<p><strong>{{ days }}</strong><br>{{ time }}</p>{% endfor %}</div></div>
    </div>

    <form id="contactForm" class="form-card reveal" novalidate>
      <h2>Send us a message</h2>
      <p class="form-sub">Questions or table bookings? Fill in the form and we will reply soon.</p>
      <label for="name">Name</label>
      <input type="text" id="name" placeholder="Your name" autocomplete="name">
      <label for="email">Email</label>
      <input type="email" id="email" placeholder="you@example.com" autocomplete="email">
      <label for="message">Message</label>
      <textarea id="message" rows="5" placeholder="How can we help?"></textarea>
      <p class="form-msg" id="formMsg" role="status" aria-live="polite"></p>
      <button type="submit" class="btn">Send message</button>
    </form>
  </div>
</section>
{% endblock %}
````

### `static/css/style.css`
````css
/* ---------- Design tokens ---------- */
:root {
  --ink:#1d1613; --ember:#c8441c; --ember-dark:#a53515; --saffron:#f2a541;
  --cream:#fbf5ec; --sand:#f1e6d4; --muted:#6e625a; --white:#fff;
  --radius:20px; --shadow:0 14px 40px rgba(29,22,19,.12);
  --font-head:"Playfair Display",Georgia,serif;
  --font-body:"Inter","Segoe UI",system-ui,-apple-system,sans-serif;
}
* { box-sizing:border-box; margin:0; padding:0; }
html { scroll-behavior:smooth; }
body { font-family:var(--font-body); color:var(--ink); background:var(--cream); line-height:1.65; -webkit-font-smoothing:antialiased; }
img { max-width:100%; display:block; }
a { color:inherit; text-decoration:none; }
h1,h2,h3 { font-family:var(--font-head); line-height:1.15; }
h2 { font-size:clamp(1.8rem,3.4vw,2.6rem); }
.container { width:min(1140px,92%); margin-inline:auto; }
.narrow { width:min(760px,92%); }
.center { text-align:center; margin-top:40px; }
.hidden { display:none !important; }
.eyebrow { display:inline-block; font-size:.78rem; font-weight:600; letter-spacing:.14em; text-transform:uppercase; color:var(--ember); margin-bottom:14px; }

/* ---------- Buttons ---------- */
.btn { display:inline-block; padding:13px 28px; background:var(--ember); color:#fff; border:2px solid var(--ember); border-radius:999px;
  font:600 .95rem var(--font-body); cursor:pointer; transition:transform .2s, background .2s, box-shadow .2s; }
.btn:hover { background:var(--ember-dark); border-color:var(--ember-dark); transform:translateY(-2px); box-shadow:0 8px 20px rgba(200,68,28,.3); }
.btn-ghost { background:transparent; color:var(--ink); border-color:var(--ink); }
.btn-ghost:hover { background:var(--ink); border-color:var(--ink); color:#fff; box-shadow:none; }
.btn-outline { background:transparent; color:var(--ember); }
.btn-outline:hover { color:#fff; }
.btn-light { background:#fff; color:var(--ember); border-color:#fff; }
.btn-light:hover { background:var(--sand); border-color:var(--sand); box-shadow:none; }
.btn-small { padding:9px 20px; font-size:.88rem; }

/* ---------- Navbar ---------- */
.navbar { position:sticky; top:0; z-index:50; background:rgba(251,245,236,.88); backdrop-filter:blur(12px); transition:box-shadow .3s; }
.navbar.scrolled { box-shadow:0 4px 20px rgba(29,22,19,.1); }
.nav-inner { display:flex; align-items:center; justify-content:space-between; height:74px; }
.logo { display:flex; align-items:center; gap:10px; font:700 1.35rem var(--font-head); }
.nav-links { display:flex; align-items:center; gap:30px; }
.nav-links a:not(.btn) { position:relative; font-weight:500; font-size:.95rem; padding:6px 0; }
.nav-links a:not(.btn)::after { content:""; position:absolute; left:0; bottom:0; height:2px; width:0; background:var(--ember); transition:width .25s; }
.nav-links a:not(.btn):hover::after, .nav-links a.active::after { width:100%; }
.nav-links a.active { color:var(--ember); }
.nav-toggle { display:none; flex-direction:column; gap:5px; background:none; border:none; padding:8px; cursor:pointer; }
.nav-toggle span { width:26px; height:2.5px; background:var(--ink); border-radius:2px; transition:.3s; }
.nav-toggle[aria-expanded="true"] span:nth-child(1) { transform:translateY(7.5px) rotate(45deg); }
.nav-toggle[aria-expanded="true"] span:nth-child(2) { opacity:0; }
.nav-toggle[aria-expanded="true"] span:nth-child(3) { transform:translateY(-7.5px) rotate(-45deg); }

/* ---------- Hero ---------- */
.hero { padding:60px 0 80px; background:radial-gradient(circle at 85% 20%, #ffe3c2 0, transparent 45%), radial-gradient(circle at 5% 90%, #f7d9b7 0, transparent 40%), var(--cream); overflow:hidden; }
.hero-grid { display:grid; grid-template-columns:1.05fr 1fr; align-items:center; gap:40px; }
.hero h1 { font-size:clamp(2.5rem,5.4vw,4.3rem); margin-bottom:20px; }
.hero h1 em { color:var(--ember); font-style:italic; }
.lead { font-size:1.12rem; color:var(--muted); max-width:520px; margin-bottom:30px; }
.hero-actions { display:flex; flex-wrap:wrap; gap:14px; margin-bottom:38px; }
.hero-stats { display:flex; gap:36px; list-style:none; }
.hero-stats strong { display:block; font:700 1.6rem var(--font-head); }
.hero-stats span { font-size:.85rem; color:var(--muted); }
.hero-visual { position:relative; aspect-ratio:1; max-width:540px; margin-inline:auto; width:100%; }
.blob { position:absolute; inset:6%; background:linear-gradient(135deg,var(--saffron),var(--ember)); border-radius:46% 54% 50% 50% / 52% 46% 54% 48%; opacity:.9; animation:morph 12s ease-in-out infinite; }
.dish { position:absolute; filter:drop-shadow(0 18px 24px rgba(29,22,19,.28)); }
.dish-main { width:74%; left:13%; top:10%; animation:float 7s ease-in-out infinite; }
.dish-burger { width:46%; left:-4%; bottom:0; animation:float 6s ease-in-out -2s infinite; }
.dish-drink { width:36%; right:-2%; bottom:6%; animation:float 8s ease-in-out -4s infinite; }
@keyframes float { 50% { transform:translateY(-14px); } }
@keyframes morph { 50% { border-radius:54% 46% 44% 56% / 46% 54% 46% 54%; transform:rotate(6deg); } }

/* ---------- Marquee ---------- */
.marquee { background:var(--ink); color:var(--saffron); overflow:hidden; padding:16px 0; }
.marquee-track { display:flex; width:max-content; animation:scroll 28s linear infinite; }
.marquee-track span { font:italic 600 1.15rem var(--font-head); padding:0 34px; white-space:nowrap; }
.marquee-track span::after { content:"✦"; margin-left:68px; color:var(--ember); }
@keyframes scroll { to { transform:translateX(-50%); } }

/* ---------- Sections ---------- */
.section { padding:90px 0; }
.section-sand { background:var(--sand); }
.section-head { text-align:center; margin-bottom:50px; }
.page-hero { padding:70px 0 60px; text-align:center; background:radial-gradient(circle at 80% 0, #ffe3c2 0, transparent 50%), var(--sand); }
.page-hero h1 { font-size:clamp(2.2rem,4.8vw,3.6rem); }

/* ---------- Dish cards ---------- */
.cards { display:grid; grid-template-columns:repeat(auto-fill,minmax(290px,1fr)); gap:28px; }
.dish-card { background:#fff; border-radius:var(--radius); overflow:hidden; box-shadow:0 6px 24px rgba(29,22,19,.07); transition:transform .3s, box-shadow .3s; }
.dish-card:hover { transform:translateY(-8px); box-shadow:var(--shadow); }
.dish-img { position:relative; background:linear-gradient(160deg,#fff2de,#f7dcb8); padding:26px; }
.dish-img img { width:78%; margin-inline:auto; aspect-ratio:1; object-fit:contain; transition:transform .5s; }
.dish-card:hover .dish-img img { transform:scale(1.07) rotate(-3deg); }
.badge { position:absolute; top:16px; left:16px; background:var(--ink); color:var(--saffron); font-size:.72rem; font-weight:600; letter-spacing:.06em; padding:5px 12px; border-radius:999px; z-index:1; }
.dish-body { padding:22px 24px 26px; }
.dish-body h3 { font-size:1.3rem; display:flex; align-items:center; gap:10px; margin-bottom:8px; }
.dish-body p { color:var(--muted); font-size:.95rem; margin-bottom:16px; }
.price { font:700 1.3rem var(--font-head); color:var(--ember); }
.veg-dot { display:inline-block; width:15px; height:15px; border:2px solid; border-radius:3px; position:relative; flex-shrink:0; vertical-align:middle; }
.veg-dot::after { content:""; position:absolute; inset:2px; border-radius:50%; background:currentColor; }
.veg-dot.veg { color:#2e9e4a; } .veg-dot.nonveg { color:#c0392b; }

/* ---------- Features, quotes ---------- */
.features, .quotes { display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:28px; }
.feature { background:#fff; padding:34px 28px; border-radius:var(--radius); text-align:center; box-shadow:0 6px 24px rgba(29,22,19,.06); }
.feature-icon { width:68px; height:68px; margin:0 auto 18px; display:grid; place-items:center; font-size:2rem; background:var(--sand); border-radius:50%; }
.feature h3 { font-size:1.3rem; margin-bottom:8px; }
.feature p { color:var(--muted); }
.quote { background:#fff; border-radius:var(--radius); padding:30px; box-shadow:0 6px 24px rgba(29,22,19,.06); }
.quote blockquote { font:italic 600 1.15rem var(--font-head); margin-bottom:20px; }
.quote blockquote::before { content:"“"; display:block; font-size:3rem; line-height:.6; color:var(--ember); }
.quote figcaption { display:flex; align-items:center; gap:12px; font-weight:600; font-size:.92rem; }
.avatar { width:40px; height:40px; display:grid; place-items:center; border-radius:50%; background:var(--ember); color:#fff; font-size:.8rem; }

/* ---------- CTA ---------- */
.cta { background:linear-gradient(135deg,var(--ember),#e0642c); color:#fff; padding:70px 0; }
.cta-inner { display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:24px; }
.cta h2 { max-width:560px; }

/* ---------- About ---------- */
.two-col { display:grid; grid-template-columns:1fr 1fr; gap:60px; align-items:center; }
.two-col.top { align-items:start; }
.two-col h2 { margin-bottom:18px; }
.two-col p { color:var(--muted); margin-bottom:14px; }
.rounded { border-radius:var(--radius); box-shadow:var(--shadow); width:100%; }
.stats-band { background:var(--ink); color:#fff; padding:50px 0; }
.stats { display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); text-align:center; gap:24px; }
.stats strong { display:block; font:700 2.4rem var(--font-head); color:var(--saffron); }
.stats span { font-size:.9rem; opacity:.8; }
.timeline { list-style:none; border-left:3px solid var(--ember); padding-left:30px; }
.timeline li { position:relative; margin-bottom:30px; }
.timeline li::before { content:""; position:absolute; left:-40px; top:6px; width:16px; height:16px; background:var(--cream); border:3px solid var(--ember); border-radius:50%; }
.timeline strong { font:700 1.3rem var(--font-head); color:var(--ember); }
.timeline p { color:var(--muted); }

/* ---------- Menu toolbar ---------- */
.toolbar { display:flex; flex-wrap:wrap; gap:18px; align-items:center; justify-content:space-between; margin-bottom:16px; }
.filters { display:flex; flex-wrap:wrap; gap:10px; }
.filter-btn { padding:9px 22px; border:2px solid var(--ink); background:transparent; border-radius:999px; font:500 .92rem var(--font-body); cursor:pointer; transition:.2s; }
.filter-btn:hover, .filter-btn.active { background:var(--ink); color:#fff; }
.search { padding:11px 20px; border:2px solid #e2d6c3; border-radius:999px; font:inherit; min-width:240px; background:#fff; }
.search:focus { outline:none; border-color:var(--ember); }
.legend { display:flex; align-items:center; gap:8px; font-size:.85rem; color:var(--muted); margin-bottom:30px; }
.legend .veg-dot + .veg-dot, .legend .veg-dot:not(:first-child) { margin-left:14px; }
.empty { text-align:center; color:var(--muted); padding:40px 0; }
.menu-item { animation:pop .4s ease; }
@keyframes pop { from { opacity:0; transform:scale(.96); } }

/* ---------- Contact ---------- */
.info-stack { display:grid; gap:18px; }
.info-card { display:flex; gap:18px; background:#fff; padding:22px 24px; border-radius:var(--radius); box-shadow:0 6px 24px rgba(29,22,19,.06); }
.info-icon { width:50px; height:50px; flex-shrink:0; display:grid; place-items:center; font-size:1.4rem; background:var(--sand); border-radius:14px; }
.info-card h3 { font-size:1.1rem; margin-bottom:2px; }
.info-card p { color:var(--muted); margin:0 0 6px; }
.form-card { background:#fff; padding:36px; border-radius:var(--radius); box-shadow:var(--shadow); }
.form-card h2 { font-size:1.8rem; margin-bottom:6px; }
.form-sub { color:var(--muted); margin-bottom:10px !important; }
label { display:block; margin:16px 0 6px; font-weight:600; font-size:.9rem; }
input, textarea { width:100%; padding:13px 16px; border:2px solid #e8dccb; border-radius:12px; font:inherit; background:var(--cream); transition:border-color .2s; }
input:focus, textarea:focus { outline:none; border-color:var(--ember); background:#fff; }
.form-msg { min-height:26px; margin:14px 0; font-weight:600; }
.form-msg.error { color:#c0392b; } .form-msg.success { color:#2e9e4a; }

/* ---------- Footer ---------- */
.footer { background:var(--ink); color:#d8cfc6; padding:64px 0 0; }
.footer-grid { display:grid; grid-template-columns:1.4fr 1fr 1fr; gap:40px; padding-bottom:40px; }
.logo-light { color:#fff; margin-bottom:14px; }
.footer-text { max-width:300px; }
.footer h4 { color:#fff; font-family:var(--font-head); font-size:1.1rem; margin-bottom:14px; }
.footer-grid a, .footer-grid p { display:block; margin-bottom:8px; font-size:.95rem; }
.footer-grid a:not(.logo):hover { color:var(--saffron); }
.footer-bottom { border-top:1px solid rgba(255,255,255,.12); padding:22px 0; font-size:.85rem; text-align:center; }

/* ---------- Scroll reveal (only when JS is running) ---------- */
.js .reveal { opacity:0; transform:translateY(28px); transition:opacity .7s ease, transform .7s ease; }
.js .reveal.visible { opacity:1; transform:none; }

/* ---------- Responsive ---------- */
@media (max-width:900px) {
  .hero-grid, .two-col { grid-template-columns:1fr; }
  .hero { padding-top:40px; }
  .hero-visual { max-width:420px; }
  .footer-grid { grid-template-columns:1fr 1fr; }
  .section { padding:64px 0; }
}
@media (max-width:760px) {
  .nav-toggle { display:flex; }
  .nav-links { position:absolute; top:74px; left:0; right:0; flex-direction:column; align-items:flex-start; gap:0; background:var(--cream);
    padding:10px 4% 24px; box-shadow:0 14px 20px rgba(29,22,19,.1); display:none; }
  .nav-links.open { display:flex; }
  .nav-links a:not(.btn) { padding:14px 0; width:100%; border-bottom:1px solid #e8dccb; }
  .nav-cta { margin-top:16px; }
}
@media (max-width:520px) {
  .footer-grid { grid-template-columns:1fr; }
  .hero-stats { gap:22px; }
  .search { width:100%; }
  .form-card { padding:26px 22px; }
}
@media (prefers-reduced-motion:reduce) {
  *, *::before, *::after { animation:none !important; transition:none !important; }
  .js .reveal { opacity:1; transform:none; }
}
````

### `static/js/script.js`
````javascript
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
````

### `Dockerfile`
````dockerfile
# Small official Python image
FROM python:3.11-slim

# Folder inside the container where our code will live
WORKDIR /app

# Copy requirements first so Docker can cache the install step
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Turn off Flask debug mode inside the container
ENV FLASK_DEBUG=0

# Flask listens on port 5000
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
````

### `.dockerignore`
````
venv/
__pycache__/
.git/
.pytest_cache/
````

### `Jenkinsfile`
````groovy
// Declarative Jenkins pipeline for a WINDOWS Jenkins agent.
// (A Linux version is in Jenkinsfile.linux.)
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'restaurant-website'   // [DOCKER_IMAGE_NAME]
        // Full paths with forward slashes (backslashes break Groovy strings).
        // Change these two lines if Python or Docker are installed elsewhere.
        PYTHON = 'C:/Users/ASUS/AppData/Local/Programs/Python/Python314/python.exe'
        DOCKER = 'C:/Users/ASUS/AppData/Local/Programs/DockerDesktop/resources/bin/docker.exe'
    }

    stages {
        // Stage 1: get the latest code from GitHub
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Stage 2: create a virtual environment and install packages
        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" --version'
                bat '"%PYTHON%" -m venv venv'
                bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
            }
        }

        // Stage 3: run the automated tests; the pipeline fails if a test fails
        stage('Run pytest') {
            steps {
                bat 'venv\\Scripts\\python -m pytest'
            }
        }

        // Stage 4: build the Docker image, tagged with the Jenkins build number
        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER%" --version'
                bat '"%DOCKER%" build -t %IMAGE_NAME%:%BUILD_NUMBER% .'
            }
        }
    }

    post {
        success { echo 'Pipeline finished successfully.' }
        failure { echo 'Pipeline failed. Check the console output.' }
    }
}
````

### `Jenkinsfile.linux`
````groovy
// Declarative Jenkins pipeline for a LINUX Jenkins agent (or a Jenkins Docker container).
// To use it: rename this file to "Jenkinsfile". Needs python3, python3-venv and docker on the agent.
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'restaurant-website'   // [DOCKER_IMAGE_NAME]
    }

    stages {
        // Stage 1: get the latest code from GitHub
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Stage 2: create a virtual environment and install packages
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        // Stage 3: run the automated tests
        stage('Run pytest') {
            steps {
                sh '. venv/bin/activate && pytest'
            }
        }

        // Stage 4: build the Docker image
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
            }
        }
    }

    post {
        success { echo 'Pipeline finished successfully.' }
        failure { echo 'Pipeline failed. Check the console output.' }
    }
}
````

### `tests/test_app.py`
````python
import pytest
from app import app


@pytest.fixture
def client():
    """Create a Flask test client (a fake browser) for every test."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.parametrize("path", ["/about", "/menu", "/contact"])
def test_other_pages_return_200(client, path):
    assert client.get(path).status_code == 200


def test_menu_shows_items(client):
    assert b"Margherita Pizza" in client.get("/menu").data


def test_unknown_page_returns_404(client):
    assert client.get("/nope").status_code == 404


def test_menu_has_prices_in_rupees(client):
    assert "₹".encode("utf-8") in client.get("/menu").data


def test_home_has_hero_heading(client):
    assert b"Fresh food, cooked with" in client.get("/").data


def test_menu_images_exist():
    """Every image named in the menu list must exist in static/images."""
    import os
    from app import MENU
    for item in MENU:
        assert os.path.exists(os.path.join("static", "images", item["image"])), item["image"]
````

### `README.md`
````markdown
# Restaurant_Project_Repo

A modern, responsive restaurant website ("Tasty Corner") built with **Flask**, HTML, CSS and JavaScript.
No database, no login, no external services. Includes **pytest** tests, a **Dockerfile** and a **Jenkins** pipeline.

## Features
- Four pages: Home, About, Menu, Contact
- Hero section with illustrated dishes, scrolling highlights strip, testimonials and call-to-action
- Menu cards with illustrations, badges and vegetarian / non-vegetarian markers
- Menu category filter **and** live search
- Responsive navigation bar (animated hamburger menu on mobile)
- Contact form with client-side validation
- Scroll-reveal animations (disabled automatically for users who prefer reduced motion)
- Menu data stored in a plain Python list (no database)

## Technology Stack
Python 3.11+ · Flask · HTML (Jinja templates) · CSS · JavaScript · pytest · Git/GitHub · Docker · Jenkins

## Folder Structure
```
Restaurant_Project_Repo/
├── app.py               # Flask app, routes and menu data
├── conftest.py          # lets pytest import app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── Jenkinsfile          # pipeline for a Windows Jenkins agent
├── Jenkinsfile.linux    # same pipeline for Linux
├── README.md
├── PROJECT_GUIDE.md
├── .gitignore
├── templates/           # base.html, index.html, about.html, menu.html, contact.html
├── static/
│   ├── css/style.css
│   ├── js/script.js
│   └── images/          # SVG dish illustrations, storefront, favicon
├── screenshots/         # screenshots for this README
└── tests/test_app.py
```

## Installation and Local Run
```bash
git clone https://github.com/OnkarYadav007/Restaurant_Project_Repo.git
cd Restaurant_Project_Repo

# Windows
python -m venv venv
venv\Scripts\activate
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Using your own photos
Put a photo in `static/images/` (for example `margherita.jpg`) and change that dish's `"image"` value in the `MENU` list in `app.py`.

## Docker
```bash
docker build -t restaurant-website .
docker run -p 5000:5000 restaurant-website
```
Open http://127.0.0.1:5000. Stop with `Ctrl+C`.

## Testing
```bash
pytest
```
The tests use Flask's test client to check that every page returns HTTP 200, unknown URLs return 404, the menu shows prices and every menu image file exists.

## Jenkins (CI pipeline)
The `Jenkinsfile` has four stages: **Checkout → Install Dependencies → Run pytest → Build Docker Image**.

Setup used for this project (Jenkins installed on Windows):
1. Install Jenkins, Python, Git and Docker Desktop. Start Docker Desktop.
2. In Jenkins create a **Pipeline** job named `restaurant-pipeline`.
3. Set *Definition* to **Pipeline script from SCM**, *SCM* to **Git**, repository to
   `https://github.com/OnkarYadav007/Restaurant_Project_Repo.git`, branch `*/main`, script path `Jenkinsfile`.
4. Edit the `PYTHON` and `DOCKER` paths at the top of the `Jenkinsfile` to match your machine (use `/` not `\`).
5. If the Docker stage cannot connect, run the Jenkins Windows service under your own account
   (`services.msc` → Jenkins → Properties → Log On → *This account*) and restart it.
6. Click **Build Now**. A successful run ends with `Finished: SUCCESS` and creates the image `restaurant-website:<build number>`.

On a Linux Jenkins server, rename `Jenkinsfile.linux` to `Jenkinsfile`.

## Git Workflow
```bash
git checkout -b feature/my-change
git add .
git commit -m "Describe the change"
git push -u origin feature/my-change
# open a Pull Request on GitHub, review, then merge into main
```

## Screenshots
Add images to the `screenshots/` folder and link them here:

| Home | Menu | Jenkins pipeline | Docker |
|---|---|---|---|
| `screenshots/home.png` | `screenshots/menu.png` | `screenshots/jenkins.png` | `screenshots/docker.png` |

## Future Improvements
- Online table-booking form with email confirmation
- Real photo gallery
- Dark mode
- Deploy the Docker image to a cloud service

## Contributing
Fork the repo, create a feature branch, commit, push and open a Pull Request.

## License
MIT License (add a LICENSE file if you want to publish it).

## Author
Onkar Yadav

## Repository
https://github.com/OnkarYadav007/Restaurant_Project_Repo
````

## 4. RUN INSTRUCTIONS
**Create virtual environment**
Windows
```
python -m venv venv
venv\Scripts\activate
```
Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```
**Install packages:** `pip install -r requirements.txt`
**Run:** `python app.py`
**Open browser:** http://127.0.0.1:5000

## 5. GIT & GITHUB WORKFLOW
| Command | What it does |
|---|---|
| `git init` | Turns the folder into a Git repository |
| `git status` | Shows changed and untracked files |
| `git add .` | Stages all changes for the next commit |
| `git commit -m "message"` | Saves a snapshot with a message |
| `git branch -M main` | Renames the current branch to `main` |
| `git remote add origin https://github.com/OnkarYadav007/Restaurant_Project_Repo.git` | Links your folder to the GitHub repo |
| `git push -u origin main` | Uploads `main` to GitHub and remembers it as the default |
| `git checkout -b feature/navbar` | Creates and switches to a new branch for one feature |
| `git checkout main` then `git merge feature/navbar` | Brings the feature into `main` |
| `git push` | Uploads new commits |
| `git pull` | Downloads and merges new commits from GitHub |

**Pull Request process:** 1) push your feature branch; 2) on GitHub click "Compare & pull request"; 3) describe the change; 4) a teammate reviews; 5) click "Merge pull request"; 6) run `git checkout main && git pull` locally.

## 6. GIT COMMIT HISTORY (MANDATORY)
Run `./create_git_history.sh` (Git Bash on Windows) to create these commits automatically, then `git push -u origin main`.

| # | Title | Files | Why |
|---|---|---|---|
| 1 | Initial Flask project setup | `app.py`, `requirements.txt`, `.gitignore`, `conftest.py` | Start with the backend skeleton and routes |
| 2 | Create frontend pages | `templates/` (all 5 files) | Pages and navigation, using a shared base layout |
| 3 | Improve styling and responsiveness | `static/css/style.css`, `static/images/` | Make it look good on desktop and mobile |
| 4 | Add JavaScript interactions | `static/js/script.js` | Menu toggle, filter, form validation |
| 5 | Add pytest tests | `tests/` | Prove the pages work before adding DevOps |
| 6 | Add Docker, Jenkins pipeline and documentation | `Dockerfile`, `.dockerignore`, `Jenkinsfile`, `README.md`, `PROJECT_GUIDE.md`, `create_git_history.sh` | Package, automate and document |

The first six commits are created by the script. After that, the real project work continued:

| # | Title | Files | Why |
|---|---|---|---|
| 7 | Update Jenkinsfile for Windows agent | `Jenkinsfile` | Jenkins on Windows has no `sh`, so the pipeline uses `bat` |
| 8 | Fix Jenkinsfile paths and relax requirement versions | `Jenkinsfile`, `requirements.txt` | Use full Python and Docker paths; support newer Python |
| 9 | Redesign UI with illustrations and animations | `templates/`, `static/`, `app.py`, `tests/` | Modern layout, new images, menu search |
| 10 | Update documentation and add Linux Jenkinsfile | `README.md`, `PROJECT_GUIDE.md`, `Jenkinsfile.linux`, `screenshots/` | Docs match the real setup |

Each commit message has a short title plus a one-line description (see the script).

## 7. DOCKERFILE
See the Dockerfile in section 3. It uses `python:3.11-slim`, sets `WORKDIR /app`, copies and installs requirements first (faster rebuilds), copies the code, exposes port 5000 and runs `python app.py`.
- `docker build -t restaurant-website .` builds an image named `restaurant-website` from the Dockerfile in the current folder.
- `docker run -p 5000:5000 restaurant-website` starts a container and maps your port 5000 to the container's port 5000. Open http://127.0.0.1:5000.

## 8. JENKINSFILE
See section 3 (`Jenkinsfile` for Windows, `Jenkinsfile.linux` for Linux). Stages: **Checkout** (get code from GitHub), **Install Dependencies** (venv + pip), **Run pytest** (fails the build if tests fail), **Build Docker Image** (tagged with the build number). Jenkins needs Python 3, Git and Docker on its agent.
**Windows setup used in this project:** install Jenkins, Python and Docker Desktop; create a Pipeline job from SCM pointing at the GitHub repo (branch `*/main`, script path `Jenkinsfile`); put the full paths of `python.exe` and `docker.exe` (with `/` slashes) at the top of the Jenkinsfile; if Docker cannot connect, run the Jenkins service under your own Windows account. Windows uses `bat` steps; Linux uses `sh`.

## 9. PYTEST SETUP
`tests/test_app.py` uses Flask's **test client**, a fake browser that calls routes without starting a server. It includes the required Home page HTTP 200 test, plus tests for the other pages, menu content and a 404.
Run from the project root with the venv active: `pytest`. Expected: `9 passed`.

## 10. README.md
The full README is in section 3 and uses the repo URL and image name.

## 11. TECHNOLOGY EXPLANATION
- **Flask:** a small Python web framework. You map a URL (like `/menu`) to a Python function, and the function returns a page.
- **HTML:** the structure of a web page: headings, paragraphs, images, forms.
- **CSS:** the styling: colours, fonts, spacing and layout. Media queries make the page adapt to phones.
- **JavaScript:** the behaviour in the browser, such as opening the mobile menu or checking a form without reloading.
- **pytest:** a Python testing tool. You write small functions with `assert` statements; pytest runs them and reports pass or fail.
- **Git:** a version control system that records snapshots (commits) of your code so you can see history, undo mistakes and work in branches.
- **GitHub:** a website that hosts Git repositories online for backup, sharing, collaboration and Pull Requests.
- **Docker:** packages the app with Python and its libraries into an image that runs the same on any machine ("works on my machine" problem solved).
- **Jenkins:** an automation server. On every change it can fetch the code, run tests and build the Docker image, which is called Continuous Integration.

## 12. PRESENTATION NOTES (about 4 minutes)
**Overview (30s):** "Our project is a restaurant website called Tasty Corner. It has four pages and is built with Flask. We also added tests, Docker and a Jenkins pipeline to show a complete development workflow."
**Folder structure (30s):** "`app.py` is the backend. `templates` holds HTML pages, `static` holds CSS, JavaScript and images, and `tests` holds our automated tests."
**Flask routing (30s):** "Each route is a Python function. For example `/menu` calls `menu()`, which sends our menu list to `menu.html`. There is no database; the menu is a Python list."
**HTML templates (30s):** "We use Jinja templates. `base.html` has the navbar and footer once, and every page extends it. A loop creates the menu cards."
**CSS (20s):** "CSS gives the colours and card layout. A media query changes the layout for screens under 768 pixels, so it is responsive."
**JavaScript (20s):** "JavaScript opens the mobile menu, filters menu categories and validates the contact form."
**Git and GitHub (30s):** "We built the project in six commits, from setup to Docker, and pushed to GitHub. Branches and Pull Requests are how teams review changes."
**Docker (25s):** "The Dockerfile packages the app. `docker build` makes the image and `docker run` starts it on port 5000."
**Jenkins (25s):** "The Jenkinsfile has four stages: checkout, install, test and build image. If a test fails the pipeline stops."
**pytest (20s):** "pytest uses Flask's test client to check that every page returns status 200."
**Closing (10s):** "This project shows the full path from code to a tested, containerised application. Thank you."

## 13. FINAL CHECKLIST
✓ Python Flask backend ✓ HTML ✓ CSS ✓ JavaScript ✓ Responsive design ✓ Flask routing ✓ No database ✓ pytest ✓ Dockerfile ✓ Jenkinsfile ✓ README ✓ Git workflow ✓ GitHub workflow ✓ Six meaningful Git commits ✓ Folder structure ✓ Complete source code ✓ Local run instructions ✓ Docker commands ✓ Beginner-friendly explanations

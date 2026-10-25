# Restaurant Website: Flask + Docker + Jenkins + pytest + Git

Repository: https://github.com/OnkarYadav007/Restaurant_Project_Repo.git
Placeholders used: `[PROJECT_NAME]` = Restaurant_Project_Repo, `[GITHUB_REPO_URL]` = the URL above, `[DOCKER_IMAGE_NAME]` = restaurant-website.

## 1. PROJECT OVERVIEW
**Purpose:** a simple restaurant website ("Tasty Corner") with Home, About, Menu and Contact pages, served by Flask.
**Technologies:** Python, Flask, HTML, CSS, JavaScript, pytest, Git, GitHub, Docker, Jenkins.
**Features:** responsive navbar, hero section, menu cards with category filter, contact info and a validated form, footer, no database or login.
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
│   └── images/
│       ├── restaurant.svg
│       ├── pizza.svg
│       └── burger.svg
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
| `Jenkinsfile` | CI pipeline: checkout, install, test, build image |
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
| `static/images/*.svg` | Illustrations (SVG, so no image downloads needed) |
| `tests/test_app.py` | Automated tests |

## 3. COMPLETE SOURCE CODE
### `app.py`
````python
"""Restaurant website - a simple Flask app (no database, no login)."""
import os
from flask import Flask, render_template

app = Flask(__name__)

# Menu data lives in a plain Python list. No database is needed.
MENU = [
    {"name": "Margherita Pizza", "category": "pizza", "price": 9.99, "icon": "🍕",
     "desc": "Tomato, fresh mozzarella and basil on a thin crust."},
    {"name": "Pepperoni Pizza", "category": "pizza", "price": 11.49, "icon": "🍕",
     "desc": "Spicy pepperoni with melted cheese."},
    {"name": "Classic Burger", "category": "burger", "price": 8.99, "icon": "🍔",
     "desc": "Beef patty, lettuce, tomato and house sauce."},
    {"name": "Veggie Burger", "category": "burger", "price": 8.49, "icon": "🍔",
     "desc": "Crispy veggie patty with avocado and mayo."},
    {"name": "Fresh Lemonade", "category": "drinks", "price": 3.49, "icon": "🍋",
     "desc": "Squeezed daily, served over ice."},
    {"name": "Chocolate Brownie", "category": "dessert", "price": 4.99, "icon": "🍫",
     "desc": "Warm brownie with a scoop of vanilla ice cream."},
]

CONTACT = {
    "address": "123 Food Street, Pune, India",
    "phone": "+91 98765 43210",
    "email": "hello@restaurant.example",
    "hours": "Mon-Sun: 11:00 AM - 11:00 PM",
}


@app.route("/")
def home():
    return render_template("index.html", active="home", featured=MENU[:3])


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
Flask==3.0.3
pytest==8.2.2
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
  <title>{% block title %}Home{% endblock %} | Tasty Corner</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
  <header class="navbar" id="navbar">
    <a class="logo" href="{{ url_for('home') }}">🍽️ Tasty Corner</a>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle menu">☰</button>
    <nav class="nav-links" id="navLinks">
      <a href="{{ url_for('home') }}" class="{{ 'active' if active == 'home' }}">Home</a>
      <a href="{{ url_for('about') }}" class="{{ 'active' if active == 'about' }}">About</a>
      <a href="{{ url_for('menu') }}" class="{{ 'active' if active == 'menu' }}">Menu</a>
      <a href="{{ url_for('contact') }}" class="{{ 'active' if active == 'contact' }}">Contact</a>
    </nav>
  </header>

  <main>{% block content %}{% endblock %}</main>

  <footer class="footer">
    <p>© <span id="year">2025</span> Tasty Corner. All rights reserved.</p>
    <p>123 Food Street, Pune · +91 98765 43210</p>
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
  <div class="hero-text">
    <h1>Fresh Food, Made With Love</h1>
    <p>Pizzas, burgers and desserts served hot in a warm, friendly place.</p>
    <a class="btn" href="{{ url_for('menu') }}">View Menu</a>
  </div>
  <img src="{{ url_for('static', filename='images/restaurant.svg') }}" alt="Restaurant illustration">
</section>

<section class="section">
  <h2>Our Favourites</h2>
  <div class="cards">
    {% for item in featured %}
    <article class="card">
      <div class="card-icon">{{ item.icon }}</div>
      <h3>{{ item.name }}</h3>
      <p>{{ item.desc }}</p>
      <span class="price">${{ "%.2f"|format(item.price) }}</span>
    </article>
    {% endfor %}
  </div>
</section>

<section class="section about-preview">
  <h2>About Us</h2>
  <p>We are a family-run restaurant serving fresh meals since 2015.</p>
  <a class="btn btn-outline" href="{{ url_for('about') }}">Read our story</a>
</section>
{% endblock %}
````

### `templates/about.html`
````html
{% extends "base.html" %}
{% block title %}About{% endblock %}
{% block content %}
<section class="section page-title"><h1>About Us</h1></section>
<section class="section two-col">
  <img src="{{ url_for('static', filename='images/pizza.svg') }}" alt="Pizza illustration">
  <div>
    <h2>Our Story</h2>
    <p>Tasty Corner started in 2015 as a small family kitchen. Today we serve hundreds of happy guests every week.</p>
    <p>We use fresh, local ingredients and cook every dish to order. Good food should be simple, honest and tasty.</p>
    <ul class="values">
      <li>🌿 Fresh ingredients</li>
      <li>👨‍🍳 Experienced chefs</li>
      <li>💛 Friendly service</li>
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
<section class="section page-title"><h1>Our Menu</h1></section>
<section class="section">
  <div class="filters" id="filters">
    <button class="filter-btn active" data-filter="all">All</button>
    <button class="filter-btn" data-filter="pizza">Pizza</button>
    <button class="filter-btn" data-filter="burger">Burgers</button>
    <button class="filter-btn" data-filter="drinks">Drinks</button>
    <button class="filter-btn" data-filter="dessert">Desserts</button>
  </div>
  <div class="cards">
    {% for item in items %}
    <article class="card menu-item" data-category="{{ item.category }}">
      <div class="card-icon">{{ item.icon }}</div>
      <h3>{{ item.name }}</h3>
      <p>{{ item.desc }}</p>
      <span class="price">${{ "%.2f"|format(item.price) }}</span>
    </article>
    {% endfor %}
  </div>
</section>
{% endblock %}
````

### `templates/contact.html`
````html
{% extends "base.html" %}
{% block title %}Contact{% endblock %}
{% block content %}
<section class="section page-title"><h1>Contact Us</h1></section>
<section class="section two-col">
  <div class="info">
    <h2>Visit Us</h2>
    <p>📍 {{ info.address }}</p>
    <p>📞 {{ info.phone }}</p>
    <p>✉️ {{ info.email }}</p>
    <p>🕒 {{ info.hours }}</p>
  </div>
  <form id="contactForm" novalidate>
    <h2>Send a Message</h2>
    <label for="name">Name</label>
    <input type="text" id="name" placeholder="Your name">
    <label for="email">Email</label>
    <input type="email" id="email" placeholder="you@example.com">
    <label for="message">Message</label>
    <textarea id="message" rows="4" placeholder="How can we help?"></textarea>
    <p class="form-msg" id="formMsg"></p>
    <button type="submit" class="btn">Send</button>
  </form>
</section>
{% endblock %}
````

### `static/css/style.css`
````css
:root { --primary:#d9480f; --dark:#2b2b2b; --light:#fff8f0; --gray:#666; }
* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:"Segoe UI",Arial,sans-serif; color:var(--dark); background:var(--light); line-height:1.6; }
a { text-decoration:none; color:inherit; }
img { max-width:100%; }

/* Navbar */
.navbar { position:sticky; top:0; z-index:10; display:flex; justify-content:space-between; align-items:center;
  padding:14px 6%; background:#fff; transition:box-shadow .3s; }
.navbar.scrolled { box-shadow:0 2px 10px rgba(0,0,0,.15); }
.logo { font-size:1.4rem; font-weight:700; color:var(--primary); }
.nav-links a { margin-left:24px; font-weight:500; padding-bottom:4px; }
.nav-links a:hover, .nav-links a.active { color:var(--primary); border-bottom:2px solid var(--primary); }
.nav-toggle { display:none; background:none; border:none; font-size:1.8rem; cursor:pointer; }

/* Buttons */
.btn { display:inline-block; padding:12px 28px; background:var(--primary); color:#fff; border:2px solid var(--primary);
  border-radius:30px; font-size:1rem; cursor:pointer; transition:.2s; }
.btn:hover { background:#b53a09; }
.btn-outline { background:transparent; color:var(--primary); }
.btn-outline:hover { background:var(--primary); color:#fff; }

/* Hero */
.hero { display:flex; align-items:center; justify-content:space-between; gap:30px; padding:60px 6%;
  background:linear-gradient(135deg,#ffe8d6,#fff8f0); }
.hero-text { flex:1; }
.hero h1 { font-size:2.8rem; line-height:1.2; margin-bottom:14px; }
.hero p { margin-bottom:24px; color:var(--gray); }
.hero img { flex:1; max-width:450px; }

/* Sections and cards */
.section { padding:50px 6%; text-align:center; }
.section h2 { margin-bottom:24px; font-size:2rem; }
.page-title { padding-bottom:10px; background:#ffe8d6; }
.cards { display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:24px; }
.card { background:#fff; padding:26px; border-radius:14px; box-shadow:0 4px 14px rgba(0,0,0,.08); transition:transform .2s; }
.card:hover { transform:translateY(-6px); }
.card-icon { font-size:3rem; }
.card h3 { margin:10px 0 6px; }
.card p { color:var(--gray); margin-bottom:10px; }
.price { font-weight:700; color:var(--primary); font-size:1.1rem; }
.hidden { display:none; }

/* Filters */
.filters { margin-bottom:28px; display:flex; flex-wrap:wrap; justify-content:center; gap:10px; }
.filter-btn { padding:8px 20px; border:2px solid var(--primary); background:#fff; color:var(--primary);
  border-radius:20px; cursor:pointer; font-size:.95rem; }
.filter-btn.active, .filter-btn:hover { background:var(--primary); color:#fff; }

/* Two column layout */
.two-col { display:grid; grid-template-columns:1fr 1fr; gap:40px; text-align:left; align-items:center; }
.two-col p { margin-bottom:12px; }
.values { list-style:none; margin-top:10px; }
.values li { margin-bottom:6px; }

/* Form */
form { background:#fff; padding:28px; border-radius:14px; box-shadow:0 4px 14px rgba(0,0,0,.08); }
label { display:block; margin:12px 0 4px; font-weight:600; }
input, textarea { width:100%; padding:10px; border:1px solid #ccc; border-radius:8px; font:inherit; }
input:focus, textarea:focus { outline:2px solid var(--primary); }
.form-msg { margin:12px 0; min-height:24px; font-weight:600; }
.form-msg.error { color:#c92a2a; }
.form-msg.success { color:#2b8a3e; }

/* Footer */
.footer { background:var(--dark); color:#ddd; text-align:center; padding:24px 6%; font-size:.9rem; }

/* Responsive */
@media (max-width:768px) {
  .nav-toggle { display:block; }
  .nav-links { display:none; position:absolute; top:100%; left:0; right:0; background:#fff;
    flex-direction:column; padding:10px 6%; box-shadow:0 6px 10px rgba(0,0,0,.1); }
  .nav-links.open { display:flex; }
  .nav-links a { margin:10px 0; }
  .hero { flex-direction:column; text-align:center; padding:40px 6%; }
  .hero h1 { font-size:2.1rem; }
  .two-col { grid-template-columns:1fr; }
}
````

### `static/js/script.js`
````javascript
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
````

### `static/images/restaurant.svg`
````xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300"><rect width="400" height="300" rx="20" fill="#ffd8b5"/><rect x="40" y="120" width="320" height="140" fill="#fff"/><polygon points="30,120 200,40 370,120" fill="#d9480f"/><rect x="170" y="180" width="60" height="80" fill="#8d5524"/><rect x="70" y="150" width="70" height="55" fill="#ffe066"/><rect x="260" y="150" width="70" height="55" fill="#ffe066"/><text x="200" y="110" font-size="28" text-anchor="middle" fill="#fff" font-family="Arial" font-weight="bold">TASTY CORNER</text></svg>
````

### `static/images/pizza.svg`
````xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300"><rect width="400" height="300" rx="20" fill="#ffe8d6"/><circle cx="200" cy="150" r="110" fill="#e8a33d"/><circle cx="200" cy="150" r="92" fill="#e03131"/><circle cx="200" cy="150" r="82" fill="#ffd43b"/><circle cx="160" cy="120" r="14" fill="#c92a2a"/><circle cx="230" cy="130" r="14" fill="#c92a2a"/><circle cx="190" cy="185" r="14" fill="#c92a2a"/><circle cx="240" cy="190" r="12" fill="#c92a2a"/></svg>
````

### `static/images/burger.svg`
````xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300"><rect width="400" height="300" rx="20" fill="#fff3bf"/><path d="M90 140a110 70 0 0 1 220 0z" fill="#e8a33d"/><rect x="80" y="145" width="240" height="22" rx="11" fill="#51cf66"/><rect x="85" y="167" width="230" height="35" rx="14" fill="#6d3b1f"/><rect x="80" y="202" width="240" height="18" rx="9" fill="#ffd43b"/><path d="M90 225h220a30 30 0 0 1-30 30H120a30 30 0 0 1-30-30z" fill="#e8a33d"/></svg>
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
// Declarative Jenkins pipeline (runs on a Linux Jenkins agent with Python 3 and Docker installed)
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'restaurant-website'   // [DOCKER_IMAGE_NAME]
    }

    stages {
        // Stage 1: download the latest code from GitHub
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/OnkarYadav007/Restaurant_Project_Repo.git'
            }
        }

        // Stage 2: create a virtual environment and install packages
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        // Stage 3: run the automated tests; the pipeline fails if a test fails
        stage('Run pytest') {
            steps {
                sh '. venv/bin/activate && pytest'
            }
        }

        // Stage 4: build the Docker image (tagged with the Jenkins build number)
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
````

### `README.md`
````markdown
# Restaurant_Project_Repo

A simple, beginner-friendly restaurant website built with **Flask**, HTML, CSS and JavaScript.
No database, no login, no external services. Includes **pytest** tests, a **Dockerfile** and a **Jenkinsfile**.

## Features
- Four pages: Home, About, Menu, Contact
- Responsive navigation bar (hamburger menu on mobile)
- Hero section, menu cards, contact info, footer
- JavaScript: menu filter, contact form validation, navbar shadow, auto year
- Menu data stored in a plain Python list (no database)

## Technology Stack
Python 3.11 · Flask · HTML · CSS · JavaScript · pytest · Git/GitHub · Docker · Jenkins

## Folder Structure
```
Restaurant_Project_Repo/
├── app.py            # Flask app and routes
├── conftest.py       # lets pytest import app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── Jenkinsfile
├── README.md
├── PROJECT_GUIDE.md
├── .gitignore
├── templates/        # base.html, index.html, about.html, menu.html, contact.html
├── static/           # css/style.css, js/script.js, images/*.svg
└── tests/            # test_app.py
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

## Docker
```bash
docker build -t restaurant-website .
docker run -p 5000:5000 restaurant-website
```

## Testing
```bash
pytest
```

## Git Workflow
```bash
git checkout -b feature/my-change
git add .
git commit -m "Describe the change"
git push -u origin feature/my-change
# open a Pull Request on GitHub, review, then merge into main
```

## Screenshots
_Add screenshots here (Home, Menu, Contact, mobile view)._

## Future Improvements
- Online table-booking form
- Image gallery
- Dark mode
- More menu categories

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

Each commit message has a short title plus a one-line description (see the script).

## 7. DOCKERFILE
See the Dockerfile in section 3. It uses `python:3.11-slim`, sets `WORKDIR /app`, copies and installs requirements first (faster rebuilds), copies the code, exposes port 5000 and runs `python app.py`.
- `docker build -t restaurant-website .` builds an image named `restaurant-website` from the Dockerfile in the current folder.
- `docker run -p 5000:5000 restaurant-website` starts a container and maps your port 5000 to the container's port 5000. Open http://127.0.0.1:5000.

## 8. JENKINSFILE
See section 3. Stages: **Checkout** (get code from GitHub), **Install Dependencies** (venv + pip), **Run pytest** (fails the build if tests fail), **Build Docker Image** (tagged with the build number). Jenkins needs Python 3, Git and Docker on its agent.

## 9. PYTEST SETUP
`tests/test_app.py` uses Flask's **test client**, a fake browser that calls routes without starting a server. It includes the required Home page HTTP 200 test, plus tests for the other pages, menu content and a 404.
Run from the project root with the venv active: `pytest`. Expected: `6 passed`.

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

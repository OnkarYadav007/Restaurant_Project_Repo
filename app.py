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

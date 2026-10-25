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

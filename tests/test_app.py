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

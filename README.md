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

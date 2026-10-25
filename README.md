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
<img width="1600" height="777" alt="Menu Page" src="https://github.com/user-attachments/assets/bafa16be-da68-41d9-a69c-02851e64eab5" />
<img width="1600" height="820" alt="Jenkins Proof" src="https://github.com/user-attachments/assets/f956c177-29b5-45f6-9660-101004b6c65b" />
<img width="1600" height="765" alt="Home page 4" src="https://github.com/user-attachments/assets/281cb660-28b8-4d57-997d-5edd76d56fe5" />
<img width="1600" height="772" alt="Home page 3" src="https://github.com/user-attachments/assets/c5345046-fab8-4aaa-b419-a3c6ede79493" />
<img width="1600" height="769" alt="Home page 2" src="https://github.com/user-attachments/assets/a603c99f-01d2-4a45-bd3a-c7a1e0b7eb71" />
<img width="1600" height="807" alt="Home page 1" src="https://github.com/user-attachments/assets/72a207ee-071c-4713-aeb7-000553393850" />
<img width="1600" height="857" alt="Docker Image Proof" src="https://github.com/user-attachments/assets/c127c80a-dbf9-4f50-8d8e-a09c2d6cb226" />
<img width="1600" height="852" alt="Docker Container Proof" src="https://github.com/user-attachments/assets/d8d0b5ba-ac6b-44bd-96c7-808a992c56e1" />
<img width="1600" height="809" alt="Contact Page" src="https://github.com/user-attachments/assets/e404f090-d2f7-4809-a5d4-753f7f6b3d2d" />
<img width="1600" height="772" alt="About page 2" src="https://github.com/user-attachments/assets/7c228bde-7ae5-48cc-b464-1aeabc072a05" />
<img width="1600" height="768" alt="About page 1" src="https://github.com/user-attachments/assets/3abe9e47-f77c-4c1c-8bdc-64df1df0dbe2" />

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

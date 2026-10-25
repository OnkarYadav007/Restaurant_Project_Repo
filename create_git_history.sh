#!/usr/bin/env bash
# Builds a realistic 6-commit history from the finished files.
# Run once, from the project folder, on a folder that is NOT yet a git repo.
set -e
git init -b main
git add app.py requirements.txt .gitignore conftest.py
git commit -m "Initial Flask project setup" -m "Add app.py with Home, About, Menu and Contact routes, requirements.txt and .gitignore."
git add templates/
git commit -m "Create frontend pages" -m "Add base layout with navigation and the Home, About, Menu and Contact templates."
git add static/css static/images
git commit -m "Improve styling and responsiveness" -m "Add CSS (hero, cards, footer, mobile layout) and SVG images."
git add static/js
git commit -m "Add JavaScript interactions" -m "Add mobile menu toggle, menu filter, contact form validation and navbar shadow."
git add tests/
git commit -m "Add pytest tests" -m "Test that all pages return 200 and unknown URLs return 404."
git add Dockerfile .dockerignore Jenkinsfile README.md PROJECT_GUIDE.md create_git_history.sh
git commit -m "Add Docker, Jenkins pipeline and documentation" -m "Add Dockerfile, Jenkinsfile, README and project guide. Final cleanup."
git remote add origin https://github.com/OnkarYadav007/Restaurant_Project_Repo.git
git log --oneline
echo "Now run: git push -u origin main"

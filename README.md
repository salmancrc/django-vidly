# 🎬 Vidly

> **Vidly** is a clean and modern Django project for managing a movie rental service. It features a simple admin interface for handling movies and genres, making it ideal for learning Django or as a starter for your own apps.

---

✨ Features

- 🎥 Manage movies and genres
- �️ Easy-to-use Django admin
- 💾 SQLite for quick setup
- 🧩 Modular, beginner-friendly codebase

---

🚀 Quick Start

1. <img alt="Clone" width="20" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"/> **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/vidly.git
   cd vidly
   ```
2. <img alt="Install" width="20" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pipenv/pipenv-original.svg"/> **Install dependencies:**
   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
   # or use your preferred virtual environment
   ```
3. <img alt="Django" width="20" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg"/> **Run migrations and start the server:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```
4. <img alt="Admin" width="20" src="https://cdn-icons-png.flaticon.com/512/1828/1828490.png"/> **Access the admin:** [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

📁 Project Structure

```
vidly/
├── movies/           # App for movies and genres
├── vidly/            # Project settings
├── manage.py         # Django management script
├── Pipfile           # Pipenv dependency file

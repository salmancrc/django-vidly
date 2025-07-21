# Vidly

Vidly is a sample Django project for managing a movie rental service. It demonstrates Django best practices, including models, admin customization, and database management. This project is ideal for learning Django or as a starting point for your own movie-related applications.

## Features

- Manage movies and genres
- Django admin interface for easy data entry
- SQLite database for quick setup
- Clean project structure

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- (Recommended) Virtual environment tool (venv, virtualenv, or pipenv)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/vidly.git
   cd vidly
   ```
2. Install dependencies:
   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
   ```
   Or, if using venv:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Access the admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Project Structure

```
vidly/
├── movies/           # App for movies and genres
├── vidly/            # Project settings
├── manage.py         # Django management script
├── db.sqlite3        # SQLite database (excluded from repo)
├── Pipfile           # Pipenv dependency file
└── .gitignore        # Git ignore rules
```

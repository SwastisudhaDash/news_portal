# NewsHub - Django News Portal

A beginner-friendly but portfolio-ready news portal built with Django.

## Features
- Responsive news homepage
- Categories
- Featured and breaking news
- Article detail pages
- Search
- View counter
- Comments
- Django Admin content management
- Image uploads
- SQLite database for easy setup

## Setup

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

Install:
```bash
pip install -r requirements.txt
```

Run migrations:
```bash
python manage.py migrate
```

Create admin:
```bash
python manage.py createsuperuser
```

Start server:
```bash
python manage.py runserver
```

Open:
http://127.0.0.1:8000/

Admin:
http://127.0.0.1:8000/admin/

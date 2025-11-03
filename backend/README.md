# Backend - Django API

This directory contains the Django backend application for the Chris-TCM e-commerce platform.

## Structure

```
backend/
├── config/              # Django project settings
│   ├── __init__.py
│   ├── settings.py     # Main settings file
│   ├── urls.py         # URL routing
│   ├── wsgi.py         # WSGI configuration
│   └── asgi.py         # ASGI configuration
├── apps/               # Django applications
│   ├── products/       # Product management
│   ├── users/          # User authentication and profiles
│   ├── orders/         # Order processing
│   └── cart/           # Shopping cart
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file with your configuration:
```bash
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

## Apps

### Products
Manages product catalog, categories, and inventory.

### Users
Handles user authentication, profiles, and permissions.

### Orders
Processes orders, payments, and order history.

### Cart
Manages shopping cart functionality.

## API Endpoints

The API will be available at `http://localhost:8000/api/`

Main endpoints:
- `/api/products/` - Product listings
- `/api/users/` - User management
- `/api/orders/` - Order processing
- `/api/cart/` - Shopping cart

Documentation available at:
- `/api/docs/` - Swagger UI
- `/api/redoc/` - ReDoc

## Testing

Run tests with:
```bash
python manage.py test
```

Or with pytest:
```bash
pytest
```

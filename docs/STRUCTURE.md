# Project Structure

This document describes the structure of the Chris-TCM project.

## Root Directory

```
Chris-TCM/
├── backend/              # Django backend application
├── frontend/             # Angular frontend application
├── docs/                 # Project documentation
├── .gitignore           # Git ignore rules
├── docker-compose.yml   # Docker configuration
├── CONTRIBUTING.md      # Contributing guidelines
├── LICENSE              # Project license
└── README.md            # Project overview
```

## Backend Structure

```
backend/
├── config/              # Django project configuration
│   ├── __init__.py
│   ├── settings.py     # Settings configuration
│   ├── urls.py         # Main URL routing
│   ├── wsgi.py         # WSGI configuration
│   └── asgi.py         # ASGI configuration
├── apps/               # Django applications
│   ├── __init__.py
│   ├── products/       # Product management
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── models.py   # Product models
│   │   ├── views.py    # API views
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── tests.py
│   ├── users/          # User management
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── models.py   # User models
│   │   ├── views.py    # Authentication views
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── tests.py
│   ├── orders/         # Order processing
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── models.py   # Order models
│   │   ├── views.py    # Order views
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── tests.py
│   └── cart/           # Shopping cart
│       ├── migrations/
│       ├── __init__.py
│       ├── models.py   # Cart models
│       ├── views.py    # Cart views
│       ├── serializers.py
│       ├── urls.py
│       └── tests.py
├── media/              # User uploaded files
├── staticfiles/        # Collected static files
├── venv/               # Virtual environment (not committed)
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md           # Backend documentation
```

## Frontend Structure

```
frontend/
├── src/
│   ├── app/
│   │   ├── core/              # Core module
│   │   │   ├── services/      # Global services
│   │   │   │   ├── auth.service.ts
│   │   │   │   ├── api.service.ts
│   │   │   │   └── storage.service.ts
│   │   │   ├── guards/        # Route guards
│   │   │   │   ├── auth.guard.ts
│   │   │   │   └── role.guard.ts
│   │   │   ├── interceptors/  # HTTP interceptors
│   │   │   │   ├── auth.interceptor.ts
│   │   │   │   └── error.interceptor.ts
│   │   │   └── models/        # Data models/interfaces
│   │   │       ├── user.model.ts
│   │   │       ├── product.model.ts
│   │   │       └── order.model.ts
│   │   ├── shared/            # Shared module
│   │   │   ├── components/    # Reusable components
│   │   │   │   ├── header/
│   │   │   │   ├── footer/
│   │   │   │   └── loading-spinner/
│   │   │   ├── directives/    # Custom directives
│   │   │   └── pipes/         # Custom pipes
│   │   ├── features/          # Feature modules
│   │   │   ├── products/      # Product feature
│   │   │   │   ├── components/
│   │   │   │   │   ├── product-list/
│   │   │   │   │   ├── product-detail/
│   │   │   │   │   └── product-card/
│   │   │   │   ├── services/
│   │   │   │   │   └── product.service.ts
│   │   │   │   ├── products-routing.module.ts
│   │   │   │   └── products.module.ts
│   │   │   ├── cart/          # Shopping cart feature
│   │   │   │   ├── components/
│   │   │   │   │   ├── cart-view/
│   │   │   │   │   └── cart-item/
│   │   │   │   ├── services/
│   │   │   │   │   └── cart.service.ts
│   │   │   │   ├── cart-routing.module.ts
│   │   │   │   └── cart.module.ts
│   │   │   ├── orders/        # Orders feature
│   │   │   │   ├── components/
│   │   │   │   │   ├── order-list/
│   │   │   │   │   ├── order-detail/
│   │   │   │   │   └── checkout/
│   │   │   │   ├── services/
│   │   │   │   │   └── order.service.ts
│   │   │   │   ├── orders-routing.module.ts
│   │   │   │   └── orders.module.ts
│   │   │   └── auth/          # Authentication feature
│   │   │       ├── components/
│   │   │       │   ├── login/
│   │   │       │   ├── register/
│   │   │       │   └── profile/
│   │   │       ├── auth-routing.module.ts
│   │   │       └── auth.module.ts
│   │   ├── app-routing.module.ts
│   │   ├── app.component.ts
│   │   ├── app.component.html
│   │   ├── app.component.scss
│   │   └── app.module.ts
│   ├── assets/            # Static assets
│   │   ├── images/
│   │   ├── fonts/
│   │   └── icons/
│   ├── environments/      # Environment configurations
│   │   ├── environment.ts
│   │   └── environment.prod.ts
│   ├── styles/            # Global styles
│   │   ├── _variables.scss
│   │   ├── _mixins.scss
│   │   └── _utilities.scss
│   ├── index.html
│   ├── main.ts
│   └── styles.scss
├── node_modules/          # Dependencies (not committed)
├── .editorconfig
├── .gitignore
├── angular.json           # Angular configuration
├── package.json           # Node dependencies
├── package-lock.json
├── tsconfig.json          # TypeScript configuration
├── tsconfig.app.json
└── README.md              # Frontend documentation
```

## Key Directories Explained

### Backend

#### `config/`
Contains Django project configuration files including settings, URL routing, and WSGI/ASGI configurations.

#### `apps/`
Contains Django applications, each focused on a specific feature:
- **products**: Product catalog, categories, inventory
- **users**: User authentication, profiles, permissions
- **orders**: Order processing, payment handling
- **cart**: Shopping cart management

#### `media/`
Stores user-uploaded files (product images, user avatars, etc.)

#### `staticfiles/`
Contains collected static files for production deployment

### Frontend

#### `core/`
Contains singleton services, guards, and interceptors that are used application-wide.

#### `shared/`
Contains reusable components, directives, and pipes that are used across multiple features.

#### `features/`
Contains feature modules, each representing a major section of the application. Each feature is self-contained with its own components, services, and routing.

#### `environments/`
Contains environment-specific configuration (development, production).

## File Naming Conventions

### Backend (Python/Django)
- Files: `lowercase_with_underscores.py`
- Classes: `PascalCase`
- Functions/Variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`

### Frontend (TypeScript/Angular)
- Files: `kebab-case.component.ts`
- Classes: `PascalCase`
- Functions/Variables: `camelCase`
- Constants: `UPPER_SNAKE_CASE`

## Module Organization

### Backend Apps

Each Django app should have:
- `models.py`: Database models
- `views.py`: API views (or viewsets)
- `serializers.py`: DRF serializers
- `urls.py`: URL routing
- `tests.py`: Unit tests
- `admin.py`: Admin interface configuration

### Frontend Features

Each Angular feature module should have:
- Components directory
- Services directory
- Routing module
- Feature module
- Models/interfaces (if complex)

## Adding New Features

### Backend

1. Create new Django app:
```bash
cd backend
python manage.py startapp new_app_name
mv new_app_name apps/
```

2. Add to `INSTALLED_APPS` in `config/settings.py`
3. Create models, views, serializers
4. Add URL routing
5. Run migrations
6. Write tests

### Frontend

1. Generate new feature module:
```bash
cd frontend
ng generate module features/new-feature --routing
ng generate component features/new-feature/components/main
ng generate service features/new-feature/services/new-feature
```

2. Update routing
3. Implement components and services
4. Write tests

## Best Practices

1. **Keep modules focused**: Each module should have a single responsibility
2. **Use lazy loading**: Load feature modules on demand (frontend)
3. **Follow DRY principle**: Don't repeat yourself
4. **Write tests**: Maintain good test coverage
5. **Document complex code**: Add comments for non-obvious logic
6. **Use type hints**: Both Python and TypeScript support strong typing

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Angular Documentation](https://angular.io/docs)
- [Angular Style Guide](https://angular.io/guide/styleguide)

# Chris-TCM E-Commerce Platform

A cross-platform web application for selling products (Amazon-style marketplace) built with Django and Angular 16.

## Project Overview

This is a full-stack e-commerce platform designed for team development with the following tech stack:

- **Backend**: Django (Python web framework)
- **Frontend**: Angular 16 (TypeScript framework)
- **Database**: PostgreSQL (production) / SQLite (development)
- **API**: Django REST Framework
- **Authentication**: JWT-based authentication

## Project Structure

```
Chris-TCM/
├── backend/              # Django backend application
│   ├── config/          # Django project configuration
│   ├── apps/            # Django applications
│   │   ├── products/    # Product management
│   │   ├── users/       # User management
│   │   ├── orders/      # Order processing
│   │   └── cart/        # Shopping cart
│   ├── manage.py
│   └── requirements.txt
├── frontend/            # Angular 16 frontend application
│   ├── src/
│   │   ├── app/
│   │   ├── assets/
│   │   └── environments/
│   ├── angular.json
│   ├── package.json
│   └── tsconfig.json
├── docker-compose.yml   # Docker configuration for development
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.10 or higher
- Node.js 18.x or higher
- npm or yarn
- PostgreSQL (for production)
- Docker & Docker Compose (optional, recommended for development)

## Getting Started

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/YSubaruY/Chris-TCM.git
cd Chris-TCM
```

2. Start the development environment:
```bash
docker-compose up
```

3. Access the applications:
   - Frontend: http://localhost:4200
   - Backend API: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin

### Manual Setup

#### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

#### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

4. Open your browser at http://localhost:4200

## Development Workflow

### Branch Strategy

- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: Feature branches
- `bugfix/*`: Bug fix branches
- `hotfix/*`: Production hotfixes

### Workflow

1. Create a new branch from `develop`:
```bash
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name
```

2. Make your changes and commit:
```bash
git add .
git commit -m "Description of changes"
```

3. Push your branch:
```bash
git push origin feature/your-feature-name
```

4. Create a Pull Request to `develop`

## API Documentation

Once the backend is running, API documentation is available at:
- Swagger UI: http://localhost:8000/api/docs/
- ReDoc: http://localhost:8000/api/redoc/

## Testing

### Backend Tests
```bash
cd backend
python manage.py test
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Team Guidelines

### Code Style

- **Python**: Follow PEP 8 style guide
- **TypeScript/Angular**: Follow Angular style guide
- Use meaningful variable and function names
- Write docstrings for functions and classes
- Keep functions small and focused

### Commit Messages

Follow conventional commits format:
```
type(scope): subject

body

footer
```

Types: feat, fix, docs, style, refactor, test, chore

Example:
```
feat(products): add product search functionality

Implement search by name, category, and price range
Add pagination for search results

Closes #123
```

## Features Roadmap

- [ ] User authentication and authorization
- [ ] Product catalog with categories
- [ ] Product search and filtering
- [ ] Shopping cart functionality
- [ ] Order processing and payment integration
- [ ] User reviews and ratings
- [ ] Admin dashboard
- [ ] Email notifications
- [ ] Inventory management
- [ ] Multi-vendor support (future)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact the development team.

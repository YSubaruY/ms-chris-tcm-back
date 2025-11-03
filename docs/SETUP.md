# Development Setup Guide

This guide will help you set up the Chris-TCM development environment.

## Prerequisites

Before you begin, ensure you have the following installed:

### Required Software

1. **Python 3.10+**
   - Download from [python.org](https://www.python.org/downloads/)
   - Verify: `python --version`

2. **Node.js 18+**
   - Download from [nodejs.org](https://nodejs.org/)
   - Verify: `node --version` and `npm --version`

3. **Git**
   - Download from [git-scm.com](https://git-scm.com/)
   - Verify: `git --version`

4. **PostgreSQL** (for production-like environment)
   - Download from [postgresql.org](https://www.postgresql.org/download/)
   - Or use SQLite for quick development

5. **Docker & Docker Compose** (optional but recommended)
   - Download from [docker.com](https://www.docker.com/)
   - Verify: `docker --version` and `docker-compose --version`

## Setup Methods

Choose one of the following setup methods:

### Option 1: Docker Setup (Recommended for Teams)

This is the easiest way to get started with a consistent environment.

1. Clone the repository:
```bash
git clone https://github.com/YSubaruY/Chris-TCM.git
cd Chris-TCM
```

2. Start all services:
```bash
docker-compose up
```

3. Access the applications:
   - Frontend: http://localhost:4200
   - Backend API: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin

4. To stop services:
```bash
docker-compose down
```

### Option 2: Manual Setup

#### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:
   - Linux/Mac: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create `.env` file:
```bash
cp .env.example .env
```

6. Edit `.env` with your configuration:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

7. Run migrations:
```bash
python manage.py migrate
```

8. Create superuser:
```bash
python manage.py createsuperuser
```

9. Start development server:
```bash
python manage.py runserver
```

Backend should now be running at http://localhost:8000

#### Frontend Setup

1. Open a new terminal and navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm start
```

Frontend should now be running at http://localhost:4200

## Verifying the Setup

### Backend Verification

1. Visit http://localhost:8000/admin
2. Login with superuser credentials
3. You should see the Django admin interface

### Frontend Verification

1. Visit http://localhost:4200
2. You should see the Angular welcome page

### API Verification

1. Visit http://localhost:8000/api/
2. You should see the API root

## Common Issues and Solutions

### Issue: Port Already in Use

**Error:** `Port 8000 is already in use`

**Solution:**
- Kill the process using the port
- Linux/Mac: `lsof -ti:8000 | xargs kill -9`
- Windows: `netstat -ano | findstr :8000` then `taskkill /PID <PID> /F`

### Issue: Database Connection Error

**Error:** `django.db.utils.OperationalError`

**Solution:**
- Check PostgreSQL is running
- Verify database credentials in `.env`
- Try using SQLite for development: `DATABASE_URL=sqlite:///db.sqlite3`

### Issue: Node Modules Error

**Error:** `Cannot find module`

**Solution:**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Issue: Python Package Installation Fails

**Error:** `pip install` fails

**Solution:**
- Upgrade pip: `pip install --upgrade pip`
- Install build tools:
  - Linux: `sudo apt-get install python3-dev build-essential`
  - Mac: `xcode-select --install`
  - Windows: Install Visual Studio Build Tools

### Issue: CORS Errors

**Error:** `CORS policy: No 'Access-Control-Allow-Origin' header`

**Solution:**
- Verify `CORS_ALLOWED_ORIGINS` in backend `.env`
- Should include: `http://localhost:4200`

## Next Steps

After successful setup:

1. Read the [Contributing Guide](../CONTRIBUTING.md)
2. Review the [Project Structure](STRUCTURE.md)
3. Check the [API Documentation](http://localhost:8000/api/docs/)
4. Start developing your feature!

## Development Tools

### Recommended IDE Extensions

**VS Code:**
- Python (Microsoft)
- Pylance
- Angular Language Service
- ESLint
- Prettier
- GitLens

**PyCharm/WebStorm:**
- Built-in support for Django and Angular

### Useful Commands

**Backend:**
```bash
# Run tests
python manage.py test

# Create new app
python manage.py startapp app_name

# Make migrations
python manage.py makemigrations

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

**Frontend:**
```bash
# Run tests
npm test

# Build for production
npm run build

# Generate component
ng generate component components/component-name

# Generate service
ng generate service services/service-name

# Lint code
ng lint
```

## Getting Help

If you encounter issues not covered here:

1. Check [GitHub Issues](https://github.com/YSubaruY/Chris-TCM/issues)
2. Ask in team chat
3. Create a new issue with detailed information

Happy coding! 🚀

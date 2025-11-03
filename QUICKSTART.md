# Quick Start Guide

Get Chris-TCM up and running in minutes!

## Prerequisites

- Python 3.10+
- Node.js 18+
- Git

## 5-Minute Setup

### Option 1: Using Make (Recommended)

```bash
# Clone the repository
git clone https://github.com/YSubaruY/Chris-TCM.git
cd Chris-TCM

# Install all dependencies and setup
make setup

# Create a superuser for Django admin
make backend-superuser

# In terminal 1: Start backend
make backend-run

# In terminal 2: Start frontend
make frontend-run
```

### Option 2: Docker (Easiest)

```bash
# Clone the repository
git clone https://github.com/YSubaruY/Chris-TCM.git
cd Chris-TCM

# Start everything
docker-compose up
```

That's it! 🎉

## Access Points

- **Frontend**: http://localhost:4200
- **Backend API**: http://localhost:8000/api
- **Admin Panel**: http://localhost:8000/admin

## Next Steps

1. **Explore the Admin Panel**
   - Login at http://localhost:8000/admin
   - Create some products, categories, etc.

2. **Read the Documentation**
   - [Full Setup Guide](docs/SETUP.md)
   - [Project Structure](docs/STRUCTURE.md)
   - [Contributing Guidelines](CONTRIBUTING.md)

3. **Start Developing**
   ```bash
   # Create a new feature branch
   git checkout -b feature/my-feature
   
   # Make your changes
   # ...
   
   # Run tests
   make test
   
   # Commit and push
   git add .
   git commit -m "feat: add my feature"
   git push origin feature/my-feature
   ```

## Common Commands

```bash
# Backend
make backend-run          # Start Django server
make backend-test         # Run backend tests
make backend-migrate      # Run migrations
make backend-superuser    # Create superuser

# Frontend
make frontend-run         # Start Angular dev server
make frontend-test        # Run frontend tests
make frontend-build       # Build for production

# Docker
make docker-up            # Start all services
make docker-down          # Stop all services
make docker-logs          # View logs

# Help
make help                 # Show all available commands
```

## Troubleshooting

### Port Already in Use

```bash
# Linux/Mac
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Database Issues

```bash
# Reset database
cd backend
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Node Modules Issues

```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

## Need Help?

- Check [docs/SETUP.md](docs/SETUP.md) for detailed setup instructions
- See [GitHub Issues](https://github.com/YSubaruY/Chris-TCM/issues) for known issues
- Read [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines

Happy coding! 🚀

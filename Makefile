.PHONY: help install setup backend-install frontend-install backend-migrate backend-run frontend-run test clean docker-up docker-down

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: backend-install frontend-install ## Install all dependencies

setup: install backend-migrate ## Setup the project (install + migrate)

# Backend commands
backend-install: ## Install backend dependencies
	cd backend && python -m venv venv && . venv/bin/activate && pip install -r requirements.txt

backend-migrate: ## Run Django migrations
	cd backend && . venv/bin/activate && python manage.py migrate

backend-makemigrations: ## Create Django migrations
	cd backend && . venv/bin/activate && python manage.py makemigrations

backend-superuser: ## Create Django superuser
	cd backend && . venv/bin/activate && python manage.py createsuperuser

backend-run: ## Run Django development server
	cd backend && . venv/bin/activate && python manage.py runserver

backend-shell: ## Open Django shell
	cd backend && . venv/bin/activate && python manage.py shell

backend-test: ## Run backend tests
	cd backend && . venv/bin/activate && python manage.py test

# Frontend commands
frontend-install: ## Install frontend dependencies
	cd frontend && npm install

frontend-run: ## Run Angular development server
	cd frontend && npm start

frontend-build: ## Build Angular for production
	cd frontend && npm run build

frontend-test: ## Run frontend tests
	cd frontend && npm test

frontend-lint: ## Lint frontend code
	cd frontend && npm run lint

# Docker commands
docker-up: ## Start all services with Docker Compose
	docker-compose up

docker-up-d: ## Start all services in background
	docker-compose up -d

docker-down: ## Stop all services
	docker-compose down

docker-build: ## Build Docker images
	docker-compose build

docker-logs: ## Show Docker logs
	docker-compose logs -f

# Testing
test: backend-test frontend-test ## Run all tests

# Cleaning
clean: ## Clean temporary files and caches
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	cd frontend && rm -rf dist node_modules/.cache 2>/dev/null || true

clean-all: clean ## Clean all generated files including dependencies
	rm -rf backend/venv
	rm -rf frontend/node_modules
	rm -rf backend/db.sqlite3

# Development
dev: ## Run both backend and frontend (requires two terminals)
	@echo "Starting backend and frontend..."
	@echo "Run 'make backend-run' in one terminal"
	@echo "Run 'make frontend-run' in another terminal"

format-backend: ## Format backend code with black
	cd backend && . venv/bin/activate && black . --exclude venv

lint-backend: ## Lint backend code with flake8
	cd backend && . venv/bin/activate && flake8 . --exclude=venv,migrations --max-line-length=100

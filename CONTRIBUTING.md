# Contributing to Chris-TCM

Thank you for your interest in contributing to Chris-TCM! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and encourage diverse perspectives
- Focus on constructive feedback
- Maintain professionalism in all interactions

## Getting Started

1. Fork the repository
2. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/Chris-TCM.git
cd Chris-TCM
```

3. Add upstream remote:
```bash
git remote add upstream https://github.com/YSubaruY/Chris-TCM.git
```

## Development Workflow

### 1. Create a Feature Branch

Always create a new branch from `develop` for your work:

```bash
git checkout develop
git pull upstream develop
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/` - New features
- `bugfix/` - Bug fixes
- `hotfix/` - Urgent production fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring

### 2. Make Your Changes

- Write clean, maintainable code
- Follow the project's coding standards
- Add tests for new functionality
- Update documentation as needed
- Commit frequently with meaningful messages

### 3. Commit Guidelines

Follow the Conventional Commits specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```bash
git commit -m "feat(products): add product search functionality"
git commit -m "fix(cart): resolve item quantity update issue"
git commit -m "docs(readme): update installation instructions"
```

### 4. Keep Your Branch Updated

Regularly sync with upstream:

```bash
git fetch upstream
git rebase upstream/develop
```

### 5. Push Your Changes

```bash
git push origin feature/your-feature-name
```

### 6. Create a Pull Request

1. Go to the repository on GitHub
2. Click "New Pull Request"
3. Select your branch
4. Fill in the PR template:
   - Clear title describing the change
   - Detailed description of what was changed and why
   - Reference any related issues
   - Include screenshots for UI changes

### 7. Code Review Process

- Address review comments promptly
- Make requested changes in new commits
- Push updates to your branch
- Re-request review when ready

## Coding Standards

### Python (Django Backend)

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Maximum line length: 100 characters
- Use docstrings for classes and functions
- Use type hints where applicable

```python
def calculate_total_price(items: List[CartItem], discount: float = 0.0) -> Decimal:
    """
    Calculate the total price of items with optional discount.
    
    Args:
        items: List of cart items
        discount: Discount percentage (0-100)
    
    Returns:
        Total price after discount
    """
    # Implementation
    pass
```

### TypeScript (Angular Frontend)

- Follow Angular style guide
- Use TypeScript strict mode
- Use meaningful component and variable names
- Keep components focused and small
- Use reactive programming patterns

```typescript
export class ProductListComponent implements OnInit {
  products$: Observable<Product[]>;
  
  constructor(private productService: ProductService) {}
  
  ngOnInit(): void {
    this.products$ = this.productService.getProducts();
  }
}
```

## Testing

### Backend Tests

```bash
cd backend
python manage.py test
```

Write tests for:
- Models
- API endpoints
- Business logic
- Utilities

### Frontend Tests

```bash
cd frontend
npm test
```

Write tests for:
- Components
- Services
- Pipes
- Guards

## Documentation

- Update README.md if you change functionality
- Add JSDoc/docstrings for new functions
- Update API documentation for endpoint changes
- Include code comments for complex logic

## Pull Request Checklist

Before submitting your PR, ensure:

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New tests added for new functionality
- [ ] Documentation updated
- [ ] Commit messages follow conventions
- [ ] No merge conflicts with develop
- [ ] PR description is clear and complete

## Questions?

If you have questions:
- Check existing issues and discussions
- Ask in PR comments
- Contact the maintainers

Thank you for contributing to Chris-TCM! 🎉

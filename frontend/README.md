# Frontend - Angular 16

This is the frontend application for Chris-TCM e-commerce platform, built with Angular 16.

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 16.2.16.

## Project Structure

```
frontend/
├── src/
│   ├── app/              # Application components and modules
│   │   ├── core/        # Core services, guards, interceptors
│   │   ├── shared/      # Shared components, directives, pipes
│   │   ├── features/    # Feature modules
│   │   │   ├── products/
│   │   │   ├── cart/
│   │   │   ├── orders/
│   │   │   └── auth/
│   │   └── app.module.ts
│   ├── assets/          # Images, fonts, static files
│   ├── environments/    # Environment configurations
│   └── styles.scss      # Global styles
├── angular.json
├── package.json
└── tsconfig.json
```

## Setup

1. Install dependencies:
```bash
npm install
```

2. Configure environment:
Edit `src/environments/environment.ts` and `src/environments/environment.prod.ts` with your API URL.

## Development

### Development server

Run `npm start` or `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

### Code scaffolding

Generate new components:
```bash
ng generate component features/products/product-list
ng generate service core/services/product
ng generate guard core/guards/auth
```

You can also use: `ng generate directive|pipe|service|class|guard|interface|enum|module`.

### Build

Run `npm run build` or `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

For production build:
```bash
npm run build:prod
```

### Running unit tests

Run `npm test` or `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

### Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Main Features

- Product catalog browsing
- Product search and filtering
- Shopping cart management
- User authentication and registration
- Order processing
- User profile management
- Admin dashboard (for administrators)

## Technologies

- **Angular 16**: Frontend framework
- **TypeScript**: Programming language
- **SCSS**: Styling
- **RxJS**: Reactive programming
- **Angular Material** (optional): UI components
- **HttpClient**: API communication

## Development Guidelines

### Code Style
- Follow Angular style guide
- Use TypeScript strict mode
- Write unit tests for components and services
- Use reactive forms for form handling
- Implement lazy loading for feature modules

### Component Structure
```typescript
@Component({
  selector: 'app-component-name',
  templateUrl: './component-name.component.html',
  styleUrls: ['./component-name.component.scss']
})
export class ComponentNameComponent implements OnInit {
  // Component logic
}
```

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.

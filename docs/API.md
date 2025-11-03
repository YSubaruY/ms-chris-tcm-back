# API Documentation

This document describes the REST API endpoints for the Chris-TCM e-commerce platform.

## Base URL

- Development: `http://localhost:8000/api`
- Production: `https://api.yourdomain.com/api`

## Authentication

The API uses JWT (JSON Web Token) for authentication.

### Obtaining Tokens

```http
POST /api/auth/jwt/create/
Content-Type: application/json

{
  "username": "your-username",
  "password": "your-password"
}
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Using Tokens

Include the access token in the Authorization header:

```http
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
```

### Refreshing Tokens

```http
POST /api/auth/jwt/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

## API Endpoints

### Products

#### List Products

```http
GET /api/products/
```

Query Parameters:
- `page` (optional): Page number for pagination
- `search` (optional): Search term
- `category` (optional): Filter by category ID
- `ordering` (optional): Sort by field (e.g., `price`, `-price`, `name`)

**Response:**
```json
{
  "count": 100,
  "next": "http://localhost:8000/api/products/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Product Name",
      "description": "Product description",
      "price": "99.99",
      "category": {
        "id": 1,
        "name": "Category Name"
      },
      "image": "http://localhost:8000/media/products/image.jpg",
      "stock": 50,
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

#### Get Product Details

```http
GET /api/products/{id}/
```

**Response:**
```json
{
  "id": 1,
  "name": "Product Name",
  "description": "Detailed product description",
  "price": "99.99",
  "category": {
    "id": 1,
    "name": "Category Name"
  },
  "images": [
    "http://localhost:8000/media/products/image1.jpg",
    "http://localhost:8000/media/products/image2.jpg"
  ],
  "stock": 50,
  "reviews": [],
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

#### Create Product (Admin Only)

```http
POST /api/products/
Authorization: Bearer {token}
Content-Type: application/json

{
  "name": "New Product",
  "description": "Product description",
  "price": "99.99",
  "category": 1,
  "stock": 50
}
```

#### Update Product (Admin Only)

```http
PUT /api/products/{id}/
Authorization: Bearer {token}
Content-Type: application/json

{
  "name": "Updated Product Name",
  "price": "89.99"
}
```

#### Delete Product (Admin Only)

```http
DELETE /api/products/{id}/
Authorization: Bearer {token}
```

### Cart

#### Get Cart

```http
GET /api/cart/
Authorization: Bearer {token}
```

**Response:**
```json
{
  "id": 1,
  "items": [
    {
      "id": 1,
      "product": {
        "id": 1,
        "name": "Product Name",
        "price": "99.99"
      },
      "quantity": 2,
      "subtotal": "199.98"
    }
  ],
  "total": "199.98",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

#### Add to Cart

```http
POST /api/cart/items/
Authorization: Bearer {token}
Content-Type: application/json

{
  "product": 1,
  "quantity": 2
}
```

#### Update Cart Item

```http
PATCH /api/cart/items/{id}/
Authorization: Bearer {token}
Content-Type: application/json

{
  "quantity": 3
}
```

#### Remove from Cart

```http
DELETE /api/cart/items/{id}/
Authorization: Bearer {token}
```

### Orders

#### List Orders

```http
GET /api/orders/
Authorization: Bearer {token}
```

**Response:**
```json
{
  "count": 10,
  "results": [
    {
      "id": 1,
      "order_number": "ORD-2024-0001",
      "status": "pending",
      "total": "199.98",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

#### Get Order Details

```http
GET /api/orders/{id}/
Authorization: Bearer {token}
```

#### Create Order

```http
POST /api/orders/
Authorization: Bearer {token}
Content-Type: application/json

{
  "shipping_address": {
    "street": "123 Main St",
    "city": "City",
    "state": "State",
    "zip_code": "12345",
    "country": "Country"
  },
  "payment_method": "credit_card"
}
```

### Users

#### Register

```http
POST /api/users/
Content-Type: application/json

{
  "username": "newuser",
  "email": "user@example.com",
  "password": "securepassword"
}
```

#### Get User Profile

```http
GET /api/users/me/
Authorization: Bearer {token}
```

#### Update User Profile

```http
PATCH /api/users/me/
Authorization: Bearer {token}
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe"
}
```

## Error Responses

### 400 Bad Request
```json
{
  "field_name": ["Error message"]
}
```

### 401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden
```json
{
  "detail": "You do not have permission to perform this action."
}
```

### 404 Not Found
```json
{
  "detail": "Not found."
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error."
}
```

## Rate Limiting

The API implements rate limiting to prevent abuse:

- Unauthenticated requests: 100 requests per hour
- Authenticated requests: 1000 requests per hour

## Pagination

List endpoints return paginated results:

```json
{
  "count": 100,
  "next": "http://localhost:8000/api/products/?page=2",
  "previous": null,
  "results": [...]
}
```

## Interactive API Documentation

Once the backend is running, you can explore the API interactively:

- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/

## Testing the API

### Using curl

```bash
# List products
curl http://localhost:8000/api/products/

# Get product details
curl http://localhost:8000/api/products/1/

# Login
curl -X POST http://localhost:8000/api/auth/jwt/create/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password"}'

# Get cart (with authentication)
curl http://localhost:8000/api/cart/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Using Postman

1. Import the API endpoints from the OpenAPI spec
2. Set up an environment with:
   - `base_url`: `http://localhost:8000/api`
   - `access_token`: Your JWT token

### Using HTTPie

```bash
# List products
http GET localhost:8000/api/products/

# Login
http POST localhost:8000/api/auth/jwt/create/ username=admin password=password

# Get cart
http GET localhost:8000/api/cart/ "Authorization: Bearer YOUR_TOKEN"
```

## Need Help?

- Check the [Django REST Framework documentation](https://www.django-rest-framework.org/)
- Review the [backend code](../backend/)
- Ask in the team chat
- Create an issue on GitHub

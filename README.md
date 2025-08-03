# Django API Server

A Django REST API server equivalent to the Express.js implementation with user authentication, role-based access, and MongoDB integration.

## Features

- **User Management**: Registration, login with PIN-based authentication
- **Role-based Access**: Support for vendors, suppliers, agents, and normal users
- **JWT Authentication**: Access and refresh token implementation
- **Image Upload**: Cloudinary integration for image storage
- **MongoDB Integration**: Using djongo for MongoDB support
- **Modular Architecture**: Clean separation of concerns with Django apps

## Project Structure

```
├── config/                 # Django project settings
├── apps/
│   ├── common/            # Shared utilities and authentication
│   ├── users/             # User management
│   ├── vendors/           # Vendor-specific functionality
│   ├── suppliers/         # Supplier-specific functionality
│   └── agents/            # Agent-specific functionality
├── media/                 # Media files storage
├── staticfiles/           # Static files
└── requirements.txt       # Python dependencies
```

## Setup Instructions

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### User Management
- `GET /api/users/` - Get user details
- `POST /api/users/create/` - Register new user
- `POST /api/users/login/` - User login
- `PATCH /api/users/details/` - Update user details

### Vendors
- `GET /api/vendors/` - Get vendor list
- `POST /api/vendors/create/` - Create vendor

### Suppliers
- `GET /api/suppliers/` - Get supplier list
- `POST /api/suppliers/create/` - Create supplier

### Agents
- `GET /api/agents/` - Get agent list
- `POST /api/agents/create/` - Create agent

## Authentication

The API uses JWT tokens for authentication:
- **Access Token**: Short-lived (15 minutes)
- **Refresh Token**: Long-lived (7 days)

Tokens are provided both in response body and as HTTP-only cookies.

## Models

### User Model
- Custom user model with phone-based authentication
- Support for multiple roles (vendor, supplier, agent, normal_user)
- PIN-based authentication instead of passwords

### Role-specific Models
- **Vendor**: Order management, payment methods, QR codes
- **Supplier**: Inventory management, delivery radius, price prediction
- **Agent**: Supplier verification system

## Environment Variables

```env
# Database
MONGODB_URL=mongodb://localhost:27017/your_database_name
MONGODB_NAME=your_database_name

# Django
SECRET_KEY=your-super-secret-django-key
DEBUG=True

# JWT Tokens
ACCESS_TOKEN_SECRET=your-access-token-secret
REFRESH_TOKEN_SECRET=your-refresh-token-secret

# Cloudinary
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

## Development

- **Admin Interface**: Available at `/admin/`
- **API Documentation**: Can be extended with DRF spectacular
- **Testing**: Use Django's built-in testing framework
- **Logging**: Configure in settings.py for production

## Deployment

1. Set `DEBUG=False` in production
2. Configure proper `ALLOWED_HOSTS`
3. Set up proper database credentials
4. Configure static file serving
5. Set up proper logging

## Contributing

1. Follow Django coding standards
2. Write tests for new features
3. Update documentation
4. Use proper commit messages
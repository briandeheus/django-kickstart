# Django Starter Project

A batteries-included Django starter project for building REST APIs quickly.

## What's Included

### Core Features
- **Django 5.2.9** - Latest Django framework
- **Django REST Framework** - Full-featured REST API toolkit
- **Django Extensions** - Includes `shell_plus` and other useful management commands
- **WhiteNoise** - Simplified static file serving
- **Custom User Model** - `CoreUser` model ready for extension

### APIs App
Pre-configured `apis` app with:
- API key authentication system
- Versioned and extendable API structure (`v1`)
- Base API classes and utilities
- Example endpoints for accounts and API key management
- Simple test suite

### Development Tools
- **IPython** - Enhanced interactive shell
- **shell_plus** - Auto-imports models and utilities
- Configurable logging (console handler with verbose formatting)

## Quick Start

Install dependencies:
```bash
uv sync
```

Run migrations:
```bash
python manage.py migrate
```

Create a superuser:
```bash
python manage.py createsuperuser
```

Start the development server:
```bash
python manage.py runserver
```

Use the enhanced shell:
```bash
python manage.py shell_plus
```

## Configuration

The project uses SQLite by default and includes:
- API key authentication (`Bearer` token scheme)
- Customizable API key prefix (default: `core`)
- Environment-based logging configuration

## API Structure

APIs are organized under `/api/v1/` with:
- Token-based authentication
- Serializers for request/response handling
- Built-in test utilities

Check `apis/apis/v1/router.py` for available endpoints.
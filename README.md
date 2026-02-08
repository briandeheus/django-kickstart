# Django Starter Project

A batteries-included Django starter project for building web-apps and REST APIs quickly.

It's designed to help you get started with a solid foundation. 
Once started, it's easy to extend, update, and add or remove parts as you'd normally do.
This starter project is a little bit opinionated, but highly extensible.

## What's Included

### Core Features
- **Django 5.2.9** - Latest Django framework
- **Django REST Framework** - Full-featured REST API toolkit
- **Django Extensions** - Includes `shell_plus` and other useful management commands
- **WhiteNoise** - Simplified static file serving
- **Custom User Model** - `CoreUser` model ready for extension
- **DotEnv Support** - Supply a `.env` files to set your environment variables
- **Postgres by default** - Uses Postgresql with the latest version of `psycopg` by default
- 
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

## API Structure

APIs are organized under `/api/v1/` with:
- Token-based authentication
- Serializers for request/response handling
- Built-in test utilities

Check `apis/apis/v1/router.py` for available endpoints.
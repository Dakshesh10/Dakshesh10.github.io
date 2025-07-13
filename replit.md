# Portfolio Website - Dakshesh Mamtora

## Overview

This is a personal portfolio website for a game developer built with Flask and SQLAlchemy. The site showcases professional experience, projects, and includes a blog and contact system. It's designed to present a professional online presence for a game developer with 9+ years of experience.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Database ORM**: SQLAlchemy with Flask-SQLAlchemy extension
- **Database**: Configurable via environment variable, defaults to SQLite for development
- **Template Engine**: Jinja2 (built into Flask)
- **Session Management**: Flask's built-in session handling with configurable secret key

### Frontend Architecture
- **CSS Framework**: Bootstrap 5 with dark theme
- **Icons**: Font Awesome 6.0
- **JavaScript**: Vanilla JavaScript for interactive features
- **Responsive Design**: Mobile-first approach using Bootstrap's grid system

### Application Structure
- **Modular Design**: Separated into distinct modules (app.py, models.py, routes.py)
- **Template Inheritance**: Base template with block structure for consistent layout
- **Static Assets**: CSS and JavaScript files organized in static directory

## Key Components

### Database Models
1. **BlogPost**: Stores blog articles with title, content, excerpt, and timestamp
2. **ContactMessage**: Captures contact form submissions with name, email, subject, message, and timestamp

### Routes and Views
1. **Home Page** (`/`): Landing page with hero section and introduction
2. **About Page** (`/description`): Professional background and experience
3. **Projects Page** (`/projects`): Portfolio showcase
4. **Blog Page** (`/blog`): List of blog posts and individual post views
5. **Contact Page** (`/contact`): Contact form with database storage

### Frontend Features
- Responsive navigation with active state indicators
- Hero section with professional statistics
- Project showcase with technology badges
- Contact form with flash messaging
- Blog system with post listing and individual views

## Data Flow

### Contact Form Submission
1. User fills out contact form on `/contact`
2. POST request validates all required fields
3. Creates ContactMessage model instance
4. Saves to database via SQLAlchemy
5. Flash message confirms successful submission
6. Redirects to prevent duplicate submissions

### Blog System
1. Blog posts stored in BlogPost model
2. `/blog` route queries all posts ordered by date
3. Individual posts accessible via `/blog/<post_id>`
4. Template displays formatted content with metadata

### Database Initialization
1. App context created on startup
2. Models imported to register with SQLAlchemy
3. `db.create_all()` creates tables if they don't exist
4. Development uses SQLite, production can use any SQLAlchemy-supported database

## External Dependencies

### CDN Resources
- Bootstrap 5 CSS (with replit dark theme)
- Font Awesome 6.0 icons
- No local dependency management for frontend assets

### Python Packages
- Flask: Web framework
- Flask-SQLAlchemy: Database ORM integration
- Werkzeug: WSGI utilities (ProxyFix for deployment)

### Environment Variables
- `SESSION_SECRET`: Flask session encryption key
- `DATABASE_URL`: Database connection string

## Deployment Strategy

### Development
- Flask development server with debug mode
- SQLite database for local development
- Hot reloading enabled for code changes

### Production Considerations
- ProxyFix middleware configured for reverse proxy deployment
- Environment-based configuration for database and secrets
- Database connection pooling configured with ping and recycle settings
- WSGI-compatible for deployment to various platforms

### Configuration
- Environment variable fallbacks for development
- Modular configuration allowing easy environment switching
- Database URL flexibility supports PostgreSQL, MySQL, SQLite

The architecture prioritizes simplicity and maintainability while providing a solid foundation for a professional portfolio website. The separation of concerns between models, routes, and templates makes the codebase easy to understand and extend.
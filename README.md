# Yellow Pages API

A custom RESTful API for managing person information and directory services.

## Project Overview

Yellow Pages is a Python-based API application built with Flask/FastAPI-like architecture, providing endpoints for managing person records, contacts, and related information with a scalable, modular structure.

## Project Structure

```
yellow_pages/
├── app/
│   ├── main.py                 # Application entry point
│   ├── database/
│   │   ├── __init__.py
│   │   └── connection.py       # Database connection setup
│   ├── handlers/
│   │   ├── __init__.py
│   │   └── person_handler.py   # Request handlers for person operations
│   ├── models/
│   │   ├── __init__.py
│   │   └── person_model.py     # Database models
│   ├── routes/
│   │   ├── __init__.py
│   │   └── person_routes.py    # API route definitions
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── person_schema.py    # Data validation schemas
│   ├── services/
│   │   ├── __init__.py
│   │   └── person_service.py   # Business logic layer
│   └── utils/
│       └── __init__.py         # Utility functions
├── requirements.txt            # Python dependencies
├── test.py                     # Test suite
└── README.md                   # This file
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Instructions

1. **Clone or navigate to the project directory:**
   ```bash
   cd yellow_pages
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the application:**
   ```bash
   python app/main.py
   ```

2. **The API will be available at:**
   ```
   http://localhost:5000
   ```

## Running Tests

Execute the test suite to verify functionality:

```bash
python test.py
```

## API Endpoints

### Person Management

- **GET /persons** - Retrieve all persons
- **GET /persons/{id}** - Retrieve a specific person by ID
- **POST /persons** - Create a new person record
- **PUT /persons/{id}** - Update an existing person record
- **DELETE /persons/{id}** - Delete a person record

## Architecture

The application follows a layered architecture pattern:

- **Routes Layer** - Defines API endpoints
- **Handlers Layer** - Processes incoming requests
- **Services Layer** - Contains business logic
- **Models Layer** - Database models and ORM mappings
- **Schemas Layer** - Request/response validation
- **Database Layer** - Database connection and queries

## Dependencies

All project dependencies are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt
```

## Configuration

Configuration details can be added to the appropriate files in the `app/` directory. Update database connection settings in `app/database/connection.py` as needed.

## Contributing

When making changes to the codebase:

1. Follow the existing project structure
2. Add appropriate validation in schemas
3. Implement business logic in services
4. Write tests for new features
5. Update this README if adding new endpoints or functionality

## License

[Add your license information here]

## Contact

For questions or support, please contact the project maintainers.

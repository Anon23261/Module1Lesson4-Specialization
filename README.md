# Mechanic Shop API

A Flask-based REST API for managing a mechanic shop, built using the Application Factory Pattern.

## Features

- RESTful API design
- Application Factory Pattern implementation
- SQLite database with SQLAlchemy ORM
- Input validation and error handling
- Pagination for list endpoints
- Search functionality

## API Endpoints

### Health Check
- `GET /api/v1/health` - System health status

### Mechanics
- `GET /api/v1/mechanics` - List all mechanics
- `POST /api/v1/mechanics` - Create a new mechanic
- `GET /api/v1/mechanics/<id>` - Get mechanic details
- `PUT /api/v1/mechanics/<id>` - Update mechanic details
- `DELETE /api/v1/mechanics/<id>` - Delete a mechanic
- `GET /api/v1/mechanics/search` - Search mechanics

### Services
- `GET /api/v1/services` - List all services
- `POST /api/v1/services` - Create a new service
- `GET /api/v1/services/<id>` - Get service details
- `PUT /api/v1/services/<id>` - Update service details
- `DELETE /api/v1/services/<id>` - Delete a service
- `GET /api/v1/services/search` - Search services

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd mechanic-shop-api
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Initialize the database:
```bash
python init_db.py
```

4. Run the application:
```bash
python run.py
```

The API will be available at `http://localhost:5000`

## Example Usage

Create a mechanic:
```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "name": "John Smith",
  "email": "john.smith@mechanic.com",
  "specialty": "Engine Repair",
  "certification": "ASE Master Technician",
  "years_experience": 10
}' http://localhost:5000/api/v1/mechanics
```

Create a service:
```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "name": "Engine Tune-up",
  "description": "Complete engine tune-up service",
  "price": 299.99,
  "duration_hours": 2.5,
  "mechanic_id": 1
}' http://localhost:5000/api/v1/services
```

## Project Structure
```
mechanic_shop/
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── mechanic.py
│   │   └── service.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── mechanic.py
│   │   └── service.py
│   └── utils/
│       ├── __init__.py
│       ├── error_handlers.py
│       └── validators.py
├── requirements.txt
├── run.py
└── init_db.py
```

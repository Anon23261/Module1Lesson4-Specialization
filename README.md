<div align="center">

# 🔧 Mechanic Shop API 🚗

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-orange.svg)](https://www.sqlalchemy.org/)

<p align="center">
  <img src="https://raw.githubusercontent.com/Anon23261/Module1Lesson4-Specialization/main/.github/assets/mechanic-logo.png" alt="Mechanic Shop API" width="200"/>
</p>

🚀 A professional Flask-based REST API for managing a mechanic shop, built using the Application Factory Pattern. Features robust error handling, input validation, and comprehensive documentation.

[Features](#features) • [Installation](#setup) • [API Reference](#api-endpoints) • [Examples](#example-usage) • [License](#license)

</div>

## ✨ Features

🔹 **Modern Architecture**
  - RESTful API design principles
  - Application Factory Pattern for scalability
  - Modular codebase organization

🔹 **Robust Backend**
  - SQLite database with SQLAlchemy ORM
  - Comprehensive input validation
  - Professional error handling

🔹 **Advanced Functionality**
  - Smart pagination for list endpoints
  - Powerful search capabilities
  - Real-time data validation

🔹 **Developer Experience**
  - Clear documentation
  - Easy-to-use endpoints
  - Consistent API responses

## 🛠 API Endpoints

### 🏥 Health Check
```http
GET /api/v1/health - System health status
```

### 👨‍🔧 Mechanics
```http
GET    /api/v1/mechanics        # List all mechanics
POST   /api/v1/mechanics        # Create a new mechanic
GET    /api/v1/mechanics/<id>   # Get mechanic details
PUT    /api/v1/mechanics/<id>   # Update mechanic details
DELETE /api/v1/mechanics/<id>   # Delete a mechanic
GET    /api/v1/mechanics/search # Search mechanics
```

### 🔨 Services
```http
GET    /api/v1/services        # List all services
POST   /api/v1/services        # Create a new service
GET    /api/v1/services/<id>   # Get service details
PUT    /api/v1/services/<id>   # Update service details
DELETE /api/v1/services/<id>   # Delete a service
GET    /api/v1/services/search # Search services
```

## 🚀 Setup

### Prerequisites
- Python 3.9 or higher
- Git
- pip (Python package installer)

### Installation Steps

1️⃣ **Clone the repository**
```bash
git clone https://github.com/Anon23261/Module1Lesson4-Specialization.git
cd Module1Lesson4-Specialization
```

2️⃣ **Set up virtual environment**
```bash
python -m venv venv

# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Initialize database**
```bash
python init_db.py
```

5️⃣ **Start the server**
```bash
python run.py
```

🌟 The API will be available at `http://localhost:5000`

## 📚 Example Usage

### 🔷 Create a Mechanic

<details>
<summary>Click to expand</summary>

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "name": "John Smith",
    "email": "john.smith@mechanic.com",
    "specialty": "Engine Repair",
    "certification": "ASE Master Technician",
    "years_experience": 10
  }' \
  http://localhost:5000/api/v1/mechanics
```

#### Response:
```json
{
  "id": 1,
  "name": "John Smith",
  "email": "john.smith@mechanic.com",
  "specialty": "Engine Repair",
  "certification": "ASE Master Technician",
  "years_experience": 10,
  "created_at": "2025-02-13T22:57:31.450566",
  "updated_at": "2025-02-13T22:57:31.450574"
}
```
</details>

### 🔷 Create a Service

<details>
<summary>Click to expand</summary>

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "name": "Engine Tune-up",
    "description": "Complete engine tune-up service",
    "price": 299.99,
    "duration_hours": 2.5,
    "mechanic_id": 1
  }' \
  http://localhost:5000/api/v1/services
```

#### Response:
```json
{
  "id": 1,
  "name": "Engine Tune-up",
  "description": "Complete engine tune-up service",
  "price": 299.99,
  "duration_hours": 2.5,
  "mechanic_id": 1,
  "created_at": "2025-02-13T22:57:40.902592",
  "updated_at": "2025-02-13T22:57:40.902597"
}
```
</details>

## 📁 Project Structure

```
📦 mechanic_shop
 ┣ 📂 app
 ┃ ┣ 📂 models
 ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┣ 📜 mechanic.py
 ┃ ┃ └ 📜 service.py
 ┃ ┣ 📂 routes
 ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┣ 📜 mechanic.py
 ┃ ┃ └ 📜 service.py
 ┃ ┣ 📂 utils
 ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┣ 📜 error_handlers.py
 ┃ ┃ └ 📜 validators.py
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 extensions.py
 ┃ └ 📜 config.py
 ┣ 📜 requirements.txt
 ┣ 📜 run.py
 ┣ 📜 init_db.py
 ┣ 📜 LICENSE
 └ 📜 README.md
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ by [Anon23261](https://github.com/Anon23261)

</div>

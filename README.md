# Metadata Service

A backend service built with FastAPI to manage dataset metadata, enable prioritized search, and track dataset lineage.  
This project simulates a simplified data governance metadata platform.

---

## 🚀 Tech Stack

- API Framework: FastAPI  
- Database: MySQL  
- ORM: SQLAlchemy  
- Migrations: Alembic  
- Containerization: Docker & docker-compose  
- Dependency Management: Poetry  
- Configuration: .env file  

---

## 📌 Features

### 1. Dataset Metadata Management

Each dataset is uniquely identified using a Fully Qualified Name (FQN):

connection.database.schema.table


Stored metadata includes:

- FQN  
- Source system type (MySQL / MSSQL / PostgreSQL)  
- Columns (name and data type)  

---

### 2. Prioritized Dataset Search

Search functionality follows this priority order:

1. Table name (highest priority)  
2. Column name  
3. Schema name  
4. Database name  

This ensures the most relevant datasets appear first.

---

### 3. Dataset Lineage (Directed Graph)

- Supports upstream and downstream relationships  
- Prevents cycle creation in lineage graph  
- Returns meaningful error on invalid lineage  

---

## 🛠️ Setup Instructions

### Prerequisites

- Docker  
- Docker Compose  

---

### Run the project locally

```bash
docker-compose up --build
```

Once started, open:

```
http://localhost:8000/docs
```

This opens Swagger UI for API testing.

📂 Project Structure
metadata-service/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   ├── schemas.py
│   └── database.py
│
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── .env
└── README.md
📑 API Endpoints
➕ Add Dataset
POST /datasets
Example:

{
  "fqn": "conn1.sales.public.users",
  "source_type": "MySQL",
  "columns": [
    { "name": "id", "dtype": "int" },
    { "name": "email", "dtype": "varchar" }
  ]
}
🔍 Search Dataset
GET /search?q=users
🔗 Create Lineage
POST /lineage
Example:

{
  "upstream": "conn1.sales.public.users",
  "downstream": "conn1.sales.public.orders"
}
🧠 Architecture & Design Decisions
FastAPI
High performance

Automatic OpenAPI documentation

Built-in validation

SQLAlchemy
Clean ORM layer

Easy integration with Alembic migrations

MySQL
Production-like relational database

Docker Compose
Isolated API and database services

Simple local setup

⚙️ Search Logic
The search query is matched against:

Table name

Column name

Schema name

Database name

Results are returned based on this strict priority order.

🔗 Lineage Handling
Stored as directed relationships

Graph traversal used to detect cycles

Prevents invalid lineage creation

📦 Sample Data
Sample datasets can be added using Swagger UI:

http://localhost:8000/docs
⚠️ Assumptions & Limitations
No authentication implemented

Basic text-based search

No UI visualization for lineage

✅ Future Improvements
Lineage traversal endpoints

Pagination for search results

Full Alembic migrations

Lineage visualization UI

👨‍💻 Author
Built as part of a backend technical assessment using FastAPI and MySQL.


---


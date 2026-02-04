# Metadata Service

A backend service built with FastAPI to manage dataset metadata, enable prioritized search, and track dataset lineage.  
This project simulates a simplified data governance metadata platform.

---

## 🚀 Tech Stack

- FastAPI  
- MySQL  
- SQLAlchemy  
- Alembic  
- Docker & Docker Compose  
- Poetry  

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

Search follows this priority order:

1. Table name (highest priority)  
2. Column name  
3. Schema name  
4. Database name  

---

### 3. Dataset Lineage

- Supports upstream and downstream relationships  
- Prevents cyclic dependencies  

---

## 🛠️ Setup Instructions

### Prerequisites

- Docker  
- Docker Compose  

---

### Run the project locally

```bash
docker-compose up --build
Once started, open:

http://localhost:8000/docs
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

{
  "upstream": "conn1.sales.public.users",
  "downstream": "conn1.sales.public.orders"
}
🧠 Architecture & Design Decisions
FastAPI for validation and automatic API documentation

SQLAlchemy as ORM layer

MySQL as production-style relational database

Docker Compose for easy setup

⚙️ Search Logic
Search is matched against:

Table name

Column name

Schema name

Database name

Results follow strict priority order.

🔗 Lineage Handling
Stored as directed relationships

Cycle detection prevents invalid graphs

⚠️ Assumptions & Limitations
No authentication

Basic text search

No lineage visualization UI

✅ Future Improvements
Lineage traversal APIs

Pagination

Advanced search

Visualization UI

👨‍💻 Author
Built as part of a backend technical assessment using FastAPI and MySQL.

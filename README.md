# 💰 Finance Dashboard API

A backend REST API built using Django and Django REST Framework for managing financial records with Role-Based Access Control (RBAC) and JWT authentication.

---

## 🚀 Features

- 🔐 JWT Authentication (Secure API access)
- 👥 Role-Based Access Control (Admin, Analyst, Viewer)
- 📄 Financial Records CRUD (Create, Read, Update, Delete)
- 🔍 Record Filtering (by category, type, date)
- 📊 Analytics APIs (summary, totals)
- ⚠️ Input Validation & Error Handling
- 💾 SQLite Database (easy setup)

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SimpleJWT (JWT Authentication)
- SQLite

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/whoismohit/finance-dashboard-api.git
cd finance_dashboard
```

### 2. Create virtual environment
python -m venv .venv

### 3. Activate virtual environement
python -m venv .venv

### 4. Install dependencies
pip install -r requirements.txt

### 5. Apply migrations
python manage.py migrate

### 6. Create superuser
python manage.py createsuperuser

### 7. Run server
python manage.py runserver

---

## 🔐 Authentication (JWT)
Get Token
```bash
    POST /api/token/
{
  "username": "your_username",
  "password": "your_password"
}
```
Use Token in Requests
-Authorization: Bearer <access_token>

---
### 📌 API Endpoints
Users
- Managed via admin panel

Records
-GET /records/ - List records
-POST /records/ - Create record
-PUT /records/{id}/ - Update record
-DELETE /records/{id}/ - Delete record


Filtering Examples
-/records/?type=income
-/records/?category=food

Analytics
-GET /analytics/summary/ → Financial summary
    
---

### 👥 Roles & Permissions
Role	Access
Viewer	Read-only
Analyst	Create & update
Admin	Full access

---

### 🧠 Technical Decisions

-Used Django REST Framework for rapid API development
-Implemented custom User model for RBAC
-Used JWT for stateless authentication
-Structured project into modular apps for scalability

---

### ⚖️ Trade-offs
-SQLite used for simplicity (not ideal for production)
-JWT chosen over sessions (harder token revocation)
-Pagination and rate limiting not implemented to focus on core features

---

### 🚧 Future Improvements
-Pagination support
-Search functionality
-Rate limiting
-API documentation (Swagger)
-Unit & integration tests

---

### 📝 Additional Notes
-The API is designed for backend use and can be integrated with frontend/mobile apps
-Can be tested using Postman or DRF interface
-Clean architecture allows easy extension

---

### 👨‍💻 Author

Mohit Awana

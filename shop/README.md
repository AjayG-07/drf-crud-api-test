# 🛠️ Python Django DRF CRUD - Machine Test

This is a **Python Django REST Framework (DRF)** project created as part of a **Machine Test Round** for a company recruitment process.

It includes complete **CRUD operations** with **relational database support**, proper **REST API endpoints**, **pagination**, and a **one-to-many** relationship between `Category` and `Product`.

---

## ✅ Features Implemented

### 📂 Category CRUD APIs

| Method | Endpoint                            | Description                     |
|--------|-------------------------------------|---------------------------------|
| GET    | `/api/categories?page=3`            | Get all categories (paginated) |
| POST   | `/api/categories`                   | Create a new category           |
| GET    | `/api/categories/{id}`              | Get category by ID              |
| PUT    | `/api/categories/{id}`              | Update category by ID           |
| DELETE | `/api/categories/{id}`              | Delete category by ID           |

---

### 📦 Product CRUD APIs

| Method | Endpoint                            | Description                             |
|--------|-------------------------------------|-----------------------------------------|
| GET    | `/api/products?page=2`              | Get all products (paginated)            |
| POST   | `/api/products`                     | Create a new product                    |
| GET    | `/api/products/{id}`                | Get product by ID (with category info)  |
| PUT    | `/api/products/{id}`                | Update product by ID                    |
| DELETE | `/api/products/{id}`                | Delete product by ID                    |

---

## 🧠 Machine Test Requirements Addressed

- ✅ Use REST Controller (**Django REST Framework**)
- ✅ Use **Relational Database (MySQL)** instead of in-memory
- ✅ Annotation-based configuration via `.env` (no XML)
- ✅ Implemented CRUD operations for `Category` and `Product`
- ✅ One-to-Many relationship: One Category → Many Products
- ✅ Server-side Pagination enabled
- ✅ Product details include nested category data

---

## 🛠️ Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- MySQL
- dotenv (`python-decouple`)
- Git & GitHub

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git https://github.com/AjayG-07/drf-crud-api-test/tree/main
cd your-repo-name

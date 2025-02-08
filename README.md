# 🎖 Nobel Prize Search API

This project provides a **FastAPI-based REST API** to search Nobel Prize winners stored in a **MongoDB** database.  
It is fully **containerized** using **Docker & Docker Compose**, making it easy to run with a single command.

---

## **🚀 Features**

- **Search Nobel Prize winners** by **name, category, or motivation**
- **Fuzzy search support** (e.g., `"Albret Enstein"` → `"Albert Einstein"`)
- **REST API with JSON responses**
- **Interactive API documentation** with Swagger (`/docs`)
- **MongoDB as the database** (runs in a separate container)
- **Containerized with Docker & Docker Compose**
- **Easily deployable with a single command**

---

## **📌 Prerequisites**

Before running this project, ensure you have the following installed:

1. **[Docker](https://www.docker.com/get-started)**
2. **[Docker Compose](https://docs.docker.com/compose/install/)**

---

## ** Installation & Setup**

### ** Clone the Repository**

```sh
git clone https://github.com/Speed3s/nobel-search-api.git
cd nobel-search-api


Run the Application
To start everything (MongoDB + FastAPI), run:


docker compose up --build

This will:
- Start MongoDB container on port 27017
- Start FastAPI API on port 8000
- Automatically fetch & store Nobel Prize data in MongoDB
```

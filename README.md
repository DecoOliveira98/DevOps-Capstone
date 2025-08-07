# 📚 Book Catalog API - DevOps Capstone 2025

This is a Django-based RESTful API for managing a catalog of books, developed as part of the DevOps Diploma Capstone Project 2025 at CCT College Dublin.

The project demonstrates full DevOps lifecycle integration including:
- CI/CD with GitHub Actions
- Docker containerization
- Deployment to Kubernetes via Helm Charts

---

## 🚀 Features

- CRUD operations for books (Title, Author, ISBN, Published Date)
- Django REST Framework
- PostgreSQL integration
- Unit tests with Django’s test framework
- Docker support (`Dockerfile` + `docker-compose`)
- GitHub Actions CI/CD pipeline
- Kubernetes deployment with Helm

---

## 🧰 Technologies Used

- Python 3.12 / Django
- Django REST Framework
- PostgreSQL
- Docker / Docker Compose
- GitHub Actions
- Kubernetes
- Helm

---

## 📦 API Endpoints

| Method | Endpoint           | Description       |
| ------ | ------------------ | ----------------- |
| GET    | `/api/books/`      | List all books    |
| POST   | `/api/books/`      | Create a new book |
| GET    | `/api/books/<id>/` | Get book details  |
| PUT    | `/api/books/<id>/` | Update book       |
| DELETE | `/api/books/<id>/` | Delete book       |

---

## 💻 Local Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/DecoOliveira98/DevOps-Capstone.git
cd DevOps-Capstone
```

### 2. Create a `.env` file (optional)
Create a `.env` file in the root folder if using environment variables locally:
```
DATABASE_NAME=book_catalog
DATABASE_USER=bookuser
DATABASE_PASSWORD=bookpass
DATABASE_HOST=db
```

### 3. Run with Docker Compose
```bash
docker-compose up --build
```

This will:
- Build the Django app image
- Start a PostgreSQL container
- Run the Django app on `http://localhost:8000`

---

## 🧪 Running Tests

Run unit tests using Django's test framework:

```bash
docker-compose exec web python manage.py test
```

This ensures all API functionality is validated.

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

The `.github/workflows/ci-cd.yml` file contains the full CI/CD pipeline.

### Trigger:
- On push or PR to `main`

### Steps:
1. **Checkout Code** – uses `actions/checkout`
2. **Set up Python** – installs Python 3.12
3. **Install Dependencies** – using `pip install -r requirements.txt`
4. **Run Migrations** – `python manage.py migrate`
5. **Run Tests** – `python manage.py test`
6. **Build Docker Image** – `docker build -t book_catalog .`
7. **(Optional)** Push image to GHCR or DockerHub
8. **(Optional)** Deploy to Kubernetes using Helm (if configured with access)

> If any test fails, the pipeline stops and deployment is prevented.

---

## ☸️ Kubernetes Deployment with Helm

A full Helm Chart is included in `/helm/bookcatalog/`

### Chart Components:
- `deployment.yaml` – defines the app pod and container spec
- `service.yaml` – exposes the app within the cluster
- `ingress.yaml` – exposes the app externally (via domain)
- `configmap.yaml` – passes env variables (e.g., DB creds)
- `values.yaml` – default values for the deployment

### Steps to Deploy:

1. Ensure you have access to a Kubernetes cluster and Helm installed.
2. Package and install the chart:
```bash
helm install bookcatalog ./helm/bookcatalog
```

3. Check resources:
```bash
kubectl get all
```

4. To upgrade:
```bash
helm upgrade bookcatalog ./helm/bookcatalog
```

5. To uninstall:
```bash
helm uninstall bookcatalog
```

---

## 🗂 Project Structure

```
book-catalog/
├── books/                 # Django app
├── Dockerfile
├── docker-compose.yml
├── helm/                  # Helm Chart
├── manage.py
└── .github/workflows/     # GitHub Actions CI/CD
```


## 📚 Lessons Learned

- CI/CD pipelines are crucial for automation and code quality
- Containerization simplifies consistent deployments
- Helm Charts streamline Kubernetes configuration
- Managing secrets securely is vital in real deployments

---

## 📬 Contact

Andre Luiz Oliveira da Cunha [2024214@student.cct.ie]  
DevOps Diploma - CCT College Dublin - 2025

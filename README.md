# 🛠️ DarraghOps

**DarraghOps** is a full-stack task management API built with Django and Django REST Framework, featuring AWS S3 integration for file uploads. It’s designed to be scalable, cloud-native, and a foundation for future expansion into a full SaaS platform.

---

## 🚀 Tech Stack

- **Backend**: Django, Django REST Framework (DRF)
- **Cloud Storage**: AWS S3
- **Database**: SQLite (dev) / PostgreSQL (prod-ready)
- **Version Control**: Git & GitHub
- **Virtual Environment**: `venv`

---

## 🧩 Features

- ✅ Create, update, and delete tasks via REST API
- 📂 Upload task-related files directly to AWS S3
- 🔒 Secure API architecture (token-based auth planned)
- 🧪 Easily testable with Postman or Pytest
- 🌱 Built with modular architecture (`task_service` app)

---

## 📁 File Structure

```

DarraghOps/
│
├── darraghops\_backend/      # Project settings
├── task\_service/            # Main app for managing tasks
├── venv/                    # Virtual environment
├── .env                     # Environment variables (not committed)
├── .gitignore               # Git tracking rules
├── manage.py                # Django entry point

````

---

## 🛠️ Getting Started (Local)

```bash
# Clone the repo
git clone https://github.com/darraghdarragh/DarraghOps.git
cd DarraghOps

# Set up virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install django djangorestframework boto3 python-decouple

# Set up environment variables
# Create a .env file with your AWS keys

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Launch server
python manage.py runserver
````

> Visit `http://127.0.0.1:8000/admin` to log in.

---

## ☁️ AWS Setup

Make sure you:

* ✅ Create an S3 bucket
* ✅ Enable programmatic access
* ✅ Add the following to your `.env` file:

```ini
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_STORAGE_BUCKET_NAME=your_bucket_name
```

---

## 📦 Upcoming Features

* 🔐 User authentication and registration
* 🖥️ Frontend UI (React or Django templates)
* 📊 Task stats and dashboard
* 🧪 Unit tests + CI/CD pipelines

---

## 🙋‍♂️ About Me

Built by **Darragh Morrissey**, an aspiring full-stack engineer with a passion for cloud-native Python development and scalable architecture.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

````

---

Once you paste that into `README.md`, run:

```bash
git add README.md
git commit -m "Add complete project README"
git push
````

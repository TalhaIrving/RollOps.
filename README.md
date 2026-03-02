README.md (Use This)
# RollOps

RollOps is a cloud-native training analytics API built to demonstrate real-world DevOps engineering skills.

This project is not a startup product — it is a technical showcase focused on:

- Containerization (Docker)
- Kubernetes orchestration
- Infrastructure as Code (Terraform)
- CI/CD (GitHub Actions)
- AWS deployment (EKS, ECR, RDS)
- Scaling and observability

---

## 🚀 MVP Functionality

- User registration
- JWT authentication
- Log training sessions
- Retrieve training history
- Weekly stats calculation

---

## 🏗 Tech Stack

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- Docker (Phase 2)
- Kubernetes (Phase 3)
- AWS EKS (Phase 4)
- Terraform (Infrastructure)
- GitHub Actions (CI/CD)

---

## 🧱 Project Structure


rollops/
│
├── app/
│ └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore


(Structure will expand as the project evolves.)

---

## 🖥 Running Locally

### 1. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
2. Install dependencies
pip install -r requirements.txt
3. Run the server
uvicorn app.main:app --reload

Visit:

http://127.0.0.1:8000/health


Author

Talha Irving

License

This project is licensed under the MIT License
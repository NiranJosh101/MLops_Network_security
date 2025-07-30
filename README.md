# 🛡️ Network Security Threat Detection with FastAPI & MLOps

This project is a full-fledged MLOps pipeline that builds, evaluates, and serves a machine learning model to detect whether a given website is malicious. The solution integrates modern DevOps and ML tooling such as FastAPI, Docker, AWS (S3, EC2, ECR), MongoDB Atlas, MLflow, and GitHub Actions to create a modular, production-ready setup.

---

## 🚀 Features

- Multi-model training with hyperparameter tuning via `GridSearchCV`
- Model tracking and versioning with MLflow
- Model and artifact storage in AWS S3
- Containerized with Docker, deployed using AWS EC2 & ECR
- CI/CD pipeline with GitHub Actions
- Real-time inference served with FastAPI
- Modular codebase with component-based pipelines

---

## 🧠 Project Workflow

The model training logic chains together several classifiers including:

- Random Forest  
- Gradient Boosting  
- Decision Tree  
- AdaBoost  
- Logistic Regression  

Each model is tuned using `GridSearchCV`, and the best-performing model is serialized along with its preprocessor for inference. All stages (ingestion, transformation, validation, training) are modularized and triggered through a unified training pipeline.

---

## 🗂️ Project Structure

Here’s a simplified view of the project structure (see screenshots for full structure):

```
├── app.py               # FastAPI inference app
├── main.py              # Entry point for training pipeline
├── Dockerfile           # Container setup
├── .github/workflows/   # CI/CD pipeline config
├── networksecurity/     # Core pipeline logic (utils, components, exceptions, etc.)
├── final_model/         # Serialized model + preprocessor (or served via S3)
├── templates/           # HTML template for prediction UI
├── prediction_output/   # CSV output from prediction
├── mlruns/              # MLflow tracking directory
```

---

## ⚙️ Setup & Usage

### ✅ Step 1: Clone the Repo

```bash
git clone <your-repo-url>
cd <project-folder>
```

### ✅ Step 2: Install Dependencies

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

### ✅ Step 3: Running the App

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Then, in your browser:

1. Visit: `http://127.0.0.1:8000/train` to trigger training  
2. Visit: `http://127.0.0.1:8000/docs` to use the `/predict` endpoint via Swagger UI

---

## ☁️ Docker & Cloud Deployment Overview

This project is fully containerized using Docker and deployed to AWS EC2 using AWS ECR as the image registry.

### 🐳 Docker Setup

Create a Docker image:

```bash
docker build -t network-threat-detector .
```

Run it locally:

```bash
docker run -p 8000:8000 network-threat-detector
```

---

### ☁️ AWS EC2 + ECR Setup (Deployment)

> Full walkthrough is covered in the [blog post](https://medium.com/@niranjosh011/going-beyond-local-mlops-in-the-cloud-9ec7db023423) — here’s a high-level summary:

1. Build and push the image to AWS ECR
2. Pull and run the container on your EC2 instance
3. Ensure port `8000` is open in your security group

**EC2 Docker Setup Commands:**

```bash
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

---

## 🔁 CI/CD with GitHub Actions

Whenever you push changes to the main branch, a GitHub Actions workflow is triggered to:

- Run unit tests
- Build the Docker image
- Push it to AWS ECR
- Deploy to EC2 via SSH

Check `.github/workflows/deploy.yml` for the setup. Full explanation is provided in the [companion blog](#).

---

## 🛠️ Tech Stack

- **Language & Frameworks:** Python, FastAPI, Scikit-learn, Pandas
- **Model Ops:** MLflow, Docker, GitHub Actions
- **Cloud:** AWS S3 (artifacts), EC2 (deployment), ECR (Docker registry)
- **Database:** MongoDB Atlas
- **DevOps:** Docker, CI/CD, Uvicorn

---

## 📬 Prediction Sample Output

The app returns a downloadable `.csv` file and renders results in a clean HTML table. It can process batch `.csv` inputs via Swagger UI `/predict`.

---

## 📖 Want More Details?

Read the full [blog post here](https://medium.com/@niranjosh011/going-beyond-local-mlops-in-the-cloud-9ec7db023423) to explore how I implemented cloud services with this project

---

## 🙌 Acknowledgements

Special thanks to open-source contributors and MLOps community projects that inspired the architecture and deployment.

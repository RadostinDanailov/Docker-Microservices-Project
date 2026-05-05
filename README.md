# Docker Microservices Project — Nginx • Python API • Redis

This project is a fully containerised microservice architecture built using Docker and Docker Compose.  
It includes:

- **Nginx reverse proxy**  
- **Python Flask API service**  
- **Redis key‑value store**  
- Internal Docker networking  
- Clean service‑to‑service communication  

This setup mirrors real production patterns used in cloud platforms like AWS ECS, Kubernetes, and Azure Container Apps.

---

##Architecture Overview

- **Nginx** routes incoming traffic to the API service  
- **Python API** exposes a `/hello` endpoint  
- **Redis** stores and retrieves data inside the API  
- All services run inside isolated containers on a shared Docker network  

---

##Project Structure

docker_training/
├── api/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── nginx/
│   └── nginx.conf
└── docker-compose.yml










Code

---

##How to Run the Project

``bash
docker-compose up -d --build
Then open:

Code
http://localhost:8080/hello
Expected output:

json
{
  "message": "Hello Radostin, your microservice works!"
}







##Technologies Used
-Docker
-Docker Compose
-Python Flask
-Redis
-Nginx
-Linux/WSL









##What I Learned
-Building multi‑service architectures
-Debugging Docker containers and volumes
-Managing Docker networks and service discovery
-Using Nginx as a reverse proxy
-Connecting Python APIs to Redis
-Fixing real‑world DevOps issues (caching, volumes, container exits, etc.)








##Possible Future Improvements:
-Add Postgres database
-Add JWT authentication
-Add a second microservice
-Deploy to AWS ECS Fargate
-Add Prometheus + Grafana monitoring

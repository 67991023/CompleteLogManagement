# CompleteLogManagement

Demo of Log Management System for Full-Stack Developer Intern Exam.

This project is a demo implementation of a Log Management system as per the exam PDF requirements. It supports ingestion from multiple sources (e.g., Syslog, HTTP, File), normalization to a central schema, storage/search in OpenSearch, dashboard UI with React, alerting, authentication (JWT with roles: admin/viewer), multi-tenant separation, and deployment in 2 modes (Appliance via Docker Compose, SaaS on cloud with HTTPS).

Objectives (from exam):
- Test full-stack skills: Architecture, Backend/API, Frontend/UI, Data Pipeline, DevOps/Deployment.
- Handle event/logs from multiple sources, normalize/index/search/visualize/alert.
- Security: AuthN/AuthZ, TLS, Multi-tenant.

Tech Stack:
- Ingest: timberio/vector (for collecting/normalizing logs from Syslog/HTTP/File).
- Storage/Search: OpenSearch (for storing and querying logs).
- Backend: FastAPI (Python) for API, auth, alert.
- Frontend: React with Vite for dashboard (charts, filters).
- Deployment: Docker Compose (Appliance), Nginx + Certbot (SaaS HTTPS).

## Prerequisites
Before building, ensure your environment is set up (tested on Fedora 43):
- Install Docker: Follow steps in guideline (remove podman, add repo, etc.).
- Install Python 3.11 and Node.js LTS.
- For SaaS: Cloud VM (e.g., AWS EC2), domain for HTTPS.

Troubleshooting:
- If Docker pull fails with GPG errors: Kill gpg-agent (`gpgconf --kill all`), remove locks (`rm ~/.gnupg/*.lock`), set GPG_TTY (`export GPG_TTY=$(tty)`), restart Docker.
- Nginx repo: Use the fixed code below to avoid 404.

## Installation
1. Clone repo:
   ```bash
   git clone https://github.com/yourusername/CompleteLogManagement.git
   cd CompleteLogManagement
2. Fix Nginx repo (for SaaS mode, to avoid 404 on Fedora):
sudo tee /etc/yum.repos.d/nginx.repo <<EOF
[nginx-stable]
name=nginx stable repo
baseurl=https://nginx.org/packages/rhel/9/\$basearch/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true
EOF
sudo dnf clean all
sudo dnf update -y
sudo dnf install nginx -y
sudo systemctl enable --now nginx

# Verification Steps
1. Test Vector (log collector)
    docker run --rm timberio/vector:0.52.0-alpine vector --version
2. Test OpenSearch (log database):
    docker run -d -p 9200:9200 -e "discovery.type=single-node" -e "DISABLE_SECURITY_PLUGIN=true" opensearchproject/opensearch:3.4.0

# Start running this project
1. docker compose up -d (using docker-compose.yml)
2. install requirements.txt : python3.11 -m pip install -r backend/requirements.txt

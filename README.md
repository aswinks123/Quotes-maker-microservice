# 📄 Project Description

Quotes maker is a containerized microservice application designed to help users store and view motivational quotes. 

The project is built to practice real-world Kubernetes, Helm, microservices, and CI/CD branching strategies.

The system consists of a frontend, a backend API, and a database, all deployed as separate containers managed entirely on Kubernetes using Helm charts.

This project is intentionally simple but architected like a real cloud-native system, making it perfect for hands-on learning.


## Application Components


1. Frontend (Python PyWebIO) 

Runs as a standalone container

Provides two features:

Add Quote form

View Daily Quote (fetched from backend)

Communicates with backend over HTTP (ClusterIP service)


2. Backend API (Python Flask)

Exposes REST API:

GET /quotes/daily → returns random or daily quote

POST /quotes → adds a new quote

Connects to PostgreSQL using environment variables

Will have more endpoints in future features

3. Database (PostgreSQL)

Runs as a Kubernetes StatefulSet

Stores quotes in a single table

Uses PersistentVolumeClaim for data durability



## Development Workflow (Git Branching Model)

1. Main Branch

Always stable

Contains production-ready configuration

Only receives pull requests from feature branches

2. Feature Branches

Each new component or improvement is done in a separate branch like:

feature/frontend-ui

feature/backend-api

feature/db-setup

feature/helm-chart-base

feature/ingress

feature/new-endpoint-random-quote

After testing, each feature branch is merged to main via PR.

Goal:

Build step-by-step, learn each part, and keep the repository clean.


More detals and features will be added when we complete each phase of the project
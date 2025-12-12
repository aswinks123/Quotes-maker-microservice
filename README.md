# 📄 Project Description

Quotes maker is a containerized microservice application designed to help users store and view motivational quotes. 

The project is built to practice real-world Kubernetes, Helm, microservices, and CI/CD branching strategies.

The system consists of a frontend, a backend API, and a database, all deployed as separate containers managed entirely on Kubernetes using Helm charts.

This project is intentionally simple but architected like a real cloud-native system, making it perfect for hands-on learning.


## Current Status:

main branch contains the first version of application

frontend Merged from frontend-feature branch:  frontend-v1

backend Merged from frontend-feature branch: backend-v1

main contains the first version of application



## Sample screenshots


### Home Page

![alt text](./resources/image.png)

### Add a new quote

![alt text](./resources/image-1.png)

![alt text](./resources/image-2.png)

### View the Quotes

![alt text](./resources/image-3.png)

![alt text](./resources/image-4.png)

### Content of quotes database

![alt text](./resources/image-5.png)












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

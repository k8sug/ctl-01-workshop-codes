# K8SUG Chatbot Project

## Overview

This repository contains the codebases for the **K8SUG CTL: Hands-On Workshop for Deploying AI/LLM on K8S**. The project demonstrates the deployment of a chatbot application using a microservices architecture on Kubernetes. The application consists of two main components:

- **Backend (Godel Flask API)**
- **Frontend (Flask Web App)**

## Overall Architecture

### Backend (Godel Flask API)
The backend handles the core logic of interacting with the Large Language Model (LLM), specifically Microsoft's GODEL-v1_1-base-seq2seq model. It performs the following tasks:

- **Configuration:** Retrieves configuration from environment variables (loaded from the ConfigMap in the Kubernetes setup).
- **Chat Processing:** Receives chat input from the frontend, processes it through the LLM, and returns a generated response.
- **Framework:** Uses Flask for the web server.
- **Endpoints:**
  - `/chat`: Handles chat requests.
  - `/health`: Provides health checks.
- **Dependencies:** Relies on the transformers library for LLM integration and Flask for the web framework.

### Frontend (Flask Web App)
The frontend is a web application that interacts with the backend API. It performs the following tasks:

- **HTTP Requests:** Sends user input to the backend's `/chat` endpoint and displays the response.
- **Framework:** Uses Flask for the web server and Jinja2 for templating the chat interface.
- **Chat History:** Maintains chat history using server-side sessions.
- **Pod Indication:** Indicates from which backend pod the response came.
- **Static Files:** Manages static files like stylesheets and favicons.

## Project Structure

```plaintext
.
├── Chatbot.excalidraw
├── chatbot-frontend-flask
│   ├── Dockerfile
│   ├── frontend_app.py
│   ├── requirements.txt
│   ├── static
│   │   ├── favicon.ico
│   │   └── styles.css
│   └── templates
│       └── chat.html
├── godel1_1-base
│   ├── app.py
│   └── Dockerfile
├── helm-charts
│   └── K8SUG-chatbot
│       ├── charts
│       ├── Chart.yaml
│       ├── k8sug-chatbot-1.0.3.tgz
│       ├── k8sug-chatbot-1.0.4.tgz
│       ├── k8sug-chatbot-1.0.5.tgz
│       ├── templates
│       │   ├── configmap.yaml
│       │   ├── deployment-backend.yaml
│       │   ├── deployment-frontend.yaml
│       │   ├── _helpers.tpl
│       │   ├── hpa.yaml
│       │   ├── NOTES.txt
│       │   ├── service.yaml
│       │   └── tests
│       │       └── test-connection.yaml
│       └── values.yaml
└── README.md
```

## Deployment

To deploy this application on Kubernetes, please follow the detailed instructions provided in our [GitBook documentation](https://k8sug.gitbook.io/k8sug-ctl-01/). The guide covers setting up the Kubernetes cluster, deploying the Helm charts, and configuring the application.

## Features

- **Microservices Architecture:** Separate backend and frontend components for scalability and maintainability.
- **Kubernetes Deployment:** Uses Helm charts for easy deployment and management.
- **Large Language Model Integration:** Leverages Microsoft's GODEL-v1_1-base-seq2seq model for generating responses.
- **Scalability:** Kubernetes handles scaling and resilience.
- **Health Checks:** Includes endpoints for health monitoring.

## GODEL Reference

The backend utilizes the GODEL model, which is detailed in the following publication:

@misc{peng2022godel,
author = {Peng, Baolin and Galley, Michel and He, Pengcheng and Brockett, Chris and Liden, Lars and Nouri, Elnaz and Yu, Zhou and Dolan, Bill and Gao, Jianfeng},
title = {GODEL: Large-Scale Pre-training for Goal-Directed Dialog},
howpublished = {arXiv},
year = {2022},
month = {June},
url = {https://www.microsoft.com/en-us/research/publication/godel-large-scale-pre-training-for-goal-directed-dialog/},
}


## Getting Started

For detailed steps on how to set up and deploy the application, refer to our [GitBook documentation](https://k8sug.gitbook.io/k8sug-ctl-01/).

Let's continue building the future of AI together! 🤖🤝

#Kubernetes #AI #Workshop #AKS #LLM #MachineLearning #K8SUG
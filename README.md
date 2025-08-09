# AGENTPY

*Empowering Intelligent Automation for Seamless Communication*

[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE) 
![Python](https://img.shields.io/badge/python-3.8%2B-blue) 
![Docker](https://img.shields.io/badge/docker-available-blue)

Built with the tools and technologies:  
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)

---

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

---

## Overview
**agentpy** is an all-in-one developer tool designed to orchestrate AI-driven email and chat workflows within a scalable, containerized environment. It combines service orchestration, reliable deployment, and advanced AI integrations to streamline complex backend systems.

### Why agentpy?
This project simplifies building and deploying AI-powered communication platforms. The core features include:

- 🌿 **Modular Service Orchestration**: Uses `compose.yaml` to coordinate core services like FastAPI and PostgreSQL, enabling seamless development and scaling.
- 🚀 **Containerized Deployment**: Ensures consistent environments with Dockerfiles and Railway configs for reliable, reproducible releases.
- 📧 **Email Automation**: Provides tools for email research, retrieval, and sending via Gmail IMAP and SMTP, integrating email workflows effortlessly.
- 🤖 **AI Model Integration**: Incorporates OpenAI models for natural language processing, powering intelligent email and chat interactions.
- 💾 **Data Persistence & Chat Management**: Manages chat messages and email data with robust database schemas and API endpoints.
- 📜 **Email Parsing & Retrieval**: Facilitates programmatic access to Gmail inboxes, supporting automation and data extraction.

---

## Getting Started

### Prerequisites
This project requires the following dependencies:

- **Programming Language**: Python  
- **Package Manager**: Pip  
- **Container Runtime**: Docker  

---

### Installation
Build **agentpy** from the source and install dependencies:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/deepnonpara9/agentpy 
   ```

2. **Navigate to the project directory:**
   ```bash
   cd agentpy
   ```

3. **Install the dependencies:**
   - *Using docker:*
   ```bash
   docker build -t deepnonpara9/agentpy .
   ```
   - *Using pip:*
   ```bash
   pip install -r backend/requirements.txt
   ```

---

### Usage
Run the project with:

**Using docker:**
```bash
docker run -it {image name}
```

**Using pip:**
```bash
python {entrypoint}
```

---

### Testing
Agentpy uses the {test_framework} test framework. Run the test suite with:

**Using docker:**
```bash
echo "INSERT-TEST-COMMAND-HERE"
```

**Using pip:**
```bash
pytest
```
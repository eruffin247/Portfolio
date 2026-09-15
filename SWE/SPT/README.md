# 🚨 Secure Password Tool 🔒

## Overview 🫆
*What is the Secure Password Tool?* The Secure Password Tool, or SPT for short, is a **web-based password generation and management application.**

The project is being developed as a hands-on software engineering project to explore **backend development, FastAPI, frontend/backend communication, database integration, authentication, and application security.**

The application will allow users to create an account, authenticate, generate **cryptographically secure random** passwords, and save & manage passwords associated with their accounts.

### How Is SPT Secure?
SPT uses Python's `secrets` module to generate passwords using a cryptographically secure source of randomness.

The number of possible passwords can be represented by:

$x^{n}$

where: 
- **x** = number of possible characters
- **n** = password length

Increasing the available character set and password length increases the total password space, making brute-force guessing more difficult. 

Application security will also include secure authentication, password hashing, encryption, input validation, and protection of sensitive configuration as the project develops.

## Current Status ⏳
SPT is currently in the prototype/development stage.

The initial password-generation prototype has been implemented using **Python and Streamlit.** The next development phase is to rebuild the application using **HTML/CSS/JS** for the frontend and a **FastAPI** backend.

### Project Stages
```
Build Prototype
    ↓
Build Frontend
    ↓
Design Database Schema
    ↓
Build FastAPI Backend
    ↓
Connect/Revise Frontend ↔ API ↔ Database
    ↓
Build Authentication
    ↓
Testing
    ↓
Deployment
```
## Features ✅

### Implemented
- Cryptographically secure password generation using Python's `secrets` module
- User-selectable password length
- User-selectable number of simultaneous password generations
- Basic prototype interface using **Streamlit**

### Planned
- User account creation/deletion
- User authentication and login
- Secure password storage
- Password management
- Save generated passwords
- Delete saved-generated passwords
- Frontend using JavaScript, HTML, and CSS
- REST API using FastAPI
- SQLite database
- Automated testing

## Tech Stack ⚙️

### Backend
- Python
- FastAPI

### Frontend
- HTML
- CSS
- JavaScript

### Development/Testing
- Git
- GitHub
- Python venv

### Prototype
- Streamlit

## Architecture 🏛️
**SPT uses a separated frontend/backend architecture.**

The frontend is responsible for the user interface and user interactions. JavaScript communicates with the FastAPI backend through HTTP requests to REST API endpoints. The FastAPI backend receives requests, validates input, executes application logic, communicates with the database, and returns responses to the frontend.

**The planned architecture is:**

```
User/Host Device
    ↓
HTML/CSS/JS Frontend
    ↓
HTTP Request
    ↓
FastAPI REST API
    ↓
Python Application Logic
    ↓
SQLite Database
```

## How It Works

A typical password-generation request follows this flow:

1. The user selects the desired password length on the frontend.
2. JavaScript sends an HTTP request to the FastAPI endpoint.
3. FastAPI receives and validates the request.
4. The backend calls the password-generation logic.
5. Python generates a password using a cryptographically secure random source.
6. The API returns the generated password to the frontend.
7. JavaScript displays the password to the user.

## Installation ⬇️
### 1. Clone the repository
```bash
git clone <repository-url>
cd SPT
```

### 2. Create a virtual environment
```bash
python3 -m venv .venv
```
or
```bash
python -m venv .venv
```

### 3. Activate the virtual environment
```bash
source .venv/bin/activate
```

### 4. Install dependencies
```bash
python3 -m pip install -r requirements.txt
```
or
```bash
python -m pip install -r requirements.txt
```
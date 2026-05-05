# 🚀 CertifyMe Admin Portal Backend (Flask)

A production-ready backend implementation for the Qatar Foundation Admin Portal, built using Flask. This system enables secure admin authentication and full lifecycle management of opportunities, ensuring strict data isolation and persistence.

---

## 📌 Project Overview

This project implements a complete backend system for an admin portal where:

* Admins can **register, log in, and manage sessions securely**
* Each admin can **create, view, edit, and delete opportunities**
* All data is **persisted in a database and scoped per admin**
* Security best practices such as **password hashing, token-based authentication, and reset token expiry** are enforced

This backend fully supports the provided frontend UI without requiring any modifications.

---

## 🧠 Key Features

### 🔐 Authentication System

* Admin Signup with validation and duplicate prevention
* Secure Login with JWT-based authentication
* "Remember Me" functionality using extended token expiry
* Forgot Password flow with secure reset token generation
* Token expiration handling (1-hour validity)

### 📊 Opportunity Management

* Create new opportunities with validation
* View all opportunities (admin-specific)
* View detailed opportunity data
* Edit existing opportunities (pre-filled data support)
* Delete opportunities with ownership restriction

### 🛡️ Security & Data Integrity

* Passwords stored using hashing (Werkzeug)
* JWT-based authentication for all protected routes
* Admin-level data isolation (no cross-user access)
* Reset tokens expire after 1 hour

---

## 🏗️ Tech Stack

| Layer          | Technology                                   |
| -------------- | -------------------------------------------- |
| Backend        | Flask                                        |
| Database       | SQLite (can be upgraded to PostgreSQL/MySQL) |
| ORM            | SQLAlchemy                                   |
| Authentication | JWT (Flask-JWT-Extended)                     |
| Security       | Werkzeug Password Hashing                    |

---

## 📁 Project Structure

```
certifyme-backend/
│
├── app.py                # Entry point
├── config.py            # Configuration settings
├── extensions.py        # DB & JWT initialization
├── models.py            # Database models
│
├── routes/
│   ├── auth.py          # Authentication routes
│   ├── opportunity.py   # Opportunity CRUD routes
│
├── utils/
│   ├── helpers.py       # Token utilities
│
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd certifyme-backend
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

Server will start at:

```
http://localhost:5000
```

---

## 🔗 API Base URL

```
http://localhost:5000/api
```

---

## 📡 API Endpoints

### 🔐 Authentication

#### ➤ Signup

```
POST /api/auth/signup
```

#### ➤ Login

```
POST /api/auth/login
```

#### ➤ Forgot Password

```
POST /api/auth/forgot-password
```

#### ➤ Reset Password

```
POST /api/auth/reset-password/<token>
```

---

### 📊 Opportunities

#### ➤ Create Opportunity

```
POST /api/opportunity/
```

#### ➤ Get All Opportunities

```
GET /api/opportunity/
```

#### ➤ Get Single Opportunity

```
GET /api/opportunity/<id>
```

#### ➤ Update Opportunity

```
PUT /api/opportunity/<id>
```

#### ➤ Delete Opportunity

```
DELETE /api/opportunity/<id>
```

---

## 🔑 Authentication Flow

1. Admin logs in → receives JWT token
2. Token must be sent in headers:

```
Authorization: Bearer <your_token>
```

3. Protected routes validate the token before granting access

---

## 🧪 Testing

You can test APIs using:

* Postman
* Thunder Client (VS Code)

### Suggested Test Flow:

1. Signup
2. Login → Copy token
3. Add Opportunity
4. Fetch Opportunities
5. Edit Opportunity
6. Delete Opportunity

---

## 🧠 Design Decisions

* **JWT over sessions** → scalable and stateless
* **SQLite** → lightweight for submission (can be upgraded easily)
* **Modular structure** → separates routes, models, and utilities
* **Token-based password reset** → avoids exposing user existence





# MediQueue — Online Doctor Appointment & Patient Queue Management System

**Course:** CSE 3242 — Web Development Bootcamp (5-Day Startup Project)  
**Team Members:** Achol Anha, Anha Mahmud, Rabeya Akter  

## 1. Project Overview
**MediQueue** is a full-stack healthcare queue and appointment management web application designed to eliminate long hospital waiting times through digital token booking, live queue tracking, and task management.

## 2. Technology Stack
* **Frontend:** HTML5, CSS3, JavaScript (ES6+), React 18 (Reusable Components: `Navbar`, `TaskForm`, `TaskList`, `TaskItem`)
* **Routing & Architecture:** Multi-page web routing (`/`, `/about`, `/dashboard`, `/tasks`, `/register`)
* **Backend:** Python 3 & Flask Web Framework
* **REST API:** JSON-based CRUD endpoints (`GET`, `POST`, `PUT`, `DELETE`)
* **Database:** SQLite (`mediqueue.db`) for persistent appointment storage
* **Version Control:** Git & GitHub (`https://github.com/Acholanha/Mediqueue`)

## 3. Folder & File Structure
```text
Codecrafts/
├── Mediqueue.py      # Flask backend server, page routing & REST API endpoints
├── mediqueue.db      # SQLite database (auto-generated on server start)
├── index.html        # Day 1 & 5: Fully Integrated Startup Landing Page
├── register.html     # Day 1: Patient Registration Form with JS validation
├── tasks.html        # Day 2: React Task & Queue Manager (4 Components)
├── about.html        # Day 3: About MediQueue & Architecture Overview
├── dashboard.html    # Day 3 & 4: Live Patient Queue Dashboard (REST API + DB)
└── README.md         # Day 5: Full Project & Architecture Documentation
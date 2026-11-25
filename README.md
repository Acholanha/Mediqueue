 # 🏥 Online Doctor Appointment and Patient Queue Management System (MediQueue)

**Course:** CSE 3292  
**Project Title:** Online Doctor Appointment and Patient Queue Management System  
**Repository Name:** Mediqueue  
**Submitted By:** Anha (`Acholanha`)  
**Team Members:** Anha & Rabeya Akter  

---

## 📋 Project Overview
**MediQueue** is a full-stack smart hospital queue management and online doctor appointment system built to eliminate waiting room congestion and streamline patient flow across hospital departments.

## ✨ Key Features
* **Smart Queue Command Center (`/dashboard`):** Live summary counters, search & department filtering, and full CRUD appointment management.
* **AI Voice Token Announcement:** Automated text-to-speech (`Web Speech API`) calling system that announces patient tokens and consultation rooms aloud.
* **Hospital Waiting Room TV Display (`/tv`):** Real-time auto-refreshing screen displaying the currently serving token (`NOW SERVING`) and upcoming patient queue.
* **Emergency Priority Queue:** High-priority emergency patient tagging that automatically elevates critical cases to the top of the queue.
* **Live Department Analytics:** Interactive doughnut chart (`Chart.js`) showing real-time patient distribution across hospital departments.
* **Printable Digital Token Receipt (`/register`):** Instant appointment booking form that generates a printable patient token slip.
* **React 18 Staff Task Tracker (`/tasks`):** Interactive component-based task board for doctors and hospital staff.

## 🛠️ Technology Stack
* **Backend:** Python 3, Flask (RESTful API)
* **Database:** SQLite (`mediqueue.db`)
* **Frontend:** HTML5, CSS3, JavaScript (ES6+), React 18, Chart.js
* **Version Control:** Git & GitHub

## 🚀 How to Run Locally
1. Run the Flask server in VS Code terminal:
   ```bash
   python Mediqueue.py
   ```
2. Open your browser and visit:
   * **Dashboard:** [http://127.0.0.1:8080/dashboard](http://127.0.0.1:8080/dashboard)
   * **TV Display:** [http://127.0.0.1:8080/tv](http://127.0.0.1:8080/tv)
   * **Patient Registration:** [http://127.0.0.1:8080/register](http://127.0.0.1:8080/register)
   * **React Tasks:** [http://127.0.0.1:8080/tasks](http://127.0.0.1:8080/tasks)
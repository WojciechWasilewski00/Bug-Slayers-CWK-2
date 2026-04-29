# 🚀 Engineering Teams Portal – CWK2

## 📌 Project Overview
This project is part of Coursework 2 and builds on the system designed in Coursework 1.  
The aim is to develop a **web-based Engineering Teams Portal** using Django, allowing users to manage teams, meetings, messaging, dependencies, and repositories.

The system must follow:
- ERD design from CWK1  
- Use case diagrams  
- Low and high-fidelity wireframes  

Tip for when to run server:
- python manage.py runserver in terminal

---

## 🧩 Core System Features

The application includes the following modules:

- 🔐 User Authentication (login/register/logout)
- 🏢 Departments and Teams
- 👥 Team Members management
- 🔗 Team Dependencies (upstream/downstream)
- 💬 Messaging system (user-to-user)
- 📅 Meeting Scheduling (Schedule module)
- 📂 Repository management

---

## 🧑‍💻 Individual Responsibilities

| Name | Module |
|------|--------|
| Jayne | Scheduling (Meetings) |
| Felipe | Voting / Sessions |
| Mariam | [Add module] |
| Heidi | Reports Page |
| Wojciech | Teams Page|

Each member is responsible for:
- Backend (models, views)
- Frontend (templates, UI)
- Testing their own feature

---

## 📅 Scheduling Module (Example – Jayne)

Includes:
- View schedule (monthly, weekly, upcoming)
- Create meeting
- Display meeting details
- (Optional) Edit/Delete meeting

---

## 🛠️ Technologies Used

- Python
- Django
- HTML, CSS (Bootstrap optional)
- SQLite
- Git & GitHub
- VS Code

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/WojciechWasilewski00/Bug-Slayers-CWK-2.git
cd Bug-Slayers-CWK-2

## How to upload to git
In group projects, always follow this "Golden Rule" to avoid these errors:

git pull (Start your day by getting the team's work).

Code (Do your amazing scheduling work).

git add .

git commit

git pull (One last check to see if anyone pushed while you were coding).

git push (Final upload).


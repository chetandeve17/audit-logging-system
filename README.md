# 🔐 Advanced Event Logging & Audit Trail System

<p align="center">
  <b>Track • Monitor • Secure • Analyze</b><br>
  Production-ready logging system with API & Dashboard 🚀
</p>

---

## 📌 Project Overview

The **Advanced Event Logging & Audit Trail System** is designed to track and record every action performed within a system.

This project is part of the **AI Interview and Assessment System** and now includes:

* ⚡ FastAPI backend integration
* 📊 Real-time dashboard visualization
* 📄 Structured logging system

---

## ✨ Features

* 📌 Full audit trail of all system actions
* ⏱️ Timestamp-based logging
* 🆔 Unique log ID for each event
* 👤 Tracks user ID and role
* 🧩 Module-based tracking (Auth, Assessment, etc.)
* 🌐 FastAPI API integration
* 📊 Streamlit dashboard for log visualization
* 📄 JSON-based storage

---

## 🧱 Project Structure

```
audit_project/
│── audit_logger.py      # Core logging module
│── main.py              # Basic simulation
│── app.py               # FastAPI backend
│── dashboard.py         # Streamlit dashboard
│── audit_logs.json      # Generated logs
```

---

## 🛠️ Tech Stack

| Technology   | Purpose          |
| ------------ | ---------------- |
| Python 🐍    | Core development |
| FastAPI ⚡    | Backend API      |
| Streamlit 📊 | Dashboard UI     |
| JSON 📄      | Log storage      |

---

## ▶️ Getting Started

### 🔹 Clone Repository

```
git clone https://github.com/chetandeve17/audit-logging-system.git
```

### 🔹 Navigate to Project

```
cd audit-logging-system
```

---

## 🚀 Run Backend (FastAPI)

```
uvicorn app:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/login
http://127.0.0.1:8000/start-test
http://127.0.0.1:8000/submit
```

---

## 📊 Run Dashboard

```
streamlit run dashboard.py
```

👉 Opens dashboard in browser showing logs

---

## 📊 Sample Log Output

```json
{
  "log_id": "a1b2c3",
  "timestamp": "2026-04-14 10:00:00",
  "user_id": "CAND001",
  "role": "Candidate",
  "action": "Login",
  "module": "Auth",
  "status": "Success",
  "details": "User logged in successfully"
}
```

---

## 🧠 How It Works

1. User performs an action
2. FastAPI API is triggered
3. Logger records event
4. Log stored in JSON file
5. Dashboard displays logs

---

## 🚀 Future Enhancements

* 🗄️ Database Integration (MySQL / MongoDB)
* ⚠️ Suspicious activity detection
* 📈 Real-time monitoring system
* 🔐 Authentication & security layer
* 📊 Advanced analytics dashboard

---

## 🏆 Key Highlights

✔ API-based logging system
✔ Real-time dashboard visualization
✔ Modular and scalable design
✔ Easy integration into any backend

---

## 👨‍💻 Author

**Chetan Deve**


<p align="center">
  Made with ❤️ by Chetan
</p>

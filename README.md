# 📌 RFP Processing Backend (FastAPI + PostgreSQL)

## 🚀 Overview

This project is a backend system for processing **RFP (Request for Proposal) documents**.

It allows you to:

* Create RFP sessions for clients
* Store questions extracted from RFPs
* Store multiple draft answers (with version control)

---

## 🧠 System Flow

Client RFP → Questions → Draft Answers

---

## 🏗️ Project Structure

```
rfp_project/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── database.py          # DB connection
│   │
│   ├── models/              # SQLAlchemy models
│   │    ├── rfp_session.py
│   │    ├── question.py
│   │    └── draft.py
│   │
│   ├── schemas/             # Pydantic schemas
│   │    └── rfp_schema.py
│   │
│   └── services/            # Business logic
│        └── rfp_service.py
│
├── alembic/                 # DB migrations
├── alembic.ini
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions (From Scratch)

### 1️⃣ Clone the Repository

```
git clone <your-repo-url>
cd rfp_project
```

---

### 2️⃣ Create Virtual Environment

#### Windows

```
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup PostgreSQL Database

Create a database:

```sql
CREATE DATABASE rfp_db;
```

---

### 5️⃣ Configure Database Connection

Update `app/database.py`:

```
DATABASE_URL = "postgresql://username:password@localhost:5432/rfp_db"
```

---

### 6️⃣ Run Migrations (Alembic)

```
alembic upgrade head
```

---

### 7️⃣ Start the Server

```
uvicorn app.main:app --reload
```

---

### 8️⃣ Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### 🔹 Create RFP

`POST /rfp`

```
{
  "client_name": "Google",
  "deadline": "2026-05-01T10:00:00"
}
```

---

### 🔹 Add Question

`POST /question`

```
{
  "text": "Explain your security architecture",
  "rfp_id": 1
}
```

---

### 🔹 Add Draft Answer

`POST /draft`

```
{
  "question_id": 1,
  "answer_text": "We use Zero Trust Architecture...",
  "version": 1
}
```

---

### 🔹 Get Questions

`GET /questions/{rfp_id}`

---

### 🔹 Get Drafts

`GET /drafts/{question_id}`

---

## 🗄️ Database Schema

### rfp_sessions

| rfp_id | client_name | deadline | status |

### questions

| question_id | text | rfp_id |

### drafts

| draft_id | question_id | answer_text | version |

---

## 🔍 Full Text Search (Optional)

```
CREATE INDEX idx_question_text
ON questions
USING GIN (to_tsvector('english', text));
```

---

## ❗ Common Issues & Fixes

### 1. Data not showing in PostgreSQL

* Ensure you are using the correct database:

```
SELECT current_database();
```

---

### 2. Schema issue (IMPORTANT)

Always query using:

```
SELECT * FROM public.rfp_sessions;
```

OR set default schema:

```
ALTER DATABASE rfp_db SET search_path TO public;
```

---

### 3. Alembic errors

```
alembic stamp head
```

---

### 4. Tables not created

```
alembic upgrade head
```

---

## ⚠️ What NOT To Do

❌ Do not run server without activating virtual environment
❌ Do not mismatch database name in code vs PostgreSQL
❌ Do not delete alembic versions manually
❌ Do not forget `db.commit()`
❌ Do not ignore schema (`public`) issues

---

## ✅ Best Practices

✔ Use `.env` file for DB credentials
✔ Use versioning for drafts
✔ Keep services separate from routes
✔ Always test APIs using Swagger/Postman

---

## 🚀 Future Improvements

* Upload RFP PDF and extract questions automatically
* AI-based answer generation
* Vector search for reusing past answers
* Frontend integration

---


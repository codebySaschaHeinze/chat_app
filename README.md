# Chat App Project (Django + Angular)

A small full-stack learning project consisting of a Django backend and an Angular frontend.
The project is built to practice a clean separation between backend (API) and frontend (SPA),
while still keeping the overall architecture simple and explicit.

The backend provides a JSON-based API for chat messages.
The frontend is a minimal Angular application that consumes this API directly via HTTP.

---

## Goal

Practice full-stack fundamentals in a realistic but controlled setup:

### Backend (Django)

- Django project and app structure
- Database models and migrations
- JSON API with GET, POST and DELETE
- Basic validation
- CSRF handling for API requests
- CORS configuration for cross-origin frontend access

### Frontend (Angular)

- Modern Angular (standalone components)
- HTTP communication with a backend API
- State handling and UI updates
- Minimal form handling without heavy abstractions
- Understanding Zone.js vs. zoneless change detection
- Basic CRUD interactions (create, read, delete)

---

## Tech Stack

### Backend

- Python
- Django
- SQLite (default Django database)
- django-cors-headers

### Frontend

- Angular (standalone setup)
- TypeScript
- HTML
- zone.js (classic Angular change detection)

---

### Project Layout

```text
chat_app/
├─ chat_app_backend/              Django backend
│  ├─ core/                       Django project (settings, urls, wsgi)
│  ├─ chat/                       Django app
│  │  ├─ migrations/
│  │  ├─ models.py
│  │  ├─ views.py
│  │  ├─ urls.py
│  │  └─ admin.py
│  ├─ db.sqlite3
│  ├─ manage.py
│  ├─ requirements.txt
│  └─ .venv/                      Virtual environment (not committed)
│
├─ chat_app_frontend/             Angular frontend
│  ├─ src/
│  │  ├─ app/
│  │  │  ├─ app.ts                Root component (standalone)
│  │  │  ├─ app.html              Template
│  │  │  └─ app.config.ts         Application configuration
│  │  ├─ main.ts
│  │  └─ polyfills.ts
│  ├─ package.json
│  ├─ package-lock.json
│  └─ angular.json
│
├─ .gitignore
└─ README.md
```

---

## Backend Overview

The backend exposes a simple REST-like API for chat messages.

### Model: Chat

- name (string)
- message (text)
- created_at (timestamp, UTC)

### Endpoints

- GET /chat/
  Returns all chat messages as JSON.
- POST /chat/
  Creates a new chat message.
- DELETE /chat/<id>/
  Deletes a chat message by ID.

All API responses are JSON.
CSRF protection is disabled for API endpoints to simplify frontend integration
(for learning purposes only).

---

## Frontend Overview

The frontend is a minimal Angular application that:

- Loads all chat messages on startup
- Displays messages as:
  Name: Message
  Timestamp (formatted)
- Allows creating new messages via two input fields
- Allows deleting messages via a per-message button

The frontend talks directly to the Django backend via absolute URLs.
CORS is enabled on the backend to allow this setup during development.

Zone.js is enabled to ensure automatic UI updates after HTTP requests.

---

## Setup (Local Development)

### Prerequisites

- Git
- Python 3.x
- Node.js (LTS recommended)
- npm (ships with Node)
- Optional: VS Code

Clone the repository

```text
git clone https://github.com/codebySaschaHeinze/chat_app.git
cd chat_app
```

---

### Backend Setup (Windows)

```text
cd chat_app_backend
```

Create and activate virtual environment:

```text
python -m venv .venv
.venv\Scripts\activate
```

Upgrade pip and install dependencies:

```text
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run migrations:

```text
python manage.py migrate
```

Start the backend:

```text
python manage.py runserver 8010
```

Test backend in browser:

http://127.0.0.1:8010/chat/

---

### Backend Setup (macOS / Linux)

```text
cd chat_app_backend
```

Create and activate virtual environment:

```text
python3 -m venv .venv
source .venv/bin/activate
```

Upgrade pip and install dependencies:

```text
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run migrations:

```text
python manage.py migrate
```

Start the backend:

```text
python manage.py runserver 8010
```

Test backend in browser:

http://127.0.0.1:8010/chat/

---

### Frontend Setup

Open a second terminal:

```text
cd chat_app_frontend
```

Install dependencies:

```text
npm install
```

Start the frontend:

```text
npm start
```

Open in browser:

http://localhost:4200

---

### Configuration Notes

Ports

- Django runs on: http://127.0.0.1:8010
- Angular runs on: http://localhost:4200

CORS (Backend)
For direct frontend-to-backend calls, CORS must allow the Angular origin.

Typical setting in core/settings.py:

- CORS_ALLOWED_ORIGINS = ["http://localhost:4200"]

Zone.js (Frontend)
Angular is configured to require Zone.js.
Ensure it is installed and imported, e.g. in src/main.ts:

- import 'zone.js';

---

### Common Troubleshooting

1. Connection refused (ERR_CONNECTION_REFUSED)

- Django server is not running
- Wrong port (check 8010)
- Verify in browser: http://127.0.0.1:8010/chat/

2. CORS errors in browser console

- CORS_ALLOWED_ORIGINS missing or wrong
- Make sure origin is exactly: http://localhost:4200
- Restart Django after changing settings

3. Angular blank page

- Check browser console for runtime errors
- Ensure zone.js is imported
- Ensure npm start is running in chat_app_frontend (not backend)

---

### API Quick Tests

Create a message (PowerShell):
$body = @{ name = "Testuser"; message = "Hello" } | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8010/chat/" -Method Post -ContentType "application/json" -Body $body

List messages:
Invoke-RestMethod -Uri "http://127.0.0.1:8010/chat/" -Method Get

Delete a message:
Invoke-RestMethod -Uri "http://127.0.0.1:8010/chat/1/" -Method Delete

---

## Notes

- This is a learning project, intentionally explicit and minimal.
- No authentication or permissions are implemented.
- CSRF exemptions and open CORS settings are for development only.
- The focus is on understanding data flow, not production hardening.
- Backend and frontend are deliberately kept decoupled.

License: Private learning project

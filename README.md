Staff Leave Management System (SLMS)
A robust and secure Django-based web application designed to automate, streamline, and manage employee leave registration and approval workflows.

---

🛠️ Tech Stack & Prerequisites
Backend Framework: Django (Python)
Database: SQLite (Default)
Frontend: HTML5, CSS3 (Bootstrap / Tailwind styled UI)
Environment: Python 3.8+

---

🚀 System Features
🔹 Admin Features
Dashboard Insights: Track real-time counts of pending, approved, and rejected leave requests.
Staff Management: Exhaustively register, edit credentials, or remove staff members from the workspace.
Request Lifecycle Control: Review submitted employee leaves with explicit `Approved` or `Rejected` actions.
🔹 Staff Features
Secure Registration: Register individual employee accounts with dedicated `Staff` roles.
Leave Application Tracking: Submit leaves with custom fields (Leave Type, Dates, Reason) and view real-time status updates.

---

🖥️ Screen Mockups & UI Workflow
Below are the key interfaces captured from the production build:

1. User Registration (`Admin` / `Staff`)
   Users can choose their appropriate role from a dynamic dropdown menu during sign-up.
   ![Registeration Page](<Screenshot (1370).png>)
2. Administrator Central Dashboard
   Provides quick access navigations to manage staff registers or review incoming employee requests.
   ![Admin Dashboard](<Screenshot (1371).png>)
3. Employee Directory Management
   An interactive table view that enables administrators to rapidly modify or delete staff records.
   ![Manage Staff Table](<Screenshot (1373).png>)
4. Record Update Form
   Allows an administrator to modify profile credentials such as usernames and encrypted passwords.
   ![Edit Staff Screen](<Screenshot (1374).png>)
5. Staff Leave Requests Tracker
   The central hub where incoming leaves are reviewed, tracked, and structurally managed through approval actions.
   ![Staff Leave Requests](<Screenshot (1372).png>)

---

🔌 System API & View Endpoints
The project maps standard CRUD paths to manage staff users and application statuses:
Method Endpoint Pattern Description Access Control
GET / POST `/register/` Renders and processes the user registration form Public
GET `/admin_dashboard/` Core workspace landing page for administrative stats Admin Only
GET `/manage_staff/` Lists all registered workspace staff employees Admin Only
GET / POST `/edit_staff/<int:id>/` Fetches edit forms or updates a specific staff profile Admin Only
POST / DELETE `/delete_staff/<int:id>/` Deletes a target staff user from the system Admin Only
GET `/leave/view/` Tabulates all staff leave applications and current statuses Authenticated
POST `/leave/action/<int:id>/<str:status>/` Updates leave request status (`Approved`/`Rejected`) Admin Only
POST `/logout/` Terminates session cookie and safely redirects user Authenticated

---

⚡ Installation & Quick Start

1. Clone & Set Up Virtual Environment

```bash
git clone https://github.com/yourusername/slms.git
cd slms

# Create environment
python -m venv venv
source venv/bin/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install Project Requirements

```bash
pip install django
```

3. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Boot Up Local Development Server

```bash
python manage.py runserver
```

Visit the local server environment at http://127.0.0.1:8000/ inside your browser.

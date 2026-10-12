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
   <img width="2880" height="1800" alt="Registationpage" src="https://github.com/user-attachments/assets/e8b4696f-dfd6-4682-8a1e-3e0d8b0fad2f" />

2. Administrator Central Dashboard
   Provides quick access navigations to manage staff registers or review incoming employee requests.
   <img width="2880" height="1800" alt="Dashboardpage" src="https://github.com/user-attachments/assets/b2d45bca-4a8b-458a-a903-e2eb5fe66fe6" />


3. Employee Directory Management
   An interactive table view that enables administrators to rapidly modify or delete staff records.
  <img width="2880" height="1800" alt="Screenshot (1505)" src="https://github.com/user-attachments/assets/feaaaae7-2021-40cc-a25a-634039c77e3b" />

4. Record Update Form
   Allows an administrator to modify profile credentials such as usernames and encrypted passwords.
  <img width="2880" height="1800" alt="Screenshot (1506)" src="https://github.com/user-attachments/assets/170cefd5-5600-4bd4-9899-ea24beb4622b" />

5. Staff Leave Requests Tracker
   The central hub where incoming leaves are reviewed, tracked, and structurally managed through approval actions.
 <img width="2880" height="1800" alt="Leaverequest" src="https://github.com/user-attachments/assets/98cfe164-3ed2-4b0b-90ce-b6974df6dd6a" />


---

🔌 System API & View Endpoints
The project maps standard CRUD paths to manage staff users and application statuses:
Method Endpoint Pattern Description Access Control
## System API & View Endpoints

The project maps standard CRUD paths to manage staff users and leave application statuses.

| Method | Endpoint | Description | Access Control |
|---|---|---|---|
| GET / POST | `/register/` | Renders and processes the user registration form | Public |
| GET | `/admin_dashboard/` | Displays the administrative dashboard and statistics | Admin Only |
| GET | `/manage_staff/` | Lists all registered staff employees | Admin Only |
| GET / POST | `/edit_staff/<int:id>/` | Displays the edit form or updates a staff profile | Admin Only |
| POST | `/delete_staff/<int:id>/` | Deletes a selected staff user | Admin Only |
| GET | `/leave/view/` | Displays staff leave applications and their current statuses | Authenticated |
| POST | `/leave/action/<int:id>/<str:status>/` | Updates a leave request status to Approved or Rejected | Admin Only |
| POST | `/logout/` | Logs out the user and redirects to the appropriate page | Authenticated |


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

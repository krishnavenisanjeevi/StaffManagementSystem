# Staff Leave Management System

A web-based Staff Leave Management System built with Django that helps organizations manage employee leave requests efficiently. The system allows employees to apply for leave online, while administrators can review, approve, or reject requests through an easy-to-use dashboard.

---

## Features

### Admin
- Admin Login
- Dashboard with leave statistics
- Add, Update, Delete Employees
- Manage Departments
- View all leave requests
- Approve or Reject leave applications
- Track leave history
- Search employees and leave records

### Employee
- Secure Login
- View Personal Dashboard
- Apply for Leave
- View Leave Status
- Check Leave History
- Update Profile
- Change Password

---

## Technologies Used

- Python 3.x
- Django
- HTML5
- CSS3
- SQLite (Default Database)
- Django ORM

---

## Database Models

### Employee
- Employee ID
- Full Name
- Email
- Department
- Designation
- Phone Number

### Department
- Department Name
- Description

### Leave Request
- Employee
- Leave Type
- Start Date
- End Date
- Reason
- Status (Pending / Approved / Rejected)
- Applied Date

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/staff-leave-management.git
```

### Navigate to Project

```bash
cd staff-leave-management
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```

---

## Screenshots

- Login Page
- Admin Dashboard
- Employee Dashboard
- Apply Leave Page
- Leave Request List
- Leave Approval Page

(Add screenshots here)

---

## Future Enhancements

- Email Notifications
- Leave Balance Calculation
- Calendar View
- Role-Based Authentication


---

## Learning Outcomes

- Django Authentication
- Django ORM
- CRUD Operations
- Model Relationships
- Forms & Validation
- Admin Customization
- Bootstrap UI
- Session Management
- Role-Based Access Control

---

## Author

**Krishna Sanjeevi**

- Python Full Stack Developer
- Django | React | Flutter Developer

---

## License

This project is developed for educational and learning purposes.

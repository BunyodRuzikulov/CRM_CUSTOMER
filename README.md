Django CRM System
A simple Customer Relationship Management (CRM) system built with Django, designed to manage clients, track activities, and handle notifications. The application features a user-friendly interface styled with Tailwind CSS and supports basic CRUD operations for clients and notifications, along with a customizable settings page.
Features

Client Management: Add, view, edit, and delete client records with details like name, phone, email, company, status, and notes.
Activity Tracking: Log client-related activities automatically (e.g., when a client is added or updated).
Notifications: Create and manage notifications with a calendar view for scheduling.
Settings: Customize the interface language and background color.
Responsive Design: Built with Tailwind CSS for a modern, mobile-friendly UI.
Admin Panel: Manage all data via Django’s built-in admin interface.

Technologies

Backend: Django 4.2+
Frontend: HTML, Tailwind CSS (via CDN)
Database: SQLite (default, configurable for PostgreSQL/MySQL)
Python: 3.8+

Installation
Prerequisites

Python 3.8 or higher
Git
Virtualenv (optional but recommended)

Setup

Clone the Repository:
git clone https://github.com/yourusername/django-crm.git
cd django-crm


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Apply Migrations:
python manage.py makemigrations
python manage.py migrate


Create a Superuser (for admin access):
python manage.py createsuperuser


Run the Development Server:
python manage.py runserver

Access the app at http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin/.


Usage

Home Page: View statistics (total clients, active clients, new clients) and recent client additions.
Clients List: Browse, search, and filter clients by name, status, or date.
Add Client: Create a new client with details like name, phone, email, and status.
Client Profile: View client details, activity history, and perform edit/delete actions.
Edit Client: Update existing client information.
Notifications: Manage notifications and view them on a calendar.
Settings: Change the interface language (O‘zbek, English, Russian) and background color.
![image](https://github.com/user-attachments/assets/1f7be92a-87dd-44c2-ad2d-94df4d2ec7ca)


Project Structure
django-crm/
├── crm/
│   ├── migrations/
│   ├── templates/crm/
│   │   ├── index.html
│   │   ├── clients.html
│   │   ├── add_client.html
│   │   ├── client_profile.html
│   │   ├── edit_client.html
│   │   ├── notifications.html
│   │   ├── settings.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
├── crm_project/
│   ├── settings.py
│   ├── urls.py
├── manage.py
├── requirements.txt
├── README.md

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit (git commit -m 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

Please ensure your code follows PEP 8 guidelines and includes tests where applicable.
Contact
https://t.me/Bunyod_Ruziqulov

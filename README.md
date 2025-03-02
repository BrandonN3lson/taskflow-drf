TaskFlow DRF API
================

TaskFlow is a Django Rest Framework (DRF) API that helps users manage tasks, categories, and task-related file uploads. This API provides authentication, task management, and file uploads using Cloudinary.

[Click here](https://task-flow-drf-api-6a658d5dbfee.herokuapp.com/) to view deployed TaskFlow DRF API

## Contents
- [Features](#features)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [Categories](#categories)
  - [Tasks](#tasks)
  - [Task Files](#task-files)
- [Manual Testing Table](#manual-testing-table)
- [Technologies Used](#technologies-used)

---

Features
--------

*   User authentication with JWT tokens.
    
*   CRUD operations for tasks and categories.
    
*   Task file uploads via Cloudinary.
    
*   Filter, search, and order tasks.
    
*   Retrieve tasks due soon.
    

Installation
------------

1. ### Clone the repository
        git clone https://github.com/BrandonN3lson/taskflow-drf.git
    
2. ### Create a virtual environment & activate it:
        python -m venv .venv
        source venv/bin/activate
    
3. ### Install Dependencies:   
        pip install -r requirements.txt
    
4. ### Setup environment variables (create a `.env` file and add the following)
        SECRET_KEY=<your_secret_key>
        DEBUG=True
        DATABASE_URL=<your_database_url>
        CLOUDINARY_URL=<your_cloudinary_url>
    
5. ### Apply migrations & create superuser:
        python manage.py migrate
        python manage.py createsuperuser
    
6. ### Run the server:
        python manage.py runserver
    

API Endpoints
-------------

### Authentication

*   `POST /dj-rest-auth/login/` – Log in a user.
    
*   `POST /dj-rest-auth/logout/` – Log out the user.
    
*   `POST /dj-rest-auth/registration/` – Register a new user.
    
*   `POST /dj-rest-auth/token/refresh/` – Refresh JWT token.
    

### Categories

*   `GET /categories/` – List all categories.
    
*   `POST /categories/` – Create a new category.
    
*   `GET /categories/<id>/` – Retrieve a specific category.
    
*   `PATCH /categories/<id>/` – Update a category.
    
*   `DELETE /categories/<id>/` – Delete a category.
    

### Tasks

*   `GET /tasks/` – List all tasks.
    
*   `POST /tasks/` – Create a new task.
    
*   `GET /tasks/<id>/` – Retrieve a specific task.
    
*   `PATCH /tasks/<id>/` – Update a task.
    
*   `DELETE /tasks/<id>/` – Delete a task.
    
*   `GET /tasks/due-soon/` – Retrieve tasks due this week or overdue.
    

### Task Files

*   `GET /task-files/` – List all task files.
    
*   `POST /task-files/` – Upload a task file.
    
*   `GET /task-files/<id>/` – Retrieve a specific task file.
    
*   `DELETE /task-files/<id>/` – Delete a task file.
    
Tests
-----

### Manual Testing Table

| Test Case | Endpoint | Method | Expected Result | Result |
|-----------|----------|--------|----------------|---------|
| Register a user | `/dj-rest-auth/registration/` | POST | User is registered | Pass |
| Log in a user | `/dj-rest-auth/login/` | POST | User receives authentication token | Pass |
| Create a category | `/categories/` | POST | Category is created | Pass |
| Retrieve all categories | `/categories/` | GET | List of categories | Pass |
| Update a category | `/categories/<id>/` | PATCH | Category is updated | Pass |
| Delete a category | `/categories/<id>/` | DELETE | Category is deleted | Pass |
| Create a task | `/tasks/` | POST | Task is created | Pass |
| Retrieve all tasks | `/tasks/` | GET | List of tasks | Pass |
| Update a task | `/tasks/<id>/` | PATCH | Task is updated | Pass |
| Delete a task | `/tasks/<id>/` | DELETE | Task is deleted | Pass |
| Retrieve tasks due soon | `/tasks/due-soon/` | GET | List of tasks due this week or overdue | Pass |
| Upload a task file | `/task-files/` | POST | File is uploaded | Pass |
| Retrieve task files | `/task-files/` | GET | List of uploaded files | Pass |
| Delete a task file | `/task-files/<id>/` | DELETE | File is deleted | Pass |


Technologies Used
-----------------

*   **Django Rest Framework** – API development
*   **PostgreSQL** – Database for deployed app
*    **SqleLite** - Databse for Dev environment
*   **Cloudinary** – Media storage
*   **JWT Authentication** – Secure user authentication

### Tools
- **GitPod**: For coding environment.    
- **Gunicorn**: For serving the application in production.  
- **Django Allauth**: For user authentication and management.  
- **Psycopg**: PostgreSQL database adapter for Django.  

References
----------

- [Code Institute](https://codeinstitute.net/)
- [Django queryset operators](https://docs.djangoproject.com/en/dev/ref/models/querysets/#field-lookups) used in the task view queryset to filter tasks due within the current week
- [TimeDelta](https://medium.com/django-unleashed/python-timedelta-with-examples-and-use-cases-81def9140880) used to filter tasks due within the current week
- [dj-rest-auth v2.1.9](https://dj-rest-auth.readthedocs.io/en/2.1.9/installation.html) user registration and authentication
- [Cloudinary](https://cloudinary.com/) for file storage
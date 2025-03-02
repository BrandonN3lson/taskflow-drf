from django.urls import path
from tasks.views import TaskList, TaskDetail, TasksDueSoon

"""
URLs for Task API endpoints.

Defines the URLs for managing Task objects, allowing users to create, list,
retrieve, update, and delete tasks, as well as view tasks due soon.

Endpoints:
    - `tasks/` (GET, POST): List all tasks or create a new task.
    - `tasks/<int:pk>/` (GET, PUT, PATCH, DELETE): Retrieve, update, or delete
      a specific task.
    - `tasks/due-soon/` (GET): Retrieve tasks that are due soon.

Views:
    - TaskList: Handles listing and creating tasks.
    - TaskDetail: Handles retrieving, updating, and deleting a specific task.
    - TasksDueSoon: Handles retrieving tasks that are due within the current
      week or overdue.
"""

urlpatterns = [
    path("tasks/", TaskList.as_view()),
    path("tasks/<int:pk>/", TaskDetail.as_view()),
    path("tasks/due-soon/", TasksDueSoon.as_view()),
]

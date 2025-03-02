from django.urls import path
from task_files import views

"""
URLs for TaskFile API endpoints.

Defines the URLs for managing TaskFile objects,
allowing users to upload, list, retrieve, and delete task-related files.

Endpoints:
    - `task-files/` (GET, POST): List all task files or upload a new file.
    - `task-files/<int:pk>/` (GET, DELETE): Retrieve or delete a specific task
       file.

Views:
    - TaskFileList: Handles listing and creating task files.
    - TaskFileDetail: Handles retrieving and deleting a specific task file.
"""

urlpatterns = [
    path("task-files/", views.TaskFileList.as_view()),
    path("task-files/<int:pk>/", views.TaskFileDetail.as_view()),
]

from django.urls import path
from task_files import views

urlpatterns = [
    path('task-files/', views.TaskFileList.as_view()),
    path('task-files/<int:pk>/', views.TaskFileDetail.as_view())
]

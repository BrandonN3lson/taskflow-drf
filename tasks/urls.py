from django.urls import path
from tasks.views import TaskList, TaskDetail, TasksDueSoon

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),
    path('tasks/due-soon/', TasksDueSoon.as_view()),
]

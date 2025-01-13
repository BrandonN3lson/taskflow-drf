from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('categories.urls')),
    path('', include('tasks.urls')),
    path('', include('task_files.urls')),
]
from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route
from dj_rest_auth.views import LoginView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserList

"""
URL configuration for the project.

This module defines the URL patterns for the Django project, including
routes for authentication, user management, and app-specific endpoints.

Routes:
    - "" (root route): Handles requests to the root URL.
    - "admin/": Django admin panel.
    - "api-auth/": Authentication routes for the Django REST Framework.
    - "dj-rest-auth/logout/": Custom logout route.
    - "dj-rest-auth/login/": Login endpoint using dj-rest-auth.
    - "dj-rest-auth/token/refresh/": Token refresh endpoint using JWT.
    - "dj-rest-auth/": Includes all dj-rest-auth authentication URLs.
    - "dj-rest-auth/registration/": Handles user registration via dj-rest-auth.
    - "users/": User list endpoint.
    - Includes additional routes for categories, tasks, and task files.

"""

urlpatterns = [
    path("", root_route),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("dj-rest-auth/logout/", logout_route),
    path("dj-rest-auth/login/", LoginView.as_view()),
    path("dj-rest-auth/token/refresh/", TokenRefreshView.as_view()),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/",
         include("dj_rest_auth.registration.urls")),
    path("users/", UserList.as_view()),
    path("", include("categories.urls")),
    path("", include("tasks.urls")),
    path("", include("task_files.urls")),
]

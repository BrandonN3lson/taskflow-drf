from django.urls import path
from categories.views import CategoryList, CategoryDetail

"""
URL configuration for category-related endpoints.

This module defines the URL patterns for managing categories in the API.
It includes endpoints for listing all categories and retrieving, updating,
or deleting a specific category by its primary key (pk).

Endpoints:
    - GET /categories/ : Retrieve a list of all categories.
    - POST /categories/ : Create a new category.
    - GET /categories/<int:pk>/ : Retrieve a specific category by ID.
    - PUT /categories/<int:pk>/ : Update a specific category.
    - DELETE /categories/<int:pk>/ : Delete a specific category.
"""

urlpatterns = [
    path("categories/", CategoryList.as_view()),
    path("categories/<int:pk>/", CategoryDetail.as_view()),
]

from django.contrib import admin
from .models import Category

"""
Admin configuration for the Category model.

This file registers the Category model with the Django admin site,
allowing it to be managed through the admin interface.
"""

admin.site.register(Category)

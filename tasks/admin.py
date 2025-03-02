from django.contrib import admin
from .models import Task

"""
Admin configuration for the Task model.

This file registers the Task model with the Django admin site,
allowing it to be managed through the admin interface.
"""

admin.site.register(Task)

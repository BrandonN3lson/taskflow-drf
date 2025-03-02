from django.contrib import admin
from .models import TaskFile

"""
Admin configuration for the TaskFiles model.

This file registers the TaskFiles model with the Django admin site,
allowing it to be managed through the admin interface.
"""

admin.site.register(TaskFile)

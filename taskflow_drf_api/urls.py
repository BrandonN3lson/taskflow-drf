from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('categories.urls')),
# ]

try:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('categories.urls')),
    ]
except Exception as e:
    import logging
    logging.error("Error loading categories.urls: %s", e)
    raise
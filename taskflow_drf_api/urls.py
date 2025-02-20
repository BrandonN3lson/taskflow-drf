from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route
from dj_rest_auth.views import LoginView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserList

urlpatterns = [
    path("", root_route),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('dj-rest-auth/logout/', logout_route),

    path('dj-rest-auth/login/', LoginView.as_view()),
    path('dj-rest-auth/token/refresh/', TokenRefreshView.as_view()),
    
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/",
         include("dj_rest_auth.registration.urls")
         ),
    path('users/', UserList.as_view()),
    path("", include("categories.urls")),
    path("", include("tasks.urls")),
    path("", include("task_files.urls")),
]

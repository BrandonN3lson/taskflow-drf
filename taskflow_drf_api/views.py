from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from .settings import (
    JWT_AUTH_COOKIE,
    JWT_AUTH_REFRESH_COOKIE,
    JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)

"""
Views for user management and authentication.

- UserList: Retrieves a list of all registered users.
- root_route: Displays a welcome message for the API root.
- logout_route: Logs out the user by clearing authentication cookies.
"""


class UserList(generics.ListAPIView):
    """
    API view to retrieve a list of all registered users.

    Methods:
    - GET: Returns a list of all users.

    Attributes:
    - serializer_class: Specifies the serializer used (UserSerializer).
    - queryset: Retrieves all users from the database.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


@api_view()
def root_route(request):
    """
    root_rout shows main message when page loads,
    taken from  code Institute moments react project.
    """
    return Response(
        {
            "message": (
                "Welcome to taskFlow DRF API.",
                "At the end of the URL, type either: ",
                "- '/categories' ",
                "- '/tasks' ",
                "- '/task-files'",
                "to view the respective endpoints.",
            )
        }
    )


@api_view(["POST"])
def logout_route(request):
    """
    taken from  code Institute moments react project.

    Logs out the user by clearing authentication cookies.

    This function removes both the access and refresh JWT cookies,
    effectively logging out the user.

    Returns:
        Response: An empty response with cleared authentication cookies.
    """
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response

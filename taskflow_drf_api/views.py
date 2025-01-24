from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User


from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)
from rest_framework import generics


class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

@api_view()
def root_route(request):
    """
    root_rout shows main message when page loads,
    taken from  code Institute moments react project.
    """
    return Response({
        "message": (
            "Welcome to taskFlow DRF API.",
            "At the end of the URL, type either: ",
            "- '/categories' ",
            "- '/tasks' ",
            "- '/task-files'",
            "to view the respective endpoints.",
        )
    })


@api_view(['POST'])
def logout_route(request):
    """
    taken from  code Institute moments react project.
    """
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    This serializer is used to convert User model into JSON
    representations. It includes the `id` and `username` fields,
    ensuring that `username` is a required field.

    Fields:
        - `id` (int): The unique identifier for the user.
        - `username` (str): The username of the user (required).

    Meta:
        - `model`: User (Django's built-in user model).
        - `fields`: Specifies the fields included in the serialized output.
        - `extra_kwargs`: Ensures the `username` field is always required.
    """

    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]
        extra_kwargs = {"username": {"required": True}}

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'id', 'username',
        ]
        extra_kwargs = {
            'username': {'required': True}
        }

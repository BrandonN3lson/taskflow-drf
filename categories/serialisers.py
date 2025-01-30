from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Category
        fields = [
            'id', 'user', 'title',
            'created_at', 'updated_at'
        ]

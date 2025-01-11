from rest_framework import serializers
from .models import Task


class TaskSerializer (serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'id', 'user', 'title', 'description',
            'category', 'status', 'priority',
            'due_date', 'created_at', 'updated_at',
        ]


class TaskTitleSerializer (serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'title',
        ]
from rest_framework import serializers
from .models import TaskFile
from tasks.serializers import TaskTitleSerializer


class TaskFileSerializer (serializers.ModelSerializer):
    task_title = TaskTitleSerializer(source='task', read_only=True)

    class Meta:
        model = TaskFile
        fields = [
            'id', 'task', 'task_title', 'file', 'uploaded_at'
        ]

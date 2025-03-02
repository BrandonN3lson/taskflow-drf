from rest_framework import serializers
from .models import TaskFile
from tasks.serializers import TaskTitleSerializer


class TaskFileSerializer(serializers.ModelSerializer):
    """
    Serializer for the TaskFile model.

    Provides a serialized representation of TaskFile objects, including
    the associated task title.

    - Attributes:
        - task_title (TaskTitleSerializer): A read-only field that displays
          the title of the associated task.

    - Meta:
        - model: Specifies the TaskFile model.
        - fields: Defines the fields to be serialized, including `id`, `task`,
          `task_title`, `file`, and `uploaded_at`.
    """

    task_title = TaskTitleSerializer(source="task", read_only=True)

    class Meta:
        model = TaskFile
        fields = ["id", "task", "task_title", "file", "uploaded_at"]

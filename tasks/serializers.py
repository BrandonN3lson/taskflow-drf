from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from datetime import datetime
from .models import Task, Category

"""
Serializers for the Task model.

TaskSerializer:
    - Serializes Tasks with additional fields
      such as `is_overdue`, `days_left`, `created_at`, and `updated_at`.
    - Restricts category selection to only the authenticated user.

TaskTitleSerializer:
    - A simplified serializer for retrieving only the task title.
"""


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.

    - Includes additional fields such as `is_overdue`, `days_left`,
      `created_at`, and `updated_at`.
    - Filters category selection to only those belonging to the authenticated 
      user.
    """

    owner = serializers.ReadOnlyField(source="user.username")
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.none()
        )
    is_overdue = serializers.SerializerMethodField()
    days_left = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    due_date = serializers.DateTimeField(required=False, allow_null=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "owner",
            "title",
            "description",
            "category",
            "status",
            "priority",
            "due_date",
            "days_left",
            "is_overdue",
            "created_at",
            "updated_at",
        ]

    def __init__(self, *args, **kwargs):
        """
        Filters the category 
        queryset based on the authenticated user.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments, including the request context.
        """
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request:
            self.fields["category"].queryset = Category.objects.filter(
                user=request.user
            )

    def get_created_at(self, obj):
        """
        Returns a time for when the task was created.

        Args:
            obj (Task): The task instance.

        Returns:
            str: A string representing the time created.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Returns a time for when the task was last updated.

        Args:
            obj (Task): The task instance.

        Returns:
            str: A string representing the time last updated.
        """
        return naturaltime(obj.updated_at)

    def get_days_left(self, obj):
        """
        Calculates the number of days left until the due date.
        Returns None if the task is marked as completed.

        Args:
            obj (Task): The task instance.

        Returns:
            int | None: Number of days left until the due date,
            or None if completed.
        """

        if obj.status == "completed":
            return None

        today = datetime.now().date()
        due_date = obj.due_date
        if due_date is not None:
            due_date = obj.due_date.date()
            days_left = (due_date - today).days
            return days_left
        return None

    def get_is_overdue(self, obj):
        """
        Determines if the task is overdue based on the due date.
        A task is overdue if its due date is in the past and it is 
        not completed.

        Args:
            obj (Task): The task instance.

        Returns:
            bool: True if the task is overdue, False otherwise.
        """

        today = datetime.now().date()

        if obj.status == "completed":
            return False

        if obj.due_date and obj.due_date.date() < today:
            return True
        return False


class TaskTitleSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving only the task title.
    """
    class Meta:
        model = Task
        fields = [
            "title",
        ]

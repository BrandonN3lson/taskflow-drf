from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from datetime import datetime
from .models import Task, Category


class TaskSerializer (serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
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
            'id', 'owner', 'title', 'description',
            'category', 'status', 'priority',
            'due_date', 'days_left', 'is_overdue', 'created_at', 'updated_at',
        ]

    def __init__(self, *args, **kwargs):
        # filter categories for the authenticated user
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            self.fields['category'].queryset = Category.objects.filter(
                user=request.user
                )

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def get_days_left(self, obj):
        if obj.status == 'completed':
            return None

        today = datetime.now().date()
        due_date = obj.due_date
        if due_date is not None:
            due_date = obj.due_date.date()
            days_left = (due_date - today).days
            return days_left
        return None

    def get_is_overdue(self, obj):
        today = datetime.now().date()

        if obj.status == 'completed':
            return False

        if obj.due_date and obj.due_date.date() < today:
            return True
        return False


class TaskTitleSerializer (serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'title',
        ]

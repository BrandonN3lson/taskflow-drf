from rest_framework import generics, filters
from datetime import datetime, timedelta
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

"""
Views for managing Task model.

- TaskList: Handles listing and creating tasks.
- TaskDetail: Handles retrieving, updating, and deleting a task.
- TasksDueSoon: Retrieves tasks that are due within the current week or
  overdue.
"""


class TaskList(generics.ListCreateAPIView):
    """
    API view for listing and creating tasks.

    - Requires authentication.
    - Supports filtering, searching, and ordering.

    Filtering:
    - Searchable fields: `title`, `category__title`
    - Ordering fields: `created_at`, `priority`

    Methods:
    - `get_queryset()`: Returns tasks belonging to the authenticated user.
    - `perform_create()`: Saves a new task under the authenticated user.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["title", "category__title"]
    ordering_fields = ["created_at", "priority"]

    def get_queryset(self):
        """
        Retrieves tasks belonging to the authenticated user.

        Returns:
            QuerySet: A filtered list of tasks for the logged-in user.
        """
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Assigns the authenticated user to the task before saving.

        Args:
            serializer (TaskSerializer): The serializer instance.
        """
        serializer.save(user=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a task.

    - Requires authentication.

    Methods:
    - `get_queryset()`: Returns only tasks owned by the authenticated user.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        """
        Retrieves the task belonging to the authenticated user.

        Returns:
            QuerySet: A filtered list of tasks for the logged-in user.
        """
        return Task.objects.filter(user=self.request.user)


class TasksDueSoon(generics.ListAPIView):
    """
    API view for retrieving tasks due soon or overdue.

    - Requires authentication.
    - Retrieves tasks:
      - Due within the current week (Monday to Sunday).
      - Overdue tasks (due before today).

    Methods:
    - `get_queryset()`: Filters tasks based on due dates.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Retrieves tasks that are due within the current week or are overdue.

        Returns:
            QuerySet: A list of tasks that are due soon or overdue.
        """
        today = datetime.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        queryset = Task.objects.filter(
            user=self.request.user, due_date__isnull=False
        ).filter(due_date__range=(
            start_of_week, end_of_week
            )) | Task.objects.filter(
            user=self.request.user, due_date__lt=today
        )

        return queryset

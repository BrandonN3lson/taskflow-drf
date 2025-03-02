from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import TaskFile
from .serializers import TaskFileSerializer
from rest_framework.permissions import IsAuthenticated

"""
API views for managing TaskFile objects.

These views allow authenticated users to list, create, retrieve, and delete
task-related files. Users can only access files associated with their own
tasks.

Views:
    - TaskFileList: Handles listing and creating task files.
    - TaskFileDetail: Handles retrieving and deleting specific task files.

Filtering:
    - Searchable fields: `task__title`
    - Ordering fields: `uploaded_at`
"""


class TaskFileList(generics.ListCreateAPIView):
    """
    API view to list and create TaskFiles.

    This view allows authenticated users to:
    - Retrieve a list of their uploaded task files.
    - Upload new files linked to their tasks.

    Attributes:
        - permission_classes (list): Restricts access to authenticated users.
        - serializer_class (TaskFileSerializer): Serializer used for TaskFile
          objects.
        - queryset (QuerySet): Queryset for TaskFile objects.
        - filter_backends (list): Enables filtering, searching, and ordering.
        - search_fields (list): Allows searching by `task__title`.
        - ordering_fields (list): Enables ordering by `uploaded_at`.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = TaskFileSerializer
    queryset = TaskFile.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["task__title"]
    ordering_fields = ["uploaded_at"]

    def get_queryset(self):
        """
        Restricts the queryset to files belonging to tasks owned by the
        authenticated user.
        """
        return TaskFile.objects.filter(task__user=self.request.user)


class TaskFileDetail(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve and delete a TaskFiles.

    This view allows authenticated users to:
    - Retrieve details of a specific task file.
    - Delete a file associated with their own tasks.

    Attributes:
        - permission_classes (list): Restricts access to authenticated users.
        - serializer_class (TaskFileSerializer): Serializer used for TaskFile
          objects.
        - queryset (QuerySet): Queryset for TaskFile objects.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = TaskFileSerializer
    queryset = TaskFile.objects.all()

    def get_queryset(self):
        """
        Restricts the queryset to files belonging to tasks owned by the
        authenticated user.
        """
        return TaskFile.objects.filter(task__user=self.request.user)

from rest_framework import generics, filters
from datetime import datetime, timedelta
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class TaskList(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    filter_backends = [
                       DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter
                       ]
    search_fields = ['title', 'category__title']
    ordering_fields = ['created_at', 'priority']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TasksDueSoon(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        today = datetime.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        queryset = Task.objects.filter(
            user=self.request.user,
            due_date__isnull=False
        ).filter(
            due_date__range=(start_of_week, end_of_week)
        ) | Task.objects.filter(
            user=self.request.user,
            due_date__lt=today
        )

        return queryset

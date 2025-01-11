from rest_framework import generics, filters
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
    search_fields = ['title', 'category__name']
    ordering_fields = ['created_at', 'priority']

    def perform_create(self, serialiser):
        serialiser.save(user=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

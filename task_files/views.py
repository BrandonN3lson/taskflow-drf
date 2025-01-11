from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import TaskFile
from .serializers import TaskFileSerializer
from rest_framework.permissions import IsAuthenticated


class TaskFileList(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = TaskFileSerializer
    queryset = TaskFile.objects.all()

    filter_backends = [
                       DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter
                       ]
    search_fields = ['task__title']
    ordering_fields = ['uploaded_at']


class TaskFileDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = TaskFileSerializer
    queryset = TaskFile.objects.all()

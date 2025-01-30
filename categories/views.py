from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category
from .serialisers import CategorySerializer
from rest_framework.permissions import IsAuthenticated


class CategoryList(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
                       DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter
                       ]
    search_fields = ['title', 'user__username']
    ordering_fields = ['-created_at']

    def perform_create(self, serialiser):
        serialiser.save(user=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

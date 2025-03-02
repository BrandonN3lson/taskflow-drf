from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category
from .serialisers import CategorySerializer
from rest_framework.permissions import IsAuthenticated

"""
Views for managing Category objects.

This provides API views for listing, creating, retrieving, updating,
and deleting categories. It uses authentication, ensuring that
users can only access their own categories.

Classes:
    - CategoryList: Handles listing all categories for the authenticated user
      and allows the creation of new categories.
    - CategoryDetail: Handles retrieving, updating, or deleting a specific
      category that belongs to the authenticated user.
"""


class CategoryList(generics.ListCreateAPIView):
    """
    API view for listing and creating categories.

    - GET: Returns a list of categories that belong to the user.
    - POST: Allows the user to create a new category.

    Filtering and Searching:
        - Filters categories by the authenticated user.
        - Allows searching by category title and username.
        - Supports ordering by creation date.

    Permissions:
        - Requires authentication.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["title", "user__username"]
    ordering_fields = ["-created_at"]

    def get_queryset(self):
        """Returns categories belonging to the user."""
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serialiser):
        """Assigns the user as the category owner before saving."""
        serialiser.save(user=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a single category.

    - GET: Returns details of a specific category that belongs to the
           authenticated user.
    - PUT/PATCH: Updates the category if the authenticated user owns it.
    - DELETE: Deletes the category if it belongs to the authenticated user.

    Permissions:
        - Requires authentication.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        """Returns the requested category if it belongs to the user."""
        return Category.objects.filter(user=self.request.user)

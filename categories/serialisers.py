from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.

    This serializer converts Category model instances into JSON format
    and ensures that the 'user' field is read-only, displaying the
    associated user's username instead of the user ID.

    Fields:
        - id (int): The unique identifier of the category.
        - user (str): The username of the category owner (read-only).
        - title (str): The title of the category.
        - created_at (datetime): The timestamp when the category was created.
        - updated_at (datetime): The timestamp when the category was last
          updated.
    """

    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Category
        fields = ["id", "user", "title", "created_at", "updated_at"]

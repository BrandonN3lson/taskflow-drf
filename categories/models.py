from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Represents a category that users can create for organizing tasks.

    Attributes:
        user (User): A ForeignKey linking the category to a specific user.
        title (str): The name of the category, limited to 100 characters.
        created_at (DateTime): The timestamp when the category was created.
        updated_at (DateTime): The timestamp when the category was last
        updated.

    Meta:
        ordering (list): Orders categories by creation date in descending
        order.
        unique_together (tuple): Ensures each user can have only one category
        with the same title.

    Methods:
        __str__(): Returns the title of the category as its string
        representation.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("user", "title")

    def __str__(self):
        return self.title

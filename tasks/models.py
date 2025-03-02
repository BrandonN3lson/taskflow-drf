from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

status_choices = [
    ("pending", "Pending"),
    ("in_progress", "In Progress"),
    ("completed", "Completed"),
]

priority_choices = [
    ("none", "None"),
    ("important", "Important"),
]


class Task(models.Model):
    """
    Task model representing a task assigned to a user.

    This model stores information about tasks created by users, including
    their status, priority, category, and due date.

    Attributes:
        - user (ForeignKey): The user who owns the task.
        - title (CharField): The title of the task (max length 100).
        - description (TextField): An optional detailed description of the
          task.
        - category (ForeignKey): The category to which the task belongs.
        - status (CharField): The current status of the task, with choices:
            - "pending" (default)
            - "in_progress"
            - "completed"
        - priority (CharField): The priority level of the task, with choices:
            - "none" (default)
            - "important"
        - due_date (DateTimeField): The optional due date for the task.
        - created_at (DateTimeField): The timestamp when the task was created.
        - updated_at (DateTimeField): The timestamp when the task was last
          updated.

    Meta:
        - Orders tasks by `created_at` in descending order.
        - Ensures uniqueness for tasks based on `user`, `title`,
          and `due_date`.

    Methods:
        - __str__(): Returns the title of the task as its string
        representation.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,
                              choices=status_choices, default="pending")
    priority = models.CharField(max_length=20,
                                choices=priority_choices, default="none")
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("user", "title", "due_date")

    def __str__(self):
        return self.title

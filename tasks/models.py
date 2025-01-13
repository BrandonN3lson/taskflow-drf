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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,
                              choices=status_choices,
                              default="pending"
                              )
    priority = models.CharField(max_length=20,
                                choices=priority_choices,
                                default="none"
                                )
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('user', 'title', 'due_date')

    def __str__(self):
        return self.title

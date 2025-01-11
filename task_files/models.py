from cloudinary_storage.storage import MediaCloudinaryStorage
from django.db import models
from tasks.models import Task


class TaskFile (models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(upload_to='taskFlow/',
                            storage=MediaCloudinaryStorage(),
                            blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

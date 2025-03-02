from cloudinary_storage.storage import MediaCloudinaryStorage
from django.db import models
from tasks.models import Task


class TaskFile(models.Model):
    """
    Model for storing files associated with tasks.

    This model represents file attachments linked to tasks.
    Files are uploaded to Cloudinary using the MediaCloudinaryStorage.

    Attributes:
        - task (ForeignKey): Links the file to a specific task.
        - file (FileField): Stores the uploaded file in Cloudinary under the
          'taskFlow/' directory.
        - uploaded_at (DateTimeField): Records the timestamp of the file
          upload.

    Methods:
        - __str__: Returns the name of the uploaded file.
    """

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(
        upload_to="taskFlow/", storage=MediaCloudinaryStorage(), blank=False
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

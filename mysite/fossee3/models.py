from django.db import models
from .validators import validate_file_extension

class Caption(models.Model):
    title = models.CharField(max_length=80, blank=False)
    description = models.TextField(blank=False)

class Documents(models.Model):
    document = models.FileField(upload_to='document/',validators=[validate_file_extension])
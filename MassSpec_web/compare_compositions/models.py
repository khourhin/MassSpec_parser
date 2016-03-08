from django.db import models


class FileUpload(models.Model):
    doc = models.FileField(upload_to='uploads')

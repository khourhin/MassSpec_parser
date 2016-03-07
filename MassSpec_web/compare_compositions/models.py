from django.db import models


class CompareMSJob(models.Model):
    file = models.FileField(upload_to='uploads')

from django.db import models
from multiselectfield import MultiSelectField

class FileUpload(models.Model):
    doc = models.FileField(upload_to='uploads')
    doctype = models.CharField(max_length=1,
                               choices=(('i', 'input_ms'),
                                        ('b', 'background_ms'),
                                        ('d', 'blast_db')),
                               default='i')

class MSJob(models.Model):
        name = models.CharField(max_length=30)
        email = models.EmailField()
        ms_in = MultiSelectField(choices=(('a', 'a'), ('b', 'b')))

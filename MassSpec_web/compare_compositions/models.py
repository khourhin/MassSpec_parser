from django.db import models


class FileUpload(models.Model):
    doc = models.FileField(upload_to='uploads')
    doctype = models.CharField(max_length=1,
                               choices=(('i', 'input_ms'),
                                        ('b', 'background_ms'),
                                        ('d', 'blast_db')),
                               default='i')

    def __str__(self):
        return self.doc.name

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


class Job(models.Model):
    """ Db entry of the jobs submitted byt the user """
    # TODO It will be nice to manage to use this model to generate the form
    name = models.CharField(max_length=30)
    ms_in = models.TextField()
    ms_bck = models.TextField()
    blast_db = models.TextField()

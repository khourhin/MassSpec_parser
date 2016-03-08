from django import forms
from .models import FileUpload


class CompareMSForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=30)
    email = forms.EmailField(label='email')

    ms_in = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                      label='Main MS data (.csv)')
    bck_in = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                       label='Background MS data (.csv)')
    blast_db = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         label='Blast database (.fas)')

    ms_in.choices = [(doc.doc.name, doc.doc.name)
                     for doc in FileUpload.objects.all()]
    bck_in.choices = [(doc.doc.name, doc.doc.name)
                      for doc in FileUpload.objects.all()]
    blast_db.choices = [(doc.doc.name, doc.doc.name)
                        for doc in FileUpload.objects.all()]

class UploadForm(forms.Form):
    ms_data = forms.FileField(label="""File to upload for MS data,
                              background or blast db""")

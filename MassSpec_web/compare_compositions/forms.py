from django import forms
from .models import FileUpload


class CompareMSForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=30)
    email = forms.EmailField(label='email')
    ms_in = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='IN')


class UploadForm(forms.Form):
    ms_data = forms.FileField(label="""File to upload for MS data,
                              background or blast db""")

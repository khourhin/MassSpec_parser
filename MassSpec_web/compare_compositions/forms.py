from django import forms
from .models import FileUpload, MSJob


class CompareMSForm(forms.ModelForm):

    class Meta:
        model = MSJob
        fields = ('name', 'email', 'ms_in')


class UploadForm(forms.ModelForm):

    class Meta:
        model = FileUpload
        fields = ('doc', 'doctype')

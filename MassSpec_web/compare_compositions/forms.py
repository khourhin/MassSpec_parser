from django import forms

from multiupload.fields import MultiFileField


class CompareMSForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=30)
    email = forms.EmailField(label='email')
    ms_data = MultiFileField(min_num=2)
    ms_background = MultiFileField(min_num=1)

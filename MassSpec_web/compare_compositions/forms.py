from django import forms
from .models import FileUpload


class CompareMSForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    ms_in = forms.ModelMultipleChoiceField(label='MS infiles (.csv)',
                                           queryset=FileUpload.objects.filter(doctype='i'),
                                           widget=forms.CheckboxSelectMultiple,)
    ms_bck = forms.ModelMultipleChoiceField(label='MS background (.csv)',
                                            queryset=FileUpload.objects.filter(doctype='b'),
                                            widget=forms.CheckboxSelectMultiple,)
    blast_db = forms.ModelMultipleChoiceField(label='blast db',
                                             queryset=FileUpload.objects.filter(doctype='d'),
                                             widget=forms.CheckboxSelectMultiple,)
class UploadForm(forms.ModelForm):

    class Meta:
        model = FileUpload
        fields = ('doc', 'doctype')

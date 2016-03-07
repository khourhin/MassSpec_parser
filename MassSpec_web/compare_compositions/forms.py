from django import forms

class CompareMSForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=30)
    ms1_file = forms.FileField()
    ms2_file = forms.FileField()
    

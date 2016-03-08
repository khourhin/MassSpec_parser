from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView

from django.contrib.auth.forms import UserCreationForm
from .forms import CompareMSForm, UploadForm
from .models import FileUpload
from .compare_ms import run_compare


def done(request):
    return render(request, 'done.html')


def create_user(request):
    # TO DO ... Not in use yet
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            pass
            # TO DO
            # Something with form.cleaned_data
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def compare_ms(request):
    docs = FileUpload.objects.all()

    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)
        runjob_form = CompareMSForm(request.POST)
        runjob_form.fields['ms_in'].choices = [(doc.id, doc.doc.name) for doc in docs]
        print(request.POST)
        if 'upload' in request.POST:

            if upload_form.is_valid():
                new_doc = FileUpload(doc=request.FILES['ms_data'])
                new_doc.save()

                return HttpResponseRedirect('/')

        elif 'runjob' in request.POST:
            print("submit job")
            if runjob_form.is_valid():
                print("Have to start a job here ... right now doing nothing")

                return HttpResponseRedirect('/')
            else:
                print("NOT CORRECT")
    else:
        upload_form = UploadForm()
        runjob_form = CompareMSForm()
        runjob_form.fields['ms_in'].choices = [(doc.id, doc.doc.name) for doc in docs]

    return render(request, 'compare_ms.html', {'upload_form': upload_form,
                                               'runjob_form': runjob_form,
                                               'docs': docs})

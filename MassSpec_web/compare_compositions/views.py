from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import CompareMSForm, UploadForm
from .models import FileUpload, Job
from .compare_ms_CLI import run_compare_cli


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
        print(request.POST)
        print(request.FILES)
        if 'upload' in request.POST:

            if upload_form.is_valid():
                upload_form.save()

                return redirect('compare_ms')

        elif 'runjob' in request.POST:
            print("submit job")
            if runjob_form.is_valid():
                data = runjob_form.cleaned_data

                ms_in = [f.doc.name for f in data['ms_in']]
                ms_bck = [f.doc.name for f in data['ms_bck']]
                blast_db = [f.doc.name for f in data['blast_db']]
                print(data)

                run_compare_cli(ms_in, ms_bck, 2, blast_db, 'MS_parse_out',
                                data['email'], 1, '')

                Job.objects.create(name=data['name'],
                                   ms_in=','.join(ms_in),
                                   ms_bck=','.join(ms_bck),
                                   blast_db=','.join(blast_db),
                                   )

                return redirect('done')

    else:
        upload_form = UploadForm()
        runjob_form = CompareMSForm()

    return render(request, 'compare_ms.html', {'upload_form': upload_form,
                                               'runjob_form': runjob_form,
                                               'docs': docs})

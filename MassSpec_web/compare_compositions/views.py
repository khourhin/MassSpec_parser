from django.shortcuts import render
from django.views.generic.edit import FormView

from django.contrib.auth.forms import UserCreationForm
from .forms import CompareMSForm
from .models import CompareMSJob
from .compare_ms import handle_uploaded_files


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


class CompareMSView(FormView):
    template_name = 'compare_ms.html'
    form_class = CompareMSForm
    success_url = '/done/'

    def form_valid(self, form):
        for each in form.cleaned_data['ms_data']:
            CompareMSJob.objects.create(file=each)
        return super(CompareMSView, self).form_valid(form)

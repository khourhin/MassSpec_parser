from django.shortcuts import render
from django.views.generic.edit import FormView

from django.contrib.auth.forms import UserCreationForm
from .forms import CompareMSForm
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


class CompareMSView(FormView):
    template_name = 'compare_ms.html'
    form_class = CompareMSForm
    success_url = '/done/'

    def form_valid(self, form):
        # This will be executed if the form is valid !
        for each in form.cleaned_data['ms_data']:
            FileUpload.objects.create(file=each)
        run_compare(form.cleaned_data)

        print(form.cleaned_data)
        return super(CompareMSView, self).form_valid(form)

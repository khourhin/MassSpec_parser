from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import CompareMSForm

def compare_ms(request):
    if request.method == 'POST':
        # Create a form instance and populate it with the request data
        form = CompareMSForm(request.POST)
        if form.is_valid():
            # Process the data
            # ...
            # redirect to new url
            return HttpResponseRedirect('/thanks/')

    # if Get method
    else:
        form = CompareMSForm()

        return render(request, 'compare_ms.html', {'form': form})

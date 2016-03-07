from .models import FileUpload


def handle_uploaded_files(infiles):
    for key in infiles:
        for chunk in infiles[key].chunks():
                print(chunk)


def run_compare(data):
    user = data['name']
    email = data['email']
    ms_background = data['ms_background']
    ms_data = data['ms_data']

    print(user)
    print(FileUpload.objects.all())

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

# Alternative:
# 1: streaming (in memory)


# 2: TO DO To check (for big files using the copy to the server)
# print(user)
    print(FileUpload.object.get())

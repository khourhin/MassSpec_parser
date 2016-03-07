from .models import FileUpload
from .compare_ms_CLI import run_compare_cli


def handle_uploaded_files(infiles):
    for key in infiles:
        for chunk in infiles[key].chunks():
                print(chunk)


def run_compare(data):
    user = data['name']
    email = data['email']
    ms_background = data['ms_background']
    ms_data = data['ms_data']

    run_compare_cli(ms_data, ms_background, 2,
                               'libs/demo/TAIR10_pep_20101214_updated.txt',
                               'MS_parse_out',
                               'khourhin@gmail.com', 1, '')

# Alternative:
# 1: streaming (in memory)


# 2: TO DO To check (for big files using the copy to the server)
# print(user)
    print(FileUpload.object.get())

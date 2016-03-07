def handle_uploaded_files(infiles):
    for key in infiles:
        for chunk in infiles[key].chunks():
                print(chunk)

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm

def handle_uploaded_file(f):
    with open('name.txt', 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/selector/file-uploaded')
    else:
        form = UploadFileForm()
        return render(request, 'core/index.html', {'form': form})

def file_uploaded(request):
    return render(request, 'core/file_uploaded.html')
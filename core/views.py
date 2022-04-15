from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

from core.selector.JsonParse import parse_task_list
from core.selector.TaskSelector import TaskSelector

def handle_uploaded_file(f):
    with open('core/static/upload/data.json', 'wb') as destination:
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

def get_tasks():
    with open('core/static/upload/data.json', 'r') as source:
        data_string = source.read()
        task_list = parse_task_list(data_string)
        return TaskSelector.select(task_list)

def file_uploaded(request):
    return render(request, 'core/file_uploaded.html', {'tasks': get_tasks()})
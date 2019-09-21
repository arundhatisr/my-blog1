from django.shortcuts import render
from .models import Upload
from . import views


def Upload(request):
    return render(request, 'blog/Upload.html', {'Upload':Upload})

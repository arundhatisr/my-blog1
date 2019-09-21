from django.shortcuts import render
from .models import Upload
from . import views
# Create your views here.
def Upload(request):
    
    return render(request, 'blog/Upload.html', {'Upload':Upload})

def objects(request):
    upload = Upload.objects.order_by('name')
    return render(request, 'blog/Upload.html', {'objects':objects})

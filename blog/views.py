from django.shortcuts import render

# Create your views here.
def Upload(request):
    return render(request, 'blog/Upload.html', {})

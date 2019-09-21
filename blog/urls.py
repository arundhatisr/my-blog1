from django.urls import path
from . import views
urlpatterns = [
    path('', views.Upload, name='Upload'),
    path('', views.objects, name='objects'),
]

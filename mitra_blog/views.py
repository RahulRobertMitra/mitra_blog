# mysite/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse('Rahul Mitra Blog!')

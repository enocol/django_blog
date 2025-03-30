from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    return HttpResponse('Hello, this is the blog page!')  # noqa: E501

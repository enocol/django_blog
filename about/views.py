from django.shortcuts import render
from . models import About

# Create your views here.

def about(request):
    """
    Display the about page.
    """
    aboutInfo = About.objects.all()
   
    return render(request, 'about/about.html', {'about': aboutInfo})

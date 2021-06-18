from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        "title": "Trigger python logic"
    }
    return render(request, "home/home.html", context)
# Create your views here.

def simple_function(request):
    print("\nThis a simple function\n")
    return HttpResponse(""" <html><scrit>windows.location.replace('/');</script></html>""")
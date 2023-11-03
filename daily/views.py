from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "daily/index.html")

def calendar(request):
    return render(request, "daily/calendar.html")

def data(request):
    return render(request, "daily/data.html")
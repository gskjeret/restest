from django.shortcuts import render

def home(request):
    return render(request, "home/home.html")

def kunder(request):
    return render(request, "home/kunder.html")

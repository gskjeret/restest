from django.shortcuts import render

def home(request):
    return render(request, "home/home.html")

def kunder(request):
    return render(request, "home/kunder.html")

def ordre(request):
    return render(request, "home/ordre.html")

def produkter(request):
    return render(request, "home/produkter.html")

def leverandorer(request):
    return render(request, "home/leverandorer.html")

def kunde_detalj(request, kid):
    return render(request, "home/kunde_detalj.html", {'kundeid': kid})

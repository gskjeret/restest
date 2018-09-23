from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return render(request, "home/home.html")
    else:
        return redirect("home_login")

@login_required
def kunder(request):
    return render(request, "home/kunder.html")

@login_required
def ordre(request):
    return render(request, "home/ordre.html")

@login_required
def produkter(request):
    return render(request, "home/produkter.html")

@login_required
def leverandorer(request):
    return render(request, "home/leverandorer.html")

@login_required
def kunde_detalj(request, kid):
    return render(request, "home/kunde_detalj.html", {'kundeid': kid})

@login_required
def produkt_detalj(request, pid):
    return render(request, "home/produkt_detalj.html", {'produktid': pid})

@login_required
def leverandor_detalj(request, lid):
    return render(request, "home/leverandor_detalj.html", {'leverandorid': lid})

@login_required
def ny_ordre(request, kid):
    return render(request, "home/ny_ordre.html", {'kundeid': kid})

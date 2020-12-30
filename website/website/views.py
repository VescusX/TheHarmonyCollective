from django.shortcuts import redirect, render

def home(request):
    return render(request, "home.html")

def volunteer(request):
    return render(request, "volunteer.html")

def involvement(request):
    return render(request, "involvement.html")

def partners(request):
    return render(request, "partners.html")

from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all() # Obtener todos los objetos generados desde el modelo
    return render(request, "portfolio/portfolio.html", {'projects':projects})
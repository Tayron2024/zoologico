from django.shortcuts import render
from .models import Animal

def buscar_animales(request):
    query = request.GET.get('q', '')  # Obtén el término de búsqueda desde el formulario
    resultados = Animal.objects.filter(nombre__icontains=query) if query else []  # Buscar por nombre
    return render(request, 'zoo/buscar_animales.html', {'query': query, 'resultados': resultados})


from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Animal, HistorialAlimentacion
from .forms import AnimalForm, HistorialInlineFormSet


# FILTROS Y BÚSQUEDA
class AnimalListView(ListView):
    model = Animal
    template_name = 'animal_list.html'
    context_object_name = 'animales'
    paginate_by = 10  # Paginación

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '')
        especie_filter = self.request.GET.get('especie', '')

        if search_query:
            queryset = queryset.filter(nombre__icontains=search_query)
        if especie_filter:
            queryset = queryset.filter(especie__iexact=especie_filter)
        return queryset


# REGISTRAR ANIMAL + HISTORIAL ALIMENTACION (Padre-Hijos)
def create_animal(request):
    if request.method == 'POST':
        animal_form = AnimalForm(request.POST)
        historial_formset = HistorialInlineFormSet(request.POST)
        if animal_form.is_valid() and historial_formset.is_valid():
            animal = animal_form.save()
            historial_formset.instance = animal
            historial_formset.save()
            return redirect('animal_list')
    else:
        animal_form = AnimalForm()
        historial_formset = HistorialInlineFormSet()

    return render(request, 'animal_create.html', {
        'animal_form': animal_form,
        'historial_formset': historial_formset,
    })


# ACTUALIZAR ANIMAL + HISTORIAL
def update_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        animal_form = AnimalForm(request.POST, instance=animal)
        historial_formset = HistorialInlineFormSet(request.POST, instance=animal)
        if animal_form.is_valid() and historial_formset.is_valid():
            animal_form.save()
            historial_formset.save()
            return redirect('animal_list')
    else:
        animal_form = AnimalForm(instance=animal)
        historial_formset = HistorialInlineFormSet(instance=animal)

    return render(request, 'animal_update.html', {
        'animal_form': animal_form,
        'historial_formset': historial_formset,
    })

from django.contrib import admin
from .models import Habitat, Especie, Animal

class AnimalInline(admin.TabularInline):
    model = Animal
    extra = 1

class EspecieInline(admin.TabularInline):
    model = Especie
    extra = 1

@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    inlines = [EspecieInline]

@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nombre_cientifico', 'nombre_comun', 'habitat')
    search_fields = ('nombre_cientifico', 'nombre_comun')
    list_filter = ('habitat',)
    inlines = [AnimalInline]

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'especie', 'fecha_ingreso')
    search_fields = ('nombre', 'especie__nombre_comun')
    list_filter = ('especie__habitat',)

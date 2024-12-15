from django.contrib import admin
from .models import Persona, Animal, RegistroMedico, Cliente, Empleado, Veterinario, EncargadoLimpieza, Inventario, \
    Comprobante, Zoologico, Habitat, GuiaTuristico, HistorialAlimentacion

# Register your models here.

admin.site.register(Persona)
admin.site.register(Animal)
admin.site.register(RegistroMedico)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Veterinario)
admin.site.register(EncargadoLimpieza)
admin.site.register(Inventario)
admin.site.register(Comprobante)
admin.site.register(Zoologico)
admin.site.register(Habitat)
admin.site.register(GuiaTuristico)
admin.site.register(HistorialAlimentacion)


import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zoo_website.settings')
django.setup()

from django.contrib.auth.models import User

# Verifica si ya existe un superusuario
if not User.objects.filter(username="admin_zoo").exists():
    User.objects.create_superuser(
        username="admin_zoo",
        email="admin@zoo.com",
        password="Zoologico123"
    )
    print("Superusuario creado con éxito.")
else:
    print("El superusuario ya existe.")

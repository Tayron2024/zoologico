from django.urls import path
from .views import AnimalListView, create_animal, update_animal

urlpatterns = [
    path('animales/', AnimalListView.as_view(), name='animal_list'),
    path('animales/create/', create_animal, name='create_animal'),
    path('animales/<int:pk>/edit/', update_animal, name='update_animal'),
]

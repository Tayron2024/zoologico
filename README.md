## Zoológico Django App 
Este proyecto implementa un sistema de gestión para un zoológico utilizando Django, que permite manejar Animales, su Historial de Alimentación, y otros modelos relacionados.
Se han desarrollado funcionalidades de filtros, búsqueda, presentación de datos, y formularios con relaciones Padre-Hijos.

## Características Principales
Se implementaron las siguientes clases principales:

Persona: Base para empleados, visitantes y clientes.
Animal: Representa animales en el zoológico.
HistorialAlimentacion: Relaciona animales con registros de alimentación.
Empleado, Veterinario, GuiaTuristico y otros modelos para el manejo de personal y administración.
Filtros y Búsqueda

Se pueden filtrar animales por nombre y especie.
Funcionalidad implementada en la vista basada en clase (ListView).
Presentación de Datos

# Datos presentados en una tabla HTML con columnas personalizadas:
Nombre, especie, género, y edad de los animales.
Implementación de paginación para mejor navegación.
Relación Padre-Hijos

Un formulario permite registrar un Animal junto con su Historial de Alimentación usando inlineformset_factory.
Incluye funciones para crear y actualizar registros.

##  Estructura del Proyecto
plaintext
Copiar código
ZoologicoPractica/
│
├── Zoologico/                 # Aplicación principal
│   ├── models.py              # Modelos (Animal, HistorialAlimentacion, Persona, etc.)
│   ├── forms.py               # Formularios personalizados
│   ├── views.py               # Vistas para CRUD y lógica de negocio
│   ├── urls.py                # Rutas de la aplicación
│   └── templates/             # Templates HTML
│       ├── animal_list.html   # Lista de animales con filtros y búsqueda
│       └── animal_create.html # Formulario de registro padre-hijos
│
└── manage.py                 # Comando para ejecutar el servidor

# Capturas de Pantalla

![image](https://github.com/user-attachments/assets/d1583144-2da4-4ec8-9e37-ffd52d4b8897)
![image](https://github.com/user-attachments/assets/cb1520d8-37bc-40f2-afd7-dc6b151a4e1c)

# Futuras Mejoras
Implementar autenticación de usuarios (admin y empleados).
Agregar gráficos para estadísticas de animales y alimentación.
Mejorar interfaz con Bootstrap.


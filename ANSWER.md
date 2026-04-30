# Análisis del Proyecto

## Descripción general

El proyecto consiste en el desarrollo de una aplicación web utilizando Django que permite gestionar información relacionada con autores, libros y reseñas. La aplicación hace uso del ORM de Django para definir modelos y establecer relaciones entre ellos, además de aprovechar el panel de administración para realizar operaciones CRUD de forma sencilla.

---

## Modelos y relaciones

Se implementaron tres modelos principales:

- **Autor**: representa a los escritores, con información básica como nombre y nacionalidad.
- **Libro**: contiene datos como título, fecha de publicación y un resumen. Este modelo está relacionado con Autor mediante una clave foránea, lo que permite que un autor tenga múltiples libros.
- **Reseña**: almacena opiniones sobre los libros, incluyendo texto, calificación y fecha. Está relacionada con Libro, permitiendo múltiples reseñas por cada libro.

Estas relaciones corresponden a estructuras de tipo uno a muchos, lo cual es coherente con el dominio del problema.

---

## Panel de administración

Se utilizó el panel de administración de Django para gestionar los datos de la aplicación. Los modelos fueron registrados en `admin.py` y se personalizó su visualización mediante:

- `list_display` para mostrar campos relevantes en las listas
- `search_fields` para facilitar la búsqueda de registros
- `list_filter` para filtrar información

Además, se implementaron `inlines` para mejorar la navegación, permitiendo visualizar los libros directamente dentro de cada autor, lo que hace más intuitiva la gestión de datos relacionados.

---

## Validaciones

Se agregaron validaciones personalizadas en los modelos para asegurar la calidad de los datos:

- En **Autor**, se valida que el nombre no esté vacío ni contenga únicamente espacios.
- En **Libro**, se exige que el resumen tenga una longitud mínima, evitando registros con información insuficiente.
- En **Reseña**, se controla que la calificación esté dentro de un rango válido y que no incluya valores no deseados.

Estas validaciones se implementaron mediante el método `clean()`, lo que permite mantener la lógica de negocio dentro de los modelos.

---

## Carga de datos iniciales

Se desarrolló un script (`poblar_datos.py`) que permite insertar datos de prueba en la base de datos utilizando el ORM de Django. Esto facilita la verificación del funcionamiento del sistema sin necesidad de ingresar manualmente cada registro desde el panel de administración.

---

## Funcionamiento general

El sistema permite:

- Crear, editar y eliminar autores, libros y reseñas desde el admin
- Establecer relaciones entre entidades de forma automática mediante claves foráneas
- Visualizar información relacionada de manera organizada
- Validar datos antes de ser almacenados

---

## Conclusión

El proyecto demuestra el uso básico pero completo de Django para la construcción de aplicaciones web con manejo de base de datos. Se aplicaron conceptos importantes como modelado de datos, relaciones entre entidades, validaciones y uso del panel administrativo. Además, se logró una estructura clara y funcional que puede servir como base para futuras ampliaciones.

from biblioteca.models import Autor, Libro, Resena
from datetime import date

# Crear autores
autor1 = Autor.objects.create(
    nombre="Gabriel García Márquez",
    nacionalidad="Colombiana"
)

autor2 = Autor.objects.create(
    nombre="Isabel Allende",
    nacionalidad="Chilena"
)

# Crear libros
libro1 = Libro.objects.create(
    titulo="Cien años de soledad",
    autor=autor1,
    fecha_publicacion=date(1967, 6, 5),
    resumen="Novela emblemática del realismo mágico."
)

libro2 = Libro.objects.create(
    titulo="La casa de los espíritus",
    autor=autor2,
    fecha_publicacion=date(1982, 1, 1),
    resumen="Historia familiar con elementos mágicos."
)

# Crear reseñas
Resena.objects.create(
    libro=libro1,
    texto="Excelente obra literaria",
    calificacion=5
)

Resena.objects.create(
    libro=libro2,
    texto="Muy buena historia",
    calificacion=4
)

print("Datos insertados correctamente")
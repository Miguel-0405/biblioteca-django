from django.db import models
from django.core.exceptions import ValidationError


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def clean(self):
        if self.nombre == "":
            raise ValidationError("El nombre del autor no puede estar vacio.")

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    resumen = models.TextField()

    def validacion(self):
        if self.titulo == "":
            raise ValidationError("El titulo del libro no puede estar vacio.")

    def clean(self):
        if len(self.resumen) < 20:
            raise ValidationError("El resumen debe tener al menos 20 caracteres.")

    def __str__(self):
        return self.titulo


class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    texto = models.TextField()
    calificacion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def validacion(self):
        if self.calificacion % 1 != 0:
            raise ValidationError("La calificación no puede tener decimales.")

    def clean(self):
        if self.calificacion < 1 or self.calificacion > 5:
            raise ValidationError("La calificación debe estar entre 1 y 5.")

    def __str__(self):
        return f"{self.libro.titulo} - {self.calificacion}/5"
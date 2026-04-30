from django.contrib import admin
from .models import Autor, Libro, Resena

class LibroInline(admin.TabularInline):
    model = Libro
    extra = 0

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')
    inlines = [LibroInline]


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    search_fields = ('titulo',)
    list_filter = ('autor', 'fecha_publicacion')


@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('libro', 'calificacion', 'fecha')
    search_fields = ('texto',)
    list_filter = ('calificacion', 'fecha')
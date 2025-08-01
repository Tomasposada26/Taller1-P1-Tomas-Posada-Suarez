# books/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    author = models.CharField(max_length=100, verbose_name="Autor")
    genre = models.CharField(max_length=100, verbose_name="Género")
    synopsis = models.TextField(verbose_name="Sinopsis")
    cover_image = models.URLField(max_length=200, verbose_name="URL de la Portada") # Usaremos URLs de imágenes externas
    publication_year = models.IntegerField(null=True, blank=True, verbose_name="Año de Publicación")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['title'] # Ordena los libros por título por defecto
# books/views.py

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Book
from django.db.models import Q

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()

        # Obtener los filtros como listas (QueryDict.getlist)
        authors_filter = self.request.GET.getlist('author')
        genres_filter = self.request.GET.getlist('genre')
        years_filter = self.request.GET.getlist('year') # Asegúrate de que el campo exista en el modelo

        # Aplicar filtros si hay valores seleccionados
        if authors_filter:
            # __in permite filtrar por múltiples valores en un campo
            queryset = queryset.filter(author__in=authors_filter)
        if genres_filter:
            queryset = queryset.filter(genre__in=genres_filter)
        if years_filter:
            # Convertir los años a enteros antes de filtrar
            years_filter_int = [int(y) for y in years_filter if y.isdigit()]
            if years_filter_int:
                queryset = queryset.filter(publication_year__in=years_filter_int)

        return queryset

class BookSearchView(ListView):
    model = Book
    template_name = "book_search_results.html"
    context_object_name = "books"
    paginate_by = 6 # Mantener paginación para resultados de búsqueda

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(
                Q(title__icontains=query) |
                Q(author__icontains=query) |
                Q(genre__icontains=query)
            ).distinct()
        return Book.objects.none()
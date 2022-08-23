from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book

class BookList(ListView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'pages', 'author', 'published_date']
    success_url = reverse_lazy('libraryapp:book_list')

class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'pages', 'author', 'published_date']
    success_url = reverse_lazy('libraryapp:book_list')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('libraryapp:book_list')
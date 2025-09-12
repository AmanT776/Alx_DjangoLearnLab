from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Book,Author
# Create your views here.
def list_all_books(request):
    books = Book.objects.all()
    titles = ", ".join(book.title + " " +  book.author.name for book in books)
    return HttpResponse(titles)
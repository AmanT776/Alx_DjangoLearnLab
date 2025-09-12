from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Library,Book,Author
# Create your views here.
def list_all_books(request):
    books = Book.objects.all()
    content = {"books": books}
    return render(request,"relationship_app/list_books.html",content)
class list_all_books_in_library(ListView):
    model = Library
    context_object_name = "libraries"
    
    def get_queryset(self):
        return super().get_queryset()

    def render_to_response(self, context, **response_kwargs):
        libraries = context["libraries"]
        books = [book.title for library in libraries for book in library.books.all()]
        content = {"libraries": libraries , "books": books}
        return render(self.request,"relationship_app/library_detail.html",content)
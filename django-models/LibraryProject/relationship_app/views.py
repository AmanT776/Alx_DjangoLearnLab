from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Library,Book,Author

# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('books')
    template_name = 'relationship_app/register.html'


def list_books(request):
    books = Book.objects.all()
    content = {"books": books}
    return render(request,"relationship_app/list_books.html",content)
class LibraryDetailView(ListView):
    model = Library
    context_object_name = "libraries"
    
    def get_queryset(self):
        return super().get_queryset()

    def render_to_response(self, context, **response_kwargs):
        libraries = context["libraries"]
        library = [library for library in libraries]
        content = {"libraries": library}
        return render(self.request,"relationship_app/library_detail.html",content)
    

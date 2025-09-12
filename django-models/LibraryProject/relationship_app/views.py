from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .models import Library,Book,Author


# Create your views here.

from django.contrib.auth import login

class register(CreateView):
    form_class = UserCreationForm()
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class LoginView(LoginView):
    template_name="relationship_app/login.html"
    redirect_authenticated_user = True
    reverse_lazy('books')

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
    

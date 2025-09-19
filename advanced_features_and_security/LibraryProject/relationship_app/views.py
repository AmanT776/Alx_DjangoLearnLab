from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from .models import Library, Book, Author
from django.http import HttpResponseForbidden

# Role-based view checks
def check_admin_role(user):
    return hasattr(user, 'profile') and user.profile.role == 'ADMIN'

@user_passes_test(check_admin_role)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome to the Admin Dashboard'})

def check_librarian_role(user):
    return hasattr(user, 'profile') and user.profile.role == 'LIBRARIAN'

@user_passes_test(check_librarian_role)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome to the Librarian Dashboard'})

def check_member_role(user):
    return hasattr(user, 'profile') and user.profile.role == 'MEMBER'

@user_passes_test(check_member_role)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome to the Member Dashboard'})

# User registration and login views
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('books')

# Book listing view (unchanged, no permission required for viewing)
def list_books(request):
    books = Book.objects.all()
    content = {"books": books}
    return render(request, "relationship_app/list_books.html", content)

# Library detail view (unchanged, no permission required for viewing)
class LibraryDetailView(ListView):
    model = Library
    context_object_name = "libraries"
    
    def get_queryset(self):
        return super().get_queryset()

    def render_to_response(self, context, **response_kwargs):
        libraries = context["libraries"]
        library = [library for library in libraries]
        content = {"libraries": library}
        return render(self.request, "relationship_app/library_detail.html", content)

# New views for book operations with permission checks
class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'publication_year']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('books')
    permission_required = 'relationship_app.can_add_book'

    def form_valid(self, form):
        return super().form_valid(form)

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_year']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('books')
    permission_required = 'relationship_app.can_change_book'

    def form_valid(self, form):
        return super().form_valid(form)

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html'
    success_url = reverse_lazy('books')
    permission_required = 'relationship_app.can_delete_book'
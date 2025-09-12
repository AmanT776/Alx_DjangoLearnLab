from django.urls import path, reverse_lazy
from .views import admin_view, librarian_view, member_view, RegisterView, list_books, LibraryDetailView, BookCreateView, BookUpdateView, BookDeleteView
from django.contrib.auth.views import LogoutView, LoginView
["add_book/", "edit_book/", "delete_book"]
urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('books/', list_books, name='books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('library/admin/', admin_view, name='admin_dashboard'),
    path('library/librarian/', librarian_view, name='librarian_dashboard'),
    path('library/member/', member_view, name='member_dashboard'),
    path('add_book/', BookCreateView.as_view(), name='book_add'),
    path('edit_book/<int:pk>/', BookUpdateView.as_view(), name='book_edit'),
    path('delete_book/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
]
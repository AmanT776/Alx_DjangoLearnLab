from django.urls import path
from .views import (
    list_books, BookCreateView, BookUpdateView, BookDeleteView,
    RegisterView, CustomLoginView, admin_view, librarian_view,
    member_view, LibraryDetailView, search_books
)

urlpatterns = [
    path('books/', list_books, name='books'),
    path('books/add/', BookCreateView.as_view(), name='book_add'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('libraries/', LibraryDetailView.as_view(), name='library_detail'),
    path('search/', search_books, name='book_search'),
]

from django.urls import path
from .views import (
    BookListAPIView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path("books/",BookListAPIView.as_view(),name='books-list'),
    path("books/<int:pk>/",BookDetailView.as_view(),name='book-list'),
    path("books/create",BookCreateView.as_view(),name='book-create'),
    path("books/<int:pk>/update",BookUpdateView.as_view(),name='book-update'),
    path("books/<int:pk>/delete",BookDeleteView.as_view(),name='book-delete')
]
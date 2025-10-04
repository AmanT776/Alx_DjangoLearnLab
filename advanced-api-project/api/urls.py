from django.urls import path
from .views import (
    BookListAPIView,
    BookDetailView
)
urlpatterns = [
    path("books/",BookListAPIView.as_view(),name='books-list'),
    path("books/<int:pk>/",BookDetailView.as_view(),name='book-list')
]
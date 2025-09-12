from django.urls import path
from .views import list_all_books, list_all_books_in_library

urlpatterns = [
    path('books',list_all_books),
    path('library',list_all_books_in_library.as_view())
]
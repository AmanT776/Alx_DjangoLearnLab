from django.urls import path
from .views import list_all_books

urlpatterns = [
    path('books',list_all_books)
]
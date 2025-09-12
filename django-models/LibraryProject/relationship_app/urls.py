from django.urls import path
from .views import list_all_books, LibraryDetailView

urlpatterns = [
    path('books',list_all_books),
    path('library',LibraryDetailView.as_view())
]
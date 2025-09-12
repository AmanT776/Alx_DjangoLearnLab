from django.urls import path
from .views import list_books, LibraryDetailView,SignupView

urlpatterns = [
    path('books/',list_books,name='books'),
    path('library/',LibraryDetailView.as_view()),
    path('signup/',SignupView.as_view(),name='signup')
]
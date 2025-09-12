from django.urls import path
from .views import list_books, LibraryDetailView,SignupView,LoginView

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('signup/',SignupView.as_view(),name='signup'),
    path('books/',list_books,name='books'),
    path('library/',LibraryDetailView.as_view()),
]
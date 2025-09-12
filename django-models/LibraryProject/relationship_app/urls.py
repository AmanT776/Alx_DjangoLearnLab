from django.urls import path, reverse_lazy
from .views import list_books, LibraryDetailView,SignupView
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('signup/',SignupView.as_view(),name='signup'),
    path('logout/',LogoutView.as_view(template_name="relationship_app/logout.html",),name='logout'),
    path('books/',list_books,name='books'),
    path('library/',LibraryDetailView.as_view()),
]
from django.urls import reverse_lazy
from .views import list_books, LibraryDetailView,SignupView,LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('signup/',SignupView.as_view(),name='signup'),
    path('logout/',LogoutView.as_view(template_name="relationship_app/logout.html",reverse_lazy='login'),name='logout'),
    path('books/',list_books,name='books'),
    path('library/',LibraryDetailView.as_view()),
]
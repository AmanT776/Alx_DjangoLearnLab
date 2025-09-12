from django.urls import path, reverse_lazy
from .views import admin_view, librarian_view, LibraryDetailView, list_books, member_view, register
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('signup/',register.as_view(),name='signup'),
    path('logout/',LogoutView.as_view(template_name="relationship_app/logout.html",),name='logout'),
    path('books/',list_books,name='books'),
    path('library/',LibraryDetailView.as_view()),
    path('library/admin/',admin_view),
    path('library/librarian/',librarian_view),
    path('library/member/',member_view)
]
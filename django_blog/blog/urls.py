from django.urls import path
from .views import RegisterUser, LoginUser, home_view,profile_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('', home_view, name='home'),
    path('profile/',profile_view,name='profile')
]

from django.urls import path
from .views import RegisterUser, LoginUser, home_view

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('', home_view, name='home'),
]

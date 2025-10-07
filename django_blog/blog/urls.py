from django.urls import path
from .views import (
    RegisterUser,LoginUser,home_view
)
urlpatterns = [
    path('register',RegisterUser.as_view(),name='signup'),
    path('login',LoginUser.as_view(),name='login'),
    path('home',home_view,name='home')
]